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

## CÁC BƯỚC THỰC THI

1. **Đọc và Phân Tích Dữ Liệu Từ `Result/outline.docx` & `ContentTour/*`**:
   - Sử dụng công cụ đọc Word trực tiếp:
     ```powershell
     python .agents/scripts/read_docx.py Result/outline.docx
     ```
   - Đối chiếu chi tiết với file tour thực tế trong thư mục `ContentTour/*` (sử dụng `read_tour_file.py`) để đảm bảo số liệu, giá tour, mốc giờ, địa điểm chính xác 100%. Tuyệt đối không chỉnh sửa hay ghi đè file tài liệu gốc trong `ContentTour/*`.

2. **Triển Khai Viết Nội Dung Chuẩn SEO & Giọng Văn Người Thật (BẮT BUỘC TUÂN THỦ)**:
   - **CẤU TRÚC PHẦN MỞ ĐẦU BÀI VIẾT (MASTER HEADER BLOCK FORMAT)**:
     - Mọi file Word bài viết bắt buộc bắt đầu bằng đúng thứ tự chuẩn hóa:
       1. **Bảng Thống kê Từ khóa**: Cột `KEY` và Cột `VOLUME` (bảng nền trắng, chữ màu đen; không tô màu ô, không dùng màu chữ; có thể in hoa/in đậm phần tiêu đề cột để dễ đọc; Cột VOLUME căn giữa).
       2. Dòng `Check spin:` (chừa trống để ghi nhận)
       3. Dòng `Check AI:` (chừa trống để ghi nhận)
       4. Dòng `Key chính: [Từ khóa chính]`
       5. Dòng `Meta: [Nội dung Meta Description]`
       6. Dòng `Title: [Nội dung SEO Title]`
       7. Dòng `H1: [Nội dung Thẻ H1 - đồng nhất với SEO Title]`
     - Ngay bên dưới dòng `H1:` là Đoạn mở bài (Sapo) 2 - 3 câu ngắn. Tiếp sau đó là các Heading thân bài `1.`, `1.1.`...
   - **TIÊU ĐỀ BÀI VIẾT (HEADING 1) = SEO TITLE**:
     - Tiêu đề to đầu tiên của bài viết (Heading 1) **BẮT BUỘC sử dụng chính xác là SEO Title** (chuẩn 55 - 60 ký tự). Không tạo phiên bản H1 khác.
   - **PHẦN CUỐI BÀI BẮT BUỘC LÀ KẾT LUẬN (VIẾT THẬT NGẮN GỌN & CÔ ĐỌNG)**:
     - Heading cuối cùng của bài phải là **Kết luận**. Sau phần Kết luận không thêm heading hoặc nội dung triển khai mới.
     - **YÊU CẦU ĐỘ DÀI KẾT BÀI**: Viết **thật ngắn gọn, cô đọng (chỉ từ 2 - 3 câu ngắn hoặc tối đa 50 - 80 từ)**. Tuyệt đối không kéo dài lê thê, không viết dài dòng, không thêm thắt các đoạn tổng kết phân tích triết lý rườm rà.
     - Kết luận phải gồm đủ 3 lớp nội dung tinh gọn: (1) Kết thúc và tóm tắt nhanh giá trị cốt lõi nhất của chuyến đi (có lặp lại 1 lần từ khóa chính), (2) Lời kêu gọi hành động (Call To Action) rõ ràng, (3) Thông tin website và số điện thoại nếu người dùng gửi kèm theo lệnh `/create-post`.
     - Chỉ được chèn đúng website, số điện thoại và thông tin liên hệ người dùng cung cấp. Nếu lệnh không có thông tin liên hệ, dùng CTA chung và không tự bịa website, hotline, email hoặc địa chỉ.
     - **Tuyệt đối không chèn ảnh hay ghi chú note ảnh trong phần Kết luận**.
   - **TRỰC DIỆN, ĐỦ Ý & KHÔNG LAN MAN (Direct, Lean & Comprehensive)**:
     - Đi thẳng vào thông tin cốt lõi (lịch trình, thời gian, giá vé, lưu ý). Đầy đủ ý nhưng không thừa chữ; không lặp ý giữa các đoạn.
     - Cung cấp giá trị thực tế ngay lập tức cho người đọc.
   - **CẮT BỎ HOÀN TOÀN HOA MỸ & SÁO RỖNG (Zero Fluff & No Poetic Padding)**:
     - Nghiêm cấm chèn các cụm từ hoa văn sáo rỗng, sến súa du lịch như: *“điểm hẹn trong mơ”, “những tâm hồn mê xê dịch”, “hít căng lồng ngực”, “bức tranh tuyệt mỹ”, “thiên đường nơi hạ giới”, “đắm say lòng người”, “viên ngọc ẩn mình”*.
     - Giữ phong cách viết thực tế, gãy gọn, thiết thực và dễ quét (scannable).
   - **CÂU VĂN NGẮN GỌN, DỨT KHOÁT (10 - 15 từ/câu, tối đa ≤ 18 từ)**:
     - Mỗi câu chỉ tải đúng 1 ý. Không viết câu ghép 3 - 4 vế dài dòng bằng các liên từ rườm rà.
     - Tách nhỏ thành các câu đơn gãy gọn, mạch lạc.
     - Đoạn văn siêu ngắn: chỉ **1 - 3 câu/đoạn**.
   - **KIỂM SOÁT TRÙNG LẶP 0% & CHỦ ĐỘNG CHECK TRÙNG LẶP SPIN TOÀN DIỆN (Zero Plagiarism & 100% Unique - Check Spin = 0%)**:
     - Khi kiểm tra qua các công cụ check trùng lặp (Spineditor, SmallSEOTools, DupliChecker...), tỷ lệ trùng lặp **bắt buộc là 0%** (hoặc < 2% với các tên riêng địa danh cố định). Mọi câu văn, dòng bảng, mục danh sách đều phải đạt tick xanh (Unique 100%).
     - **QUY ĐỊNH BẮT BUỘC VỀ CHECK SPIN ĐỂ KHÔNG PHẢI SỬA ĐI SỬA LẠI**:
       - Agent phải **chủ động rà soát và kiểm tra kỹ lưỡng tỷ lệ trùng lặp spin trong toàn bộ nội dung** (mở bài, thân bài, lịch trình chi tiết, bảng giá, danh mục dịch vụ, chính sách trẻ em, lưu ý thực tế, kết bài) ngay trong quá trình viết và trước khi xuất file `.docx`.
       - **Tuyệt đối không để xảy ra tình trạng người dùng mang đi check spin bị báo đỏ hoặc báo vàng trùng lặp**, khiến người dùng phải mất công kiểm tra lại và bắt Agent sửa đi sửa lại rất vất vả.
       - Mọi câu chữ phải đạt chuẩn **Unique 100% ngay từ lần xuất bản đầu tiên**.
     - **Kỹ thuật Paraphrase toàn diện cho tài liệu tour**:
       - *Chính sách trẻ em*: Tuyệt đối không chép khuôn mẫu (*“Trẻ dưới 5 tuổi: Miễn phí”*, *“Trẻ từ 5-9 tuổi: 75%”*). Phải diễn giải thành câu văn tự nhiên, phong phú của người viết.
       - *Điểm đón & Thời gian*: Không ghi cụm từ cứng nhắc (*“05h30 tại Nhà hát Lớn...”*). Diễn giải thành câu có ngữ cảnh và linh hoạt từ ngữ.
       - *Bảng biểu & Bảng chi phí*: Mọi mục dịch vụ, khoản tự túc, danh sách điểm đến đều phải được làm mới từ ngữ, không dùng các cụm từ phổ thông dễ trùng trên web.
       - *Câu chuyển đoạn & Mở đầu*: Cấm các câu sáo rỗng thường gặp trên blog (*“Bài viết này tổng hợp toàn bộ lịch trình”*, *“Bạn chỉ cần chuẩn bị đồ cá nhân”*, *“Tự lái xe mang lại cảm giác tự do”*). Thay bằng các câu diễn đạt trải nghiệm cụ thể, độc nhất.
       - *Tiền tip & Phụ phí*: Dùng các từ thay thế tự nhiên (*“khoản thưởng bồi dưỡng tùy sự hài lòng”*, *“tiêu vặt phát sinh ngoài lề”*).
     - **Cơ chế Tự Rà Soát Trùng Lặp**: Agent chủ động rà soát từng dòng, từng câu trong bài trước khi xuất file `.docx`, đảm bảo tính độc nhất 100%, triệt tiêu hoàn toàn nguy cơ dính spin trùng lặp để người dùng có thể sử dụng ngay mà không phải sửa lại.
   - **GIỌNG VĂN CON NGƯỜI VIẾT (Human Voice & Tone)**:
     - Đóng vai người hướng dẫn viên/người trải nghiệm thực tế chia sẻ kinh nghiệm cụ thể, thiết thực, tự nhiên và gần gũi.
     - Không dùng văn phong dịch thuật máy móc, không lý thuyết suông.
    - **ĐẢM BẢO TỶ LỆ AI DƯỚI 5% (Strict Anti-AI & Undetectable < 5%)**:
      - Khi quét qua các công cụ phát hiện AI (Copyleaks, GPTZero, Winston AI...), tỷ lệ AI Content **bắt buộc phải dưới 5% (Human Content ≥ 95%)**. Không dùng màu để đánh dấu câu văn; chỉ ghi chú ảnh được phép bôi đỏ theo quy định riêng.
      - **DANH SÁCH ĐEN CÁC MẪU CÂU & CÚ PHÁP AI BỊ CẤM TIỆT (SYNTACTIC AI BLACKLIST)**:
        - **CẤM cấu trúc "Bạn có thể tự do [động từ]..."** (*"Bạn có thể tự do thưởng thức một ly cà phê...", "bạn có thể tự do dạo phố..."*): Đây là mẫu câu dịch máy số 1 bị Copyleaks gắn cờ AI. Thay bằng câu hành động cụ thể hoặc chỉ dẫn thực tế (*"Quán phục vụ cà phê sữa và đen đá nguyên chất. Bạn gọi một ly rồi ngồi uống dưới tán cây cổ thụ mát rượi."*).
        - **CẤM cấu trúc "Đây là dịp / cơ hội tuyệt vời để..."** (*"Đây là dịp tuyệt vời để bạn tự do khám phá...", "mang đến cơ hội chiêm ngưỡng..."*). Thay bằng câu trực diện (*"Buổi tối bạn tự do đi ăn uống. Quanh khu chợ đêm có nhiều quán ăn ngon."*).
        - **CẤM liên từ chuyển tiếp máy móc ở đầu câu** (*"Tiếp đó, đoàn ghé...", "Sau đó, xe đưa đoàn...", "Kế tiếp...", "Đồng thời..."*). Thay bằng mốc thời gian, khoảng cách hoặc hành động cụ thể (*"Rời làng cà phê, xe chạy chừng 10 phút vào buôn...", "Đoàn xuất phát lúc 13h00..."*).
        - **CẤM các cụm khen ngợi sáo rỗng vô thưởng vô phạt**:
          - *"Đây là buôn làng giàu đẹp bậc nhất..."*, *"khuôn viên rực rỡ sắc hoa"*, *"được gìn giữ rất ngăn nắp"*.
          - *"...rồi nghỉ ngơi ít phút / giây lát"*.
          - *"Đường trải nhựa êm thuận"*, *"quãng đường khoảng..."*.
          - *"sở hữu kiến trúc giao thoa độc đáo, ... uy nghiêm soi bóng xuống mặt hồ tĩnh lặng"*.
          - *"Lựa chọn chuyến du lịch... giúp bạn tối ưu thời gian..."*.
          - *"Mỗi vùng đất trong chuyến đi mang một dấu ấn cảnh quan riêng biệt..."*.
          - *"Nắm chắc các lưu ý thực tế giúp chuyến đi... diễn ra suôn sẻ và an tâm hơn..."*.
        - **CẤM các mô thức kết bài khuôn sáo**: *“Chuyến đi ... là khoảng thời gian vừa vặn để bạn tạm gác lại những xô bồ, khói bụi của phố thị và hòa mình vào thiên nhiên hoang sơ hùng vĩ”*, *“Đứng giữa biển mây... sẽ là liều thuốc tinh thần tuyệt vời giúp bạn tái tạo năng lượng”*, *“Chúc bạn có một hành trình đáng nhớ và rinh về những bức hình tuyệt đẹp!”*.
        - **CẤM các từ ngữ hoa mỹ AI**: *“liều thuốc tinh thần”, “tái tạo năng lượng”, “tạm gác lại những xô bồ khói bụi”, “hòa mình vào thiên nhiên”, “hít căng lồng ngực”, “bức tranh tuyệt mỹ”, “ấm nồng”, “vượt trội”, “lắng đọng”, “không chỉ là... mà còn là...”, “được ví như...”, “hành trình này không đơn thuần là...”*.
        - **Mở bài và kết bài thực tế**: Mở bài đi thẳng vào thông tin tour, giá vé và điều kiện thời tiết. Kết bài viết **thật ngắn gọn, súc tích (2 - 3 câu ngắn, dưới 80 từ)**, tóm tắt ngày khởi hành, cách thức giữ chỗ, CTA và chỉ hiển thị website/số điện thoại khi người dùng đã cung cấp. Tuyệt đối không viết lan man dài dòng, không tự tạo thông tin liên hệ, không chúc tụng sến súa, không triết lý cuộc sống.
      - **KỸ THUẬT ĐẠT 100% HUMAN CONTENT (HIGH BURSTINESS & REALISM)**:
        - **Đan xen câu siêu ngắn (High Burstiness)**: Cứ sau 1-2 câu trần thuật (10 - 14 từ), BẮT BUỘC chèn 1 câu siêu ngắn (3 - 6 từ): *"Đường khá dốc."*, *"Trời rét nhanh."*, *"Quốc lộ phẳng lì."*, *"Xe chạy rất êm."*, *"Giá vé đã bao gồm trọn gói."*, *"Bạn nên chuẩn bị sớm."*. Điều này phá vỡ hoàn toàn thuật toán nhận diện tính đồng nhất của AI.
        - **Chi tiết thực tế & giá tiền đời thường (High Perplexity)**: Đưa các chi tiết mắt thấy tai nghe: giá tô phở khô 40.000 - 50.000đ, bát nước dùng xương ngọt lịm, ly cà phê 35.000đ, chặng đường 180km chạy 3.5 - 4 tiếng, đèo Măng Đen dài 12km dốc quanh co, nền đá thác Pa Sỹ trơn ướt cần giày bám tốt, áo khoác gió vì đêm hạ 15 độ C...
   - **ĐỊNH DẠNG KEY VÀ MÀU SẮC**:
     - Mọi lần xuất hiện của từ khóa chính và từ khóa phụ trong file Word (`Result/bai-viet.docx`) để dạng văn bản thông thường: chữ màu đen, không bôi đỏ, không tô nền và không in đậm chỉ vì đó là từ khóa.
     - Tiêu đề, H1-H6 và các key trong tiêu đề cũng phải giữ định dạng sạch, không dùng màu để đánh dấu key.
     - Toàn bộ bài viết mặc định dùng chữ đen, nền trắng. Không tự ý thêm màu chữ, màu nền hoặc hiệu ứng màu vào đoạn văn, tiêu đề, danh sách và bảng.
   - **QUY CHUẨN FONT VÀ CỠ CHỮ**:
     - Áp dụng font Google Sans Flex cho toàn bộ file Word, gồm phần thông tin đầu bài, nội dung, tiêu đề, bảng, danh sách và ghi chú ảnh.
     - Nội dung thường và các cấp Heading phụ: Google Sans Flex **13px**. Heading 1: Google Sans Flex **16px**, in đậm và căn giữa.
     - Các đoạn văn, đoạn Sapo, nội dung danh sách và phần diễn giải trong bảng phải căn đều hai bên khi phù hợp; không tự ý dùng màu hoặc kiểu chữ trang trí.
     - Trước khi xuất file, Agent phải rà soát và loại bỏ toàn bộ emoji, icon, ký tự trang trí không phù hợp; đồng thời kiểm tra font, cỡ chữ, căn lề, kiểu đậm và màu chữ của từng nhóm nội dung.
   - **ÉP ĐÚNG TỶ LỆ KEY VÀ PHÂN BỔ MƯỢT MÀ, KHÔNG GƯỢNG ÉP**:
     - Mật độ tổng cụm từ khóa chuẩn SEO: **1.5% - 2.5%** (tối đa 3.0%, tuyệt đối không dưới 1.0% và không quá 3.5%).
     - Tích hợp từ khóa mềm mại, tự nhiên, đúng ngữ pháp; cấm nhồi nhét thô cứng làm gượng gạo câu văn.
   - **QUY CHUẨN MÔ TẢ HÌNH ẢNH NGẮN GỌN & DỄ HIỂU (SIMPLE IMAGE NOTES)**:
     - Trung bình mỗi **250 - 350 từ** hoặc mỗi **H2/H3 phù hợp** chèn một dòng ghi chú mô tả ảnh **ngắn gọn, đơn giản, dễ hiểu**, đặt trong ngoặc đơn (...) ngay tại vị trí cần chèn ảnh.
     - **Ngoại lệ bắt buộc**: Phần **Kết luận** và các đoạn CTA cuối bài không chèn ảnh, không chèn note ảnh và không đặt ghi chú hình ảnh trong ngoặc đơn.
     - Ghi chú phải hiển thị đúng dạng một đoạn text thường trong ngoặc đơn (...), mô tả ngắn thôi và dùng màu đỏ `#C00000` để dễ nhận diện. Không in đậm, không thêm icon, không chèn biểu tượng, không đóng khung, không tô nền và không viết thành đoạn dài. Không áp dụng màu đỏ này cho key hay nội dung khác.
     - **Tuyệt đối không viết rườm rà**: Bỏ toàn bộ các trường thông số kỹ thuật dài dòng (chủ thể góc máy, quy cách kích thước pixel, dung lượng KB, tên file ảnh SEO, thẻ alt text, caption...).
     - Chỉ cần mô tả trực diện yêu cầu nội dung hoặc ý tưởng thiết kế hình ảnh để người đăng bài/designer nhìn vào là hiểu ngay cần chọn hoặc làm loại ảnh gì.
     - **Ví dụ chuẩn**:
       - (Timeline lịch trình từ 05:00 đến 19:00)
       - (Ảnh tổng hợp các điểm đến đẹp ở Hà Giang)
       - (Phòng homestay nhìn ra biển mây buổi sáng)
     - Đa dạng hóa định dạng: Bảng so sánh (Table), Danh sách gạch đầu dòng (List) rõ ràng. Bảng chỉ dùng định dạng Word cơ bản, nền trắng, chữ đen, không tô màu tùy tiện.
   - **QUY CHUẨN BẢNG**:
     - Toàn bộ bảng dùng font Google Sans Flex, cỡ chữ 13px, giãn dòng đơn và khoảng cách trước/sau đoạn bằng 0 để bảng gọn, dễ đọc.
     - Bảng có viền màu đen mặc định, nền trắng, không tô màu xen kẽ và không dùng màu chữ khác.
     - Tiêu đề tất cả các cột phải in đậm, căn giữa theo chiều ngang, màu đen. Nội dung ô giữ chữ đen; cột số liệu có thể căn giữa khi phù hợp.
   - **GIỚI HẠN ĐỘ DÀI BẮT BUỘC**:
     - Tổng nội dung bài viết từ H1 đến hết bài phải nằm trong khoảng **1.800 - 2.500 từ**. Không xuất bài dài 3.000 - 4.000 từ.
     - Trước khi xuất `.docx`, Agent phải tự đếm từ và biên tập lại phần lan man, ý trùng lặp hoặc chi tiết phụ nếu vượt 2.500 từ; nếu dưới 1.800 từ thì bổ sung thông tin thực tế cần thiết, không kéo dài bằng câu sáo rỗng.
     - Đoạn áp chót viết đầy đủ, sâu sắc, không bị cụt. Phần Kết luận viết **thật ngắn gọn (2 - 3 câu ngắn, dưới 80 từ)**, chứa từ khóa chính, CTA và thông tin liên hệ được cung cấp hợp lệ nếu có.

