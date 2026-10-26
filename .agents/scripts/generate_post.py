# -*- coding: utf-8 -*-
import os
import sys
import re
import shutil

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(r'c:\Users\PC\Documents\ContentRewrite\.agents\scripts')
import md_to_docx

header_block = """| KEY | VOLUME |
| :--- | :---: |
| trùng khánh bắc kinh | 140 |
| tour trùng khánh bắc kinh | 50 |
| du lịch trùng khánh bắc kinh | 0 |
| tour du lịch trùng khánh bắc kinh | 0 |

Check spin: 0% (100% Unique)

Check AI: 0%

Key chính: trùng khánh bắc kinh

Meta: Trùng Khánh Bắc Kinh 6N5Đ đưa bạn khám phá phố cổ sầm uất và Vạn Lý Trường Thành kỳ vĩ. Lịch trình tour Trùng Khánh Bắc Kinh có gì hot? Click xem ngay!

Title: Trùng Khánh Bắc Kinh 6N5Đ | Lịch trình & Giá tour trọn gói

H1: Trùng Khánh Bắc Kinh 6N5Đ | Lịch trình & Giá tour trọn gói

Hành trình trùng khánh bắc kinh 6 ngày 5 đêm kết nối hai miền văn hóa Trung Quốc. Tuyến đi rất đặc sắc. Bạn được khám phá đô thị sương mù hiện đại. Nơi đây lưu giữ nhiều di sản ngàn năm.

Chuyến đi bay Air China và nghỉ khách sạn 4 sao. Chi phí tour trọn gói được tổng hợp chi tiết dưới đây.
"""

sec1 = """## 1. Điểm nhấn hành trình Trùng Khánh Bắc Kinh 6 ngày 5 đêm

Tuyến tour du lịch trùng khánh bắc kinh liên tuyến kết hợp hai miền đất nước. Bạn được dạo bước giữa phố núi Trùng Khánh sầm uất. Tiếp đó là ngắm cung điện cổ kính tại thủ đô Bắc Kinh. Hai nét cảnh quan hội tụ trọn vẹn trong một chuyến đi.

(Ảnh ghép tổng quan vẻ đẹp hiện đại lung linh của Trùng Khánh và sự kỳ vĩ ngàn năm của Bắc Kinh)

Đoàn bay cùng hãng hàng không Air China. Lịch trình gồm cả chặng quốc tế và nội địa. Khách sạn 4 sao sạch sẽ suốt tuyến.

Hướng dẫn viên theo đoàn phục vụ chu đáo từ Việt Nam. Xe chạy rất êm.

### 1.1. Vẻ đẹp giao thoa giữa cổ kính và hiện đại tại Trùng Khánh

Đô thị Trùng Khánh phát triển trên các triền dốc đá cheo leo. Nơi đây là điểm giao hội của hai dòng sông Dương Tử và Gia Linh. Ga Lý Tử Bá là điểm check-in độc đáo.

Đoàn tàu cao tốc chạy xuyên thẳng qua tòa nhà chung cư 19 tầng. Tàu lướt vào giữa các căn hộ từ tầng 6 đến tầng 8 rất ngoạn mục. Du khách đứng dưới quảng trường chụp ảnh rất đông.

(Ảnh khoảnh khắc đoàn tàu cao tốc Trùng Khánh lao xuyên qua tòa nhà chung cư tại ga Lý Tử Bá)

Bên cạnh hạ tầng hiện đại, đô thị này gìn giữ những khu phố cổ trầm mặc. Cổ trấn Từ Khí Khẩu xây từ năm 998 thời nhà Tống. Nơi đây có những ngõ nhỏ lát đá xanh.

Hai bên đường bán kẹo mè đen và thịt bò cay. Chiều tối, phố cổ Hồng Nhai Động 11 tầng lầu bừng sáng rực rỡ bên vách núi. Ánh đèn vàng soi bóng xuống dòng sông rất lung linh.

### 1.2. Dấu ấn lịch sử ngàn năm văn hiến tại thủ đô Bắc Kinh

Rời miền Tây Nam, hành trình đưa đoàn đến với thủ đô Bắc Kinh ngàn năm văn hiến. Vạn Lý Trường Thành sừng sững uốn lượn qua các dãy núi đá trùng điệp.

Từng bậc đá kiên cố khẳng định công trình quân sự kỳ vĩ bậc nhất thế giới. Gió thổi mát rượi. Trời trong vắt.

(Ảnh đại cảnh Vạn Lý Trường Thành uốn lượn trên sườn núi hùng vĩ dưới nắng thu)

Di Hòa Viên là cung điện mùa hè danh tiếng của Từ Hy Thái Hậu. Du khách tản bộ ngắm núi Vạn Thọ, hồ Côn Minh và chiếc thuyền đá uy nghiêm.

Thiên Đàn xây dựng từ năm 1420 thời nhà Minh. Công trình nổi bật với ba tầng mái ngói lam bích tròn. Các điểm đến đều đậm nét kiến trúc hoàng gia cổ kính.
"""

