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
       5. Dòng Meta: [Nội dung Meta Description 140 - 155 ký tự có CTA]
       6. Dòng Title: [Nội dung SEO Title 55 - 60 ký tự, tối ưu Key 1]
       7. Dòng H1: [Nội dung Thẻ H1 55 - 60 ký tự - BẮT BUỘC KHÁC 100% SO VỚI SEO TITLE (tối ưu Key 2 nếu có nhiều key, hoặc đổi hoàn toàn cấu trúc & góc giật tít nếu chỉ có 1 key)]
     - Ngay bên dưới dòng H1: là Đoạn mở bài (Sapo) **ngắn gọn 2 - 3 câu (<155 từ), thu hút, bắt buộc chứa Key chính trong 100 từ đầu và khéo léo nhắc tên thương hiệu của công ty (tên thương hiệu công ty bắt buộc được gắn link website chính thức theo dạng anchor text `[Tên công ty](URL website)`)** nhằm giải quyết trực diện vấn đề của tiêu đề bài viết và định vị thương hiệu. Tiếp sau đó là các Heading thân bài 1., 1.1... (chủ động khai thác ý mới mẻ, góc nhìn độc đáo cho từng đề mục H2, H3).
       - **THẺ H1 BẮT BUỘC KHÁC BIỆT 100% SO VỚI SEO TITLE (NGHIÊM CẤM TRÙNG LẶP TUYỆT ĐỐI)**:
      - **SEO Title**: Chuẩn 55 - 60 ký tự, tối ưu **Key 1** ở đầu, có số, từ bổ trợ, dấu | hoặc -, độc nhất và thu hút click từ Google (ví dụ: `Tour Trùng Khánh Lệ Giang Shangrila 6N5Đ | Giá Tốt Trọn Gói`).
      - **Thẻ H1 (Tiêu đề chính bài viết trên trang)**: Chuẩn 55 - 60 ký tự, **BẮT BUỘC KHÁC 100% SO VỚI SEO TITLE TRONG MỌI TRƯỜNG HỢP**:
        * **Nếu có từ 2 từ khóa trở lên**: Tối ưu **Key 2** (chọn từ danh sách từ khóa người dùng giao).
        * **Nếu chỉ có DUY NHẤT 1 từ khóa**: Cả Title và H1 đều chứa key đó nhưng **phải khác nhau 100% về cấu trúc câu, từ ngữ bổ trợ và góc giật tít** (Title thiên về giá tour/CTR, H1 thiên về cẩm nang trải nghiệm/khám phá từ A-Z, ví dụ: `Khám Phá Tour Trùng Khánh Lệ Giang Shangrila Chi Tiết Từ A-Z`).
      - **Cơ chế Tự Rà Soát (Self-Check Validation)**: Trước khi xuất file `.docx`, Agent phải tự đối chiếu giữa dòng `Title:` và dòng `H1:`. Nếu phát hiện Title trùng H1 (như lỗi `Title: Tour Trùng Khánh...` và `H1: Tour Trùng Khánh...`), Agent BẮT BUỘC viết lại H1 ngay lập tức để đạt khác biệt 100%.
   - **PHẦN CUỐI BÀI BẮT BUỘC LÀ KẾT LUẬN (VIẾT THẬT NGẮN GỌN, CTA ZALO & THƯƠNG HIỆU)**:
     - Heading cuối cùng của bài phải là **Kết luận**. Sau phần Kết luận không thêm heading hoặc nội dung triển khai mới.
     - **YÊU CẦU ĐỘ DÀI KẾT BÀI**: Viết **thật ngắn gọn, cô đọng (chỉ từ 2 - 3 câu ngắn hoặc tối đa 50 - 80 từ)**. Tuyệt đối không kéo dài lê thê, không viết dài dòng, không thêm thắt các đoạn tổng kết phân tích triết lý rườm rà.
     - Kết luận phải gồm đủ 3 lớp nội dung tinh gọn: (1) Kết thúc và tóm tắt nhanh giá trị cốt lõi nhất của chuyến đi (**bắt buộc chứa 1 lần từ khóa chính**), (2) **Lời kêu gọi hành động (CTA) dứt khoát gắn liền với số Zalo tư vấn và tên thương hiệu của công ty** (kèm website nếu có) để người đọc liên hệ nhận tư vấn/đặt tour ngay, (3) Thông tin website/hotline nếu người dùng gửi kèm theo lệnh /create-post.
     - Chỉ được chèn đúng website, số Zalo/hotline và tên thương hiệu người dùng cung cấp. Nếu lệnh chưa có thông tin liên hệ cụ thể, sử dụng lời kêu gọi chuẩn kèm thông tin liên hệ theo định dạng `Zalo: [Số Zalo tư vấn] - [Tên thương hiệu]`.
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
   - **QUY CHUẨN BẮT BUỘC VIẾT HOA ĐỊA DANH VÀ TÊN NGƯỜI (PROPER NOUNS & PLACES CAPITALIZATION)**:
     - **BẮT BUỘC VIẾT HOA ĐÚNG CHÍNH TẢ TOÀN BỘ ĐỊA DANH & TÊN NGƯỜI**:
       * **Địa danh**: Quốc gia, tỉnh/thành phố, quận/huyện, thị xã, phường/xã, bản/làng/buôn, danh lam thắng cảnh, di tích lịch sử, sông, núi, đèo, hồ, thác, công trình kiến trúc (Ví dụ: *Hà Nội, Hà Giang, Măng Đen, Quản Bạ, Đồng Văn, Mèo Vạc, Mã Pí Lèng, Cột Cờ Lũng Cú, Thác Pa Sỹ, Núi Đôi Cô Tiên, Hồ Ba Bể, Chợ Đêm Phố Cổ, Cửu Trại Câu, Trương Gia Giới...*).
       * **Tên người / Nhân vật lịch sử / Tên dân tộc**: Viết hoa chuẩn xác (Ví dụ: *Bác Hồ, Nguyễn Trãi, đồng bào H'Mông, người Tày, người Dao...*).
     - **TUYỆT ĐỐI KHÔNG VIẾT THƯỜNG ĐỊA DANH & TÊN RIÊNG**:
       * AI thường mắc lỗi viết chữ thường cẩu thả cho các địa danh (*"hà giang"*, *"quản bạ"*, *"núi đôi cô tiên"*, *"thác pa sỹ"*, *"măng đen"*...). Agent bắt buộc phải rà soát và sửa lại toàn bộ thành chữ viết hoa đúng chuẩn chính tả tiếng Việt.
       * **Trường hợp từ khóa mục tiêu do người dùng cung cấp ở dạng chữ thường** (ví dụ: `tour hà giang 3 ngày 2 đêm`, `du lịch măng đen kon tum`): Khi đưa vào câu văn bài viết, **BẮT BUỘC PHẢI VIẾT HOA CÁC ĐỊA DANH** (*"tour Hà Giang 3 ngày 2 đêm"*, *"du lịch Măng Đen Kon Tum"*). Google hiểu trọn vẹn từ khóa không phân biệt hoa thường, còn bài viết giữ được tính chuyên nghiệp và đúng ngữ pháp.
   - **GIỌNG VĂN CON NGƯỜI VIẾT (Human Voice & Tone)**:
     - Đóng vai người hướng dẫn viên/người trải nghiệm thực tế chia sẻ kinh nghiệm cụ thể, thiết thực, tự nhiên và gần gũi.
     - Không dùng văn phong dịch thuật máy móc, không lý thuyết suông.
    - **ĐẢM BẢO TỶ LỆ AI DƯỚI 5% (Strict Anti-AI & Undetectable < 5%)**:
      - Khi quét qua các công cụ phát hiện AI (Copyleaks, GPTZero, Winston AI...), tỷ lệ AI Content **bắt buộc phải dưới 5% (Human Content ≥ 95%)**. Không dùng màu để đánh dấu câu văn; chỉ ghi chú ảnh được phép bôi đỏ theo quy định riêng.
      - **DANH SÁCH ĐEN CÁC MẪU CÂU & CÚ PHÁP AI BỊ CẤM TIỆT (SYNTACTIC AI BLACKLIST)**:
        - **CẤM TUYỆT ĐỐI cấu trúc khuyên răn, lên lớp máy móc: "bạn nên...", "bạn phải...", "bạn cần...", "bạn hãy...", "du khách nên/cần/phải..."**:
          - *Lý do*: Mẫu câu thuyết giáo đặc trưng của AI, gây cảm giác xa cách và lập tức bị các công cụ quét AI (Copyleaks, GPTZero) nhận diện.
          - *Cách thay thế*: Chuyển thành câu trần thuật khách quan, diễn giải lợi ích hoặc hành động trực diện:
            - Thay vì: *"Bạn nên mang theo áo ấm vì đêm Măng Đen rất lạnh."* -> *"Đêm Măng Đen nhiệt độ hạ xuống 15 độ C. Một chiếc áo khoác gió dày sẽ giữ ấm vừa vặn."*
            - Thay vì: *"Bạn cần đặt tour trước 2 tuần để giữ chỗ."* -> *"Mùa cao điểm phòng hết rất sớm. Đặt tour trước 2 tuần giúp bạn chủ động lịch trình và giữ được chỗ ngồi đẹp."*
            - Thay vì: *"Bạn phải xuất trình CCCD tại quầy vé."* -> *"Tại quầy soát vé, bạn chỉ cần xuất trình CCCD bản gốc để nhận vé lên cáp treo trong 2 phút."*
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
        - **Mở bài và kết bài thực tế**: Mở bài đi thẳng vào thông tin tour, giá vé, điều kiện thời tiết và khéo léo nhắc tên thương hiệu. Kết bài viết **thật ngắn gọn, súc tích (2 - 3 câu ngắn, dưới 80 từ)**, tóm tắt ngày khởi hành, cách thức giữ chỗ, CTA kèm số Zalo tư vấn và tên thương hiệu của công ty. Tuyệt đối không viết lan man dài dòng, không chúc tụng sến súa, không triết lý cuộc sống.
      - **KỸ THUẬT ĐẠT 100% HUMAN CONTENT (HIGH BURSTINESS & REALISM)**:
        - **Đan xen câu siêu ngắn (High Burstiness)**: Cứ sau 1-2 câu trần thuật (10 - 14 từ), BẮT BUỘC chèn 1 câu siêu ngắn (3 - 6 từ): *"Đường khá dốc."*, *"Trời rét nhanh."*, *"Quốc lộ phẳng lì."*, *"Xe chạy rất êm."*, *"Giá vé đã bao gồm trọn gói."*, *"Chuẩn bị từ sớm."*. Điều này phá vỡ hoàn toàn thuật toán nhận diện tính đồng nhất của AI.
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
   - **QUY TẮC BẮT BUỘC VỀ SỰ HIỆN DIỆN CỦA KEY CHÍNH & KEY PHỤ TRONG MỌI MỤC H2 (MỤC H2 NÀO CŨNG PHẢI CÓ TỐI THIỂU 2 - 3 KEY CHÍNH VÀ KEY PHỤ ĐI KÈM)**:
     - **Mục H2 nào cũng bắt buộc xuất hiện tối thiểu 2 - 3 key chính trong thân bài**:
       * Trong **mọi mục H2** (tính toàn bộ phần nội dung thân bài và các nhánh H3/H4 trực thuộc mục H2 đó), từ khóa chính **BẮT BUỘC PHẢI XUẤT HIỆN TỐI THIỂU TỪ 2 ĐẾN 3 LẦN**.
       * **Tiêu đề H2 KHÔNG được tính là 1 lần xuất hiện**: Từ khóa chính xuất hiện trong dòng tiêu đề H2 **tuyệt đối không được tính** vào số lần xuất hiện này. Định mức tối thiểu 2 - 3 lần bắt buộc phải nằm hoàn toàn trong các câu văn nội dung thân bài của mục H2 đó.
     - **Bắt buộc thêm các từ khóa phụ hiển thị cùng trong từng mục H2**:
       * Tại mỗi mục H2, bên cạnh 2 - 3 lần xuất hiện của key chính, Agent **bắt buộc phải phân bổ thêm các từ khóa phụ (Key phụ 1, Key phụ 2...) hiển thị cùng** một cách nhịp nhàng, đan xen hợp lý.
     - **Triệt tiêu hoàn toàn tình trạng "trống key" và khoảng cách quá xa**:
       * Tuyệt đối không để xảy ra tình trạng "trống key" (viết cả một đoạn dài 150 - 250 từ hoặc nguyên một mục H2 mà chỉ có tiêu đề có key, còn phần nội dung thân bài bên dưới rất lâu mới xuất hiện 1 key chính hoặc không có key nào).
       * Phân bổ từ khóa chính và phụ trải đều đặn khắp các phân đoạn của từng H2, giữ cho tín hiệu SEO luôn liên tục, dày dặn vừa phải và tự nhiên xuyên suốt bài viết.
     - **QUY TẮC TRÁNH ĐẶT KEY NGAY CẠNH TIÊU ĐỀ H2, H3 (ƯU TIÊN HIỂN THỊ Ở KHOẢNG GIỮA ĐOẠN/MỤC)**:
       * **Hạn chế tối đa việc hiển thị key ngay sát cạnh tiêu đề H2, H3**: Tuyệt đối không vừa dứt dòng tiêu đề H2/H3 xuống dòng là câu văn đầu tiên đã lập tức nhồi ngay từ khóa chính hoặc key phụ (như lỗi: `1.1. Khách sạn...` -> `Tham gia tour Trùng Khánh...`, hay `2. Lịch trình...` -> `Lịch trình tour Trùng Khánh...`). Cách chèn này tạo cảm giác máy móc, lặp từ thô cứng và rất gượng gạo.
       * **Nên hiển thị key ở vị trí khoảng giữa**: Câu mở đầu dưới heading nên dùng để dẫn dắt bối cảnh hoặc nêu thông tin thực tế tự nhiên. Sau đó mới đưa từ khóa xuất hiện ở **vị trí khoảng giữa đoạn văn** (sau khi đã đi qua 1 - 2 câu dẫn dắt) hoặc ở **đoạn văn thứ 2, thứ 3** trong nhánh nội dung đó, giúp mạch đọc mượt mà và tự nhiên nhất.
   - **ÉP ĐÚNG TỶ LỆ KEY VÀ PHÂN BỔ MƯỢT MÀ, TRẢI ĐỀU TOÀN BÀI**:
     - Mật độ tổng cụm từ khóa chuẩn SEO: **1.5% - 2.5%** (tối đa 3.0%, tuyệt đối không dưới 1.0% và không quá 3.5%).
     - **Tỉ lệ từ khóa phải trải đều trong toàn bài và trong từng mục (H2, H3)**:
       - **Mật độ không quá dày & không xuất hiện quá gần nhau**: Tuyệt đối không nhồi nhiều từ khóa liên tiếp trong cùng 1 câu hoặc 2 câu liền kề; không lặp lại dồn dập khiến người đọc thấy ngột ngạt hoặc spam.
       - **Không để khoảng cách quá xa mới xuất hiện key một lần**: Tránh viết liền 200 - 300 từ mà hoàn toàn vắng bóng từ khóa rồi mới xuất hiện lại.
       - **Dùng câu chữ linh hoạt, biến tấu ngữ cảnh mượt mà để luôn tự nhiên nhất**: Dùng cấu trúc câu phong phú, từ khóa được hòa tan tự nhiên vào lời kể trải nghiệm thực tế, chuẩn ngữ pháp tiếng Việt, đọc lên thấy hoàn toàn tự nhiên như người thật viết.
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
