# 📝 EasyOCR - Nhận Diện & Trích Xuất MSSV Sinh Viên HCMUE

## 📖 Giới thiệu (Introduction)
Dự án ứng dụng công nghệ **Nhận dạng ký tự quang học (OCR)** kết hợp với thư viện `EasyOCR` và framework `Flask`. Hệ thống được xây dựng để tự động phát hiện, nhận diện và trích xuất chính xác văn bản từ hình ảnh, cụ thể là **Mã số sinh viên (MSSV)** của sinh viên Trường Đại học Sư phạm TP.HCM (HCMUE).

Dự án minh chứng khả năng làm việc với các bài toán **Computer Vision**, xử lý ảnh (Image Processing) và xây dựng RESTful API.

## ✨ Tính năng chính (Key Features)
- 🔍 **Nhận diện MSSV HCMUE:** Trích xuất chính xác định dạng mã số sinh viên từ hình ảnh thẻ sinh viên hoặc tài liệu.
- 🌐 **Web API (Flask):** Cung cấp API endpoint để nhận ảnh đầu vào và trả về kết quả trích xuất, dễ dàng tích hợp với các hệ thống khác.
- 🧠 **Tối ưu hóa dữ liệu:** Sử dụng OpenAI API để hỗ trợ chuẩn hóa và xử lý văn bản sau khi nhận diện.
- ⚡ **Tốc độ xử lý cao:** Tối ưu hóa pipeline xử lý ảnh với OpenCV trước khi đưa vào mô hình OCR (PyTorch) để tăng độ chính xác.

## 🛠️ Công nghệ sử dụng (Tech Stack)
- **Ngôn ngữ:** Python
- **Backend API:** Flask
- **Thư viện AI/ML & OCR:** easyocr, torch (PyTorch), openai
- **Xử lý ảnh:** opencv-python
- **Công cụ khác:** python-dotenv (quản lý biến môi trường)

## 🚀 Hướng dẫn cài đặt (Installation)

**Bước 1:** Clone repository về máy tính của bạn
    git clone https://github.com/Fong62/EasyOCR.git
    cd EasyOCR

**Bước 2:** Cài đặt các thư viện cần thiết (Khuyến nghị dùng virtual environment)
    pip install -r requirements.txt

**Bước 3:** Cấu hình biến môi trường
    Tạo một file .env ở thư mục gốc của dự án và cấu hình các biến cần thiết:
    OPENAI_API_KEY=your_openai_api_key_here

## 💡 Hướng dẫn sử dụng (Usage)
1. Đặt hình ảnh bạn muốn trích xuất văn bản vào thư mục images của dự án.
2. Mở terminal/command prompt và chạy lệnh app.py để khởi chạy EasyOCR:
    python app.py
4. Mở terminal/command prompt và chạy lệnh sau để test ảnh:
    python test.py
3. Kết quả MSSV được trích xuất sẽ hiển thị trực tiếp trên Terminal hoặc trả về JSON qua API.

## 👨‍💻 Tác giả (Author)
- **Nguyễn Hoàng Phong**
- **Sinh viên:** Đại học Sư phạm TP.HCM (HCMUE)
- **Email:** nguyenhoangphongsupham@gmail.com
- **GitHub:** [Fong62](https://github.com/Fong62)
