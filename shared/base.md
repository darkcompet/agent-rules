# Agent rules dùng chung

Mục tiêu: thay đổi nhỏ, chính xác, được kiểm chứng. Ưu tiên thay đổi nhỏ nhất
đáp ứng yêu cầu.

## Thứ tự ưu tiên

1. Chỉ dẫn trực tiếp từ task owner.
2. `.agent-rules/project.md` (rule riêng của project).
3. `.agent-rules/framework.md`, sau đó là file này.

Nếu các rule mâu thuẫn, làm theo rule có ưu tiên cao hơn và nêu rõ trong báo cáo.

## Ngôn ngữ trả lời

- Mọi câu trả lời, giải thích, câu hỏi và báo cáo của AI phải viết bằng tiếng Việt.
- Giữ nguyên tên file, identifier, lệnh, code và thuật ngữ kỹ thuật bằng ngôn ngữ gốc khi cần.

## An toàn

- Không commit, push hoặc mở PR nếu chưa được yêu cầu.
- Không thực hiện thao tác phá hủy (xóa file, `reset --hard`, force push, viết lại
  lịch sử, xóa dữ liệu) nếu chưa được duyệt rõ ràng.
- Không hoàn tác hoặc ghi đè thay đổi do người khác tạo. Trước tiên, kiểm tra
  `git status`.
- Không in, ghi log hoặc commit secret hay thông tin xác thực.

## File được tạo

- Không sửa thủ công `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`. Các file này được tạo
  tự động.
- Trong target repo, `.agent-rules/base.md` và `.agent-rules/framework.md` là
  bản sao được sync từ `agent-rules/shared/base.md` và
  `agent-rules/shared/frameworks/<framework>.md`. Không sửa các file này. Đặt
  rule riêng của project trong `.agent-rules/project.md`, sau đó chạy
  `./scripts/gen-agent-rules.py`.

## Trước khi sửa

- Đọc các rule áp dụng và tập file liên quan nhỏ nhất.
- Kiểm tra `git status` và diff liên quan.
- Xác định acceptance criteria và check hẹp nhất.
- Chỉ hỏi khi điểm chưa rõ làm thay đổi behavior. Nếu không, nêu giả định rồi tiếp tục.
- Không tự suy đoán thông tin về repository (path, command, API). Phải kiểm chứng.

## Spec trước khi triển khai

Áp dụng cho thay đổi về behavior, scope, API, data, security hoặc compatibility.

Ngoại lệ: sửa typo, chỉ sửa docs mà không đổi contract đã duyệt, formatting,
refactor thuần túy không đổi behavior và test cho behavior hiện có.

Với thay đổi không thuộc ngoại lệ:

1. Đọc `docs/specs/README.md`, `docs/README.md` và các spec liên quan đến thay
   đổi. Spec là một scope contract, không phải một feature hay task; một spec có
   thể chứa nhiều feature liên quan. Cập nhật feature hiện có hoặc thêm feature
   trong spec hiện tại khi cùng outcome/workflow/lifecycle và cần review/duyệt
   cùng nhau. Chỉ tạo spec mới cho outcome có contract riêng, có thể review,
   duyệt, implement và verify độc lập. Dùng `Feature list` và requirement detail
   theo format trong `docs/specs/README.md`; ghi thay đổi contract đã duyệt vào
   `Proposed changes`.
2. Spec phải mô tả outcome, scope, workflow khi áp dụng, requirements,
   acceptance criteria và cách kiểm chứng. Thêm design/implementation,
   delivery/rollout, dependency hoặc risk detail khi task cần.
3. Spec mới hoặc có thay đổi phải bắt đầu ở trạng thái `Draft`. Trình task owner
   và chờ duyệt. Chỉ owner được đặt trạng thái `Approved`. Không tự duyệt.
4. Chỉ triển khai nội dung đã được spec `Approved` quy định.
5. Nếu code không khớp spec đã duyệt, sửa code để conform. Nếu contract chưa rõ
   hoặc cần thay đổi, dừng phần việc bị ảnh hưởng, ghi đề xuất trong spec và chờ
   duyệt trước khi triển khai behavior thay đổi.
6. Nếu thiếu `docs/specs/README.md`, dừng và báo cần sync quy chuẩn spec trước.
7. Nếu không có người duyệt (chạy non-interactive), ghi spec `Draft`, không triển
   khai và báo lại.

## Không dùng workaround để sửa issue

- Trước khi viết code để sửa issue, đọc lại approved spec và architecture liên
  quan, rồi truy nguyên root cause. Xác định lỗi nằm ở implementation hay
  contract/spec.
- Bắt buộc sửa đúng root cause tại source of truth và boundary sở hữu behavior,
  conform với approved spec. Không viết workaround để che symptom, né contract,
  ép test pass hoặc trì hoãn việc tìm cách sửa đúng.
- Không thêm special case, fallback, silent conversion, duplicate code path hoặc
  error suppression chỉ để làm issue biến mất khi chưa chứng minh đó là behavior
  được spec yêu cầu.
