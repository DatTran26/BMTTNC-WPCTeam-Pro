<p align="center">
  <img src="img/LOGO%201.png" alt="WPC Team" width="760">
</p>

> Bộ bài tập Python cơ bản và mã hóa cổ điển (Lab 01-03) của **Trần Tấn Đạt - 2380600468**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Learning-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Giới thiệu

Repository này lưu các bài thực hành Python trong **Lab 01**, **Lab 02** và **Lab 03**, gồm bài tập Python căn bản, thuật toán mã hóa cổ điển, API Flask và giao diện PyQt5.

Mục tiêu:

- Làm quen cú pháp Python căn bản
- Thực hành biến, input, output, điều kiện, vòng lặp
- Sử dụng list, tuple, dictionary
- Viết hàm xử lý dữ liệu đơn giản
- Xây dựng chương trình CLI quản lý sinh viên
- Triển khai các thuật toán mã hóa cổ điển
- Xây dựng API Flask, giao diện web và ứng dụng PyQt5 gọi API

## Cấu trúc dự án

```text
BMTTNC-WPCTeam-Pro/
|-- lab_01/
|   |-- Text_01.py
|   |-- explain/
|   |   `-- Text_01.md
|   |-- ex01/
|   |   |-- Text_01.py
|   |   `-- explain/
|   |       `-- Text_01.md
|   |-- ex02/
|   |   |-- ex02_01.py ... ex02_10.py
|   |   `-- explain/
|   |       `-- ex02_01.md ... ex02_10.md
|   |-- ex03/
|   |   |-- ex03_01.py ... ex03_06.py
|   |   `-- explain/
|   |       `-- ex03_01.md ... ex03_06.md
|   `-- ex04/
|       |-- main.py
|       |-- QuanLySinhVien.py
|       |-- SinhVien.py
|       `-- explain/
|           |-- main.md
|           |-- QuanLySinhVien.md
|           `-- SinhVien.md
|-- lab_02/
|   |-- ex01/
|   |   |-- Caesar.py
|   |   `-- Vigenere.py
|   `-- ex01_API/
|       |-- api.py
|       |-- cipher/
|       |   |-- caesar/
|       |   |   |-- alphabet.py
|       |   |   `-- caesar_cipher.py
|       |   |-- playfair/
|       |   |   `-- playfair_cipher.py
|       |   |-- railfence/
|       |   |   `-- railfence_cipher.py
|       |   |-- transposition/
|       |   |   `-- transposition_cipher.py
|       |   `-- vigenere/
|       |       `-- vigener_cipher.py
|       |-- postman/
|       |   |-- api-cipher.postman_collection.json
|       |   `-- postman-usage-guide.md
|       |-- static/
|       |   |-- app.js
|       |   `-- styles.css
|       |-- templates/
|       |   `-- index.html
|       `-- ui/
|-- lab_03/
|   |-- api.py
|   |-- caesar_cipher.py
|   |-- ecc_cipher.py
|   |-- cipher/
|   |   |-- ecc/
|   |   |   |-- __init__.py
|   |   |   `-- ecc_cipher.py
|   |   `-- rsa/
|   |       |-- __init__.py
|   |       |-- requirements.txt
|   |       `-- rsa_cipher.py
|   |-- postman/
|   |   |-- api-cipher-merged-with-rsa.postman_collection.json
|   |   |-- api-cipher-with-rsa.postman_collection.json
|   |   `-- postman-usage-guide.md
|   |-- ui/
|   |   |-- caesar.py
|   |   |-- caesar.ui
|   |   |-- ecc.py
|   |   |-- ecc.ui
|   |   |-- rsa.py
|   |   `-- rsa.ui
|   `-- platform/
|       |-- qminimal.dll
|       |-- qoffscreen.dll
|       |-- qwebgl.dll
|       `-- qwindows.dll
|-- img/
|-- .gitignore
|-- AGENTS.md
|-- LICENSE
|-- requirements.txt
`-- readme.md
```

## Yêu cầu môi trường

- Python `3.10+` khuyến nghị
- Flask, Requests, PyQt5 trong `requirements.txt`
- Terminal: PowerShell, CMD, Git Bash hoặc terminal trong VS Code

Kiểm tra Python:

```bash
python --version
```

Nếu máy dùng `python3`, thay `python` bằng `python3` trong các lệnh bên dưới.

### Cài thư viện

```bash
python -m pip install -r requirements.txt
```

## Cách chạy

### Chạy file Python bất kỳ

Từ thư mục gốc dự án:

```bash
python <duong-dan-file>
```

Ví dụ:

```bash
python lab_01/ex02/ex02_01.py
python lab_01/ex03/ex03_05.py
```

### Chạy mini project quản lý sinh viên

Vì `main.py` import trực tiếp `QuanLySinhVien`, nên nên chạy trong thư mục `ex04`:

```bash
cd lab_01/ex04
python main.py
```

Quay lại thư mục gốc:

```bash
cd ../..
```

### Chạy Flask UI Lab 02

```bash
cd lab_02/ex01_API
python api.py
```

