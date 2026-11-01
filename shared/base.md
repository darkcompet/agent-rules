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

- Không commit, push hoặc mở PR nếu chưa được yêu cầu để task owner kiểm soát các
  thay đổi được chia sẻ ra ngoài working tree.
- Phải được duyệt rõ trước khi xóa file/dữ liệu, `reset --hard`, force push hoặc
  viết lại lịch sử. Ngoại lệ: artifact tạm agent tạo, code/file source trở nên
  không dùng do chính task sau khi kiểm tra references. Ngoại lệ không gồm dữ
  liệu người dùng, thay đổi của người khác hoặc code/file không liên quan vì các
  thao tác đó có thể làm mất dữ liệu hoặc thay đổi lịch sử không thể khôi phục.
- Kiểm tra `git status` trước khi sửa; không ghi đè hoặc hoàn tác thay đổi của
  người khác để không làm mất công việc đang có. Không in, log hoặc commit secret
  hay thông tin xác thực để tránh lộ quyền truy cập.
- Không sửa thủ công `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.agent-rules/base.md`
  hoặc `.agent-rules/framework.md`: lần sync/generate tiếp theo sẽ ghi đè chúng.
  Đặt rule riêng trong `.agent-rules/project.md`, chạy
  `./scripts/gen-agent-rules.py` để tạo lại entrypoint, rồi chạy
  `python3 scripts/gen-agent-rules.py --check` để xác nhận chúng khớp nguồn.
- Không tạo `AGENTS.override.md` để bổ sung rules: Codex chọn file này thay cho
  `AGENTS.md` cùng thư mục, nên nội dung generated sẽ không được nạp. Dùng
  `.agent-rules/project.md` và generator.

## Git branch, commit và push

- Khi task owner yêu cầu commit và push, phải commit trên branch `develop` và
  push lên remote branch `develop`. Không tạo hoặc chuyển sang branch task/feature
  mới. Nếu branch `develop` không có sẵn hoặc không thể dùng an toàn, dừng thao
  tác commit/push và báo task owner; không tự tạo branch thay thế.
- Trước khi commit, pull branch `develop` từ remote đích để cập nhật source mới
  nhất. Chỉ fast-forward; không tự tạo merge commit hoặc rewrite history. Nếu pull
  bị conflict, không thể fast-forward hoặc không an toàn với thay đổi hiện có,
  dừng và báo task owner trước khi commit.
- Trước khi commit, kiểm tra `git status` và diff để chỉ commit thay đổi thuộc
  task được yêu cầu. Giữ nguyên thay đổi sẵn có của task owner hoặc người khác;
  không stage hoặc commit chúng nếu không thuộc phạm vi được yêu cầu.
- Chỉ thực hiện commit và push khi task owner đã yêu cầu rõ; quy tắc chọn branch
  này không tự cấp quyền commit hoặc push.

## Trước khi sửa

- Đọc rule áp dụng và tập file nhỏ nhất đủ hiểu thay đổi để tránh suy luận từ
  context thiếu. Đọc spec khi task liên quan contract; đọc architecture khi task
  chạm boundary/dependency. Xác định acceptance criteria và check hẹp nhất.
- Kiểm chứng path, command, API và các giả định về repository; không tự suy đoán.
- Chỉ hỏi khi điểm chưa rõ có thể đổi behavior hoặc approval gate yêu cầu;
  nếu không, nêu giả định rồi tiếp tục.

## Spec và approval

Spec bắt buộc khi task đổi behavior, scope, API, data, security hoặc compatibility,
vì các thay đổi này ảnh hưởng contract được duyệt. Ngoại lệ: typo; docs không đổi
contract; formatting/refactor không đổi behavior; test cho behavior hiện có.

- Đọc `docs/specs/README.md` và spec liên quan để theo đúng format, scope và trạng
  thái. Đọc `docs/README.md` khi tạo task document ngoài spec.
- Implement requirement `Approved` như contract mong đợi, kể cả khi file đang
  `Draft` vì có proposal khác; không implement requirement `Proposed`.
