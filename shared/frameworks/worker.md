## Quy tắc Worker

- Đặt startup và composition của process trong host project.
- Đặt orchestration trong application service và adapter trong infrastructure.
- Truyền cancellation qua I/O và background work.
- Giới hạn concurrency và dọn temporary workspace.
- Không ghi log credential, token hoặc private URL.
- Kiểm thử behavior của public protocol và xử lý lỗi.