3. **Đóng Gói Trực Tiếp Sang File `.docx` Vào Thư Mục `Result/`**:
   - Agent biên dịch nội dung hoàn chỉnh và xuất bản trực tiếp ra file Word trong thư mục `Result/` (ví dụ `Result/bai-viet.docx` hoặc theo slug từ khóa).
   - Bảo toàn nguyên vẹn thư mục `ContentTour/*`, tuyệt đối không chỉnh sửa hay ghi đè file tour gốc.
   - Xóa ngay mọi tệp tạm (nếu phát sinh trong quá trình build), không để lại file `.md` trong thư mục làm việc.
   - Xác nhận file `.docx` trong thư mục `Result/` hoàn tất với đầy đủ styles Word chuẩn: Heading 1 -> Heading 4, font Google Sans Flex đúng cỡ, Heading 1 căn giữa, đoạn văn căn đều hai bên, bảng font 13px giãn dòng đơn, viền đen, nền trắng, tiêu đề cột in đậm căn giữa, chữ đen mặc định, không có emoji/icon, phần cuối là Kết luận với CTA và thông tin liên hệ hợp lệ nếu có, không có ảnh/note ảnh trong Kết luận, các note ảnh còn lại ngắn gọn.

4. **Bàn Giao Cho Người Dùng**:
   - Gửi đường link trực tiếp đến file Word `.docx` trong thư mục `Result/` để người dùng click mở ngay.
   - Đính kèm bảng Checklist đối soát Pre-publish tóm tắt các chỉ số kỹ thuật của bài viết.
