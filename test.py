import requests

url = "http://127.0.0.1:5000/ocr"
files = {"file": open("images\covu4.jpg", "rb")}
response = requests.post(url, files=files)


print(response.json())