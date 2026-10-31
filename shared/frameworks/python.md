## Quy tắc Python

- Tuân theo phiên bản Python, dependency manager, formatter, linter và cấu trúc package hiện có của repository.
- Giữ type hint nhất quán với code hiện tại; validate dữ liệu ở boundary và dùng exception phù hợp.
- Giữ UI responsive: không chạy tác vụ blocking trên UI thread; giữ việc giao tiếp giữa worker và UI theo pattern hiện có.
- Đặt tương tác với hệ điều hành, thiết bị và process bên ngoài sau adapter rõ ràng; xử lý timeout, lỗi và cleanup tài nguyên.
- Giữ cấu hình, dữ liệu runtime, log và artifact build ở đúng vị trí của ứng dụng; không ghi secret hoặc dữ liệu nhạy cảm vào log.
- Không sửa generated output hoặc file đóng gói thủ công nếu repository có source/config làm chuẩn.
- Chạy formatter, linter, type check hoặc test hẹp nhất đã được cấu hình cho phần thay đổi.
