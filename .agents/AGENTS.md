# AGENT OPERATING INSTRUCTIONS: SEO CONTENT REWRITE & WRITING

Dự án này chuyên trách sản xuất, tối ưu và viết lại (rewrite) nội dung bài viết chuẩn SEO cho Website.
Mọi Agent khi thực thi tác vụ viết content, lập dàn ý (outline), tạo tiêu đề hay kiểm tra bài viết đều phải tuân thủ nghiêm ngặt quy chuẩn dưới đây.

Chi tiết quy chuẩn toàn diện được lưu trữ tại: [.agents/rules/seo-content-standard.md](file:///c:/Users/PC/Documents/ContentRewrite/.agents/rules/seo-content-standard.md)

---

## 1. NGUYÊN TẮC CỐT LÕI (CORE DIRECTIVES)

1. **Title (SEO Title)**:
   - **Tối ưu 1 key riêng biệt**: SEO Title tối ưu 1 cụm từ khóa (thường là từ khóa chính có Search Intent cao nhất hoặc Volume cao nhất do người dùng cung cấp).
   - **Độ dài chuẩn**: **55 - 60 ký tự** (kiểm soát ngầm bên dưới, không in số ký tự thừa thãi).
   - **Vị trí từ khóa**: Từ khóa mục tiêu của Title nằm **ngay đầu Title**, xuất hiện **1 - 2 lần** (2 lần nếu tự nhiên, không chèn từ xen ngang).
   - **Yếu tố phụ**: Có số (TOP 10, 5+...), từ bổ trợ (uy tín, giá rẻ, chuẩn, trọn gói...), dấu ngăn cách `|` hoặc `-`, độc nhất và thu hút click.

2. **Meta Description**:
   - Độ dài: **140 - 155 ký tự**.
   - Key chính ở đầu đoạn, key phụ ở vế sau.
   - Không cung cấp ngay câu trả lời cuối cùng; khơi gợi nỗi đau và sự tò mò.
   - Bắt buộc kết thúc bằng lời kêu gọi hành động (CTA): *Click xem ngay!, Xem thêm!...*

3. **Thẻ H1 (Tiêu đề chính trên trang) & NGUYÊN TẮC CHỐNG TRÙNG LẶP TITLE - H1 TUYỆT ĐỐI**:
   - **H1 KHÁC TITLE 100% (NGHIÊM CẤM TRÙNG LẶP DƯỚI MỌI HÌNH THỨC)**:
     * H1 và Title là 2 tiêu đề hoàn toàn độc lập, tuyệt đối không dùng chung một câu chữ, không copy nguyên văn của nhau.
     * **Trường hợp có từ 2 từ khóa trở lên**: Title tối ưu **Key 1**, H1 tối ưu **Key 2** (2 key hoàn toàn khác nhau lấy từ danh sách người dùng cấp).
     * **Trường hợp CHỈ CÓ 1 TỪ KHÓA DUY NHẤT (Single Keyword)**: Title và H1 **VẪN BẮT BUỘC PHẢI KHÁC NHAU 100%**:
       + Cùng chứa từ khóa chính đó, nhưng **khác nhau hoàn toàn về cấu trúc câu, từ ngữ bổ trợ, vế phụ và góc giật tít**.
       + **SEO Title**: Giật tít theo hướng bán tour/dịch vụ/kích thích CTR (Key ở đầu + số ngày đêm/giá tour/từ bổ trợ uy tín, trọn gói + dấu `|` hoặc `-`). Ví dụ: `Tour Trùng Khánh Lệ Giang Shangrila 6N5Đ | Giá Tốt Trọn Gói` (58 ký tự).
       + **Thẻ H1**: Giật tít theo hướng cẩm nang trải nghiệm, khám phá thực tế, bao quát toàn bài (Dùng cấu trúc động từ khác biệt: "Khám Phá...", "Kinh Nghiệm Đi...", "Lịch Trình Chi Tiết..."). Ví dụ: `Khám Phá Tour Trùng Khánh Lệ Giang Shangrila Chi Tiết Từ A-Z` (59 ký tự).
     * **Cơ chế Tự Rà Soát (Self-Check Validation)**: Trước khi xuất file dàn ý hoặc bài viết, Agent bắt buộc tự so sánh đối chiếu giữa `Title` và `H1`. Nếu phát hiện Title và H1 giống nhau hoặc trùng lặp cấu trúc >70%, Agent xem đây là **LỖI NGHIÊM TRỌNG (CRITICAL ERROR)** và phải viết lại H1 ngay lập tức để đạt 100% khác biệt.
   - **Duy nhất 1 H1/bài**: H1 đứng đầu bài viết trên trang web, tự nhiên, hấp dẫn, bao quát toàn bài và chuẩn SEO.

4. **Sapo (Đoạn mở đầu)**:
   - **Ngắn gọn & Thu hút**: Độ dài **2 - 3 dòng** (<155 từ), mở đầu hấp dẫn, khơi gợi tò mò mạnh mẽ để giữ chân người đọc.
   - **Chứa từ khóa chính & Nhắc tên thương hiệu**: Bắt buộc chứa từ khóa chính ngay trong **100 từ đầu tiên**, giải quyết bài toán của Title và H1; đồng thời **bắt buộc nhắc tên thương hiệu** của công ty một cách tự nhiên để định vị và gia tăng uy tín, nhận diện (tên thương hiệu công ty bắt buộc được gắn link website chính thức theo dạng anchor text: `[Tên công ty](URL website)`).

5. **Heading 2 - Heading 6**:
   - Độ dài mỗi thẻ thường **< 60 ký tự**.
   - Tối thiểu từ **4 H2 trở lên** cho một bài viết hoàn chỉnh.
   - Mỗi H2 nên có từ **2 H3 trở lên**.
   - **H2 đầu tiên**: Bắt buộc chứa **từ khóa chính**. Các H2 tiếp theo dùng từ khóa phụ/liên quan.
   - **Khai thác ý mới mẻ, góc nhìn độc đáo (Freshness & Unique Value)**: Chủ động tìm tòi và đưa các ý mới, góc tiếp cận độc đáo, điểm nhấn khác biệt vào các thẻ H2, H3 (ví dụ: góc check-in ít người biết, khung giờ vàng săn mây/ngắm cảnh, quán ăn ngõ ngách chuẩn vị bản địa, mẹo tránh đông, kinh nghiệm thực chiến độc lạ từ người đi trước). Tránh rập khuôn các tiêu đề sáo mòn, giúp bài viết có tính mới cao (Information Gain), tạo sự mới mẻ và lôi cuốn cho người đọc.
   - **Quy chuẩn Bắt buộc Gắn Link Website vào Tên Công Ty (Brand Anchor Text Link)**:
     * Toàn bộ các vị trí nhắc đến tên công ty / thương hiệu trong bài viết (đoạn Sapo mở đầu, phần thân bài giới thiệu giá tour/dịch vụ, phần Kết luận & CTA...) **bắt buộc phải gắn link website chính thức của công ty trực tiếp vào tên công ty** (Anchor text là tên công ty, ví dụ: `[LE Travel](http://Letravel.vn)`).
     * Tuyệt đối không để tên công ty ở dạng text trơn không gắn link. Không ghi URL trần thô sơ như `website: http://...` trừ khi có yêu cầu đặc thù. Việc neo link website vào tên thương hiệu giúp tối ưu tín hiệu thực thể SEO (Brand Entity) và điều hướng độc giả trực tiếp về trang chủ của công ty.
6. **Thân bài & UX Writing**:
   - **Đoạn văn ngắn (1 - 3 câu/đoạn)**: Không viết khối văn bản dày đặc. Cấu trúc thông thoáng, dễ đọc lướt trên di động.
   - **Tách câu ngắn gọn (10 - 15 từ/câu)**: Mỗi câu chỉ chứa 1 ý trọn vẹn. Tuyệt đối không viết câu ghép 3 - 4 vế lê thê.
   - **Cắt bỏ hoa mỹ, sáo rỗng (Zero Fluff)**: Không thêm thắt từ ngữ bay bướm, sến súa (*"điểm hẹn trong mơ", "tâm hồn mê xê dịch", "hít căng lồng ngực", "bức tranh tuyệt mỹ"...*). Đi thẳng vào thông tin thực tế.
   - Tích cực sử dụng **Bảng (Table)** và **Danh sách (List)** để tóm tắt dữ liệu, tăng độ trực quan.
   - Số liệu, mốc thời gian, giá tour phải chuẩn xác 100% theo tài liệu nguồn.
   - **Quy chuẩn Bắt buộc Viết Hoa Địa Danh và Tên Người (Capitalization Rules)**:
     * Toàn bộ danh từ riêng chỉ **Địa danh** (quốc gia, tỉnh, thành phố, huyện, xã, bản làng, danh thắng, sông, núi, đèo, thác, công trình...) và **Tên người** / dân tộc bắt buộc phải **VIẾT HOA ĐÚNG CHUẨN CHÍNH TẢ TIẾNG VIỆT** (Ví dụ: *Hà Giang, Măng Đen, Quản Bạ, Đồng Văn, Mèo Vạc, Thác Pa Sỹ, Núi Đôi Cô Tiên, Đèo Mã Pí Lèng, Cột Cờ Lũng Cú...*).
     * Tuyệt đối không để AI viết thường cẩu thả (*"hà giang"*, *"măng đen"*, *"thác pa sỹ"*...).
     * Ngay cả khi từ khóa người dùng cung cấp viết chữ thường, khi đưa vào câu văn bài viết bắt buộc phải viết hoa đúng địa danh (*"tour Hà Giang"*, *"kinh nghiệm đi Măng Đen"*).
   - H3/H2 áp chót trước Kết luận không được viết quá ngắn.
   - **Quy chuẩn Phần Kết luận (Ngắn gọn, CTA Số Zalo, Thương hiệu & Chứa Key chính)**:
     - Kết bài viết **thật ngắn gọn, súc tích (chỉ từ 2 - 3 câu ngắn hoặc dưới 50 - 80 từ)**. Tuyệt đối không kéo dài lê thê, không triết lý sáo rỗng.
     - **Bắt buộc chứa 1 lần từ khóa chính**.
     - **Lời kêu gọi hành động (CTA) gắn liền với số Zalo và thương hiệu công ty**: Bắt buộc có CTA rõ ràng, dứt khoát kèm **số Zalo tư vấn** và **tên thương hiệu của công ty** (trong đó **tên công ty được gắn link website chính thức** theo dạng anchor text `[Tên công ty](URL website)`) để thúc đẩy liên hệ trực tiếp.
     - Tuyệt đối không chèn ảnh hay ghi chú note ảnh ở Kết luận.
   - **Quy chuẩn Mô tả Hình ảnh Ngắn Gọn & Dễ Hiểu (Simple Image Notes)**:
     - Trung bình mỗi **250 - 350 từ** hoặc mỗi **H2/H3** chèn một dòng ghi chú mô tả ảnh **ngắn gọn, đơn giản, dễ hiểu**, đặt trong ngoặc đơn (...) ngay tại vị trí cần chèn ảnh.
     - **Tuyệt đối không viết rườm rà**: Bỏ toàn bộ các trường thông số kỹ thuật dài dòng (chủ thể góc máy, quy cách kích thước pixel, dung lượng KB, tên file ảnh SEO, thẻ alt text, caption...).
     - Chỉ cần mô tả trực diện yêu cầu nội dung hoặc ý tưởng thiết kế hình ảnh để người đăng bài/designer nhìn vào là hiểu ngay cần chọn hoặc làm loại ảnh gì.
     - **Ví dụ chuẩn**:
       - (Thiết kế dạng timeline dọc, thể hiện các mốc giờ từ 05:00 đến 19:00, kết hợp hình ảnh Nhà hát Lớn Hà Nội, Km 0 Hà Giang, Cổng Trời Quản Bạ và Núi đôi Cô Tiên ở mục này)
       - (Cần làm 1 cái ảnh chung tổng hợp 1 số điểm đến đẹp ở Hà Giang trong 3 ngày 2 đêm ở đây)
       - (Cần làm 1 ảnh phòng riêng homestay sạch sẽ, cửa sổ kính nhìn thẳng ra biển mây sớm mai ở mục này)

7. **Chiến lược Từ khóa & Phân Bổ Trải Đều (Keyword Strategy & Even Distribution)**:
   - **QUY ĐỊNH BẮT BUỘC VỀ DANH SÁCH TỪ KHÓA (STRICT KEYWORD INVENTORY & ZERO HALLUCINATION)**:
     - **Chỉ sử dụng ĐÚNG số lượng và cụm từ khóa do người dùng cung cấp**:
       - Người dùng cung cấp bao nhiêu cụm key thì dùng **CHÍNH XÁC bấy nhiêu cụm key**.
       - Tuyệt đối **KHÔNG tự ý bịa đặt, suy diễn, mở rộng hay thêm bớt** bất kỳ từ khóa nào khác (nghiêm cấm tự chế "từ khóa liên quan", "từ khóa LSI tự nghĩ", "từ khóa phụ tự sinh").
       - Toàn bộ Dàn ý, Bảng KEY & VOLUME, Ma trận phân bổ từ khóa và Thân bài viết **CHỈ ĐƯỢC PHÉP CHỨA VÀ PHÂN BỔ ĐÚNG CÁC CỤM KEY NGƯỜI DÙNG ĐÃ GIAO**.
       - Trong Bảng Ma trận phân bổ từ khóa: Cột "Từ khóa mục tiêu" **CHỈ ĐƯỢC PHÉP** điền các từ khóa nằm trong danh sách người dùng đã cung cấp. Các phần nội dung không chứa từ khóa thì để dấu `-` hoặc ghi rõ không chèn key, tuyệt đối không tự bịa ra từ khóa khác để nhét vào bảng.
   - **Tuyệt đối KHÔNG tự ý bôi đỏ hay tô màu từ khóa (Giữ chữ đen tự nhiên)**: Mọi lần xuất hiện của từ khóa chính và từ khóa phụ trong file Word (`Result/bai-viet.docx`) để dạng văn bản thông thường: **chữ màu đen mặc định, không bôi đỏ, không tô nền, không in đậm** chỉ vì đó là từ khóa (người dùng sẽ tự kiểm tra phân bổ từ khóa). Màu đỏ (`#C00000`) chỉ áp dụng duy nhất cho các đoạn ghi chú ảnh đặt trong ngoặc đơn `(...)` để người đăng bài/designer nhận diện.
   - **QUY TẮC BẮT BUỘC VỀ SỰ HIỆN DIỆN CỦA KEY CHÍNH & KEY PHỤ TRONG MỌI MỤC H2 (MỤC H2 NÀO CŨNG PHẢI CÓ TỐI THIỂU 2 - 3 KEY CHÍNH VÀ KEY PHỤ ĐI KÈM)**:
     - **Mục H2 nào cũng bắt buộc xuất hiện tối thiểu 2 - 3 key chính trong thân bài**:
       * Trong **mọi mục H2** (tính toàn bộ phần nội dung thân bài và các nhánh H3/H4 trực thuộc mục H2 đó), từ khóa chính **BẮT BUỘC PHẢI XUẤT HIỆN TỐI THIỂU TỪ 2 ĐẾN 3 LẦN**.
       * **Tiêu đề H2 KHÔNG được tính là 1 lần xuất hiện**: Từ khóa chính xuất hiện trong dòng tiêu đề H2 **tuyệt đối không được tính** vào số lần xuất hiện này. Định mức tối thiểu 2 - 3 lần bắt buộc phải nằm hoàn toàn trong các câu văn nội dung thân bài của mục H2 đó.
     - **Bắt buộc thêm các từ khóa phụ hiển thị cùng trong từng mục H2**:
       * Tại mỗi mục H2, bên cạnh 2 - 3 lần xuất hiện của key chính, Agent **bắt buộc phải phân bổ thêm các từ khóa phụ (Key phụ 1, Key phụ 2...) hiển thị cùng** một cách nhịp nhàng, đan xen hợp lý.
     - **Triệt tiêu hoàn toàn tình trạng "trống key" và khoảng cách quá xa**:
       * Tuyệt đối không để xảy ra tình trạng "trống key" (viết cả một đoạn dài 150 - 250 từ hoặc nguyên một mục H2 mà chỉ có tiêu đề có key, còn bên dưới rất lâu mới xuất hiện 1 key chính hoặc không có key nào).
       * Phân bổ từ khóa chính và phụ trải đều đặn khắp các phân đoạn của từng H2, giữ cho tín hiệu SEO luôn liên tục, dày dặn vừa phải và tự nhiên xuyên suốt bài viết.
     - **QUY TẮC TRÁNH ĐẶT KEY NGAY CẠNH TIÊU ĐỀ H2, H3 (ƯU TIÊN HIỂN THỊ Ở KHOẢNG GIỮA ĐOẠN/MỤC)**:
       * **Hạn chế tối đa việc hiển thị key ngay sát cạnh tiêu đề H2, H3**: Tuyệt đối không vừa dứt dòng tiêu đề H2/H3 xuống dòng là câu văn đầu tiên đã lập tức nhồi ngay từ khóa chính hoặc key phụ (như kiểu `1.1. Khách sạn...` -> `Tham gia tour Trùng Khánh...`). Cách chèn này tạo cảm giác máy móc, lặp từ thô cứng và rất gượng gạo.
       * **Nên hiển thị key ở vị trí khoảng giữa**: Câu mở đầu dưới heading nên dùng để dẫn dắt bối cảnh hoặc nêu thông tin thực tế tự nhiên. Sau đó mới đưa từ khóa xuất hiện ở **vị trí khoảng giữa đoạn văn** (sau khi đã đi qua 1 - 2 câu dẫn dắt) hoặc ở **đoạn văn thứ 2, thứ 3** trong nhánh nội dung đó, giúp mạch đọc mượt mà và tự nhiên nhất.
   - **Tỉ lệ key trải đều toàn bài & trong từng mục (Không quá dày, không quá gần, không để khoảng cách quá xa)**:
     - Từ khóa cần được **phân bổ trải đều khắp bài viết và trong từng mục (H2, H3)** một cách nhịp nhàng.
     - **Mật độ không quá dày & không xuất hiện quá gần nhau**: Tuyệt đối không nhồi nhiều từ khóa liên tiếp trong cùng 1 câu hoặc 2 câu liền kề; không để từ khóa lặp lại dồn dập khiến người đọc thấy ngột ngạt hoặc spam.
     - **Không để khoảng cách giữa các lần xuất hiện quá xa**: Tránh việc viết liền 200 - 300 từ mà hoàn toàn không có từ khóa nào rồi mới xuất hiện lại.
     - **Câu chữ linh hoạt, uyển chuyển để luôn tự nhiên nhất**: Dùng cấu trúc câu đa dạng, ngữ cảnh dẫn dắt phong phú. Từ khóa phải được hòa tan mượt mà vào mạch chia sẻ trải nghiệm thực tế, chuẩn ngữ pháp tiếng Việt, đọc lên thấy hoàn toàn tự nhiên như người thật viết.
   - **Ép đúng tỷ lệ chuẩn SEO (Mật độ 1.5% - 2.5%)**:
     - Key chính: Xuất hiện từ 6 - 10 lần (tùy dung lượng bài 1.200 - 2.000 từ).
     - Key phụ: Mỗi key xuất hiện từ 2 - 4 lần rải đều tại các mục tương ứng.
     - Tổng mật độ từ khóa mục tiêu được khống chế chặt chẽ trong khoảng **1.5% - 2.5%** (tối đa 3.0%), tuyệt đối không dưới 1% (thiếu tín hiệu SEO) và không quá 3.5% (chống spam keyword).
   - **Không gượng ép, ngữ cảnh mượt mà (Natural & Fluent Placement)**:
     - Tuyệt đối không nhồi nhét từ khóa thô cứng làm hỏng cấu trúc câu hoặc gượng gạo văn phong.
     - Các câu trước và sau từ khóa phải liền mạch về ý nghĩa, mang lại cảm giác chân thực, mạch lạc.
   - **Bản đồ phân bổ đều đặn**: Title (Key 1), H1 (Key 2 khác Title 100% nếu có nhiều key, hoặc khác biệt hoàn toàn cấu trúc & góc giật tít nếu chỉ có 1 key), Mở bài (Sapo: 1 key chính trong 100 từ đầu), TẤT CẢ các mục H2 (mỗi mục H2 có tối thiểu 2 - 3 key chính trong thân bài + key phụ hiển thị cùng), Kết bài (1 key chính kèm CTA).
8. **Quy cách lập Dàn ý (Outline Format)**:
   - **Khai thác ý mới trong H2, H3 (Content Freshness & Information Gain)**: Chủ động tìm tòi và đưa các ý mới, góc tiếp cận độc đáo, điểm nhấn mới mẻ vào các đề mục H2, H3 (góc check-in độc lạ, khung giờ đẹp săn ảnh/săn mây, trải nghiệm ẩm thực ngõ ngách bản địa, mẹo tránh đông...). Tuyệt đối không lập dàn ý rập khuôn, sáo mòn theo lối cũ.
   - **Đánh số tự nhiên (Numbering)**: Tiêu đề hiển thị phải dùng dạng số tự nhiên (`1.`, `1.1.`, `1.2.`, `2.`, `2.1.`,...). **Tuyệt đối KHÔNG hiển thị ký hiệu kỹ thuật như `H2.1`, `H3.1.1`**. (Trong file Word, các mục này vẫn được gán đúng Style Heading 2, Heading 3 chuẩn SEO).
   - **Không hiển thị số đếm ký tự (Clean & Copy-Ready)**: Agent tự động kiểm soát độ dài chuẩn SEO ngầm bên dưới, nhưng **tuyệt đối KHÔNG hiển thị số đếm ký tự `(xx ký tự)`** trên Title, H1 hay các Heading trong dàn ý. Dàn ý phải sạch sẽ hoàn toàn để người dùng copy và sử dụng được ngay mà không cần xóa tay.
   - **Tinh gọn & Trực diện**: Chỉ tập trung vào ý chính, không giải thích dài dòng, rườm rà.
   - **Thông tin dạng Bullet**: Dưới mỗi Heading chỉ gạch đầu dòng các ý chính/thông tin cốt lõi cần viết.
   - **Không thêm nhãn giải thích rườm rà**: Tuyệt đối không chèn các nhãn thừa dưới tiêu đề như `Mục tiêu nội dung`, `Định dạng`, `Ý triển khai:`, `Hình ảnh:...`. Giữ cấu trúc heading và các bullet ý chính thật gọn gàng, dễ đọc.
   - Việc quy hoạch ảnh và format (Bảng/List) được tổng hợp gọn tại bảng Ma trận phân bổ ở cuối dàn ý.

9. **Nguồn Dữ Liệu Tour Bắt Buộc (`ContentTour/*`)**:
   - Mọi thông tin chi tiết về tour (lịch trình từng ngày, thời gian di chuyển, giá tour, dịch vụ bao gồm / không bao gồm, chính sách phụ thu, điểm tham quan, lưu ý...) **bắt buộc phải lấy từ file tài liệu tour do người dùng chỉ định trong thư mục `ContentTour/*`**.
   - Tuyệt đối không tự bịa đặt, suy diễn số liệu hay lộ trình khác với nội dung thực tế trong file tour người dùng cung cấp.

9.2. **Phân Loại Định Dạng Bài Viết: Dạng Bài Tour ([tour]) vs Dạng Bài Blog ([blog])**:
   - Khi người dùng gọi lệnh `/create-outline <cụm từ khóa> [tour]` (hoặc mặc định khi có chỉ định file tour):
     * **Mục tiêu**: Xây dựng bài viết giới thiệu, quảng bá và bán tour du lịch cụ thể.
     * **Nguồn dữ liệu**: Bắt buộc đọc từ file tour trong `ContentTour/*`. Giữ đúng cấu trúc chuẩn của bài tour: lịch trình từng ngày/mốc giờ, bảng giá tour, dịch vụ bao gồm/loại trừ, chính sách phụ thu, điểm tham quan và lưu ý tour.
   - Khi người dùng gọi lệnh `/create-outline <cụm từ khóa> [blog]`:
     * **Mục tiêu**: Xây dựng bài viết dạng blog cẩm nang, chia sẻ kinh nghiệm, hướng dẫn du lịch hoặc review thực tế.
     * **Tham khảo dàn ý của 10 đối thủ đầu tiên (TOP 10 SERP Google)**: Agent bắt buộc sử dụng công cụ `search_web` để nghiên cứu, khảo sát dàn ý của 10 bài viết đang đứng đầu bảng xếp hạng Google cho từ khóa mục tiêu.
     * **Sắp xếp hợp lý, đúng và đủ Intent người đọc**: Tổng hợp đầy đủ các nội dung cốt lõi mà người tìm kiếm mong muốn giải đáp từ A - Z; loại bỏ thông tin rác hoặc trùng lặp; sắp xếp bố cục đề mục theo luồng tư duy mạch lạc, tự nhiên.
     * **Tìm kiếm ý mới trong thẻ H2, H3 (Content Freshness & Information Gain)**: Chủ động tìm tòi, đào sâu và đưa vào các góc nhìn độc đáo, điểm nhấn mới lạ mà 10 đối thủ chưa có hoặc nói còn sơ sài (góc check-in độc lạ, khung giờ vàng săn ảnh, quán ăn ngõ ngách chuẩn vị, mẹo tránh đông, bí quyết tiết kiệm chi phí thực chiến...).
     * **Quy chuẩn SEO On-page giữ nguyên 100%**: Title 55-60 ký tự Key 1, H1 khác Title 55-60 ký tự Key 2, Sapo 2-3 dòng <155 từ chứa key trong 100 từ đầu và nhắc thương hiệu công ty, Kết bài ngắn gọn có CTA số Zalo + thương hiệu, không dùng "bạn nên/cần/phải", xuất file Word ra `Result/outline.docx`.

9.1. **Phân Định Tuyệt Đối Thư Mục Đầu Vào (`ContentTour/`) & Thư Mục Đầu Ra (`Result/`) - Bảo Toàn File 100%**:
   - **Thư mục đầu vào (`ContentTour/`)**: Chuyên chứa toàn bộ file tài liệu nguồn về tour do người dùng cung cấp (Word `.docx`, PDF `.pdf`, text `.txt`...).
     - Agent **CHỈ ĐỌC** dữ liệu từ `ContentTour/*`.
     - **TUYỆT ĐỐI KHÔNG** ghi đè, chỉnh sửa, di chuyển hoặc xóa bất kỳ file nào trong thư mục `ContentTour/`.
   - **Thư mục đầu ra (`Result/`)**: Chuyên chứa toàn bộ sản phẩm hoàn thiện do Agent tạo ra:
     - Dàn ý: Lưu trực tiếp vào `Result/outline.docx` (hoặc `Result/[slug]-outline.docx`).
     - Bài viết hoàn chỉnh: Lưu trực tiếp vào `Result/bai-viet.docx` (hoặc `Result/[slug].docx`).
     - **BẮT BUỘC** trả mọi kết quả hoàn chỉnh vào thư mục `Result/`. Tuyệt đối không lưu file kết quả ở thư mục gốc workspace hoặc thư mục khác để đảm bảo không bị thất lạc file, không làm xáo trộn dữ liệu nguồn và giúp người dùng dễ dàng quản lý.
   - **Luồng xử lý liên thông giữa hai thư mục**:
     - Lệnh `/create-outline`: Đọc tài liệu tour từ `ContentTour/*`, xuất dàn ý ra `Result/outline.docx`.
     - Lệnh `/update-outline`: Đọc dàn ý từ `Result/outline.docx`, cập nhật trực tiếp vào `Result/outline.docx`.
     - Lệnh `/create-post`: Đọc dàn ý đã duyệt từ `Result/outline.docx`, đối chiếu tài liệu tour từ `ContentTour/*`, xuất bài viết hoàn chỉnh vào `Result/bai-viet.docx`.
     - Lệnh /fix-post: Đọc bài viết có sẵn từ ContentTour/*, tinh chỉnh chuẩn SEO (mật độ & vị trí key trải đều, giữ nguyên format và nội dung đã duyệt), xuất kết quả hoàn thiện vào DUY NHẤT 1 file Result/[slug]-fixed.docx (tuyệt đối không xuất thêm file phụ, không nhân bản ra 2 bài).

10. **Quy chuẩn Viết Bài Tự Nhiên, Trực Diện & Kiểm Soát Tỷ Lệ AI Dưới 5% (Strict Anti-AI & Burstiness Standard)**:
   - **Cam kết Tỷ lệ AI < 5% (Human Content ≥ 95%)**: Khi kiểm tra qua các công cụ quét AI hàng đầu hiện nay như **Copyleaks, GPTZero, Winston AI...**, tỷ lệ AI Content **bắt buộc phải dưới 5%**. Tuyệt đối không để sót câu văn nào bị công cụ bôi màu gắn cờ AI.
   - **DANH SÁCH ĐEN CÁC MẪU CÂU & CÚ PHÁP AI BỊ CẤM TIỆT (SYNTACTIC AI BLACKLIST)**:
     - **CẤM TUYỆT ĐỐI cấu trúc khuyên răn, lên lớp máy móc: "bạn nên...", "bạn phải...", "bạn cần...", "bạn hãy...", "du khách nên/cần/phải..."**:
       - *Lý do*: Đây là mẫu câu sáo rỗng mang tính thuyết giáo điển hình của AI, tạo cảm giác thiếu tự nhiên và lập tức bị Copyleaks/GPTZero gắn cờ AI.
       - *Cách thay thế*: Chuyển thành câu trần thuật khách quan, câu chia sẻ thực tế hoặc hành động cụ thể:
         - Thay vì: *"Bạn nên mang theo áo ấm vì đêm Măng Đen rất lạnh."* -> *"Đêm Măng Đen nhiệt độ hạ xuống 15 độ C. Một chiếc áo khoác gió dày sẽ giữ ấm vừa vặn."*
         - Thay vì: *"Bạn cần đặt tour trước 2 tuần để giữ chỗ."* -> *"Mùa cao điểm phòng hết rất sớm. Đặt tour trước 2 tuần giúp bạn chủ động lịch trình và giữ được vị trí đẹp."*
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
     - **CẤM các từ ngữ hoa mỹ AI thường dùng**: *“liều thuốc tinh thần”, “tái tạo năng lượng”, “tạm gác lại những xô bồ khói bụi”, “hòa mình vào thiên nhiên”, “hít căng lồng ngực”, “bức tranh tuyệt mỹ”, “ấm nồng”, “vượt trội”, “lắng đọng”, “không chỉ là... mà còn là...”, “được ví như...”, “hành trình này không đơn thuần là...”*.
     - **Mở bài và kết bài thực tế**: Mở bài đi thẳng vào thông tin tour, giá vé, điều kiện thời tiết và khéo léo nhắc tên thương hiệu. Kết bài viết **thật ngắn gọn, súc tích (chỉ từ 2 - 3 câu ngắn, dưới 80 từ)**, tóm tắt mốc khởi hành, chốt CTA kèm số Zalo tư vấn và tên thương hiệu của công ty. Tuyệt đối không viết lan man dài dòng, không chúc sến súa, không triết lý cuộc sống.
   - **KỸ THUẬT ĐẠT 100% HUMAN CONTENT (HIGH BURSTINESS & REALISM)**:
     - **Đan xen câu siêu ngắn (High Burstiness)**: Cứ sau 1-2 câu trần thuật (10 - 14 từ), BẮT BUỘC chèn 1 câu siêu ngắn (3 - 6 từ): *"Đường khá dốc."*, *"Trời rét nhanh."*, *"Quốc lộ phẳng lì."*, *"Xe chạy rất êm."*, *"Giá vé đã bao gồm trọn gói."*, *"Chuẩn bị từ sớm."*. Điều này phá vỡ hoàn toàn thuật toán nhận diện tính đồng nhất của AI.
     - **Chi tiết thực tế & giá tiền đời thường (High Perplexity)**: Đưa các chi tiết mắt thấy tai nghe: giá tô phở khô 40.000 - 50.000đ, bát nước dùng xương ngọt lịm, ly cà phê 35.000đ, chặng đường 180km chạy 3.5 - 4 tiếng, đèo Măng Đen dài 12km dốc quanh co, nền đá thác Pa Sỹ trơn ướt cần giày bám tốt, áo khoác gió vì đêm hạ 15 độ C...
   - **Câu văn ngắn gọn, dứt khoát (10 - 15 từ/câu, tối đa ≤ 18 từ)**: Mỗi câu chỉ chứa đúng 1 ý. Tách nhỏ câu đơn gãy gọn, mạch lạc.
   - **Đoạn văn ngắn (1 - 3 câu/đoạn)**: Giữ khối văn bản thông thoáng, tối ưu trải nghiệm đọc lướt trên điện thoại.

10.1. **Quy chuẩn Chống Trùng Lặp Tuyệt Đối & Tự Động Check Spin Toàn Diện (Zero Plagiarism & 100% Unique - Check Spin = 0%)**:
   - **Cam kết Tỷ lệ Trùng Lặp = 0%**: Khi kiểm tra qua các công cụ check trùng lặp (Spineditor, SmallSEOTools, DupliChecker...), tỷ lệ trùng lặp **bắt buộc là 0%** (hoặc < 2% với các tên riêng địa danh cố định). Mọi câu văn, dòng bảng, mục danh sách đều phải đạt tick xanh (Unique 100%).
   - **QUY ĐỊNH BẮT BUỘC CHECK TRÙNG LẶP SPIN TRƯỚC KHI BÀN GIAO (KHÔNG ĐỂ SỬA ĐI SỬA LẠI)**:
     - Agent phải **chủ động rà soát và kiểm tra kỹ lưỡng tỷ lệ trùng lặp spin trong toàn bộ nội dung** (mở bài, thân bài, lịch trình chi tiết, bảng giá, danh mục dịch vụ, chính sách trẻ em, lưu ý thực tế, kết bài) ngay trong quá trình viết và trước khi xuất file `.docx`.
     - **Tuyệt đối không để xảy ra tình trạng người dùng mang đi check spin bị báo đỏ hoặc báo vàng trùng lặp**, khiến người dùng phải mất công kiểm tra lại và bắt Agent sửa đi sửa lại rất vất vả.
     - Toàn bộ nội dung phải đạt chuẩn **Unique 100% ngay từ lần xuất bản đầu tiên**.
   - **Kỹ thuật Paraphrase toàn diện cho tài liệu tour**:
     - *Chính sách trẻ em*: Tuyệt đối không sao chép nguyên văn mẫu (*“Trẻ dưới 5 tuổi: Miễn phí”*, *“Trẻ từ 5-9 tuổi: Tính 75%”*). Phải diễn giải thành câu văn tự nhiên, uyển chuyển của người viết.
     - *Điểm đón & Thời gian*: Không dùng cụm từ cứng nhắc (*“05h30 tại Nhà hát Lớn và 06h00 tại Big C...”*). Diễn giải thành câu có ngữ cảnh và linh hoạt từ ngữ.
     - *Bảng biểu & Bảng chi phí*: Mọi mục dịch vụ, khoản tự túc, danh sách điểm đến đều phải được làm mới từ ngữ, không dùng các cụm từ phổ thông dễ trùng trên web.
     - *Câu chuyển đoạn & Mở đầu*: Cấm các câu sáo rỗng thường gặp trên blog (*“Bài viết này tổng hợp toàn bộ lịch trình”*, *“Bạn chỉ cần chuẩn bị đồ cá nhân”*, *“Tự lái xe mang lại cảm giác tự do”*). Thay bằng các câu diễn đạt trải nghiệm cụ thể, độc nhất.
     - *Tiền tip & Phụ phí*: Dùng các từ thay thế tự nhiên (*“khoản thưởng bồi dưỡng tùy sự hài lòng”*, *“tiêu vặt phát sinh ngoài lề”*).
   - **Cơ chế Tự Rà Soát Trùng Lặp**: Agent chủ động rà soát từng dòng, từng câu trong bài trước khi xuất file `.docx`, đảm bảo tính độc nhất 100%, triệt tiêu hoàn toàn nguy cơ dính spin trùng lặp để người dùng có thể sử dụng ngay mà không phải sửa lại.

11. **Cấu trúc Phần Mở Đầu Bài Viết DOCX (Master Header Block Format)**:
   - Mọi bài viết hoàn chỉnh xuất ra file `.docx` bắt buộc phải có cấu trúc phần đầu chuẩn hóa theo đúng thứ tự sau:
     1. **Bảng Thống kê Từ khóa (KEY & VOLUME)**:
        - Tiêu đề cột: `KEY` và `VOLUME` (In hoa, in đậm, căn giữa).
        - Màu nền hàng tiêu đề: **Màu vàng tươi** (`#FFFF00`).
        - Liệt kê toàn bộ cụm từ khóa mục tiêu cùng chỉ số Volume tương ứng (nếu người dùng không cung cấp số volume thì ghi nhận theo số liệu ước lượng hoặc `-`). Cột Volume căn giữa.
     2. **Các trường thẩm định chất lượng**:
        - `Check spin:`
        - `Check AI:`
     3. **Khối Thông tin SEO On-page**:
        - `Key chính: [Từ khóa chính]`
        - `Meta: [Đoạn Meta Description 140 - 155 ký tự có CTA]`
        - `Title: [SEO Title 55 - 60 ký tự, tối ưu Key 1 ở đầu, có số, từ bổ trợ, | hoặc -]`
         - `H1: [Tiêu đề H1 - BẮT BUỘC KHÁC TITLE 100%, tối ưu Key 2 nếu có nhiều key, hoặc khác biệt hoàn toàn cấu trúc & góc giật tít nếu chỉ có 1 key]`
     4. **Đoạn Mở bài (Sapo)**: Bắt đầu viết trực tiếp ngay dưới dòng `H1: ...`, ngắn gọn 2 - 3 câu (<155 từ), thu hút, bắt buộc chứa từ khóa chính trong 100 từ đầu tiên và khéo léo nhắc tên thương hiệu của công ty.
     5. **Thân bài**: Tiếp nối liền mạch bằng các heading đánh số tự nhiên: `1.`, `1.1.`, `1.2.`, `2.`, `2.1.`...

---

## 2. QUY TRÌNH THỰC HIỆN KHI NHẬN YÊU CẦU

Quy trình chi tiết tạo Outline chuẩn SEO: [.agents/workflows/seo-outline-workflow.md](file:///c:/Users/PC/Documents/ContentRewrite/.agents/workflows/seo-outline-workflow.md)

Khi người dùng cung cấp từ khóa và chỉ định file trong `ContentTour/*`:
1. **Bước 1**: Tiếp nhận từ khóa và xác định dạng bài viết:
   - Nếu là **`[tour]`**: Đọc và trích xuất dữ liệu thực tế từ file chỉ định trong `ContentTour/*` (lịch trình, giá, dịch vụ, điểm đến).
   - Nếu là **`[blog]`**: Sử dụng `search_web` tham khảo dàn ý của 10 đối thủ đầu tiên trên Google, phân tích sắp xếp đúng & đủ intent, tìm ý mới mẻ độc đáo cho các thẻ H2, H3.
2. **Bước 2**: Đề xuất bộ **SEO Title** (đạt chuẩn 55-60 ký tự, tối ưu Key 1) & **Thẻ H1** (BẮT BUỘC KHÁC TITLE 100%, tối ưu Key 2 nếu có nhiều key hoặc khác biệt hoàn toàn cấu trúc & góc giật tít nếu chỉ có 1 key) & **Meta Description** (140-155 ký tự có CTA).
3. **Bước 3**: Đề xuất **Sapo** ngắn gọn, thu hút (2-3 dòng, có key chính trong 100 từ đầu và nhắc tên thương hiệu của công ty).
4. **Bước 4**: Xây dựng **Dàn ý Headings (đánh số 1., 1.1., 1.2., 2., 2.1.,...)** bám sát dữ liệu file tour, chủ động khai thác ý mới mẻ và góc tiếp cận độc đáo trong các H2, H3, chỉ gạch đầu dòng các ý chính cốt lõi. Phân bổ từ khóa trải đều trong từng mục, không để khoảng cách quá xa.
5. **Bước 5**: Lập bảng Ma trận phân bổ từ khóa & format trình bày (quy hoạch tập trung ảnh, Alt text, Table/List tại đây).
6. **Bước 6**: Tự động xuất dàn ý ra file Word **`Result/outline.docx`** (với đầy đủ style Word Heading, Bảng biểu và gạch đầu dòng trực quan) kèm bảng Pre-publish Checklist để người dùng mở xem dễ dàng trong thư mục `Result/`.

---

## 3. HỆ THỐNG LỆNH ĐIỀU KHIỂN (COMMAND ROUTER & DOCX STANDARD)

Tất cả sản phẩm nội dung bàn giao cho người dùng (từ Dàn ý đến Bài viết hoàn chỉnh) **bắt buộc xuất ra file `.docx` (Microsoft Word) trong thư mục `Result/`** để người dùng dễ mở, dễ đọc, dễ chỉnh sửa và bảo toàn tuyệt đối dữ liệu gốc trong `ContentTour/`. Agent tuân thủ chặt chẽ ranh giới của từng lệnh, **tuyệt đối không làm vượt phạm vi**:

| Lệnh (Command) | Thao tác thực hiện | Giới hạn bắt buộc (Constraints) |
| :--- | :--- | :--- |
| `/create-outline <cụm key> [tour\|blog] [file tour]` | Tạo dàn ý chuẩn SEO cho 2 dạng bài viết: <br>- **Dạng [tour]**: Giữ đúng cấu trúc tour hiện tại, đọc dữ liệu thực tế từ file tour trong `ContentTour/*`. <br>- **Dạng [blog]**: Tham khảo dàn ý của 10 đối thủ đầu tiên trên Google (`search_web`), sắp xếp hợp lý đúng & đủ intent người đọc, tìm ý mới mẻ độc đáo trong thẻ H2, H3. <br>Cả 2 dạng đều tối ưu Title (Key 1), H1 (KHÁC TITLE 100% trong mọi trường hợp, tối ưu Key 2 hoặc khác cấu trúc/góc giật tít nếu 1 key), Meta Des có CTA, Sapo nhắc thương hiệu, Kết luận có CTA số Zalo + thương hiệu, phân bổ key đều. **ĐẦU RA: Tự động xuất trực tiếp ra file `Result/outline.docx`**. | **TUYỆT ĐỐI KHÔNG VIẾT BÀI CHI TIẾT**. Dạng [tour] bám sát `ContentTour/*`. Dạng [blog] khảo sát 10 đối thủ TOP Google và tìm ý mới H2/H3. Chỉ tạo dàn bài và xuất ra file `Result/outline.docx`. |
| `/update-outline <nội dung sửa>` | Đọc trực tiếp từ file `Result/outline.docx`, cập nhật theo phản hồi của người dùng, **tự động cập nhật lại file `Result/outline.docx`**. | **VẪN KHÔNG VIẾT BÀI**. Chỉ cập nhật lại dàn bài theo đúng ý kiến người dùng. |
| `/create-post` | Đọc dàn bài trực tiếp từ file `Result/outline.docx` và đối chiếu dữ liệu file tour trong `ContentTour/*`, tiến hành viết bài hoàn chỉnh chuẩn SEO 100%. Title tối ưu Key 1, H1 KHÁC TITLE 100% (tối ưu Key 2 nếu nhiều key hoặc khác hoàn toàn cấu trúc nếu 1 key), Sapo ngắn gọn thu hút chứa Key chính và nhắc tên thương hiệu, Kết bài ngắn gọn kêu gọi CTA kèm số Zalo và thương hiệu công ty, từ khóa phân bổ trải đều toàn bài và từng mục không để cách xa nhau, tuyệt đối không dùng cấu trúc khuyên răn AI ("bạn nên...", "bạn phải...", "bạn cần..."). **ĐẦU RA: Xuất trực tiếp ra file `.docx` (Microsoft Word) trong thư mục `Result/`** (ví dụ: `Result/bai-viet.docx`). | Chỉ thực hiện khi người dùng đã duyệt dàn ý và phát lệnh này. Lưu thành file `.docx` tại thư mục `Result/`. |
| /fix-post <file tour> [keys] | Đọc bài viết đã chuẩn bị sẵn trong ContentTour/*, giữ nguyên format và nội dung đã duyệt, chỉ tinh chỉnh tối ưu chuẩn SEO (mật độ key 1.5% - 2.5%, phân bổ trải đều không quá dày, không quá gần, không để cách quá xa, câu chữ linh hoạt tự nhiên, Title/H1 KHÁC NHAU 100% (sửa ngay nếu phát hiện Title trùng H1), Sapo nhắc tên thương hiệu, Kết bài ngắn gọn có CTA số Zalo + thương hiệu, loại bỏ các cấu trúc "bạn nên...", "bạn phải...", "bạn cần..."). **ĐẦU RA: Xuất trực tiếp ra DUY NHẤT 1 file Word .docx trong thư mục Result/** (Result/[slug]-fixed.docx, tuyệt đối không xuất thêm file thứ 2 như bai-viet.docx). | **KHÔNG LÀM MỚI TOÀN BỘ BÀI**, không xáo trộn format đã có. Bảo toàn 100% file gốc trong ContentTour/*. Kết quả CHỈ LƯU DUY NHẤT 1 FILE vào Result/. |
| `/create-sapo <key / H1>` | Đề xuất 3 phương án mở bài Sapo ngắn gọn, thu hút (2-3 dòng, <155 từ, có key chính trong 100 từ đầu và khéo léo nhắc tên thương hiệu công ty). | Chỉ xuất 3 phương án Sapo, không viết thêm các phần khác. |
| `/create-title <keys>` | Đề xuất bộ phương án **SEO Title** (tối ưu Key 1) và **Thẻ H1** (KHÁC TITLE 100% trong mọi trường hợp, kể cả khi chỉ có 1 từ khóa), chuẩn 55 - 60 ký tự, mỗi tiêu đề sử dụng 1 key riêng biệt từ danh sách từ khóa. | Chỉ xuất các phương án Title và H1 kèm số đếm ký tự, không viết bài. |
| `/create-des <key>` | Đề xuất 2 phương án Meta Description (140-155 ký tự, key ở đầu, có CTA). | Chỉ xuất 2 phương án Meta Description kèm số đếm ký tự. |

* **Quy chuẩn Định dạng DOCX (Thuần DOCX 100% trong Workspace & Lưu Tại `Result/`)**:
  - Mọi dàn bài xuất ra `Result/outline.docx` và bài viết xuất ra `Result/bai-viet.docx` đều được biên dịch và lưu trữ trực tiếp dưới dạng `.docx` trong thư mục `Result/`.
  - **Tuyệt đối không lưu file `.md` trong thư mục làm việc của người dùng**. Mọi khâu đọc/ghi dữ liệu đều thông qua các công cụ `.docx` chuyên dụng (`read_docx.py`, `md_to_docx.py`).
  - Tiêu đề đánh số chuyên nghiệp (`1.`, `1.1.`, `1.2.`, `2.`, `2.1.`,...), font Arial/Calibri hoặc Google Sans Flex, lề 1 inch, Heading 1 đến Heading 4 có phân cấp rõ nét, Bảng biểu (Table) đẹp mắt.
  - Người dùng có thể click đúp mở trực tiếp bằng Microsoft Word hoặc Google Docs mà không gặp bất kỳ khó khăn nào về hiển thị.