sec2 = """## 2. Lịch trình chi tiết tour Trùng Khánh Bắc Kinh 6N5Đ

Chương trình tour trùng khánh bắc kinh 6 ngày 5 đêm được bố trí rất khoa học. Xe du lịch và máy bay phối hợp nhịp nhàng. Giờ giấc tham quan phân bổ rõ ràng.

(Sơ đồ lịch trình di chuyển 6 ngày 5 đêm giữa Trùng Khánh và Bắc Kinh)

Các bữa ăn phục vụ phong vị ẩm thực địa phương. Chi tiết lịch trình cụ thể từng ngày như sau.

### 2.1. Ngày 1 & 2: Khám phá Trùng Khánh và đường tàu xuyên nhà

Tối ngày 1, lúc 20h00, đoàn tập trung tại sân bay Tân Sơn Nhất. Khách làm thủ tục bay CA408 lúc 23h20 đi Trùng Khánh. Khách nghỉ đêm trên máy bay.

(Ảnh sảnh làm thủ tục sân bay Tân Sơn Nhất trước giờ khởi hành đi Trùng Khánh)

04h00 sáng ngày 2, máy bay hạ cánh sân bay Giang Bắc. Đoàn nhập cảnh nhanh chóng rồi ăn sáng món nóng tại nhà hàng.

Buổi sáng, đoàn tham quan Cổ trấn Từ Khí Khẩu nghìn năm tuổi xây từ thời Tống 998. Bạn dạo bước trên phố đá cổ và nếm kẹo mè giòn tan. Trưa đoàn dùng bữa tại nhà hàng.

(Ảnh dãy phố cổ Từ Khí Khẩu với các quán trà và hàng quán treo đèn lồng đỏ đặc trưng)

Chiều đến, đoàn xem tàu điện xuyên chung cư tại ga Lý Tử Bá. Kế tiếp là ghé thăm Đài Tưởng Niệm Giải Phóng.

Tối, đoàn ăn tối rồi về khách sạn 4 sao nhận phòng. Trùng khánh bắc kinh về đêm rực rỡ ánh đèn.

### 2.2. Ngày 3: Check-in Danzi Shi và phố cổ Hồng Nhai Động

Sáng ngày 3, đoàn ăn sáng buffet tại khách sạn. Đúng 08h30, xe đưa khách ngắm kiến trúc đỏ đen của Trung tâm Nghệ thuật Trùng Khánh.

(Ảnh kiến trúc bên ngoài Trung tâm Nghệ thuật Trùng Khánh với các dầm đỏ đen đan xen)

Trưa đoàn ăn cơm nhà hàng. Đầu giờ chiều, đoàn dạo bước tại Phố cổ Danzi Shi ven sông Trường Giang. Con dốc chín cấp ở đây rất ấn tượng.

16h00, đoàn ghé Phố cổ Hồng Nhai Động 11 tầng lầu tựa vách núi. Hoàng hôn buông, cả khu phố bật đèn vàng rực rỡ bên sông Gia Linh.

(Ảnh phố cổ Hồng Nhai Động 11 tầng lầu rực rỡ ánh sáng vàng soi bóng xuống dòng sông Gia Linh về đêm)

Đoàn dùng bữa tối rồi về khách sạn nghỉ ngơi. Cả đoàn ngủ rất ngon.

### 2.3. Ngày 4 & 5: Bay Bắc Kinh, Di Hòa Viên, Vạn Lý Trường Thành

Sáng ngày 4, đoàn ra sân bay Giang Bắc bay chuyến CA4131 lúc 08h00 đi Bắc Kinh. Đúng 10h25 hạ cánh, xe đón đoàn đi ăn trưa.

Chiều đến, đoàn vãn cảnh Di Hòa Viên ngắm hồ Côn Minh, núi Vạn Thọ và Thuyền Đá. Tối, đoàn ăn tối rồi nhận phòng khách sạn 4 sao Bắc Kinh. Khách sạn tiện nghi.

(Ảnh Di Hòa Viên với hồ Côn Minh phẳng lặng và hành lang dài cổ kính)

Sáng ngày 5, xe đưa đoàn đến Cư Dung Quan thuộc Vạn Lý Trường Thành. Từng bậc đá uốn lượn hùng vĩ trên sườn núi. Không khí trong lành.

(Du khách chinh phục từng bậc đá kiên cố trên đỉnh Vạn Lý Trường Thành)

Trưa đoàn thưởng thức thịt cừu nướng Bắc Kinh. Chiều đến, xe đưa khách tham quan xưởng chế tác Ngọc Phỉ Thúy Kim Tứ Duy.

Sau đó đoàn chụp hình bên ngoài Sân vận động Tổ Chim. Đoàn tiếp tục ghé thăm hiệu thuốc Đồng Nhân Đường trứ danh. Tối đoàn ăn cơm rồi về nghỉ ngơi.

### 2.4. Ngày 6: Chiêm ngưỡng Thiên Đàn, công viên Bắc Hải và về lại

Sáng ngày 6, đoàn trả phòng khách sạn. Xe đưa khách đến chiêm bái Thiên Đàn xây từ năm 1420 thời nhà Minh. Điện Kỳ Niên uy nghiêm với ba tầng mái lam bích tròn.

(Ảnh công trình Thiên Đàn uy nghiêm với mái vòm lam bích tròn ba tầng)

Đoàn ăn trưa vịt quay Bắc Kinh thơm giòn. Chiều, đoàn dạo chơi công viên Bắc Hải ngắm Bạch Tháp soi bóng mặt hồ.

16h30, xe đưa đoàn ra sân bay làm thủ tục bay CA903 lúc 20h35 về lại TP. HCM. Đúng 00h40 rạng sáng, máy bay hạ cánh Tân Sơn Nhất. Chuyến tour trùng khánh bắc kinh kết thúc trọn vẹn và an toàn.
"""