- Khi thêm hoặc đổi contract, viết proposal cụ thể theo quy chuẩn spec và chờ
  task owner duyệt đúng nội dung/phạm vi. Giữ contract đã duyệt trong khi chờ.
  Approval phải xác định proposal/requirement và nội dung được duyệt trong hội
  thoại hoặc PR/commit; “Implement X” chung chung chưa đủ. Ghi nguồn approval đã
  có, không tự duyệt hoặc hỏi lại khi scope không đổi.
- Nếu thiếu quy chuẩn, contract mong đợi hoặc người duyệt, dừng phần implementation
  bị ảnh hưởng và báo điều còn thiếu. Tiếp tục được điều tra read-only, soạn
  proposal và làm phần độc lập đã được phép.

## Sửa issue

- Trước khi sửa, đọc approved spec và architecture liên quan rồi truy nguyên root
  cause đến điều kiện và cơ chế cụ thể gây lỗi; xác định lỗi ở implementation hay
  contract/spec để sửa đúng nơi sở hữu. Đối chiếu symptom với đường thực thi và
  evidence trong code, test, log hoặc output tái hiện; không dừng ở mô tả symptom,
  tương quan hoặc nguyên nhân nghe có vẻ hợp lý.
- Chỉ trình bày nguyên nhân là đã xác nhận khi evidence cho thấy được vì sao lỗi
  xảy ra. Nêu evidence cụ thể hỗ trợ kết luận (path/function, test, log hoặc kết
  quả command phù hợp). Không dùng phỏng đoán như “maybe the bug is...” thay cho
  kết luận hoặc điều tra. Nếu còn nhiều khả năng, kiểm tra chúng bằng evidence
  phân biệt được; nếu không thể xác nhận sau khi đã kiểm tra, nói rõ chưa xác
  định được root cause, đã kiểm tra gì, evidence hiện có và phần chưa rõ. Không
  khẳng định đã tìm ra hoặc sửa nguyên nhân khi chưa có căn cứ.
- Sửa root cause tại source of truth và boundary sở hữu, conform approved spec.
  Không workaround để che symptom, né contract, ép test pass hoặc trì hoãn sửa đúng,
  vì workaround giữ nguyên nguyên nhân và dễ tái tạo lỗi.
- Không thêm special case, fallback, silent conversion, duplicate path hay error
  suppression nếu chưa được spec yêu cầu; các đường xử lý ẩn có thể làm behavior
  lệch contract và khó truy nguyên.
- Spec xác định behavior, không cần thuật toán/implementation detail trừ khi là
  constraint đã duyệt. Thiếu chi tiết implementation không cần approval mới.
- Nếu behavior mong đợi thiếu, mâu thuẫn hoặc cần đổi, áp dụng approval gate ở
  trên; không thêm workaround tạm. Nếu chưa rõ root cause, tiếp tục điều tra;
  khi không thể lấy thêm evidence, dừng sửa code và báo điều chưa rõ theo yêu cầu
  evidence ở trên.

## Phạm vi và style của target project

- Trước khi thiết kế hoặc sửa implementation, tìm và đọc code có cùng vai trò
  trong đúng boundary/module. Đọc thêm caller, tests và docs/config liên quan khi
  cần để hiểu cách pattern được dùng; không chỉ dựa vào tên hoặc kiến thức chung
  khi repo đã có precedent phù hợp.
- Rút ra và áp dụng convention hiện có về naming, file/type structure, thứ tự
  khai báo, comments/docs, logging, validation, error handling, tests và workflow.
  Kiểm tra các quyết định, constraint và edge case đã thể hiện trong code, tests
  hoặc config, rồi ưu tiên pattern phù hợp thay vì tạo đường triển khai song song.
  Bước này giúp giữ nhất quán và tránh lặp lại lỗi hoặc vấn đề project đã xử lý.
- Nếu chưa tìm thấy ví dụ cùng vai trò, tìm trong boundary hoặc module gần nhất
  và đọc framework/repo guidance liên quan. Nếu vẫn không có precedent rõ ràng,
  dùng convention thể hiện trong repo config và code gần nhất, rồi nêu giả định
  khi báo cáo; không trình bày lựa chọn mới như convention đã có.
- Precedent bổ sung, không miễn rule. Nếu precedent mâu thuẫn, đối chiếu spec,
  architecture và repo config; vẫn mơ hồ thì báo rõ trước khi chọn cách triển
  khai. Nếu convention cần cải thiện, báo evidence, tác động và đề xuất; không tự
  mở rộng task để đổi convention.
