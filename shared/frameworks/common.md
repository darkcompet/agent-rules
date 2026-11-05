## Quy tắc repository

- Đọc tài liệu gần nhất trước khi đổi behavior vì tài liệu có thể định nghĩa
  contract mà implementation phải giữ.
- Tuân theo ngôn ngữ, tooling và cấu trúc thư mục hiện có để thay đổi mới chạy
  trong môi trường và quy trình mà repository đang hỗ trợ.
- Dùng script và dependency hiện có trước khi thêm cái mới để tránh trùng chức
  năng và chi phí bảo trì.
- Khi thay đổi code, config, script hoặc tài liệu vận hành, rà các boundary có
  liên quan về quyền truy cập, dữ liệu nhạy cảm, secret và side effect. Giữ
  nguyên cơ chế bảo vệ đã có; không đưa thông tin nhạy cảm vào output/log hoặc
  mở rộng quyền truy cập ngoài yêu cầu.