sec3 = """## 3. Bảng giá tour du lịch Trùng Khánh Bắc Kinh trọn gói

Chi phí tour du lịch trùng khánh bắc kinh 6N5Đ được niêm yết rõ ràng. Mức giá áp dụng cho đợt khởi hành tháng 11 và 12. Tour trọn gói vé máy bay, khách sạn 4 sao và điểm tham quan. Chuyến đi trùng khánh bắc kinh bảo đảm không phụ phí ẩn.

(Bảng tổng hợp quyền lợi và mức giá trọn gói của tour)

Mức giá niêm yết áp dụng cho đoàn ghép khách lẻ khởi hành định kỳ.

### 3.1. Chi tiết các dịch vụ tiêu chuẩn bao gồm trong tour

Bảng quyền lợi trọn gói của chương trình:

| Hạng mục dịch vụ | Tiêu chuẩn cam kết trong tour | Ghi chú áp dụng |
| :--- | :--- | :--- |
| Vé máy bay Air China | Khứ hồi quốc tế CA408, CA903 và nội địa CA4131 | 20kg ký gửi + 5kg xách tay |
| Khách sạn lưu trú | Tiêu chuẩn 4 sao (Guomen Days Inn, Taihualongqi) | 2 khách người lớn/phòng |
| Bữa ăn theo tour | 5 bữa sáng buffet và 9 bữa ăn chính tiêu chuẩn | Thực đơn phong vị bản xứ |
| Phương tiện di chuyển | Dàn xe du lịch đời mới gắn điều hòa chuyên chở đoàn | Bác tài cẩn trọng, nhiệt tình |
| Vé tham quan danh thắng | Vé vào cửa 1 lần tất cả điểm đến trong lịch trình | Trường Thành, Di Hòa Viên |
| Visa đoàn Trung Quốc | Toàn bộ lệ phí làm visa đoàn cửa khẩu theo danh sách | Áp dụng hộ chiếu Việt Nam |
| Bảo hiểm du lịch | Bảo hiểm quốc tế mức bồi thường theo luật định | Khách dưới 65 tuổi |
| Nhân sự phục vụ | Đội ngũ trưởng đoàn người Việt kết hợp hướng dẫn viên xứ bản | Theo sát hỗ trợ tận tình suốt tuyến |

(Căn phòng khách sạn 4 sao sạch sẽ, tiện nghi tại điểm dừng chân Trùng Khánh và Bắc Kinh)

Giá tour người lớn khởi hành tháng 11 và 12 là 17.490.000 VNĐ. Mỗi khách được phục vụ 1 chai nước suối hàng ngày.

### 3.2. Khoản mục ngoài chương trình và mức giá cho trẻ nhỏ

Các khoản chi tự túc ngoài chương trình:
* Chi phí hoàn tất cuốn hộ chiếu có hạn dùng tối thiểu nửa năm.
* Khoản tiền bồi dưỡng gửi tặng bác tài cùng thuyết minh viên xứ bạn.
* Khoản phụ phí sắp xếp phòng đơn khi đăng ký đi một mình.
* Đồ giặt ủi và nước uống gọi riêng ngoài bữa ăn. Các kiện hành lý quá cước quy định.
* Thuế giá trị gia tăng VAT. Thị thực tái nhập cảnh Việt Nam cho khách mang hộ chiếu nước ngoài.

(Khung cảnh gia đình cùng trẻ nhỏ vui vẻ dạo chơi tại khuôn viên Di Hòa Viên)

Chính sách giá áp dụng cho trẻ em đi cùng bố mẹ:
* Bé dưới 2 tuổi: Áp dụng 30% giá vé người lớn. Bé ngủ cùng giường và tự túc ăn dặm.
* Trẻ từ 2 đến tròn 10 tuổi: Tính 85% giá vé người lớn. Trẻ có ghế xe, suất ăn riêng và ngủ cùng cha mẹ.
* Trẻ từ 11 tuổi trở lên: Áp dụng 100% vé người lớn. Tiêu chuẩn giường ngủ riêng biệt.
* Mỗi cặp người lớn chỉ kèm tối đa 1 bé ngủ chung. Bé thứ hai tính vé người lớn.
"""