- Nếu spec chưa quy định cách sửa đúng, mâu thuẫn với requirement khác hoặc cần
  đổi behavior, dừng phần code bị ảnh hưởng; ghi đề xuất trong spec ở trạng thái
  `Draft` và chờ task owner duyệt. Không thêm workaround tạm trong lúc chờ.
- Nếu chưa xác định được root cause hoặc cách sửa đúng, tiếp tục điều tra; nếu
  vẫn chưa đủ căn cứ, dừng phần code bị ảnh hưởng và báo evidence cùng thông tin
  còn thiếu thay vì đoán hoặc vá tạm.

## Giới hạn phạm vi thay đổi

- Giữ nguyên pattern, workflow và formatting hiện có.
- Không thêm feature, abstraction, config hoặc dependency mang tính suy đoán.
- Không refactor, đổi tên, format hoặc cleanup phần không liên quan.
- Chỉ xóa code không còn dùng do chính thay đổi này tạo ra.

## Boundary và architecture

- Tuân theo architecture đã được tài liệu hóa và boundary hiện có của repository; không tự áp đặt một pattern khác. Trước khi thêm code, xác định module, feature hoặc layer nào sở hữu behavior đó.
- Giữ file, class/type và function tập trung vào một trách nhiệm rõ ràng. Đặt business rule ở owner của nó, orchestration ở workflow/use case, và I/O hoặc tương tác hệ thống bên ngoài tại boundary phù hợp với architecture hiện có.
- Giữ dependency theo hướng mà architecture quy định. Không bypass module/layer boundary, tạo dependency cycle hoặc gọi implementation nội bộ của module khác khi đã có contract/port công khai.
- Ưu tiên giữ file mã nguồn do người viết duy trì ở khoảng 300 dòng. File dài
  hơn vẫn phù hợp khi có lý do rõ ràng và nội dung cohesive, như một bảng
  constants lớn cho cùng một target. Chỉ tách file khi việc đó tạo boundary
  trách nhiệm tốt hơn; không chia máy móc theo số dòng hoặc refactor file legacy
  không liên quan chỉ để đạt ngưỡng.
- Giữ function tập trung vào một operation có ý nghĩa. Tách bước riêng thành helper khi nó có trách nhiệm hoặc rule riêng, không chỉ để giảm số dòng.

## Đặt tên và comment

- Dùng từ IT phổ biến, đơn giản: `Create`, `Ensure`, `Update`, `Load`, `Save`.
  Không dùng: `Instantiate`, `Materialize`, `Persist`, `Hydrate`.
- Comment trong code ngắn, dùng English cơ bản; giải thích lý do, không diễn giải
  code. Quy ước ngôn ngữ của spec chỉ được định nghĩa trong
  `docs/specs/README.md`.
- Viết comment cho business rule, quyết định không hiển nhiên, giới hạn,
  workaround và xử lý lỗi.
- Không comment phần code đã rõ.
- Với function dài (trên khoảng 30 dòng), thêm comment ngắn nêu mục đích trước mỗi
  giai đoạn riêng biệt.
- Formatter/linter áp dụng quy tắc về độ dài dòng, dấu ngoặc và bố cục. Hãy chạy
  công cụ đó, không tự đếm.

## Contract của input

- Xem input từ user và bên ngoài là contract. Validate tại boundary. Từ chối
  input không hợp lệ trước mọi side effect.
- Không âm thầm normalize, suy luận, đặt default, fallback hoặc đổi cấu trúc input
  hay output chỉ để workflow chạy qua.
- Nếu input không khớp format chuẩn, giải thích format và yêu cầu input đã chỉnh
  hoặc approval cho compatibility. Chỉ thêm compatibility khi được yêu cầu.

## Cấu hình

- Mỗi setting có một owner và một source of truth. Truyền giá trị đó đến nơi cần
  dùng, không tạo bản sao.
- Behavior của product nằm trong app config. Vị trí environment/host nằm trong
  deployment config. Credential nằm trong secret store.
- Default nằm trong config contract đã được tài liệu hóa của owner. Override dùng
  biến có tên. Không đặt literal ẩn trong script dùng chung.
- Validate config đã resolve đầy đủ trước side effect. Báo lỗi rõ khi thiếu hoặc
  xung đột giá trị.
- Với setting deployment dùng chung, kiểm tra mọi environment được hỗ trợ và chỉ
  giữ khác biệt đã được tài liệu hóa.

## Kiểm chứng và báo cáo

- Chạy check liên quan hẹp nhất. Nếu không có check hoặc không thể chạy, phải nêu rõ.
- Không làm yếu check để đạt kết quả pass. Không báo check đã pass nếu chưa chạy.
- Báo cáo cuối: file đã đổi, check và kết quả cụ thể, link đến spec, sai khác đã được duyệt và rủi ro chưa giải quyết.
- Câu trả lời và review chỉ đọc không cần spec.
