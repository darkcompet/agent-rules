## Quy tắc operations runbook

- Mỗi chỉ dẫn phải ngắn, dễ đọc lướt và nêu một hành động. Đặt giải thích,
  bối cảnh và kết quả mong đợi không yêu cầu hành động trong blockquote.
- Khi giải thích hoặc hướng dẫn người dùng, AI phải viết ngắn gọn, chỉ nêu thông
  tin cần thiết và không vượt quá 2 dòng; bỏ giải thích dài dòng hoặc thông tin
  không hữu ích.
- Trước khi dùng placeholder, nêu ngắn cách lấy hoặc chọn giá trị, hoặc khai báo
  thành variable. Không để placeholder không rõ nguồn.
- Với giá trị người dùng cần chọn hoặc điền, ưu tiên ví dụ cụ thể đúng định dạng
  kèm phần cần thay; tránh giải thích dài cách suy ra giá trị. Ví dụ:
  ```sh
  # Tenant acme, environment prod
  ALIAS='alias/acme-prod-ncp-project-secrets'
  ./scripts/secrets/ensure_project_secret_kms_key.py --alias "$ALIAS"
  ```
  Ghi rõ `acme` và `prod` là giá trị mẫu cần thay. Nếu có các trường hợp khác
  nhau, nêu mỗi trường hợp bằng một ví dụ ngắn.
- Trước khi viết hoặc sửa procedure, đọc runbook hiện hành, operational spec đã
  được phê duyệt và deployment config liên quan. Runbook quy định workflow;
  spec xác định ý định đã duyệt; config cung cấp chi tiết triển khai. Nếu các
  nguồn mâu thuẫn và không xác định được procedure đúng, dừng thay đổi trên host
  và hỏi owner.
- Mỗi procedure phải nêu environment, host, service, working directory, điều
  kiện tiên quyết, entrypoint, command/path theo đúng thứ tự, kết quả mong đợi
  và bước verification cuối cùng. Ghi rõ cách cung cấp variable; tham chiếu
  secret qua secret manager hoặc cơ chế bảo mật tương ứng, không ghi giá trị
  secret.
- Khi sửa procedure, rà quyền cần thiết, environment/host đích, phạm vi side
  effect và dữ liệu có thể xuất hiện trong output/log. Dùng quyền tối thiểu, giữ
  secret ngoài command/output/tài liệu và không mở rộng thao tác phá huỷ ngoài
  contract đã duyệt.
- Khi setup, reconcile, deploy, recovery hoặc vận hành service, mọi người và AI
  phải chạy đúng entrypoint và thứ tự bước của runbook cho environment/host đã
  chọn. Không tự ghép lệnh/script để thay procedure, bỏ qua bước hoặc né
  entrypoint đã định nghĩa.
- Nếu một bước thất bại, dừng mọi thao tác làm thay đổi trạng thái trên host hoặc
  environment; chỉ thực hiện điều tra read-only tại đó. Có thể sửa source/config
  của implementation mà procedure sử dụng ở ngoài host, rồi chạy lại theo đúng
  retry/resume procedure trong runbook. Không dùng lệnh/script workaround tự tạo.
  Nếu runbook không quy định cách retry/resume, không tự chọn bước để chạy tiếp.
- Nếu procedure thiếu, sai hoặc entrypoint không còn hợp lệ, không tự tạo cách
  vận hành thay thế. Chỉ cập nhật runbook khi procedure đúng xác định được từ ý
  định đã duyệt và deployment config; sau đó tiếp tục bằng entrypoint trong
  runbook đã cập nhật. Nếu chưa xác định được, dừng và hỏi owner.
