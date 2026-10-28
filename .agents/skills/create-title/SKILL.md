---
name: create-title
description: Tạo bộ tiêu đề SEO Title (55-60 ký tự) và Thẻ H1 (55-70 ký tự) chuẩn SEO: Title và H1 KHÁC NHAU 100%, H1 viết sau Title và thường dài hơn Title, mỗi tiêu đề tối ưu key riêng biệt hoặc khác biệt cấu trúc.
---

# KỸ NĂNG: TẠO BỘ TIÊU ĐỀ SEO TITLE & THẺ H1 (/create-title)

## MỤC TIÊU & PHẠM VI HOẠT ĐỘNG
* Khi người dùng nhập lệnh `/create-title [danh sách từ khóa]` hoặc yêu cầu tạo tiêu đề bài viết:
* Agent đề xuất bộ phương án **SEO Title** và **Thẻ H1** đạt chuẩn SEO tuyệt đối, có đếm ký tự rõ ràng, tuân thủ nghiêm ngặt nguyên tắc độc lập giữa Title và H1.
* **LƯU Ý QUAN TRỌNG KHI XUẤT BẢN BÀI VIẾT**: Nội dung **Title** sẽ được đưa xuống dưới để sử dụng làm tiêu đề chính của bài viết (Heading 1, 16px, in đậm, căn giữa, đặt ngay phía trên đoạn Sapo) chứ không phải H1. Thẻ H1 là trường dữ liệu SEO bổ trợ lưu trong khối thông số Header Block.

---

## QUY TẮC BẮT BUỘC VỀ VIẾT HOA TIÊU ĐỀ (CHỐNG LỖI TITLE CASE)
* **TUYỆT ĐỐI KHÔNG viết hoa chữ cái đầu của từng từ (Cấm Title Case như phong cách tiếng Anh)**:
  * Không viết hoa kiểu: *"Kinh Nghiệm Du Lịch Hà Giang Tự Túc Giá Rẻ"* (SAI).
* **CHỈ VIẾT HOA**:
  1. Chữ cái đầu tiên của tiêu đề (chuẩn ngữ pháp câu).
  2. Tên riêng, địa danh (ví dụ: *Hà Nội, Hà Giang, Trùng Khánh, Lệ Giang, Shangrila, Măng Đen...*).
  3. Tên người, nhân vật lịch sử, tên thương hiệu.
  4. Các ký hiệu/từ viết tắt đặc biệt (ví dụ: *A-Z, TOP 10, 6N5Đ, 2026, GPS...*).
* **CÒN LẠI TẤT CẢ TỪ KHÁC VIẾT THƯỜNG TOÀN BỘ**: Mọi động từ, tính từ, danh từ chung (*tour, du lịch, kinh nghiệm, khám phá, giá tốt, trọn gói, chi tiết, cẩm nang, tự túc, chuẩn nhất...*) đều **bắt buộc viết thường**.
  * Ví dụ chuẩn: `Tour Trùng Khánh Lệ Giang Shangrila 6N5Đ | Giá tốt trọn gói` (ĐÚNG).
  * Ví dụ chuẩn: `Tour Trùng Khánh Lệ Giang Shangrila 6N5Đ trọn gói giá rẻ chuẩn nhất` (ĐÚNG).

---

## NGUYÊN TẮC CỐT LÕI: TIÊU ĐỀ & H1 BẮT BUỘC KHÁC NHAU 100%

1. **Title và H1 là 2 tiêu đề hoàn toàn độc lập**:
   - H1 được viết sau Title và viết dựa vào Title.
   - Thường H1 dài hơn Title do thêm các từ bổ nghĩa.
   - Tuyệt đối KHÔNG dùng chung 1 nội dung, KHÔNG sao chép nguyên văn Title sang H1.
