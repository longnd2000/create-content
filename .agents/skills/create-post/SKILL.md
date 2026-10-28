---
name: create-post
description: Đọc dàn bài đã duyệt từ file Result/outline.docx và tiến hành viết bài viết hoàn chỉnh chuẩn SEO 100%, xuất trực tiếp ra file .docx chuẩn Heading 1 - Heading 6 trong thư mục Result/.
---

# KỸ NĂNG: VIẾT BÀI HOÀN CHỈNH XUẤT RA FILE DOCX (/create-post)

## MỤC TIÊU & PHẠM VI HOẠT ĐỘNG
* Khi người dùng nhập lệnh `/create-post`:
* Agent hiểu rằng người dùng đã chốt dàn ý trong `Result/outline.docx` và kích hoạt bước viết bài viết hoàn chỉnh.
* **Định dạng đầu ra bắt buộc**: Xuất trực tiếp ra file Word **`.docx`** trong thư mục **`Result/`** (ví dụ: `Result/bai-viet.docx` hoặc theo slug từ khóa) với đầy đủ định dạng chuẩn **Heading 1, Heading 2, Heading 3, Heading 4, ...** của Microsoft Word.
* **Quy chuẩn trình bày bắt buộc**: Toàn bộ nội dung sử dụng font **Google Sans Flex**. Cỡ chữ chung là **13px**; tiêu đề chính Heading 1 dùng **16px**, in đậm và căn giữa. Nội dung các đoạn văn căn đều hai bên. Toàn bộ chữ dùng màu đen mặc định; ngoại lệ duy nhất là ghi chú ảnh trong ngoặc đơn được bôi đỏ theo quy định bên dưới.
* **Cấm ký tự trang trí và icon**: Không chèn emoji, icon hoặc ký tự trang trí như `⭐`, `📷` và các biểu tượng tương tự vào tiêu đề, nội dung, bảng, danh sách, ghi chú ảnh hay phần thông tin đầu bài. Chỉ sử dụng chữ, số và dấu câu phù hợp với phong cách bài viết. Danh sách gạch đầu dòng chỉ dùng khi cần thiết và phải dùng định dạng danh sách Word sạch.
* **Quy tắc tuyệt đối**: **KHÔNG tạo hoặc lưu trữ file `.md` trong thư mục làm việc của người dùng**. Mọi khâu chuyển đổi nhị phân (nếu cần file tạm) đều được xử lý ngầm và tự động xóa ngay, trả lại thư mục sạch sẽ chỉ có file `.docx` trong thư mục `Result/`.

---

## QUY CHUẨN VIẾT HOA TIÊU ĐỀ VÀ CÁC THẺ HEADINGS (TITLE, H1, H2, H3, H4...)
* **CẤM TUYỆT ĐỐI phong cách viết hoa chữ cái đầu của mỗi từ (Title Case tiếng Anh)**:
  * SAI: `Kinh Nghiệm Du Lịch Hà Giang Tự Túc Giá Rẻ`
  * SAI: `Lịch Trình Chi Tiết Khám Phá Tour Trùng Khánh 6N5Đ`
* **QUY TẮC BẮT BUỘC**:
  1. Chỉ viết hoa chữ cái đầu tiên của câu/tiêu đề/heading (sau số thứ tự).
  2. Bắt buộc viết hoa đúng chính tả: Địa danh (*Hà Nội, Hà Giang, Măng Đen, Trùng Khánh, Lệ Giang...*), tên người, tên thương hiệu, ký hiệu/từ viết tắt đặc biệt (*A-Z, TOP 10, 6N5Đ, Zalo...*).
  3. **TẤT CẢ CÁC TỪ THÔNG THƯỜNG CÒN LẠI VIẾT THƯỜNG TOÀN BỘ**: Mọi động từ, tính từ, danh từ chung (*kinh nghiệm, du lịch, tự túc, trọn gói, giá tốt, lịch trình, chi tiết, cẩm nang, khám phá, hướng dẫn, lưu ý thực tế...*) đều **bắt buộc viết chữ thường**.
  * ĐÚNG: `Tour Trùng Khánh Lệ Giang Shangrila 6N5Đ | Giá tốt trọn gói`
  * ĐÚNG: `1.1. Lịch trình chi tiết khám phá Hà Giang 3 ngày 2 đêm`
  * ĐÚNG: `2. Kinh nghiệm ăn uống và chuẩn bị hành lý khi đi tour`

---

## CÁC BƯỚC THỰC THI

