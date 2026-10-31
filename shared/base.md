# Agent rules dùng chung

Mục tiêu: thay đổi nhỏ nhất đáp ứng yêu cầu, chính xác và được kiểm chứng.

## Thứ tự ưu tiên

Thứ tự dưới đây áp dụng giữa các chỉ dẫn của task owner và repository; không
thay thế instruction hierarchy của agent/runtime.

1. Chỉ dẫn trực tiếp từ task owner.
2. `.agent-rules/project.md`.
3. `.agent-rules/framework.md`.
4. Rule dùng chung trong `.agent-rules/base.md`.

Chỉ phần mâu thuẫn nhường cho chỉ dẫn ưu tiên cao hơn; báo rõ mâu thuẫn.
Mệnh lệnh trực tiếp và “phải/không được/chỉ” là bắt buộc; “ưu tiên/tránh” là
preference theo contract/convention. Yêu cầu làm task không tự miễn approval
gate; owner phải chỉ rõ ngoại lệ và phạm vi.

## Ngôn ngữ

- Trả lời, giải thích, câu hỏi và báo cáo cho task owner bằng tiếng Việt.
- Giữ nguyên tên file, identifier, lệnh, code và thuật ngữ IT theo ngôn ngữ gốc.

## An toàn và file được quản lý

- Không commit, push hoặc mở PR nếu chưa được yêu cầu.
- Phải được duyệt rõ trước khi xóa file/dữ liệu, `reset --hard`, force push hoặc
  viết lại lịch sử. Ngoại lệ: artifact tạm agent tạo, code/file source trở nên
  không dùng do chính task sau khi kiểm tra references. Ngoại lệ không gồm dữ
  liệu người dùng, thay đổi của người khác hoặc code/file không liên quan.
- Kiểm tra `git status` trước khi sửa; không ghi đè hoặc hoàn tác thay đổi của
  người khác. Không in, log hoặc commit secret hay thông tin xác thực.
- Không sửa thủ công `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.agent-rules/base.md`
  hoặc `.agent-rules/framework.md`: chúng được tạo/sync tự động. Đặt rule riêng
  trong `.agent-rules/project.md`, rồi chạy `./scripts/gen-agent-rules.py`.
- Sau khi đổi rule riêng, chạy `python3 scripts/gen-agent-rules.py --check`.
  Không tạo `AGENTS.override.md` để bổ sung rules: Codex chọn nó thay cho
  `AGENTS.md` cùng thư mục. Dùng `.agent-rules/project.md` và generator.

## Trước khi sửa

- Đọc rule áp dụng và tập file nhỏ nhất đủ hiểu thay đổi. Đọc spec khi task
  liên quan contract; đọc architecture khi task chạm boundary/dependency.
  Xác định acceptance criteria và check hẹp nhất.
- Kiểm chứng path, command, API và các giả định về repository; không tự suy đoán.
- Chỉ hỏi khi điểm chưa rõ có thể đổi behavior hoặc approval gate yêu cầu;
  nếu không, nêu giả định rồi tiếp tục.

## Spec và approval

Spec bắt buộc cho thay đổi behavior, scope, API, data, security hoặc compatibility.
Ngoại lệ: typo; docs không đổi contract đã duyệt; formatting/refactor không đổi
behavior; test cho behavior hiện có.

Với thay đổi cần spec:

1. Đọc `docs/specs/README.md` và spec liên quan; dùng quy chuẩn đó cho format,
   scope và trạng thái. Đọc `docs/README.md` khi tạo task document ngoài spec.
2. Nếu requirement đã `Approved` quy định behavior mong đợi, được implement hoặc
   sửa code để conform mà không xin duyệt lại, kể cả file spec đang `Draft` vì
   proposal khác. Không implement proposal chưa duyệt.
3. Nếu thêm hoặc đổi contract, viết proposal cụ thể theo quy chuẩn spec và chờ
   owner duyệt phần bị ảnh hưởng. Giữ nguyên contract đã duyệt trong khi chờ.
4. Approval xác định proposal/requirement và nội dung owner duyệt qua hội thoại
   hoặc PR/commit. “Implement X” chưa có proposal cụ thể không tự là approval.
   Agent chỉ ghi nhận quyết định đã có, cập nhật trạng thái và ngoại lệ owner
   chỉ rõ; không tự duyệt hoặc hỏi lại approval khi scope không đổi.
5. Thiếu quy chuẩn spec, contract mong đợi hoặc người duyệt thì dừng implementation
   phần bị ảnh hưởng và báo điều còn thiếu. Được tiếp tục điều tra read-only,
   soạn proposal và làm phần độc lập đã được phép.

## Sửa issue

- Trước khi sửa, đọc approved spec và architecture liên quan rồi truy nguyên root cause;
  xác định lỗi ở implementation hay contract/spec.
- Sửa root cause tại source of truth và boundary sở hữu, conform approved spec.
  Không workaround để che symptom, né contract, ép test pass hoặc trì hoãn sửa đúng.
- Không thêm special case, fallback, silent conversion, duplicate path hay error
  suppression nếu chưa được spec yêu cầu.
- Spec xác định behavior, không cần thuật toán/implementation detail trừ khi là
  constraint đã duyệt. Thiếu chi tiết implementation không cần approval mới.
- Nếu behavior mong đợi thiếu, mâu thuẫn hoặc cần đổi, áp dụng approval gate ở
  trên; không thêm workaround tạm. Nếu chưa rõ root cause, tiếp tục điều tra;
  khi không thể lấy thêm evidence, dừng sửa code và báo điều chưa rõ.

