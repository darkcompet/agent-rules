## Quy tắc .NET

- Tuân theo `.editorconfig`, nullable annotations và target framework hiện có vì
  các constraint này ảnh hưởng compile và boundary của project.
- Trong layered/module architecture, giữ dependency theo hướng vào trong và
  không tạo chu trình: Domain sở hữu business rule; Application điều phối use
  case và khai báo contract/port; Infrastructure triển khai persistence và
  external adapter; HTTP xử lý transport/mapping và giữ mỏng. Cách chia này giữ
  business rule độc lập với I/O và ngăn dependency cycle.
- Gọi qua public contract/port tại boundary của module hoặc feature sở hữu. Không
  gọi trực tiếp Infrastructure hay orchestration nội bộ module khác để giảm
  coupling và giữ quyền sở hữu rõ ràng.
- Dùng async API; truyền tiếp cancellation token hiện có để request bị hủy không
  tiếp tục giữ tài nguyên hoặc tạo side effect ngoài ý muốn.
- Tạo migration bằng script của repository; không sửa thủ công generated output,
  migration hoặc snapshot để giữ output đồng bộ với source và metadata của framework.
- Chạy targeted test trước validation diện rộng để nhận feedback nhanh trên phần
  vừa đổi trước khi tốn thời gian cho cả repository.
