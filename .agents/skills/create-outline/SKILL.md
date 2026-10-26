---
name: create-outline
description: Tạo dàn ý bài viết chuẩn SEO từ cụm từ khóa được cung cấp. Chỉ tạo dàn bài, tuyệt đối KHÔNG viết nội dung bài viết.
---

# KỸ NĂNG: TẠO DÀN Ý BÀI VIẾT CHUẨN SEO (/create-outline)

## MỤC TIÊU & PHẠM VI HOẠT ĐỘNG
* Khi người dùng kích hoạt lệnh `/create-outline [cụm từ khóa]` hoặc yêu cầu tạo dàn bài cho 1 từ khóa:
* **PHẠM VI**: Chỉ tập trung nghiên cứu, thiết kế dàn ý, tiêu đề, mô tả và khung kiến trúc bài viết.
* **ĐIỀU CẤM KỴ (CRITICAL DIRECTIVE)**: **TUYỆT ĐỐI KHÔNG VIẾT BÀI CHI TIẾT** ở bước này. Không tạo các đoạn văn hoàn chỉnh của bài viết ngoại trừ đoạn Sapo demo mẫu.

---

## CÁC BƯỚC THỰC THI

1. **Đọc Dữ Liệu Tour Từ `ContentTour/*` & Tiếp Nhận Đúng Danh Sách Từ Khóa**:
   - Mở và đọc nội dung file tour được chỉ định trong thư mục `ContentTour/*` để nắm dữ liệu thực tế (lịch trình từng mốc giờ, giá vé, dịch vụ bao gồm/loại trừ, chính sách phụ thu, điểm tham quan).
   - Xác định Search Intent (Thông tin / Hướng dẫn / So sánh / Dịch vụ...).
   - **QUY ĐỊNH BẮT BUỘC VỀ KEYWORD**: **Chỉ sử dụng đúng số lượng và cụm từ khóa do người dùng cung cấp**. Tuyệt đối **KHÔNG tự ý bịa đặt, suy diễn, mở rộng hay thêm bớt** bất kỳ từ khóa nào khác (không tự thêm "từ khóa liên quan", "từ khóa LSI tự nghĩ", "từ khóa phụ tự chế").

2. **Khởi tạo Bộ Tiêu Đề & Mô Tả**:
   - **3 Tiêu đề SEO (Title)**: Chuẩn 55 - 60 ký tự, tối ưu Key 1 ở đầu (1-2 lần), có số, từ bổ trợ, dấu `|` hoặc `-`, độc nhất và thu hút click.
   - **3 Tiêu đề Thẻ H1 (Tiêu đề bài viết trên trang)**: Chuẩn 55 - 60 ký tự, **KHÁC 100% so với SEO Title**, tối ưu **Key 2** (từ khóa khác Key 1, lấy từ danh sách từ khóa người dùng giao).
   - **2 Thẻ mô tả (Meta Description)**: Chuẩn 140 - 155 ký tự, Key chính ở đầu, không tiết lộ đáp án, có CTA cuối đoạn (*Click xem ngay!*).
   - **1 Đoạn Sapo mẫu**: Ngắn gọn 2 - 3 dòng (<155 từ), thu hút, giải quyết vấn đề của tiêu đề bài viết, Key chính trong 100 từ đầu.
   - ⚠️ **LƯỢC BỎ HIỂN THỊ SỐ KÝ TỰ**: Agent kiểm soát độ dài chuẩn SEO ngầm bên dưới, **tuyệt đối KHÔNG in `(xx ký tự)`** ra Title, Meta Des hay các Headings để người dùng copy dùng ngay.

