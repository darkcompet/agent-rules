## Quy tắc React

- Tuân theo pattern component/state hiện có; tái sử dụng design system và semantic
  token để giữ state ownership và trải nghiệm UI nhất quán.
- Thể hiện rõ các trạng thái loading, error, empty, responsive và accessibility
  để người dùng hiểu kết quả thao tác và có thể dùng UI bằng nhiều phương thức.
- Đặt durable state tại component/feature sở hữu nó; tránh abstraction chỉ dùng
  cho một component hoặc call site để tránh state trùng và indirection không cần.
- Chạy typecheck, lint hoặc build hẹp nhất phù hợp để bắt lỗi thuộc phạm vi đổi.