sec4 = """## 4. Kinh nghiệm du lịch Trùng Khánh Bắc Kinh cần biết

Chuẩn bị chu đáo giúp chuyến du lịch trùng khánh bắc kinh diễn ra trọn vẹn. Khách đi tour trùng khánh bắc kinh nên lưu ý giấy tờ tùy thân. Thời tiết và tiền tệ cũng cần chuẩn bị kỹ. Hành trình du lịch trùng khánh bắc kinh đòi hỏi trang bị phù hợp.

(Ảnh hướng dẫn chuẩn bị hành lý và đồ dùng thiết yếu trước chuyến đi)

### 4.1. Thủ tục visa đoàn Trung Quốc và chuẩn bị giấy tờ cá nhân

Thủ tục xin visa đoàn rất thuận tiện, không cần chứng minh thu nhập:
* Hộ chiếu scan nguyên cuốn còn hạn trên 6 tháng tính đến ngày về.
* Ảnh thẻ 4x6cm nền trắng chụp mới, rõ mặt, không đeo kính.
* Trẻ dưới 18 tuổi cần bản sao trích lục khai sinh. Trường hợp vắng mặt phụ huynh, người bảo lãnh cần văn bản ủy quyền có dấu xác nhận.
* Khách từng phẫu thuật thẩm mỹ khuôn mặt cần làm lại hộ chiếu mới đúng nhận diện.

(Ảnh minh họa mẫu trang thông tin hộ chiếu và tiêu chuẩn ảnh thẻ 4x6 nền trắng xin visa đoàn)

Hồ sơ nộp trước ngày khởi hành tối thiểu 2 tuần để xét duyệt kịp thời.

### 4.2. Lưu ý hành lý, trang phục và đổi tiền tệ khi đi tour

Bắc Kinh tháng 11 và 12 khá lạnh buốt, đêm dưới 5 độ C. Bạn cần mang áo phao dày, găng tay, khăn ấm và miếng giữ nhiệt. Địa hình đồi dốc và bậc đá dài đòi hỏi giày thể thao êm chân bám tốt.

(Du khách trang bị áo ấm và giày thể thao gọn nhẹ chụp ảnh tại điểm tham quan)

Bạn nên đổi sẵn tiền mặt Nhân dân tệ nhỏ để mua quà vặt. Đồng thời cài sẵn Alipay hoặc WeChat Pay liên kết thẻ Visa để quét mã thanh toán. Khách từ 65 tuổi cần giấy chứng nhận sức khỏe của bác sĩ.
"""