Mở trình duyệt tại:

```text
http://127.0.0.1:5000
```

API root:

```text
http://127.0.0.1:5000/api
```

UI có tab cho `Caesar`, `Vigenere`, `Playfair`, `Rail Fence`, `Transposition`.

Postman collection và hướng dẫn test API:

```text
lab_02/ex01_API/postman/api-cipher.postman_collection.json
lab_02/ex01_API/postman/postman-usage-guide.md
```

### Chạy Flask API Lab 03 RSA/ECC

```bash
python lab_03/api.py
```

API RSA chạy tại:

```text
http://127.0.0.1:5000/api/rsa/generate_keys
http://127.0.0.1:5000/api/rsa/encrypt
http://127.0.0.1:5000/api/rsa/decrypt
http://127.0.0.1:5000/api/rsa/sign
http://127.0.0.1:5000/api/rsa/verify
```

API ECC chạy tại:

```text
http://127.0.0.1:5000/api/ecc/generate_keys
http://127.0.0.1:5000/api/ecc/sign
http://127.0.0.1:5000/api/ecc/verify
```

Postman collection và hướng dẫn test RSA/ECC:

```text
lab_03/postman/api-cipher-with-rsa.postman_collection.json
lab_03/postman/api-cipher-merged-with-rsa.postman_collection.json
lab_03/postman/postman-usage-guide.md
```

### Chạy PyQt5 UI Lab 03

Mở terminal tại thư mục gốc dự án. Trước khi chạy UI Caesar, cần chạy Flask API của Lab 02 ở một terminal khác.

```bash
python lab_03/caesar_cipher.py
```

Ứng dụng Lab 03 gọi API Caesar tại:

```text
http://127.0.0.1:5000/api/caesar/encrypt
http://127.0.0.1:5000/api/caesar/decrypt
```

Chạy UI ECC sau khi chạy Flask API Lab 03:

```bash
python lab_03/ecc_cipher.py
```

## Danh sách file, chức năng và giải thích

> Bấm vào tên file để mở mã nguồn. Bấm vào `Giải thích` để xem mô tả chi tiết hàm và luồng xử lý trong từng file.

