## Chọn và đặt tên task document

- Trước khi tạo task document, tìm trong README/index và các spec hiện có theo feature. Cập nhật spec hiện có khi công việc mở rộng hoặc tinh chỉnh behavior hay tiêu chí nghiệm thu của cùng feature.
- Tạo spec mới khi công việc có outcome riêng, có thể được duyệt và hoàn thành độc lập.
- Tên file mới theo dạng `yyyy-mm-dd-<feature>-<capability>.md`; ngày là ngày tạo lần đầu, slug mô tả feature và capability, ví dụ `2026-10-25-workspace-filesystem-auto-refresh.md`.
- Khi tiếp tục một task, giữ tên file hiện có. Chỉ đổi tên nếu tên không còn đúng phạm vi; đồng thời cập nhật README/index và các liên kết.

## Quy ước tên task file

- Tên mọi task document phải bắt đầu bằng ngày tạo theo định dạng
  `yyyy-mm-dd-`, ví dụ `2026-10-24-improve-alerts.md`; áp dụng cả với task cũ.
- Giữ các quy ước bổ sung về loại task hoặc số thứ tự được ghi trong README task
  của project.
- README và file index không cần tiền tố ngày.

## Metadata task

- Mỗi task document có `## Task metadata` ngay sau tiêu đề, gồm `Complexity`
  (`Easy`, `Medium`, `Hard`, `Expert`) và `Implementation status` (`Not
  started`, `In progress`, `Implemented`, `Blocked`, `Not applicable`,
  `Unknown`). Ví dụ: `- Complexity: Medium` và
  `- Implementation status: Not started`.
- Chọn `Unknown` cho task cũ khi chưa xác minh trạng thái; không suy đoán từ nội
  dung tài liệu. Chỉ đánh dấu `Implemented` khi tiêu chí nghiệm thu đã đạt và
  tài liệu ghi lại kiểm tra đã chạy.
- Ước lượng theo phạm vi: `Easy` là thay đổi nhỏ, cô lập; `Medium` chạm vài
  component hoặc cần phối hợp state; `Hard` thay đổi nhiều boundary, dữ liệu
  hoặc tích hợp; `Expert` có rủi ro cao hay cần thay đổi kiến trúc lớn.
