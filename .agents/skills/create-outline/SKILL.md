---
name: create-outline
description: Tạo dàn ý bài viết chuẩn SEO cho 2 dạng: [tour] (dựa trên file tour) hoặc [blog] (khảo sát dàn ý 10 đối thủ TOP đầu, sắp xếp đúng đủ intent, tìm ý mới H2/H3). Tuyệt đối KHÔNG viết bài.
---

# KỸ NĂNG: TẠO DÀN Ý BÀI VIẾT CHUẨN SEO (/create-outline)

## MỤC TIÊU & PHẠM VI HOẠT ĐỘNG
* Khi người dùng kích hoạt lệnh `/create-outline <cụm từ khóa> [tour|blog]` hoặc yêu cầu tạo dàn bài:
  * **HẬU TỐ [tour] (Dạng bài viết Tour du lịch)**: Xây dựng bài viết giới thiệu/bán tour, giữ nguyên cấu trúc tour hiện tại dựa trên tài liệu thực tế từ file trong `ContentTour/*`.
  * **HẬU TỐ [blog] (Dạng bài viết Blog / Cẩm nang chia sẻ)**: Xây dựng bài viết cẩm nang, kinh nghiệm. Agent **bắt buộc khảo sát dàn ý của 10 đối thủ đầu tiên (TOP 10 SERP Google)** qua công cụ `search_web`, sắp xếp cấu trúc logic giải quyết đúng và đủ Search Intent của người đọc, đồng thời **tìm tòi các ý mới mẻ, độc đáo trong các thẻ H2, H3** để tạo sự khác biệt vượt trội.
  *(Nếu người dùng không ghi rõ tag, mặc định là `[tour]` nếu có kèm file tour trong `ContentTour/*`, hoặc là `[blog]` nếu là từ khóa thông tin/kinh nghiệm).*
* **PHẠM VI**: Chỉ tập trung nghiên cứu, thiết kế dàn ý, tiêu đề, mô tả và khung kiến trúc bài viết.
* **ĐIỀU CẤM KỴ (CRITICAL DIRECTIVE)**: **TUYỆT ĐỐI KHÔNG VIẾT BÀI CHI TIẾT** ở bước này. Không tạo các đoạn văn hoàn chỉnh của bài viết ngoại trừ đoạn Sapo demo mẫu.

---

## QUY TẮC BẮT BUỘC VỀ VIẾT HOA TIÊU ĐỀ & HEADINGS (H1, H2, H3, H4...)
* **CẤM TUYỆT ĐỐI phong cách viết hoa chữ cái đầu của mỗi từ (Title Case tiếng Anh)**:
  * SAI: `1.1. Kinh Nghiệm Du Lịch Hà Giang Tự Túc Tiết Kiệm Nhất`
  * SAI: `2. Lịch Trình Chi Tiết Khám Phá Tour Trùng Khánh 6N5Đ`
* **QUY TẮC CHUẨN**:
  1. Chỉ viết hoa chữ cái đầu tiên của câu/tiêu đề (sau số thứ tự).
  2. Bắt buộc viết hoa đúng chính tả: Địa danh (*Hà Nội, Hà Giang, Măng Đen, Trùng Khánh...*), tên người, tên thương hiệu, ký hiệu/từ viết tắt đặc biệt (*A-Z, TOP 10, 6N5Đ, Zalo...*).
  3. **Tất cả các từ thông thường còn lại VIẾT THƯỜNG TOÀN BỘ** (*kinh nghiệm, du lịch, tự túc, chi tiết, lịch trình, khám phá, giá tốt, hướng dẫn, lưu ý...*).
  * ĐÚNG: `1.1. Kinh nghiệm du lịch Hà Giang tự túc tiết kiệm nhất`
  * ĐÚNG: `2. Lịch trình chi tiết khám phá tour Trùng Khánh 6N5Đ`

---

## CÁC BƯỚC THỰC THI

