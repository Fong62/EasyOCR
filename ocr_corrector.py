from google import genai
from config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)


def correct_ocr_text_gemini(ocr_text: str) -> str:
    prompt = f"""
Sửa lỗi OCR tiếng Việt.

- Chỉ sửa lỗi chính tả, dấu, ký tự OCR
- Không thêm, không giải thích

Chuẩn hóa:
- Trường: Trường ĐH Sư Phạm TP.HCM
- Họ tên: sửa lỗi, không rõ → Chưa xác định
- Ngành: Công nghệ thông tin | Sư phạm tin học | Chưa xác định
- Niên khóa: YYYY-YYYY | Chưa xác định
- MSSV: xx.xx.xxx.xxx | Chưa xác định

Output đúng 5 dòng:
Trường ĐH Sư Phạm TP.HCM
Họ tên: ...
Ngành: ...
Niên khóa: ...
MSSV: ...

OCR:
{ocr_text}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview", 
        contents=prompt
    )

    return response.text.strip()