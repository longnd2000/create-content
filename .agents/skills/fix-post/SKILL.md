---
name: fix-post
description: Fix và tối ưu bài viết có sẵn trong ContentTour/* chuẩn SEO 100%, bảo toàn format và nội dung đã duyệt, tối ưu mật độ key, phân bổ đều, xuất ra Result/.
---

# KỸ NĂNG: TỐI ƯU & FIX NỘI DUNG BÀI VIẾT CÓ SẴN (/fix-post)

## MỤC TIÊU & PHẠM VI HOẠT ĐỘNG
* Khi người dùng nhập lệnh `/fix-post [tên file hoặc đường dẫn trong ContentTour/*]`:
  * **NGUỒN DỮ LIỆU ĐẦU VÀO**: Lấy trực tiếp bài viết do người dùng đã chuẩn bị sẵn trong thư mục `ContentTour/*` (file `.docx`, `.txt`...).
  * **MỤC TIÊU CỐT LÕI**: Nội dung trong file đã được kiểm duyệt về thông tin thực tế, lịch trình, giá cả. Tác vụ của Agent là **chỉnh sửa, tối ưu (fix) bài viết để đạt chuẩn SEO tuyệt đối** mà **KHÔNG LÀM MỚI LẠI TOÀN BỘ BÀI** và **KHÔNG XÁO TRỘN CÁC FORMAT ĐÃ CÓ**.
  * **KẾT QUẢ ĐẦU RA (DUY NHẤT 1 FILE)**: Xuất bản trực tiếp ra **DUY NHẤT 1 file Word `.docx`** trong thư mục `Result/` theo định dạng `Result/[slug]-fixed.docx` (ví dụ: `Result/tour-trung-khanh-thanh-do-fixed.docx`). Tuyệt đối KHÔNG xuất ra 2 file, không tạo thêm bản sao `bai-viet.docx` hay file phụ nào khác.

---

## CÁC NGUYÊN TẮC FIX NỘI DUNG (CORE FIXING DIRECTIVES)

### 1. Giữ Nguyên Nội Dung & Cấu Trúc Đã Được Kiểm Duyệt
* Giữ nguyên vẹn các ý chính, dữ liệu thực tế, lịch trình chi tiết, mốc thời gian, giá tour và cấu trúc các đề mục (Headings) mà người dùng đã sắp xếp.
* Giữ nguyên các định dạng trực quan đã có: Bảng biểu (Table), Danh sách gạch đầu dòng (List), Box lưu ý, Timeline.
* Không tự ý xóa bỏ các phần quan trọng, không đảo lộn trật tự các đề mục khiến bài viết mất mạch logic ban đầu.

### 2. Tinh Chỉnh Bộ Nhận Diện SEO Đầu Bài (Master Header Block)
* Nếu bài viết chưa có hoặc chưa chuẩn khối đầu bài, bổ sung/hiệu chỉnh theo chuẩn:
  1. **Bảng Thống kê Từ khóa (KEY & VOLUME)**: Tiêu đề in đậm căn giữa, hàng tiêu đề màu vàng tươi (`#FFFF00`).
  2. Dòng `Check spin:`
  3. Dòng `Check AI:`
  4. Dòng `Key chính: [Từ khóa chính]`
  5. Dòng `Meta: [Đoạn Meta Description 140 - 155 ký tự có CTA]`
  6. Dòng `Title: [SEO Title 55 - 60 ký tự, tối ưu Key 1 ở đầu]`
  7. Dòng `H1: [Thẻ H1 55 - 60 ký tự, tối ưu Key 2 - KHÁC 100% so với SEO Title]`
* **Đoạn Mở bài (Sapo)**: Rà soát và gọt giũa ngắn gọn **2 - 3 dòng (<155 từ)**, thu hút, **bắt buộc chứa từ khóa chính trong 100 từ đầu tiên**.

### 3. Tối Ưu Mật Độ & Tần Suất Xuất Hiện Từ Khóa (Keyword Optimization)
* **Chỉ sử dụng đúng danh sách từ khóa người dùng cung cấp**: Không tự bịa thêm từ khóa LSI hay từ khóa phụ ngoài danh sách.
* **Mật độ chuẩn SEO**: Điều chỉnh tổng mật độ cụm từ khóa nằm chuẩn trong khoảng **1.5% - 2.5%** (tối đa 3.0%).
* **Phân bổ trải đều khắp bài và trong từng mục (H2, H3)**:
  - **Mật độ không quá dày & không xuất hiện quá gần nhau**: Tuyệt đối không để 2 từ khóa xuất hiện trong cùng 1 câu hoặc 2 câu liền kề; không dồn cục từ khóa gây cảm giác spam/ngột ngạt.
  - **Không để khoảng cách quá xa mới xuất hiện key 1 lần**: Rà soát các khoảng trống văn bản (200 - 300 từ) đang vắng bóng từ khóa để chèn bổ sung khéo léo 1 lần từ khóa thích hợp (key chính hoặc key phụ của mục đó).
* **Câu chữ linh hoạt, uyển chuyển để luôn tự nhiên nhất**:
  - Dùng cấu trúc câu đa dạng, hòa tan từ khóa vào ngữ cảnh kể chuyện/chia sẻ kinh nghiệm thực tế.
  - Tuyệt đối không nhồi nhét thô cứng làm sượng câu văn hoặc sai ngữ pháp tiếng Việt.

### 4. Tinh Chỉnh Phần Kết Luận (Concise Conclusion)
* Rà soát phần Kết luận:
  - Viết **thật ngắn gọn, cô đọng (2 - 3 câu ngắn, dưới 50 - 80 từ)**.
  - Cắt bỏ các đoạn lan man, triết lý sáo rỗng.
  - **Bắt buộc chứa 1 lần từ khóa chính**.
  - **Có lời kêu gọi hành động (Call To Action - CTA)** rõ ràng, dứt khoát.
  - Tuyệt đối không chèn ảnh hay ghi chú note ảnh ở Kết luận.

### 5. Chuẩn Hóa Ghi Chú Mô Tả Ảnh (Simple Image Notes)
* Rà soát các vị trí chèn ảnh: nếu ghi chú ảnh quá dài hoặc chứa thông số kỹ thuật rườm rà (pixel, alt text, dung lượng...), gọt giũa lại thành dạng ngắn gọn, dễ hiểu đặt trong ngoặc đơn `(...)` với màu đỏ `#C00000`.

---

## QUY TRÌNH THỰC THI LỆNH /fix-post

1. **Bước 1: Đọc & Phân Tích Bài Viết Nguồn**:
   - Dùng script chuyên dụng đọc file từ thư mục `ContentTour/*`:
     ```powershell
     python .agents/scripts/read_tour_file.py ContentTour/[ten-file]
     ```
   - Tiếp nhận danh sách từ khóa mục tiêu do người dùng chỉ định kèm theo lệnh.

2. **Bước 2: Quét & Đánh Giá Các Chỉ Số SEO Hiện Tại**:
   - Đếm tần suất xuất hiện và mật độ của từng từ khóa trong bài.
   - Kiểm tra các đoạn bị dồn cục key hoặc bị trống key quá dài (>250 từ).
   - Kiểm tra Title, H1 (đảm bảo khác nhau và tối ưu 2 key), Sapo (độ dài, vị trí key) và Kết luận.

3. **Bước 3: Tinh Chỉnh Cục Bộ (In-place Optimization)**:
   - Giữ nguyên cấu trúc, câu chữ hay và dữ liệu gốc.
   - Thêm/bớt/thay thế từ ngữ để đưa từ khóa vào các vị trí còn thiếu hoặc giãn khoảng cách giữa các từ khóa đang bị quá dày.
   - Chuẩn hóa văn phong mượt mà, gãy gọn, tự nhiên.

4. **Bước 4: Đóng Gói Xuất Ra DUY NHẤT 1 File Trong Result/**:
   - Xuất bản trực tiếp ra **DUY NHẤT 1 file Word `.docx`** trong `Result/`:
     ```powershell
     python .agents/scripts/md_to_docx.py [file-tam.md] Result/[ten-file-fixed].docx
     ```
   - Tuyệt đối không xuất thêm file thứ 2 như `bai-viet.docx`. Chỉ lưu đúng 1 file kết quả duy nhất.
   - Dọn dẹp sạch sẽ mọi file trung gian `.md`.
   - File gốc trong `ContentTour/*` được bảo toàn nguyên vẹn 100%.

5. **Bước 5: Bàn Giao & Báo Cáo Thay Đổi**:
   - Trả về đường dẫn file Word đã fix trong `Result/` cho người dùng.
   - Báo cáo tóm tắt các điểm đã tối ưu: số lần xuất hiện của từng key, mật độ trước/sau khi fix, độ dài Sapo và Kết luận.
