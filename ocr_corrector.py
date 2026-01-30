from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME
from google import genai

client = genai.Client()
def correct_ocr_text_gemini(ocr_text):
   prompt = f"""
      Bạn là hệ thống sửa lỗi văn bản OCR tiếng Việt.
      Nhiệm vụ:
      + Chỉ sửa lỗi chính tả, lỗi dấu, lỗi OCR.
      + Không thêm nội dung mới, không bỏ thông tin, không giải thích, chỉ xuất ra kết quả cuối cùng.
      + Giữ nguyên số dòng so với văn bản gốc.

      Quy tắc về thông tin sinh viên:
      1. Trường: 
         - Mặc định là "Trường ĐH Sư Phạm TP.HCM"
         - Nếu không xác định được trường trong OCR → thêm vào "Trường ĐH Sư Phạm TP.HCM"
         - Nếu có trường nhưng lỗi OCR → sửa về "Trường ĐH Sư Phạm TP.HCM"

      2. Họ tên:
         + Nếu không có lỗi → giữ nguyên.
         + Nếu lỗi dấu / lỗi OCR → sửa lại
         + Nếu không thể xác định chính xác → suy đoán và tạo họ tên tiếng Việt hợp lý nhất, Tràn thành Trần 
         + Nếu hoàn toàn không xác định được → để "Chưa xác định"

      3. Ngành học: 
         - Chỉ được là "Công nghệ thông tin" hoặc "Sư phạm tin học"
         - Nếu không xác định được từ OCR → để "Chưa xác định"

      4. Niên khóa:
         - Định dạng: YYYY-YYYY (ví dụ: 2023-2027)
         - Nếu không xác định được → để "Chưa xác định"

      5. Mã số sinh viên (MSSV):
         - Luôn được ngăn cách bằng dấu chấm (ví dụ: 48.01.104.106)
         - Giữ nguyên định dạng, chỉ sửa lỗi OCR (như thiếu/chệch dấu chấm)
         - Nếu không xác định được → để "Chưa xác định"

      Yêu cầu đầu ra:
      - Luôn xuất ra đủ 5 dòng theo format cố định:
      Trường ĐH Sư Phạm TP.HCM
      Họ tên: [giá trị]
      Ngành: [giá trị]
      Niên khóa: [giá trị]
      MSSV: [giá trị]

      - Không thêm tiêu đề, không bình luận, không chú thích.
      - Nếu giá trị không xác định được, thay bằng "Chưa xác định"

      {ocr_text}
      """
   response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=prompt)
   return response.text




def correct_ocr_text_openai(ocr_text: str) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
Bạn là hệ thống sửa lỗi văn bản OCR tiếng Việt.
Nhiệm vụ:
+ Chỉ sửa lỗi chính tả, lỗi dấu, lỗi OCR.
+ Không thêm nội dung mới, không bỏ thông tin, không giải thích, chỉ xuất ra kết quả cuối cùng.
+ Giữ nguyên số dòng so với văn bản gốc.

Quy tắc về thông tin sinh viên:
1. Trường: 
   - Mặc định là "Trường ĐH Sư Phạm TP.HCM"
   - Nếu không xác định được trường trong OCR → thêm vào "Trường ĐH Sư Phạm TP.HCM"
   - Nếu có trường nhưng lỗi OCR → sửa về "Trường ĐH Sư Phạm TP.HCM"

2. Họ tên:
   + Nếu không có lỗi → giữ nguyên.
   + Nếu lỗi dấu / lỗi OCR → sửa lại
   + Nếu không thể xác định chính xác → suy đoán và tạo họ tên tiếng Việt hợp lý nhất, Tràn thành Trần 
   + Nếu hoàn toàn không xác định được → để "Chưa xác định"

3. Ngành học: 
   - Chỉ được là "Công nghệ thông tin" hoặc "Sư phạm tin học"
   - Nếu không xác định được từ OCR → để "Chưa xác định"

4. Niên khóa:
   - Định dạng: YYYY-YYYY (ví dụ: 2023-2027)
   - Nếu không xác định được → để "Chưa xác định"

5. Mã số sinh viên (MSSV):
   - Luôn được ngăn cách bằng dấu chấm (ví dụ: 48.01.104.106)
   - Giữ nguyên định dạng, chỉ sửa lỗi OCR (như thiếu/chệch dấu chấm)
   - Nếu không xác định được → để "Chưa xác định"

Yêu cầu đầu ra:
- Luôn xuất ra đủ 5 dòng theo format cố định:
  Trường ĐH Sư Phạm TP.HCM
  Họ tên: [giá trị]
  Ngành: [giá trị]
  Niên khóa: [giá trị]
  MSSV: [giá trị]

- Không thêm tiêu đề, không bình luận, không chú thích.
- Nếu giá trị không xác định được, thay bằng "Chưa xác định"

{ocr_text}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()