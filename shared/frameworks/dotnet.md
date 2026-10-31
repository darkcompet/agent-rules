## Quy tắc .NET

- Tuân theo `.editorconfig`, nullable annotations và target framework hiện có của
  project.
- Trong layered/module architecture, giữ dependency theo hướng vào trong và
  không tạo chu trình: Domain sở hữu business rule; Application điều phối use
  case và khai báo contract/port; Infrastructure triển khai persistence và
  external adapter; HTTP xử lý transport/mapping và giữ mỏng.
- Gọi qua public contract/port tại boundary của module hoặc feature sở hữu. Không
  gọi trực tiếp Infrastructure hay orchestration nội bộ của module khác.
- Dùng async API; truyền tiếp cancellation token hiện có.
- Tạo migration bằng script của repository; không sửa thủ công generated output,
  migration hoặc snapshot.
- Viết comment và XML docs ngắn gọn bằng English; comment quyết định, constraint,
  thứ tự và invariant không hiển nhiên, không comment code đã rõ.
- Chạy targeted test trước validation diện rộng.