1. **Tiếp Nhận Từ Khóa & Phân Nhánh Xử Lý Theo Định Dạng ([tour] vs [blog])**:
   - **QUY ĐỊNH BẮT BUỘC VỀ KEYWORD**: **Chỉ sử dụng đúng số lượng và cụm từ khóa do người dùng cung cấp**. Tuyệt đối **KHÔNG tự ý bịa đặt, suy diễn, mở rộng hay thêm bớt** bất kỳ từ khóa nào khác.
   - **NHÁNH 1: DẠNG BÀI TOUR (`[tour]`)**:
     * Mở và đọc nội dung file tour được chỉ định trong thư mục `ContentTour/*` để nắm dữ liệu thực tế (lịch trình từng mốc giờ, giá vé, dịch vụ bao gồm/loại trừ, chính sách phụ thu, điểm tham quan).
     * Giữ nguyên cấu trúc tour chuẩn: Giới thiệu tour, Điểm nhấn hành trình, Lịch trình chi tiết từng ngày, Bảng giá & Chính sách, Kinh nghiệm & Lưu ý khi đi tour, Kết luận.
   - **NHÁNH 2: DẠNG BÀI BLOG (`[blog]`)**:
     * **Khảo sát dàn ý 10 đối thủ đầu tiên (TOP 10 SERP)**: Gọi công cụ `search_web` tìm kiếm từ khóa chính để thu thập và nghiên cứu cấu trúc đề mục (Headings H2, H3) của 10 trang web đang đứng đầu Google.
     * **Sắp xếp hợp lý, đúng và đủ Intent người đọc**:
       + Phân tích toàn diện nhu cầu tìm kiếm (Search Intent): Người đọc muốn biết gì? (Khái niệm, thời điểm đẹp nhất, cách di chuyển, địa điểm ăn chơi, chi phí, lịch trình tự túc gợi ý, lưu ý thực tế...).
       + Gom nhóm các ý cốt lõi, loại bỏ thông tin rác/thừa/trùng lặp của đối thủ; sắp xếp trật tự các phần mạch lạc, logic theo luồng suy nghĩ của người đọc.
     * **Tìm ý mới mẻ trong thẻ H2, H3 (Information Gain & Content Freshness)**:
       + Đào sâu tìm tòi các góc tiếp cận độc đáo, chi tiết mới lạ mà 10 đối thủ chưa có hoặc chỉ đề cập hời hợt.
       + Đưa các góc nhìn mới mẻ này trực tiếp vào tiêu đề H2, H3 để tạo sự khác biệt và giá trị thông tin vượt trội cho bài blog.

2. **Khởi tạo Bộ Tiêu Đề & Mô Tả**:
   - **3 Tiêu đề SEO (Title)**: Chuẩn **55 - 60 ký tự**, tối ưu Key 1 ở đầu (1-2 lần), có số, từ bổ trợ (*uy tín, giá rẻ nhất, chuyên nghiệp...*), dấu `|` hoặc `-`, độc nhất (kiểm tra `Allintitle:"từ khóa"`), tuân thủ quy tắc viết hoa (chỉ viết hoa đầu dòng, địa danh, tên riêng, từ đặc biệt).
   - **3 Tiêu đề Thẻ H1 (Thẻ H1 kỹ thuật On-page)**: Chuẩn **55 - 70 ký tự**, **viết dựa vào Title và BẮT BUỘC KHÁC 100% SO VỚI SEO TITLE** (thường dài hơn Title do thêm các từ bổ nghĩa, tuân thủ quy tắc viết thường các từ thông thường):
     * Khi có ≥ 2 từ khóa: Tối ưu **Key 2** (khác Key 1, lấy từ danh sách từ khóa người dùng giao).
     * Khi chỉ có 1 từ khóa duy nhất: Vẫn bắt buộc khác 100% về cấu trúc, vế phụ và góc giật tít. Tuyệt đối không sao chép nguyên văn Title sang H1.
   - **2 Thẻ mô tả (Meta Description)**: Chuẩn **140 - 155 ký tự**, Key chính ở đầu, có thêm key phụ phía sau, gợi nỗi đau và giải pháp (không tiết lộ hết đáp án), có CTA cuối đoạn (*Click xem ngay!, Xem thêm!...*).
   - **1 Đoạn Sapo mẫu**: Ngắn gọn 2 - 3 dòng (<155 từ), giải quyết vấn đề của H1 đưa ra, Key chính trong 100 từ đầu, khéo léo nhắc tên thương hiệu công ty.
   - ⚠️ **LƯỢC BỎ HIỂN THỊ SỐ KÝ TỰ**: Agent kiểm soát độ dài chuẩn SEO ngầm bên dưới, **tuyệt đối KHÔNG in `(xx ký tự)`** ra Title, Meta Des hay các Headings để người dùng copy dùng ngay.

