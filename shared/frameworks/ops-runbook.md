## Quy tắc operations runbook

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
