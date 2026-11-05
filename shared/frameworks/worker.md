## Quy tắc Worker

- Đặt startup và composition của process trong host project để host kiểm soát
  lifecycle và dependency composition.
- Đặt orchestration trong application service và adapter trong infrastructure để
  giữ I/O ở boundary.
- Truyền cancellation qua I/O và background work để shutdown không để lại task
  hoặc side effect chạy ngầm.
- Giới hạn concurrency và dọn temporary workspace để kiểm soát tài nguyên và
  tránh dữ liệu tạm tồn đọng.
- Không ghi log credential, token hoặc private URL để tránh lộ thông tin truy cập.
- Sau khi implement hoặc fix, rà authorization trước side effect, validation của
  message/event không tin cậy, quyền egress và dữ liệu nhạy cảm trong log/artifact.
  Giữ retry và xử lý lỗi trong giới hạn đã định nghĩa để không nhân side effect.
- Kiểm thử behavior của public protocol và xử lý lỗi để bảo vệ caller tích hợp.