3. **Cấu trúc Dàn ý Headings (Đánh số 1., 1.1., 1.2., 2., 2.1.,...)**:
   - **Độ dài Headings (H2 > H6)**: Thường **dưới 60 ký tự**, ngắn gọn thể hiện rõ nội dung đoạn văn sắp viết.
   - **Quy tắc viết hoa**: Chỉ viết hoa chữ đầu câu và địa danh/tên riêng/từ đặc biệt, còn lại viết thường hết.
   - **Số lượng**: Tối thiểu **4 phần H2 trở lên**, mỗi H2 có **≥2 mục H3 trở lên** (càng nhiều H2 H3 hợp lý Google càng đánh giá bài viết chuyên sâu).
   - **Phân cấp nghiêm ngặt**: H4 bổ trợ cho H3, H3 bổ trợ cho H2, H2 bổ trợ cho H1. Tuyệt đối không nhồi nhét từ khóa.
   - **Phân bổ từ khóa**:
     * **Mục 1 (H2 đầu tiên)**: Bắt buộc chứa **Từ khóa chính**.
     * **Các H2 sau**: Bố trí các từ khóa phụ hoặc từ khóa mở rộng/bổ trợ cho từ khóa chính do người dùng cung cấp.
     * **Mỗi H3**: Chỉ tập trung tối đa 1 từ khóa mục tiêu (nếu có). Các mục không nhắm key thì tập trung triển khai nội dung thực tế, không chèn gượng ép.
   - **Đa dạng hóa nội dung theo chỉ định trên outline**:
     * Chủ động quy hoạch các phần hiển thị dạng **Bảng biểu (Table)** hoặc **Dạng danh sách (List)** để làm đa dạng hóa nội dung hiển thị trong bài viết.
   - **Đánh dấu Heading trọng tâm**: Đánh dấu ⭐ cho heading cần tập trung dồn trọng tâm triển khai dẫn dắt người đọc.
   - **Quy cách hiển thị số (Numbering Style)**: Dùng cách đánh số tự nhiên: `1.`, `1.1.`, `1.2.`, `2.`, `2.1.`,... Tuyệt đối KHÔNG hiển thị nhãn kỹ thuật `H2.1`, `H3.1.1` trên tiêu đề.
   - **Phong cách trình bày tinh gọn**:
     * Chỉ đưa ý chính cốt lõi dạng gạch đầu dòng (bullet points).
     * Không giải thích dài dòng dưới tiêu đề (không chèn nhãn thừa `Mục tiêu nội dung`, `Định dạng`...).
   - **Phần áp chót trước Kết luận**: H3 hoặc H2 cuối cùng gần Kết luận **không được viết quá ngắn** (tránh nhìn vào thấy kết luận như 1 phần của H3 đó).
   - **PHẦN CUỐI BẮT BUỘC LÀ KẾT LUẬN**:
     * H2 cuối cùng của dàn ý phải là **Kết luận**, không đặt thêm heading nội dung nào sau phần này.
     * Quy cách: Viết thật ngắn gọn, súc tích (chỉ từ 2 - 3 câu ngắn hoặc dưới 50 - 80 từ).
     * Quy hoạch: tóm tắt nhanh giá trị chính, **bắt buộc chứa 1 lần từ khóa chính**, kèm **lời kêu gọi hành động (CTA) dứt khoát gắn liền với số Zalo tư vấn và tên thương hiệu công ty**. Tuyệt đối không chèn ảnh hay ghi chú ảnh tại Kết luận.

4. **Lập Bảng Ma Trận Phân Bổ Từ Khóa & Checklist Thẩm Định**:
   - Lập bảng ánh xạ: Heading -> Từ khóa mục tiêu -> Định dạng (Text/Bảng/List) -> Kế hoạch Ảnh & Ghi chú mô tả ảnh (quy hoạch 1 ảnh/250 từ hoặc mỗi H2/H3).
   - Cột "Từ khóa mục tiêu": CHỈ ĐƯỢC PHÉP điền đúng các từ khóa người dùng cung cấp.
   - Đảm bảo từ khóa rải đều khắp các mục, mật độ tổng thể đạt 1.5% - 3%.

5. **XUẤT BẢN FILE WORD DOCX VÀO THƯ MỤC RESULT/ (CHỈ GIỮ FILE DOCX)**:
   - Đóng gói toàn bộ dàn ý trực tiếp ra file Word `Result/outline.docx`.
   - **Quy tắc tuyệt đối**: Lưu kết quả vào thư mục `Result/`. KHÔNG để lại file `.md` trong thư mục làm việc của người dùng.
   - Xác nhận file `Result/outline.docx` được tạo thành công với các styles Word chuẩn.
   - Bàn giao trực tiếp đường dẫn file `Result/outline.docx` cho người dùng.