3. **Cấu trúc Dàn ý Headings (Đánh số 1., 1.1., 1.2., 2., 2.1.,...)**:
   - Tối thiểu **4 phần H2 trở lên**, mỗi H2 có **≥2 mục H3 trở lên**.
   - Mỗi thẻ <60 ký tự (kiểm soát ngầm, **KHÔNG ghi số ký tự cạnh tiêu đề**).
   - **Mục 1 (H2 đầu tiên)**: Bắt buộc chứa từ khóa chính.
   - Phân bổ các từ khóa phụ người dùng cung cấp vào các mục tiếp theo. Các mục còn lại không nhắm key thì tập trung triển khai nội dung thực tế, không chèn gượng ép.
   - **Tỉ lệ từ khóa phải trải đều trong toàn bài và trong từng mục (H2, H3)**:
     - Mật độ không quá dày và không xuất hiện quá gần nhau (tuyệt đối không nhồi 2 key liền kề nhau).
     - Không để khoảng cách quá xa mới xuất hiện key một lần.
     - Dùng câu chữ linh hoạt, uyển chuyển để khi viết bài người đọc luôn cảm thấy tự nhiên, trôi chảy nhất.
   - Đánh dấu Heading trọng tâm ⭐.
   - **Quy cách hiển thị số (Numbering Style)**:
     - Dùng cách đánh số tự nhiên: `1.`, `1.1.`, `1.2.`, `2.`, `2.1.`,...
     - **Tuyệt đối KHÔNG hiển thị nhãn kỹ thuật `H2.1`, `H3.1.1`** trên tiêu đề (khi xuất ra Word, các thẻ này vẫn mang style `Heading 2`, `Heading 3`).
   - **Phong cách trình bày tinh gọn**:
     - **Chỉ đưa ý chính cốt lõi**: Trình bày thông tin dạng **gạch đầu dòng (bullet points)** ngắn gọn, súc tích dựa trên file tour.
     - **Không giải thích dài dòng dưới tiêu đề**: Tuyệt đối không chèn các nhãn thừa như `Mục tiêu nội dung`, `Định dạng`, `Ý triển khai:`, `Hình ảnh:...` dưới từng heading.
     - **Copy & Use Ready**: Toàn bộ tiêu đề và gạch đầu dòng đều sạch sẽ, không có bất kỳ ký hiệu chú thích thừa nào.
     - Kế hoạch hình ảnh, alt text và format hiển thị (Bảng/List) được quy hoạch tập trung tại Bảng Ma Trận ở cuối dàn ý.
   - **PHẦN CUỐI BẮT BUỘC LÀ KẾT LUẬN**:
     - H2 cuối cùng của dàn ý phải là **Kết luận**, không đặt thêm heading nội dung nào sau phần này.
     - **Quy cách viết Kết luận**: Viết thật ngắn gọn, súc tích (chỉ từ 2 - 3 câu ngắn hoặc dưới 50 - 80 từ).
     - Trong Kết luận phải quy hoạch đủ: tóm tắt nhanh giá trị chính, **bắt buộc chứa 1 lần từ khóa chính**, kèm **lời kêu gọi hành động (CTA)** rõ ràng, dứt khoát. Nếu người dùng gửi kèm website/hotline thì đưa vào, không có thì kêu gọi chung, tuyệt đối không tự bịa liên hệ. Tuyệt đối không chèn ảnh hay ghi chú ảnh tại Kết luận.
   - Đảm bảo phần áp chót trước Kết luận được xây dựng kỹ lưỡng.

4. **Lập Bảng Ma Trận Phân Bổ Từ Khóa & Checklist Thẩm Định**:
   - Lập bảng ánh xạ: Heading -> Từ khóa mục tiêu -> Định dạng -> Kế hoạch Ảnh & Ghi chú mô tả ảnh.
   - **Cột "Từ khóa mục tiêu"**: **CHỈ ĐƯỢC PHÉP** điền đúng các từ khóa người dùng đã cung cấp. Các mục không chứa key thì ghi `-` hoặc không chèn key, tuyệt đối không tự bịa thêm cụm từ mới để điền vào.
   - **Kiểm soát rải đều**: Đảm bảo từ khóa phân bố đều khắp các mục, tránh xuất hiện thưa thớt hoặc ngắt quãng quá dài.
   - Kiểm tra đối chiếu với Pre-publish Checklist.

5. **XUẤT BẢN FILE WORD DOCX VÀO THƯ MỤC RESULT/ (CHỈ GIỮ FILE DOCX)**:
   - Đóng gói toàn bộ dàn ý trực tiếp ra file Word `Result/outline.docx`.
   - **Quy tắc tuyệt đối**: **BẮT BUỘC lưu kết quả vào thư mục `Result/`** để tránh mất file, không lưu ở thư mục gốc hoặc trong `ContentTour/`. **KHÔNG để lại file `.md` trong thư mục làm việc của người dùng**. Mọi khâu trung gian được dọn dẹp sạch sẽ ngay sau khi xuất bản.
   - Xác nhận file `Result/outline.docx` được tạo thành công với các styles Word chuẩn (Heading 1-4, Bảng biểu chuyên nghiệp, Bullet point rõ ràng).
   - Bàn giao trực tiếp đường dẫn file `Result/outline.docx` cho người dùng.
   - Hướng dẫn người dùng: dùng `/update-outline [nội dung cần sửa]` nếu cần chỉnh sửa, hoặc `/create-post` để tiến hành viết bài hoàn chỉnh.
