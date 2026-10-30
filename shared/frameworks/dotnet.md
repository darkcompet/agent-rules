## Quy tắc .NET

- Tuân theo `.editorconfig`, nullable annotations và target framework hiện có của
  project.
- Giữ dependency theo một chiều, không tạo chu trình; giữ domain rule độc lập với
  HTTP/persistence, HTTP adapter mỏng và application workflow tường minh.
- Dùng async API; truyền tiếp cancellation token hiện có.
- Tạo migration bằng script của repository; không sửa thủ công generated output,
  migration hoặc snapshot.
- Viết comment và XML docs ngắn gọn bằng English; comment quyết định, constraint,
  thứ tự và invariant không hiển nhiên, không comment code đã rõ.
- Chạy targeted test trước validation diện rộng.
