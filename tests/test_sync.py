"""Exercise publishing and read-only drift checks in disposable projects."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1]


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.rules = self.root / 'rules'
        self.rules.mkdir()
        for name in ('shared', 'templates'):
            shutil.copytree(SOURCE / name, self.rules / name)
        shutil.copyfile(SOURCE / 'sync.py', self.rules / 'sync.py')
        (self.rules / 'local').mkdir()
        self.targets = self.rules / 'local/targets.tsv'
        self.targets.write_text('app|common\n')
        self.app = self.root / 'app'
        (self.app / '.agent-rules').mkdir(parents=True)
        (self.app / '.agent-rules/project.md').write_text('# Local rules\nKeep local behavior.\n')
        (self.app / 'docs').mkdir()
        (self.app / 'docs/README.md').write_text('# Local documentation\nKeep this text.\n')
        self.env = dict(os.environ, WORKSPACE_PROJECTS_ROOT=str(self.root))

    def run_sync(self, *args, success=True):
        result = subprocess.run([sys.executable, str(self.rules / 'sync.py'), *args],
                                env=self.env, capture_output=True, text=True)
        self.assertEqual(result.returncode == 0, success, result.stdout + result.stderr)
        return result

    def snapshot(self):
        return {str(p.relative_to(self.app)): (p.read_bytes(), p.stat().st_mtime_ns)
                for p in self.app.rglob('*') if p.is_file()}

    def test_publish_and_read_only_check(self):
        self.run_sync()
        content = (self.app / 'AGENTS.md').read_text()
        for name in ('base', 'framework', 'project'):
            self.assertIn(f'BEGIN SOURCE: .agent-rules/{name}.md', content)
        for name in ('CLAUDE.md', 'GEMINI.md'):
            self.assertEqual(content, (self.app / name).read_text())
        self.assertIn('Keep this text.', (self.app / 'docs/README.md').read_text())
        self.assertEqual('# Local rules\nKeep local behavior.\n',
                         (self.app / '.agent-rules/project.md').read_text())
        before = self.snapshot()
        self.run_sync('--check')
        self.assertEqual(before, self.snapshot())
        self.run_sync()
        self.assertEqual({p: value[0] for p, value in before.items()},
                         {p: value[0] for p, value in self.snapshot().items()})

    def test_drift_and_missing_files_fail_without_writing(self):
        self.run_sync()
        for name in ('AGENTS.md', 'CLAUDE.md', 'GEMINI.md', '.agent-rules/base.md',
                     '.agent-rules/framework.md', '.agent-rules/project.md',
                     'scripts/gen-agent-rules.py', 'docs/README.md', 'docs/specs/README.md'):
            with self.subTest(name=name):
                path = self.app / name
                original = path.read_bytes()
                path.write_bytes(b'changed\n')
                before = self.snapshot()
                self.run_sync('--check', success=False)
                self.assertEqual(before, self.snapshot())
                path.write_bytes(original)
        (self.app / 'GEMINI.md').unlink()
        self.run_sync('--check', success=False)
        self.assertFalse((self.app / 'GEMINI.md').exists())

    def test_override_blocks_sync_and_local_generator(self):
        self.run_sync()
        (self.app / 'AGENTS.override.md').write_text('# Override\n')
        before = self.snapshot()
        for args in ((), ('--check',)):
            result = self.run_sync(*args, success=False)
            self.assertIn('hides generated AGENTS.md', result.stderr)
            result = subprocess.run([sys.executable, str(self.app / 'scripts/gen-agent-rules.py'), *args],
                                    capture_output=True, text=True)
            self.assertNotEqual(0, result.returncode)
        self.assertEqual(before, self.snapshot())

    def test_check_before_first_sync_does_not_create_files(self):
        before = self.snapshot()
        self.run_sync('--check', success=False)
        self.assertEqual(before, self.snapshot())

    def test_missing_target_does_not_skip_other_targets(self):
        self.targets.write_text('missing|common\napp|common\n')
        self.run_sync(success=False)
        self.assertTrue((self.app / 'AGENTS.md').is_file())

    def test_bad_markers_fail_before_any_target_write(self):
        self.run_sync()
        start = '<!-- BEGIN SHARED TASK DOC RULES -->\n'
        end = '<!-- END SHARED TASK DOC RULES -->\n'
        for markers in (start, end + start, start + start + end + end):
            with self.subTest(markers=markers):
                (self.app / 'docs/README.md').write_text('# Keep local docs\n' + markers)
                (self.app / '.agent-rules/base.md').write_text('old base\n')
                before = self.snapshot()
                self.run_sync(success=False)
                self.assertEqual(before, self.snapshot())


if __name__ == '__main__':
    unittest.main()
