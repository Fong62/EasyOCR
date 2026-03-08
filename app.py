from flask import Flask, request, jsonify
import easyocr
import os
from ocr_corrector import correct_ocr_text_gemini, correct_ocr_text_openai
from ocr_reader import process_image
app = Flask(__name__)

UPLOAD_DIR = "./temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/ocr", methods=["POST"])
def ocr():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(UPLOAD_DIR, file.filename)
    file.save(filepath)

    try:
        results = process_image(filepath)
        corrected_text = correct_ocr_text_gemini(results), 
       
        print("Raw test")
        print(results)
        print("Đã qua chỉnh sửa")
        print(corrected_text)
        
        return jsonify({
            # "ocr_text": results,
            "corrected_text": corrected_text
        })
       

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
