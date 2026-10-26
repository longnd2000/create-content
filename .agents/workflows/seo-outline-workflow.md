# WORKFLOW: QUY TRÌNH TẠO DÀN BÀI (OUTLINE) CHUẨN SEO CHO CỤM TỪ KHÓA

Quy trình này hướng dẫn chi tiết từng bước mà Agent thực hiện ngay khi nhận được **Cụm từ khóa (Primary Keyword & Keyword Cluster)** từ người dùng, đảm bảo tạo ra một Dàn bài (Outline) bài viết chuẩn SEO 100% theo quy chuẩn dự án.

---

## TỔNG QUAN LUỒNG THỰC THI (5 GIAI ĐOẠN)

```mermaid
flowchart TD
    A[Nhận Cụm Từ Khóa & Xác định Search Intent] --> B[Giai đoạn 1: Tạo Bộ Title & Meta Description]
    B --> C[Giai đoạn 2: Tạo H1 & Khung Sapo]
    C --> D[Giai đoạn 3: Xây dựng Dàn ý Phân cấp H2 - H3 - H4]
    D --> E[Giai đoạn 4: Thiết lập Bản đồ Content Format, Ảnh & Alt Text]
    E --> F[Giai đoạn 5: Xuất Bảng Ma trận Từ khóa & Checklist Thẩm định]
    F --> G[Giai đoạn 6: Xuất bản ra File Word Result/outline.docx]
```

---

## CHI TIẾT CÁC BƯỚC TRIỂN KHAI

### BƯỚC 1: TIẾP NHẬN & PHÂN TÍCH TỪ KHÓA (STRICT KEYWORD INVENTORY)
1. **Phân tích Search Intent**: Người dùng đang tìm kiếm điều gì? (Thông tin / Hướng dẫn cách làm / So sánh / Mua sắm dịch vụ).
2. **Quy định bắt buộc về danh sách từ khóa**:
   - **Chỉ sử dụng đúng số lượng và cụm từ khóa do người dùng cung cấp**.
   - Tuyệt đối **KHÔNG tự ý bịa đặt, suy diễn, mở rộng hay thêm bớt** bất kỳ từ khóa nào khác (nghiêm cấm tự thêm "từ khóa liên quan", "từ khóa LSI tự nghĩ", "từ khóa phụ tự sinh").
   - Xác định rõ vai trò: Key chính (Key có Search Intent bao quát hoặc Volume cao nhất), các Key phụ (các cụm từ khóa còn lại trong danh sách người dùng đưa). Cột "Từ khóa mục tiêu" trong Ma trận phân bổ chỉ chứa các key này, các mục không chèn key thì để dấu `-`.

---

### BƯỚC 2: THIẾT KẾ TIÊU ĐỀ (SEO TITLE) - SỬ DỤNG LÀM TIÊU ĐỀ BÀI VIẾT (H1) & MÔ TẢ (META DESCRIPTION)
* **Đề xuất 3 phương án SEO Title (dùng làm Tiêu đề bài viết / Thẻ H1)**:
  - Chuẩn 55 - 60 ký tự (kiểm soát ngầm bên dưới, không in số ký tự).
  - Từ khóa chính đứng ngay đầu.
  - Chứa con số, từ bổ trợ, dấu `|` hoặc `-`, độc nhất (unique).
  - **Lưu ý thực chiến**: SEO Title này sẽ được đặt làm Tiêu đề to đầu tiên của bài viết (Thẻ H1), đảm bảo đồng bộ hoàn hảo với CMS.
* **Đề xuất 2 phương án Meta Description**:
  - Chuẩn 140 - 155 ký tự (kiểm soát ngầm bên dưới).
  - Từ khóa chính ở đầu, từ khóa phụ ở vế sau.
  - Gợi mở nỗi đau/tò mò, **không trả lời ngay kết quả**.
  - Kết thúc bắt buộc bằng CTA: *Click xem ngay!, Xem thêm!...*

---

### BƯỚC 3: XÁC LẬP TIÊU ĐỀ BÀI VIẾT (H1) & KHUNG MỞ BÀI (SAPO)
* **Heading 1 (H1)**:
  - Lấy chính xác 100% từ SEO Title được chọn ở Bước 2. Không sinh thêm phiên bản H1 khác.
* **Định hướng Sapo**:
  - 2 - 3 dòng (dưới 155 từ).
  - Giải quyết bài toán của tiêu đề bài viết, khơi gợi tò mò.
  - Chứa từ khóa chính ngay trong 100 từ đầu tiên.

---

