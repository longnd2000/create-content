---
name: update-outline
description: Cập nhật, chỉnh sửa dàn bài hiện tại dựa trên phản hồi của người dùng và ghi nhớ lại trạng thái. Tuyệt đối KHÔNG viết bài.
---

# KỸ NĂNG: CẬP NHẬT DÀN Ý BÀI VIẾT (/update-outline)

## MỤC TIÊU & PHẠM VI HOẠT ĐỘNG
* Khi người dùng nhập lệnh `/update-outline [nội dung góp ý / yêu cầu sửa]`:
* Agent tiếp nhận các điểm người dùng chưa hài lòng (thêm bớt heading, đổi góc nhìn, thay Title, đổi format bảng/list...).
* **PHẠM VI**: Cập nhật chỉnh sửa Dàn ý hiện có.
* **ĐIỀU CẤM KỴ (CRITICAL DIRECTIVE)**: **TUYỆT ĐỐI KHÔNG VIẾT BÀI CHI TIẾT**. Vẫn chỉ làm việc trên dàn ý (outline).

---

## CÁC BƯỚC THỰC THI

1. **Đọc Dàn Ý Hiện Tại Từ `Result/outline.docx`**:
   - Sử dụng công cụ đọc Word trực tiếp:
     ```powershell
     python .agents/scripts/read_docx.py Result/outline.docx
     ```
   - Nắm rõ toàn bộ cấu trúc hiện tại (Title, Meta Des, H1, Sapo, các Heading H2-H3 và bảng Ma trận).

2. **Phân tích Yêu Cầu Chỉnh Sửa Của Người Dùng**:
   - Xác định chính xác các điểm cần thay đổi (ví dụ: đổi Title, thêm 1 H2 về giá cả, bỏ H3 không cần thiết, đổi vị trí bảng so sánh...).
   - Đảm bảo các thay đổi mới vẫn tuân thủ nghiêm ngặt quy chuẩn SEO (H2 đầu có key chính, Title 55-60 ký tự, mỗi H2 ≥2 H3, v.v.).

3. **Cập Nhật Cấu Trúc & Ma Trận Phân Bổ**:
   - Điều chỉnh lại các thẻ Headings, kế hoạch ảnh, bảng biểu và ma trận từ khóa.
   - Giữ nguyên các phần đã tối ưu mà người dùng không yêu cầu sửa.

4. **XUẤT BẢN VÀ CẬP NHẬT TRỰC TIẾP FILE `Result/outline.docx`**:
   - Ghi đè cập nhật trực tiếp vào file Word `Result/outline.docx` trong thư mục `Result/`.
   - **Tuyệt đối KHÔNG để file `.md` trong thư mục làm việc**. Dọn dẹp mọi tệp tạm phát sinh.
   - Báo cáo rõ ràng: Những điểm nào đã được sửa đổi theo yêu cầu.
   - Gửi đường dẫn file `Result/outline.docx` đã cập nhật để người dùng mở xem trực tiếp trên Word.
   - Nhắc nhở người dùng: Nếu vẫn muốn sửa tiếp thì gõ `/update-outline [ý kiến]`, nếu đã ưng ý thì gõ `/create-post` để bắt đầu viết bài.