- Giữ nguyên pattern, workflow, formatting hiện có. Không thêm feature,
  abstraction, config, dependency suy đoán; không refactor, rename, format,
  cleanup phần không liên quan để diff chỉ phản ánh yêu cầu và dễ review. Chỉ xóa
  code không còn dùng do thay đổi này tạo ra.

## Boundary và architecture

- Theo architecture và boundary đã tài liệu hóa; xác định module/feature/layer sở
  hữu behavior. Không áp pattern khác, bypass boundary, tạo dependency cycle hoặc
  gọi implementation nội bộ module khác khi đã có public contract/port, để giữ
  dependency và ownership tường minh.
- Giữ mỗi file, type và function tập trung vào trách nhiệm rõ ràng. Business rule
  ở owner; orchestration ở workflow/use case; I/O ở boundary phù hợp.
- Xem khoảng 300 dòng là tín hiệu để rà cohesion, không phải giới hạn bắt buộc;
  file dài được phép nếu cohesive và có lý do.
  Chỉ tách file/helper khi trách nhiệm hoặc rule riêng cần boundary; không chia
  máy móc hay refactor legacy chỉ vì số dòng. Function tập trung một operation.

## Naming và comments

- Ưu tiên từ IT phổ biến, đơn giản như `Create`, `Ensure`, `Update`, `Load`, `Save`
  để tên dễ hiểu và nhất quán;
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
  giá trị và phạm vi hardcode để owner kiểm soát source of truth; approval về
  behavior chung chưa đủ. Nếu đã có approval cho đúng hardcode đó, ghi nguồn và
  không hỏi lại. Nếu chưa được duyệt hoặc không thể hỏi, dừng phần phụ thuộc và
  báo điều còn chờ.
- Giá trị được duyệt phải định nghĩa có tên tại một nơi thuộc boundary sở hữu;
  nơi dùng tham chiếu lại. Hardcode cũ không cho phép thêm bản sao mới.
- Literal cấu trúc (`0` khởi tạo bộ đếm, chuỗi rỗng) và dữ liệu test giả lập không
  quyết định behavior production không cần approval. Ngoại lệ không gồm business
  value/default hay magic number; chưa rõ thì hỏi owner. Không tạo config hoặc
  abstraction chỉ để thay literal cấu trúc vì chúng không có source of truth
  nghiệp vụ cần cấu hình.

### Runtime input và nguồn cấu hình

- Runtime input (API, CLI, file, event, UI): validate tại boundary trước side
  effect nghiệp vụ để input sai không tạo trạng thái nghiệp vụ dở dang. Chỉ dùng
  normalization/default/fallback theo contract; từ chối input còn sai bằng error
  theo contract. Không tự coercion hay đổi input/output để workflow chạy qua;
  compatibility mới cần approval. Schema runtime không áp dụng cho lời nhắn
  trong chat vì đó là chỉ dẫn của task owner, không phải application input. Nếu
  lời nhắn mơ hồ, áp dụng “Trước khi sửa”.
- Mỗi setting có một owner và source of truth; truyền giá trị, không tạo bản sao.
  Cách này tránh các bản giá trị lệch nhau. Product behavior ở app config,
  host/environment ở deployment config, credentials ở secret store. Default phải
  thuộc config contract đã tài liệu hóa; override dùng biến có tên, không hardcode
  literal ẩn trong script dùng chung.
- Resolve và validate config trước side effect để phát hiện thiếu hoặc xung đột
  trước khi tạo thay đổi một phần. Với deployment settings dùng chung, kiểm tra
  mọi environment và giữ khác biệt đã ghi nhận để không làm lệch môi trường.

## Kiểm chứng và báo cáo

- Chạy check liên quan hẹp nhất để xác nhận phần thay đổi mà không che lỗi bằng
  check yếu hơn. Nếu không có hoặc không chạy được, nêu rõ; không báo pass khi
  chưa chạy.
- Báo cáo cuối nêu file đổi, check và kết quả, link đến spec liên quan, sai khác
  đã duyệt và risks còn lại. Câu trả lời hoặc review chỉ đọc không cần spec.