### BƯỚC 4: XÂY DỰNG CẤU TRÚC PHÂN CẤP HEADINGS (H2, H3, H4)
Tuân thủ nghiêm ngặt các quy tắc:
1. **Quy tắc số lượng**: Tối thiểu từ **4 H2 trở lên**. Mỗi H2 phải có từ **2 H3 trở lên**.
2. **Quy tắc độ dài**: Mỗi heading dưới **60 ký tự**.
3. **Quy tắc từ khóa**:
   - **H2 đầu tiên**: Bắt buộc chứa từ khóa chính.
   - **Các H2 tiếp theo**: Phân bổ từ khóa phụ, từ khóa mở rộng, từ khóa liên quan.
   - Trong mỗi phân đoạn thân bài của 1 H3 chỉ nhắm tối đa 1 key.
4. **Quy tắc phân tầng**: H4 bổ trợ cho H3, H3 bổ trợ cho H2, H2 bổ trợ cho H1.
5. **Quy tắc đoạn áp chót**: H2 hoặc H3 cuối cùng trước Kết luận không được làm sơ sài hoặc quá ngắn.

---

### BƯỚC 5: XÂY DỰNG Ý CHÍNH DƯỚI DẠNG BULLET & QUY HOẠCH TINH GỌN
1. **Phong cách trình bày tối giản (Minimalist & Direct)**:
   - Dưới mỗi Heading (H2, H3) **chỉ liệt kê các ý chính/thông tin cốt lõi dưới dạng bullet points** (`- [Ý chính...]`).
   - **Tuyệt đối KHÔNG giải thích dài dòng** hay chèn nhãn thừa dưới tiêu đề (không viết `Mục tiêu nội dung`, `Định dạng`, `Ý triển khai:`, `Hình ảnh:...`).
   - Tiêu đề để sạch sẽ, súc tích.
2. **Quy hoạch định dạng & Hình ảnh tập trung**:
   - Vị trí chèn Bảng (Table), Danh sách (List), Box Lưu ý cũng như kế hoạch Hình ảnh và Alt text được quy hoạch gọn gàng tại **Bảng Ma Trận Phân Bổ** (Giai đoạn 5), không chèn rải rác làm loãng dàn ý.

---

### BƯỚC 6: XÂY DỰNG KẾT LUẬN & BẢNG ĐIỀU PHỐI TỪ KHÓA
* **Phần Kết luận**: Tóm tắt giải pháp, chứa 1 lần từ khóa chính + CTA hành động.
* **Bảng Ma trận phân bổ từ khóa (Keyword Distribution Matrix)**: Thống kê vị trí rải từ khóa đảm bảo mật độ tổng bài 1.5% - 3.0%, tích hợp kế hoạch Định dạng (Table/List) và Ảnh + Alt text.
* **Bảng Checklist Thẩm định**: Rà soát lại toàn bộ tiêu chí kỹ thuật trước khi bàn giao dàn bài cho người dùng.

---

### BƯỚC 7: XUẤT BẢN RA FILE WORD DOCX VÀO THƯ MỤC RESULT/
* Dữ liệu nguồn tour được trích xuất từ `ContentTour/*` (giữ nguyên vẹn, không chỉnh sửa file nguồn).
* Lưu dàn ý nền tạm vào `outline.md` (tự động xóa sau khi convert).
* Tự động chạy script đóng gói vào thư mục `Result/`:
  ```powershell
  python .agents/scripts/md_to_docx.py outline.md Result/outline.docx
  ```
* Bàn giao file `Result/outline.docx` để người dùng mở trực tiếp bằng Microsoft Word hoặc Google Docs.

---

## TEMPLATE XUẤT BẢN DÀN BÀI CHUẨN (STANDARD OUTPUT FORMAT)

Mỗi khi người dùng cung cấp cụm từ khóa, Agent sẽ trả về kết quả theo đúng cấu trúc tiêu chuẩn dưới đây:

