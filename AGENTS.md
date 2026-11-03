# Ngôn ngữ trả lời

- Mọi câu trả lời, giải thích, câu hỏi và báo cáo cho task owner phải viết bằng tiếng Việt.
- Dùng English cho thuật ngữ IT, tên lệnh, path và identifier.

# Mục đích repository

- Repository này duy trì các agent rules dùng chung và phân phối chúng tới các
  target projects bằng `sync.py`.
- Với task về nội dung rules được áp dụng cho target projects, xem `shared/` là
  nguồn canonical: kiểm tra và sửa file phù hợp trong `shared/`, không sửa
  `AGENTS.md` ở root như thể đó là nguồn rules được phân phối.