1. **Đọc và Phân Tích Dữ Liệu Từ `Result/outline.docx` & Xác Định Nguồn Dữ Liệu (Tour vs Blog)**:
   - Sử dụng công cụ đọc Word trực tiếp:
     ```powershell
     python .agents/scripts/read_docx.py Result/outline.docx
     ```
   - **Xác định dạng bài viết từ Dàn ý**:
     * **Bài viết Tour (`[tour]`)**: Đối chiếu chi tiết với file tour thực tế trong thư mục `ContentTour/*` (sử dụng `read_tour_file.py`) để đảm bảo số liệu, giá tour, mốc giờ, địa điểm chính xác 100%. Tuyệt đối không chỉnh sửa hay ghi đè file tài liệu gốc trong `ContentTour/*`.
     * **Bài viết Blog (`[blog]`)**: Triển khai chuyên sâu theo các đề mục dàn ý đã được duyệt, phân tích cặn kẽ các ý mới mẻ H2, H3, đưa vào các dữ liệu thực tế, kinh nghiệm đời thường sinh động, đảm bảo tỷ lệ Human Content ≥ 95%.

2. **Triển Khai Viết Nội Dung Chuẩn SEO & Giọng Văn Người Thật (BẮT BUỘC TUÂN THỦ)**:
   - **CẤU TRÚC PHẦN MỞ ĐẦU BÀI VIẾT (MASTER HEADER BLOCK FORMAT)**:
     - Mọi file Word bài viết bắt buộc bắt đầu bằng đúng thứ tự chuẩn hóa:
       1. **Bảng Thống kê Từ khóa**: Cột KEY và Cột VOLUME (bảng nền trắng, chữ màu đen; không tô màu ô, không dùng màu chữ; có thể in hoa/in đậm phần tiêu đề cột để dễ đọc; Cột VOLUME căn giữa).
       2. Dòng Check spin: (chừa trống để ghi nhận)
       3. Dòng Check AI: (chừa trống để ghi nhận)
       4. Dòng Key chính: [Từ khóa chính]
       5. Dòng Meta: [Nội dung Meta Description 140 - 155 ký tự có CTA, gợi nỗi đau và giải pháp]
       6. Dòng Title: [Nội dung SEO Title 55 - 60 ký tự, tối ưu Key 1 ở đầu, có số, từ bổ trợ, dấu | hoặc -, đúng quy tắc viết hoa]
       7. Dòng H1: [Nội dung Thẻ H1 55 - 70 ký tự - viết dựa vào Title, bổ nghĩa cho Title, thường dài hơn Title, đúng quy tắc viết hoa và BẮT BUỘC KHÁC 100% SO VỚI SEO TITLE]
       8. **Tiêu đề chính bài viết trên trang (Heading 1 - 16px, in đậm, căn giữa)**:
          - **QUY CHUẨN BẮT BUỘC: ĐƯA TIÊU ĐỀ (TITLE) XUỐNG DƯỚI ĐỂ SỬ DỤNG, CHỨ KHÔNG PHẢI H1**:
          - Ngay bên dưới dòng `H1:`, trước khi vào đoạn mở bài (Sapo), bắt buộc có Tiêu đề chính bài viết (Style Heading 1 của Word, font Google Sans Flex 16px, in đậm, căn giữa).
          - Tiêu đề này **BẮT BUỘC LẤY CHÍNH XÁC NỘI DUNG TỪ DÒNG `Title` (SEO TITLE) ĐƯA XUỐNG ĐỂ SỬ DỤNG ĐĂNG BÀI/HIỂN THỊ TRÊN WEBSITE**, tuyệt đối **KHÔNG LẤY `H1`**.
          - Dòng `Title:` và `H1:` ở trên là text thông số kỹ thuật bình thường (13px), còn tiêu đề sử dụng thực tế của bài viết hiển thị phía trên Sapo là Title.
       9. **Đoạn mở bài (Sapo)**: Nằm ngay dưới Tiêu đề chính bài viết (Title đưa xuống), **ngắn gọn 2 - 3 câu (<155 từ), thu hút, bắt buộc chứa Key chính trong 100 từ đầu và khéo léo nhắc tên thương hiệu của công ty (tên thương hiệu công ty bắt buộc được gắn link website chính thức theo dạng anchor text `[Tên công ty](URL website)`)** nhằm giải quyết trực diện vấn đề của tiêu đề bài viết và định vị thương hiệu. Tiếp sau đó là các Heading thân bài 1., 1.1... (chủ động khai thác ý mới mẻ, góc nhìn độc đáo cho từng đề mục H2, H3).
       - **THẺ H1 BẮT BUỘC KHÁC BIỆT 100% SO VỚI SEO TITLE (NGHIÊM CẤM TRÙNG LẶP TUYỆT ĐỐI)**:
      - **SEO Title**: Chuẩn 55 - 60 ký tự, tối ưu **Key 1** ở đầu, có số, từ bổ trợ, dấu `|` hoặc `-`, độc nhất và thu hút click từ Google.
      - **Thẻ H1 (Tiêu đề trên trang)**: Chuẩn **55 - 70 ký tự**, viết sau Title và dựa vào Title để thêm từ bổ nghĩa, thường dài hơn Title, **BẮT BUỘC KHÁC 100% SO VỚI SEO TITLE TRONG MỌI TRƯỜNG HỢP**:
        * **Nếu có từ 2 từ khóa trở lên**: Tối ưu **Key 2** (chọn từ danh sách từ khóa người dùng giao).
        * **Nếu chỉ có DUY NHẤT 1 từ khóa**: Dựa vào Title để thêm từ bổ trợ, mở rộng góc nhìn khám phá từ A-Z.
      - **Cơ chế Tự Rà Soát (Self-Check Validation)**: Trước khi xuất file `.docx`, Agent phải tự đối chiếu giữa dòng `Title:` và dòng `H1:`. Nếu phát hiện Title trùng H1, Agent BẮT BUỘC viết lại H1 ngay lập tức để đạt khác biệt 100%.

   - **PHẦN CUỐI BÀI BẮT BUỘC LÀ KẾT LUẬN (VIẾT THẬT NGẮN GỌN, CTA ZALO & THƯƠNG HIỆU)**:
     - Heading cuối cùng của bài phải là **Kết luận**. Sau phần Kết luận không thêm heading hoặc nội dung triển khai mới.
     - **YÊU CẦU ĐỘ DÀI KẾT BÀI**: Viết **thật ngắn gọn, cô đọng (chỉ từ 2 - 3 câu ngắn hoặc tối đa 50 - 80 từ)**. Tuyệt đối không kéo dài lê thê, không viết dài dòng, không thêm thắt các đoạn tổng kết triết lý rườm rà.
     - Kết luận phải gồm đủ 3 lớp nội dung tinh gọn: (1) Kết thúc và tóm tắt nhanh giá trị cốt lõi nhất của chuyến đi (**bắt buộc chứa 1 lần từ khóa chính**), (2) **Lời kêu gọi hành động (CTA) dứt khoát gắn liền với số Zalo tư vấn và tên thương hiệu của công ty** (kèm website nếu có) để người đọc liên hệ nhận tư vấn/đặt tour ngay, (3) Thông tin website/hotline nếu người dùng gửi kèm theo lệnh /create-post.
     - **Tuyệt đối không chèn ảnh hay ghi chú note ảnh trong phần Kết luận**.

   - **QUY CHUẨN TRIỂN KHAI THÂN BÀI (BODY CONTENT)**:
     - **Mức độ dễ đọc (Readability)**: Chia thành từng đoạn text nhỏ (2 - 3 câu/đoạn). Có câu chuyển mạch lạc giữa các heading, tránh viết khối text dài mà không có ảnh hoặc điểm nghỉ.
     - **Đa dạng hóa nội dung**: Tích cực dùng **Bảng biểu (Table)** hoặc **Danh sách (List)** để làm đa dạng hóa cách hiển thị nội dung theo đúng chỉ định trong outline.
     - **Không lỗi chính tả & Số liệu chuẩn xác**: Số liệu phải chính xác tuyệt đối, có tham chiếu từ nguồn rõ ràng.
     - **Spin Text các đề mục Outline**: Các thẻ heading và ý gợi ý trong outline là định hướng nội dung; khi viết bài bắt buộc **spin text / diễn đạt lại bằng từ ngữ mới** để tránh trùng lặp mà không thay đổi ý nghĩa gốc.
     - **Phạm vi nội dung**: Không viết chi tiết đi quá sâu vào các ý phụ mà đã có bài viết chính riêng trên website (tránh loãng bài và ăn thịt từ khóa).
     - **Heading trọng tâm ⭐**: Khi gặp heading được đánh dấu quan trọng trong outline, dồn trọng tâm triển khai sâu sắc, chi tiết, dẫn dắt người đọc thu hút nhất.
     - **Heading áp chót trước Kết luận**: H3 hoặc H2 cuối cùng gần Kết luận **tuyệt đối không viết quá ngắn** (tránh nhìn vào thấy kết luận như 1 phần của H3/H2 đó).
     - **Nguyên tắc ưu tiên số 1**: Trong trường hợp quá khó để viết khác mà vẫn đảm bảo hiển thị từ khóa, **Ưu tiên sự viết khác và văn phong tự nhiên hơn là gượng ép tuân thủ từ khóa**.

   - **CHIẾN LƯỢC TỐI ƯU VÀ PHÂN BỔ TỪ KHÓA (KEYWORD STRATEGY)**:
     - **Mật độ từ khóa chuẩn SEO**: Duy trì từ **1.5% – 3.0%** trên toàn bài.
     - **Định dạng từ khóa**: Sử dụng linh hoạt và tự nhiên các định dạng **in đậm**, *in nghiêng*, <u>gạch chân</u> cho từ khóa chính và từ khóa mở rộng ở các vị trí đắc địa.
     - **Ứng dụng 3 nhóm từ khóa**:
       * **Từ khóa chính xác**: Là từ khóa chủ đạo bài viết nhắm đến. Xuất hiện đầu tiên ở các khu vực quan trọng:
         + **Mở bài (Sapo)**: 1 lần từ khóa chính (trong 100 từ đầu).
         + **H2 đầu tiên**: 1 lần từ khóa chính.
         + **Kết luận**: 1 lần từ khóa chính.
         *Lưu ý*: Mật độ không cần lặp lại từ chính xác quá dày, dùng các từ "đồng nghĩa" để thay thế nhằm tránh nhồi nhét key.
       * **Từ khóa đồng nghĩa**: Dùng để thay thế cho từ khóa chính nhằm mục đích tự nhiên hóa văn phong và tránh nhồi nhét. Áp dụng hợp lý tùy ngữ cảnh, không máy móc.
       * **Từ khóa liên quan (LSI/Subtopic)**: Nói đến một khía cạnh nhỏ/ngách bổ sung ý nghĩa cho từ khóa chính, xuất hiện ở các H2/H3 sau hoặc một đoạn nhỏ trong bài.
     - **Phân bổ trong các phân đoạn H3**: Trong phần triển khai nội dung của mỗi H3, **chỉ nên có tối đa 1 từ khóa**.
     - **Vị trí xuất hiện**: Tránh đặt key ngay sát mép dưới tiêu đề; nên để key xuất hiện tự nhiên ở giữa đoạn văn sau 1-2 câu dẫn nhập.

   - **QUY CHUẨN MÔ TẢ HÌNH ẢNH NGẮN GỌN & DỄ HIỂU (SIMPLE IMAGE NOTES)**:
     - Trung bình mỗi **250 từ** hoặc mỗi **H2/H3 phù hợp** chèn một dòng ghi chú mô tả ảnh **ngắn gọn, đơn giản, dễ hiểu**, đặt trong ngoặc đơn (...) ngay tại vị trí cần chèn ảnh.
     - Ghi chú text thường màu đỏ `#C00000`, không in đậm, không icon, không đóng khung. (Ví dụ: `(Ảnh khách chụp tại Cột Cờ Lũng Cú buổi sáng)`).
     - Tuyệt đối không chèn ảnh hay note ảnh trong phần Kết luận.

   - **CẮT BỎ HOÀN TOÀN HOA MỸ & MẪU CÂU AI (Strict Anti-AI & Human Voice)**:
     - Tỷ lệ AI Content bắt buộc **dưới 5% (Human Content ≥ 95%)**, tỷ lệ trùng lặp Spin bằng **0%**.
     - CẤM các cấu trúc máy móc: "bạn nên...", "bạn phải...", "bạn cần...", "bạn hãy...", "du khách nên/cần/phải...". Thay bằng các câu mô tả trải nghiệm khách quan.
     - CẤM từ ngữ sáo rỗng: *“điểm hẹn trong mơ”, “những tâm hồn mê xê dịch”, “hít căng lồng ngực”, “bức tranh tuyệt mỹ”, “thiên đường nơi hạ giới”, “đắm say lòng người”*.

   - **QUY CHUẨN FONT VÀ CỠ CHỮ**:
     - Font: **Google Sans Flex** toàn bài.
     - Tiêu đề chính Heading 1: **16px**, in đậm, căn giữa.
     - Thân bài & Heading phụ: **13px**. Đoạn văn căn đều hai bên.
     - Bảng biểu: Viền đen, nền trắng, chữ đen, dòng tiêu đề in đậm căn giữa.

3. **Đóng Gói Trực Tiếp Sang File `.docx` Vào Thư Mục `Result/`**:
   - Agent biên dịch nội dung hoàn chỉnh và xuất bản trực tiếp ra file Word trong thư mục `Result/` (ví dụ `Result/bai-viet.docx` hoặc theo slug từ khóa).
   - Bảo toàn nguyên vẹn thư mục `ContentTour/*`. Xóa ngay mọi tệp tạm (nếu phát sinh), không để lại file `.md` trong thư mục làm việc.
   - Xác nhận file `.docx` trong thư mục `Result/` hoàn tất với đầy đủ styles Word chuẩn: Heading 1 -> Heading 4, bảng chuẩn, không icon/emoji thừa, tuân thủ đúng quy cách viết hoa chữ cái đầu tiêu đề và headings.

4. **Bàn Giao Cho Người Dùng**:
   - Gửi đường link trực tiếp đến file Word `.docx` trong thư mục `Result/` để người dùng click mở ngay.
   - Đính kèm bảng Checklist đối soát Pre-publish tóm tắt các chỉ số kỹ thuật của bài viết.