```markdown
# DÀN BÀI CHUẨN SEO: [TÊN TỪ KHÓA CHÍNH]

## I. THÔNG TIN TỔNG QUAN & PHÂN TÍCH TỪ KHÓA
- Danh sách từ khóa người dùng cung cấp:
  1. [Từ khóa chính] (Volume: ...)
  2. [Từ khóa phụ 1] (Volume: ...)
  3. [Từ khóa phụ 2] (Volume: ...)
- Ý định tìm kiếm (Search Intent): [Phân tích chi tiết nhu cầu người đọc]
*(Cam kết: Sử dụng chuẩn xác 100% số lượng cụm từ khóa trên, tuyệt đối không tự bịa đặt hay thêm bớt bất kỳ từ khóa nào khác).*

## II. BỘ TIÊU ĐỀ & MÔ TẢ TỐI ƯU
### 1. Đề xuất SEO Title (Sử dụng làm Tiêu đề bài viết / H1 - Chuẩn 55 - 60 ký tự)
- Option 1 (Khuyên dùng): [Tiêu đề 1]
- Option 2: [Tiêu đề 2]
- Option 3: [Tiêu đề 3]

### 2. Đề xuất Meta Description (Chuẩn SEO 140 - 155 ký tự)
- Option 1 (Khuyên dùng): [Mô tả 1]
- Option 2: [Mô tả 2]

### 3. Khung định hướng Sapo (2-3 dòng, <155 từ, Key trong 100 từ đầu)
- [Đoạn Sapo mẫu gợi ý]

---

## III. DÀN Ý CHI TIẾT (OUTLINE HIERARCHY - COPY & USE READY)

### 1. [Tiêu đề chứa Key chính]
- [Ý chính 1 / thông tin cốt lõi]
- [Ý chính 2 / dữ liệu quan trọng từ file ContentTour/*]
  #### 1.1. [Tiêu đề con]
  - [Ý triển khai 1]
  - [Ý triển khai 2]
  #### 1.2. [Tiêu đề con]
  - [Ý triển khai 1]
  - [Ý triển khai 2]

### 2. [Tiêu đề chứa Key phụ / Phân loại]
- [Ý chính 1]
- [Ý chính 2]
  #### 2.1. [Tiêu đề con]
  - [Ý triển khai 1]
  - [Ý triển khai 2]
  #### 2.2. [Tiêu đề con]
  - [Ý triển khai 1]
  - [Ý triển khai 2]

### 3. [Heading trọng tâm - Chứa Key mở rộng] ⭐ [TRỌNG TÂM]
- [Ý chính 1]
- [Ý chính 2]
  #### 3.1. [Tiêu đề con]
  - [Ý triển khai 1]
  - [Ý triển khai 2]
  #### 3.2. [Tiêu đề con]
  - [Ý triển khai 1]
  - [Ý triển khai 2]

### 4. [Kinh nghiệm / Lời khuyên thực tế]
- [Ý chính 1]
- [Ý chính 2]
  #### 4.1. [Tiêu đề con]
  - [Ý triển khai 1]
  - [Ý triển khai 2]
  #### 4.2. [Tiêu đề con]
  - [Ý triển khai 1]
  - [Ý triển khai 2]

### 5. Kết Luận
- [Tóm lược giải pháp và bài học cốt lõi, lặp lại 1 lần Từ khóa chính]
- [Lời kêu gọi hành động CTA thúc đẩy tương tác]

---

## IV. MA TRẬN PHÂN BỔ TỪ KHÓA & FORMAT TRÌNH BÀY
*(Cột "Từ khóa mục tiêu" CHỈ PHÉP điền các key người dùng đã giao, các mục không chèn key thì để dấu `-`, tuyệt đối không tự bịa thêm key khác).*
| Phần | Thẻ Heading | Từ khóa mục tiêu | Định dạng hiển thị | Kế hoạch Ảnh & Ghi chú mô tả ảnh |
| :--- | :--- | :--- | :--- | :--- |
| Mở bài | Sapo | [Key chính] | Đoạn văn ngắn 2-3 dòng | - |
| Thân 1 | Mục 1 (H2) | [Key chính] | Text + Bullet | Ảnh 1: (Mô tả ảnh ngắn gọn) |
| Thân 1.1 | Mục 1.1 (H3) | - | Text + Bullet | Ảnh 2: (Mô tả ảnh ngắn gọn) |
| Thân 2 | Mục 2 (H2) | [Key phụ 1] | Lịch trình + Timeline | Ảnh 3: (Mô tả ảnh ngắn gọn) |
| Thân 3 | Mục 3 (H2) | [Key phụ 2] | Bảng giá / Table | Ảnh 4: (Mô tả ảnh ngắn gọn) |
| Thân 4 | Mục 4 (H2) | - | Text + Checklist chuẩn bị | Ảnh 5: (Mô tả ảnh ngắn gọn) |
| Kết bài | Mục 5 (H2) | [Key chính] | Text tổng kết + CTA | - |

---

## V. CHECKLIST KIỂM SOÁT DÀN Ý TRƯỚC KHI BÀN GIAO
- [ ] SEO Title đạt 55 - 60 ký tự, Key ở đầu, có số, từ bổ trợ, dấu `|` hoặc `-`, được dùng làm Tiêu đề bài viết (H1) luôn.
- [ ] Description đạt 140 - 155 ký tự, có CTA kích thích click, không tiết lộ đáp án.
- [ ] Sapo 2 - 3 dòng (<155 từ), có Key chính trong 100 từ đầu, giải quyết đúng tiêu đề bài viết.
- [ ] Tối thiểu 4 thẻ H2, mỗi H2 có ít nhất 2 thẻ H3.
- [ ] H2 đầu tiên chứa Key chính.
- [ ] Các thẻ Heading ngắn gọn (<60 ký tự).
- [ ] Đã có kế hoạch dùng Bảng (Table) và Danh sách (List).
- [ ] Đã quy hoạch ảnh (trung bình mỗi 250 từ hoặc mỗi H2/H3 có 1 ảnh).
- [ ] H2/H3 áp chót được xây dựng chi tiết, không bị cụt.
```