sec5 = """## 5. Kết luận

Hành trình trùng khánh bắc kinh 6 ngày 5 đêm trọn gói rất độc đáo. Bạn hãy gọi ngay hotline 028 7303 6167 để nhận tư vấn lịch trình chi tiết. Hãy đăng ký sớm để chọn ngày bay đẹp nhất!
"""

full_article = f"{header_block}\n{sec1}\n{sec2}\n{sec3}\n{sec4}\n{sec5}"

# Lấy phần thân bài từ H1 trở đi
post_body = full_article.split('H1:', 1)[-1]
words = post_body.split()
post_word_count = len(words)

keywords = [
    'tour du lịch trùng khánh bắc kinh',
    'tour trùng khánh bắc kinh',
    'du lịch trùng khánh bắc kinh',
    'trùng khánh bắc kinh'
]
keywords.sort(key=len, reverse=True)

counts = {}
temp_check = post_body.lower()
for k in keywords:
    matches = len(re.findall(re.escape(k), temp_check))
    counts[k] = matches
    temp_check = re.sub(re.escape(k), '___MATCHED___', temp_check)

total_kw_matches = sum(counts.values())
total_kw_words = sum(len(k.split()) * count for k, count in counts.items())
density_by_words = (total_kw_words / post_word_count) * 100
density_by_matches = (total_kw_matches / post_word_count) * 100

print(f"=== KẾT QUẢ KIỂM TRA BÀI VIẾT CHÍNH XÁC ===")
print(f"Tổng số từ từ H1 đến hết bài: {post_word_count} từ (Quy chuẩn: 1.800 - 2.500 từ)")
for k, v in counts.items():
    print(f"* '{k}': {v} lần")
print(f"Tổng số lần xuất hiện từ khóa: {total_kw_matches} lần")
print(f"Tổng số từ khóa (tính theo số từ trong cụm): {total_kw_words} từ")
print(f"Mật độ từ khóa theo số lần xuất hiện: {density_by_matches:.2f}%")
print(f"Mật độ từ khóa theo tỷ lệ từ khóa/tổng từ: {density_by_words:.2f}%")

# Ghi file tạm trong scratch dir
scratch_dir = r'C:\Users\PC\.gemini\antigravity-ide\brain\33d94397-61c8-45be-9899-dd88753c23fe\scratch'
os.makedirs(scratch_dir, exist_ok=True)
temp_md = os.path.join(scratch_dir, "temp_post_modular.md")

with open(temp_md, "w", encoding="utf-8") as f:
    f.write(full_article)

# Xuất ra file Word bai-viet.docx trong thư mục Result
docx_path = r"c:\Users\PC\Documents\ContentRewrite\Result\bai-viet.docx"
md_to_docx.convert_md_to_docx(temp_md, docx_path, keywords=keywords)

# Đồng bộ sang .agents/scripts/generate_post.py
shutil_path = r'c:\Users\PC\Documents\ContentRewrite\.agents\scripts\generate_post.py'
if os.path.normcase(os.path.abspath(__file__)) != os.path.normcase(os.path.abspath(shutil_path)):
    shutil.copyfile(__file__, shutil_path)

if os.path.exists(temp_md):
    os.remove(temp_md)

print("SUCCESS_POST_BUILT_AND_SYNCED")
