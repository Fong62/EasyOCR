import cv2 as cv
import numpy as np
import easyocr
import imutils
import sys
import os

def extract_text(image_path):
    """Hàm chính để trích xuất văn bản từ ảnh, trả về string"""
    # Kiểm tra và đọc ảnh
    if not os.path.exists(image_path):
        return f"Lỗi: File '{image_path}' không tồn tại!"
    
    img = cv.imread(image_path)
    if img is None:
        return f"Lỗi: Không thể đọc file '{image_path}'!"
    
    # Chuyển sang RGB và resize
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_rgb = imutils.resize(img_rgb, width=800)
    
    # Tiền xử lý (phương pháp 3)
    gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    denoised = cv.medianBlur(enhanced, 3)
    blurred = cv.GaussianBlur(denoised, (5, 5), 0)
    _, thresh3 = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    
    kernel = np.ones((2, 2), np.uint8)
    opening3 = cv.morphologyEx(thresh3, cv.MORPH_OPEN, kernel)
    closing3 = cv.morphologyEx(opening3, cv.MORPH_CLOSE, kernel)
    
    dilation_kernel = np.ones((1, 1), np.uint8)
    final = cv.dilate(closing3, dilation_kernel, iterations=1)
    
    # Nhận diện văn bản (phương pháp 3)
    reader = easyocr.Reader(['vi'], gpu=True)
    results = reader.readtext(img_rgb, detail=1)
    
    # Xử lý và trả về kết quả dưới dạng string
    if results:
        results.sort(key=lambda x: x[0][0][1])
        lines = []
        current_line = []
        current_y = None
        
        for bbox, text, _ in results:
            y = bbox[0][1]
            if current_y is None:
                current_y = y
                current_line.append(text)
            elif abs(y - current_y) < 20:
                current_line.append(text)
            else:
                # Sắp xếp các từ trong dòng theo tọa độ x
                current_line_sorted = []
                for t in current_line:
                    # Tìm bounding box của từ tương ứng
                    for b, txt, _ in results:
                        if txt == t:
                            current_line_sorted.append((b[0][0], txt))
                            break
                current_line_sorted.sort(key=lambda x: x[0])
                line_text = " ".join([t[1] for t in current_line_sorted])
                lines.append(line_text)
                current_line = [text]
                current_y = y
        
        # Xử lý dòng cuối cùng
        if current_line:
            current_line_sorted = []
            for t in current_line:
                for b, txt, _ in results:
                    if txt == t:
                        current_line_sorted.append((b[0][0], txt))
                        break
            current_line_sorted.sort(key=lambda x: x[0])
            line_text = " ".join([t[1] for t in current_line_sorted])
            lines.append(line_text)
        
        # Trả về tất cả các dòng dưới dạng một string
        return "\n".join(lines)
    else:
        return "Không nhận diện được văn bản!"

def process_image(image_path):
    return extract_text(image_path)

# if __name__=="__main__":
#     imgpath= "D:\MY WORK\SPNC\EasyOCR\images\z7369545640623_e8fea150b3d5a28a8d34b2edb6121833.jpg"
#     reader = easyocr.Reader(['vi'], gpu=False)
#     print("Ocr bth:")
#     print(reader.readtext(imgpath,detail=0))
#     print("Ocr có xử lý:")
#     print(process_image(imgpath))
