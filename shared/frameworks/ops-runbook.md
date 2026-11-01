## Quy tắc operations runbook

- Trước khi thêm hoặc sửa procedure, đọc runbook cùng loại và deployment config
  liên quan. Chúng xác định environment, host, directory và thứ tự thao tác thực
  tế; giả định sai có thể khiến người vận hành chạy lệnh sai nơi hoặc sai thứ tự.
- Nêu rõ environment, host, service và working directory để người vận hành biết
  chính xác nơi chạy procedure.
- Dùng command, path, giá trị và kết quả mong đợi chính xác để các bước có thể
  thực hiện và kiểm tra mà không phải tự đoán.
- Đặt phần mô tả hoặc bối cảnh không yêu cầu hành động trong blockquote để phân
  biệt với các bước người đọc phải làm.
- Khai báo variable trước khi sử dụng để mỗi lệnh có đủ input.
- Đặt các thao tác theo thứ tự trong cùng một mục procedure vì bước sau có thể
  phụ thuộc kết quả bước trước.
- Đặt verification làm bước cuối để xác nhận procedure đã đạt kết quả mong đợi.
- Không đưa giá trị secret vào tài liệu để tránh lộ thông tin xác thực.
- Giữ nguyên các environment được hỗ trợ và các nhánh vận hành để không làm mất
  đường triển khai đang được sử dụng.