2. **Quy chuẩn xử lý theo số lượng từ khóa**:
   - **Kịch bản 1: Khi người dùng cung cấp từ 2 từ khóa trở lên**:
     * **SEO Title**: Tối ưu **Key 1** (từ khóa chính có Search Intent bao quát hoặc Volume cao nhất).
     * **Thẻ H1**: Tối ưu **Key 2** (từ khóa khác Key 1, bắt buộc lấy từ danh sách từ khóa do người dùng cung cấp).
   - **Kịch bản 2: Khi người dùng CHỈ CUNG CẤP DUY NHẤT 1 TỪ KHÓA (Single Keyword)**:
     * Cả Title và H1 đều chứa từ khóa chính đó, **NHƯNG BẮT BUỘC Title và H1 PHẢI KHÁC NHAU 100% VỀ CÂU CHỮ, CẤU TRÚC NGỮ PHÁP, VẾ PHỤ BỔ TRỢ VÀ GÓC GIẬT TÍT**:
       + **SEO Title**: Giật tít kích thích CTR (Key ở đầu + số + từ bổ trợ uy tín/giá rẻ + dấu `|` hoặc `-`).
         * *Ví dụ*: `Tour Trùng Khánh Lệ Giang Shangrila 6N5Đ | Giá tốt trọn gói` (58 ký tự).
       + **Thẻ H1**: Viết dựa vào Title, bổ sung từ bổ nghĩa, thường dài hơn Title:
         * *Ví dụ*: `Tour Trùng Khánh Lệ Giang Shangrila 6N5Đ trọn gói giá rẻ chuẩn nhất` (66 ký tự).
3. **Cơ chế Tự Rà Soát Chống Trùng Lặp (Self-Check Validation)**:
   - Trước khi trả kết quả, Agent tự động đối chiếu Title và H1.
   - Nếu phát hiện trùng lặp câu chữ (ngoại trừ cụm từ khóa bắt buộc), Agent xem đây là **LỖI NGHIÊM TRỌNG** và bắt buộc phải viết lại H1 ngay lập tức.

---

## TIÊU CHUẨN THỰC THI CHI TIẾT

### 1. Tiêu chuẩn Thẻ Tiêu đề SEO (SEO Title)
* **Tối ưu**: Tập trung tối ưu **Key 1** (hoặc key chính duy nhất).
* **Độ dài**: **55 – 60 ký tự** (đếm chính xác ký tự kể cả dấu cách).
* **Vị trí từ khóa**: Key nằm **ngay đầu tiêu đề**, xuất hiện **1 - 2 lần** (2 lần là tốt nhất nhưng cần tự nhiên, không chèn từ xen giữa cụm key).
* **Thành phần bổ trợ**:
  * Đan xen các cụm từ bổ trợ cho từ khóa chính và từ khóa mở rộng: *chuyên nghiệp, uy tín, giá rẻ nhất, chuẩn nhất...*
  * Chứa con số: *TOP 10, 5+ cách, 3 phương pháp, 6N5Đ...*
  * Dấu ngăn cách khi cần: dùng `|` hoặc `-`.
* **Độ độc nhất (Unique)**: Title là duy nhất, chưa ai dùng (kiểm tra bằng cú pháp: `Allintitle:"từ khóa"`).
* **Viết hoa**: Tuân thủ quy tắc Sentence case (không viết hoa chữ cái đầu của mọi từ, chỉ viết hoa chữ đầu câu, địa danh, tên người, từ đặc biệt).

### 2. Tiêu chuẩn Thẻ H1 (Tiêu đề trên trang)
* **Quy trình**: Viết H1 sau và viết dựa vào Title.
* **Độ dài**: **55 – 70 ký tự** (thường dài hơn Title bằng cách thêm các từ bổ nghĩa cho Title).
* **Khác biệt 100% so với Title**: Câu cú, cấu trúc, cách giật tít và từ ngữ bổ trợ khác biệt hoàn toàn với SEO Title.
* **Văn phong**: Tự nhiên, hấp dẫn, bao quát toàn bộ nội dung bài viết và chuẩn SEO.
* **Viết hoa**: Chỉ viết hoa chữ đầu câu, tên riêng, địa danh, từ đặc biệt; còn lại viết thường.
* **Quy cách**: Duy nhất 1 thẻ H1 trên trang web.

---

## ĐẦU RA YÊU CẦU

Khi người dùng cung cấp từ khóa, Agent đề xuất:
1. **3 phương án SEO Title** (tối ưu Key 1 ở đầu câu, đạt 55 - 60 ký tự, đúng quy tắc viết hoa, có đếm ký tự và giải thích lý do).
2. **3 phương án Thẻ H1** (viết dựa theo Title, thường dài hơn Title, đạt 55 - 70 ký tự, KHÁC 100% so với Title, đúng quy tắc viết hoa, có đếm ký tự).
