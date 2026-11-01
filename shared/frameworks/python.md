## Quy tắc Python

- Tuân theo phiên bản Python, dependency manager, formatter, linter và cấu trúc
  package hiện có để code tương thích với runtime và workflow của repository.
- Giữ type hint nhất quán với code hiện tại; validate dữ liệu ở boundary và dùng
  exception phù hợp để caller nhận lỗi dự đoán được tại điểm nhận input.
- Giữ UI responsive: không chạy tác vụ blocking trên UI thread; giữ giao tiếp
  worker/UI theo pattern hiện có để tránh treo giao diện hoặc sai sót giữa thread.
- Đặt tương tác với hệ điều hành, thiết bị và process bên ngoài sau adapter rõ
  ràng; xử lý timeout, lỗi và cleanup để lỗi I/O không rò rỉ tài nguyên.
- Giữ cấu hình, dữ liệu runtime, log và artifact build ở đúng vị trí của ứng
  dụng; không ghi secret hoặc dữ liệu nhạy cảm vào log để tránh lộ dữ liệu.
- Không sửa generated output hoặc file đóng gói thủ công nếu repository có
  source/config làm chuẩn; lần generate tiếp theo sẽ ghi đè thay đổi đó.
- Chạy formatter, linter, type check hoặc test hẹp nhất đã được cấu hình để xác
  nhận đúng lớp thay đổi.