## Phạm vi và style của target project

- Trước khi sửa code, đọc ví dụ cùng vai trò trong boundary; xem thêm nếu pattern
  chưa rõ. Theo convention về naming, structure, declaration order, comments/docs,
  logging, validation, error handling và tests. Precedent bổ sung, không miễn rule.
- Nếu precedent mâu thuẫn, đối chiếu spec, architecture và repo config; vẫn mơ hồ
  thì báo rõ. Nếu convention cần cải thiện, báo evidence, tác động và đề xuất;
  không tự mở rộng task để đổi convention.
- Giữ nguyên pattern, workflow, formatting hiện có. Không thêm feature,
  abstraction, config, dependency suy đoán; không refactor, rename, format,
  cleanup phần không liên quan. Chỉ xóa code không còn dùng do thay đổi này tạo ra.

## Boundary và architecture

- Theo architecture và boundary đã tài liệu hóa; xác định module/feature/layer sở
  hữu behavior. Không áp pattern khác, bypass boundary, tạo dependency cycle hoặc
  gọi implementation nội bộ module khác khi đã có public contract/port.
- Giữ mỗi file, type và function tập trung vào trách nhiệm rõ ràng. Business rule
  ở owner; orchestration ở workflow/use case; I/O ở boundary phù hợp.
- Ưu tiên file source khoảng 300 dòng; file dài được phép nếu cohesive, có lý do.
  Chỉ tách file/helper khi trách nhiệm hoặc rule riêng cần boundary; không chia
  máy móc hay refactor legacy chỉ vì số dòng. Function tập trung một operation.

## Naming và comments

- Ưu tiên từ IT phổ biến, đơn giản như `Create`, `Ensure`, `Update`, `Load`, `Save`;
  tránh `Instantiate`, `Materialize`, `Persist`, `Hydrate`.
  Giữ tên do framework/public API quy định và convention của boundary hiện có;
  không rename code ngoài task chỉ để theo preference này.
- Comments/XML docs trong code dùng English cơ bản, ngắn, giải thích lý do thay vì
  diễn giải code. Comment business rules, quyết định/constraint không hiển nhiên,
  thứ tự, invariant, workaround và error handling; không comment code đã rõ.
- Với function có nhiều giai đoạn mà tên/code chưa thể hiện mục đích hoặc lý do
  thứ tự, thêm comment ngắn trước giai đoạn đó; số dòng không quyết định comment.
  Ngôn ngữ của spec theo `docs/specs/README.md`. Dùng formatter/linter của repo
  cho line length, braces và layout; không tự đếm.

## Input và configuration

### Hardcoding — bắt buộc

- Không tự thêm/đổi hardcode trong code, script hoặc template: business value,
  ID, URL/path, environment, limit, timeout, retry, default hay mapping cố định
  điều khiển behavior. Phải dùng source of truth của owner qua config/parameter/
  contract, không rải bản sao. Đưa literal vào `const` không miễn approval.
- Nếu cần hardcode, phải hỏi owner trước khi implement: nêu giá trị, vị trí, lý
  do, phương án không hardcode và tác động khi đổi. Chỉ làm khi owner duyệt rõ
  giá trị và phạm vi hardcode; approval behavior chung chưa đủ. Approval đó đã
  có thì ghi nguồn, không hỏi lại. Chưa được duyệt hoặc không hỏi được thì dừng
  phần phụ thuộc và báo điều còn chờ.
- Giá trị được duyệt phải định nghĩa có tên tại một nơi thuộc boundary sở hữu;
  nơi dùng tham chiếu lại. Hardcode cũ không cho phép thêm bản sao mới.
- Literal cấu trúc (`0` khởi tạo bộ đếm, chuỗi rỗng) và dữ liệu test giả lập không
  quyết định behavior production không cần approval. Ngoại lệ không gồm business
  value/default hay magic number; chưa rõ thì hỏi owner. Không tạo config hoặc
  abstraction chỉ để thay literal cấu trúc.

### Runtime input và nguồn cấu hình

- Runtime input (API, CLI, file, event, UI): validate tại boundary trước side
  effect nghiệp vụ. Chỉ dùng normalization/default/fallback theo contract;
  từ chối input còn sai bằng error theo contract. Không tự coercion hay đổi
  input/output để workflow chạy qua; compatibility mới cần approval. Schema
  runtime không áp dụng cho lời nhắn trong chat; xem “Trước khi sửa” khi task mơ hồ.
- Mỗi setting có một owner và source of truth; truyền giá trị, không tạo bản sao.
  Product behavior ở app config, host/environment ở deployment config, credentials
  ở secret store. Default phải thuộc config contract đã tài liệu hóa; override dùng
  biến có tên, không hardcode literal ẩn trong script dùng chung.
- Resolve và validate config trước side effect; báo thiếu hoặc xung đột. Với
  deployment settings dùng chung, kiểm tra mọi environment và giữ khác biệt đã ghi nhận.

## Kiểm chứng và báo cáo

- Chạy check liên quan hẹp nhất; nếu không có hoặc không chạy được, nêu rõ. Không
  làm yếu check hoặc báo pass khi chưa chạy.
- Báo cáo cuối nêu file đổi, check và kết quả, link đến spec liên quan, sai khác
  đã duyệt và risks còn lại. Câu trả lời hoặc review chỉ đọc không cần spec.
