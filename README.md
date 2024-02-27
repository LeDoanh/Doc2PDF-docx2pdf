Source test dùng lib docx2pdf để convert word qua pdf.
Note: 
  - Cần máy chạy cài microsoft word nên không chạy được trên linux.
  - Nếu dùng spire.doc thì chỉ convert được file cơ bản không hình và có watermask của lib

** Hướng dẫn sử dụng:

1. Tạo evn riêng cho source:
    - Tạo evn ảo (Lần đầu chạy source): 
        python -m venv doc2pdf

    - Activate evn (Mỗi lần mở source): 
        doc2pdf\Scripts\activate

    - Install package từ file requirements (Lần đầu chạy source)
        pip install -r requirements.txt

2. Chạy source:
    - Lấy đường đẫn file cần convert:
        PathIn = FileIn.doc / FileIn.docx

    - Chọn đường đẫn file lưu
        PathOut = FileOut.pdf

    - Chạy lệnh terminal hoặc cmd (Đổi PathIn, PathOut )
        python doc2pdf.py "PathIn" "PathOut"