| File | Chức năng chính | Giải thích | Cách chạy nhanh |
|---|---|---|---|
| <a href="lab_02/ex01_API/api.py" target="_blank" rel="noopener noreferrer"><code>lab_02/ex01_API/api.py</code></a> | Flask API và web UI cho các thuật toán mã hóa | Postman: <a href="lab_02/ex01_API/postman/postman-usage-guide.md" target="_blank" rel="noopener noreferrer"><code>Hướng dẫn</code></a> | `cd lab_02/ex01_API && python api.py` |
| <a href="lab_02/ex01_API/static/app.js" target="_blank" rel="noopener noreferrer"><code>lab_02/ex01_API/static/app.js</code></a> | Xử lý tab thuật toán, gọi API encrypt/decrypt | - | Chạy qua Flask UI |
| <a href="lab_02/ex01_API/templates/index.html" target="_blank" rel="noopener noreferrer"><code>lab_02/ex01_API/templates/index.html</code></a> | Giao diện web Cipher Workbench | - | Chạy qua Flask UI |
| <a href="lab_03/caesar_cipher.py" target="_blank" rel="noopener noreferrer"><code>lab_03/caesar_cipher.py</code></a> | Ứng dụng PyQt5 Caesar gọi API Flask | - | `python lab_03/caesar_cipher.py` |
| <a href="lab_03/ui/caesar.py" target="_blank" rel="noopener noreferrer"><code>lab_03/ui/caesar.py</code></a> | Mã giao diện PyQt5 sinh từ file `.ui` | - | Chạy qua `caesar_cipher.py` |
| <a href="lab_01/Text_01.py" target="_blank" rel="noopener noreferrer"><code>lab_01/Text_01.py</code></a> | In thông tin cá nhân/nhóm | <a href="lab_01/explain/Text_01.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/Text_01.py` |
| <a href="lab_01/ex01/Text_01.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex01/Text_01.py</code></a> | In thông tin cá nhân/nhóm | <a href="lab_01/ex01/explain/Text_01.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex01/Text_01.py` |
| <a href="lab_01/ex02/ex02_01.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex02/ex02_01.py</code></a> | Nhập tên, tuổi và in lời chào | <a href="lab_01/ex02/explain/ex02_01.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex02/ex02_01.py` |
| <a href="lab_01/ex02/ex02_02.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex02/ex02_02.py</code></a> | Tính diện tích hình tròn | <a href="lab_01/ex02/explain/ex02_02.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex02/ex02_02.py` |
| <a href="lab_01/ex02/ex02_03.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex02/ex02_03.py</code></a> | Kiểm tra số chẵn/lẻ | <a href="lab_01/ex02/explain/ex02_03.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex02/ex02_03.py` |
| <a href="lab_01/ex02/ex02_04.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex02/ex02_04.py</code></a> | Lọc số chia hết cho 7 và không chia hết cho 5 | <a href="lab_01/ex02/explain/ex02_04.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex02/ex02_04.py` |
| <a href="lab_01/ex02/ex02_05.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex02/ex02_05.py</code></a> | Tính lương tuần, có tăng ca | <a href="lab_01/ex02/explain/ex02_05.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex02/ex02_05.py` |
| <a href="lab_01/ex02/ex02_06.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex02/ex02_06.py</code></a> | Tạo ma trận theo X, Y | <a href="lab_01/ex02/explain/ex02_06.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex02/ex02_06.py` |
| <a href="lab_01/ex02/ex02_07.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex02/ex02_07.py</code></a> | Nhập nhiều dòng và chuyển sang chữ hoa | <a href="lab_01/ex02/explain/ex02_07.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex02/ex02_07.py` |
| <a href="lab_01/ex02/ex02_08.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex02/ex02_08.py</code></a> | Lọc số nhị phân chia hết cho 5 | <a href="lab_01/ex02/explain/ex02_08.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex02/ex02_08.py` |
| <a href="lab_01/ex02/ex02_09.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex02/ex02_09.py</code></a> | Kiểm tra số nguyên tố | <a href="lab_01/ex02/explain/ex02_09.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex02/ex02_09.py` |
| <a href="lab_01/ex02/ex02_10.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex02/ex02_10.py</code></a> | Đảo ngược chuỗi | <a href="lab_01/ex02/explain/ex02_10.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex02/ex02_10.py` |
| <a href="lab_01/ex03/ex03_01.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex03/ex03_01.py</code></a> | Tính tổng các số chẵn trong dãy | <a href="lab_01/ex03/explain/ex03_01.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex03/ex03_01.py` |
| <a href="lab_01/ex03/ex03_02.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex03/ex03_02.py</code></a> | Đảo ngược chuỗi bằng hàm | <a href="lab_01/ex03/explain/ex03_02.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex03/ex03_02.py` |
| <a href="lab_01/ex03/ex03_03.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex03/ex03_03.py</code></a> | Chuyển list sang tuple | <a href="lab_01/ex03/explain/ex03_03.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex03/ex03_03.py` |
| <a href="lab_01/ex03/ex03_04.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex03/ex03_04.py</code></a> | Lấy phần tử đầu/cuối của tuple | <a href="lab_01/ex03/explain/ex03_04.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex03/ex03_04.py` |
| <a href="lab_01/ex03/ex03_05.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex03/ex03_05.py</code></a> | Đếm số lần xuất hiện của từng từ | <a href="lab_01/ex03/explain/ex03_05.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex03/ex03_05.py` |
| <a href="lab_01/ex03/ex03_06.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex03/ex03_06.py</code></a> | Xóa key khỏi dictionary | <a href="lab_01/ex03/explain/ex03_06.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `python lab_01/ex03/ex03_06.py` |
| <a href="lab_01/ex04/main.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex04/main.py</code></a> | Menu chính quản lý sinh viên | <a href="lab_01/ex04/explain/main.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | `cd lab_01/ex04 && python main.py` |
| <a href="lab_01/ex04/QuanLySinhVien.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex04/QuanLySinhVien.py</code></a> | Class xử lý nghiệp vụ sinh viên | <a href="lab_01/ex04/explain/QuanLySinhVien.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | Chạy qua `main.py` |
| <a href="lab_01/ex04/SinhVien.py" target="_blank" rel="noopener noreferrer"><code>lab_01/ex04/SinhVien.py</code></a> | Class lưu thông tin sinh viên | <a href="lab_01/ex04/explain/SinhVien.md" target="_blank" rel="noopener noreferrer"><code>Giải thích</code></a> | Chạy qua `main.py` |

## Luồng hoạt động mini project `ex04`

```text
main.py
  |
  |-- tạo object QuanLySinhVien
  |-- hiển thị menu
  |-- nhận lựa chọn người dùng
  |
  +--> QuanLySinhVien.py
          |
          |-- thêm/sửa/xóa/tìm/sắp xếp/hiển thị
          |
          +--> SinhVien.py
                  |
                  +-- lưu thông tin từng sinh viên
```

## Gợi ý cải tiến tiếp theo

- Sửa tìm kiếm tên trong `findByName()` để không phân biệt hoa/thường ở cả keyword và tên sinh viên.
- Lưu danh sách sinh viên ra file `JSON` hoặc `CSV`.
- Thêm kiểm tra điểm trung bình nằm trong khoảng `0` đến `10`.
- Tách phần nhập/xuất khỏi class xử lý nghiệp vụ để dễ viết unit test.
- Bổ sung test cho các hàm trong `QuanLySinhVien`.

## Thông tin tác giả

- **Họ tên:** Trần Tấn Đạt
- **MSSV:** 2380600468
- **Nhóm:** WPCTeam

## License

Dự án phát hành theo giấy phép `MIT`. Xem chi tiết tại <a href="LICENSE" target="_blank" rel="noopener noreferrer"><code>LICENSE</code></a>.

