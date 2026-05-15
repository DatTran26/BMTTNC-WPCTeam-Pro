# BMTTNC - WPC Team Pro

> Bộ bài tập Python cơ bản (Lab 01) của **Trần Tấn Đạt - 2380600468**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Learning-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Giới thiệu

Repository này lưu các bài thực hành Python trong **Lab 01**, gồm từ thao tác nhập/xuất cơ bản đến mini project quản lý sinh viên bằng giao diện dòng lệnh.

Mục tiêu:

- Làm quen cú pháp Python căn bản
- Thực hành biến, input, output, điều kiện, vòng lặp
- Sử dụng list, tuple, dictionary
- Viết hàm xử lý dữ liệu đơn giản
- Xây dựng chương trình CLI quản lý sinh viên

## Cấu trúc dự án

```text
BMTTNC-WPCTeam-Pro/
├── lab_01/
│   ├── Text_01.py
│   ├── explain/
│   │   └── Text_01.md
│   ├── ex01/
│   │   ├── Text_01.py
│   │   └── explain/
│   │       └── Text_01.md
│   ├── ex02/
│   │   ├── ex02_01.py ... ex02_10.py
│   │   └── explain/
│   │       ├── ex02_01.md ... ex02_10.md
│   ├── ex03/
│   │   ├── ex03_01.py ... ex03_06.py
│   │   └── explain/
│   │       ├── ex03_01.md ... ex03_06.md
│   └── ex04/
│       ├── main.py
│       ├── QuanLySinhVien.py
│       ├── SinhVien.py
│       └── explain/
│           ├── main.md
│           ├── QuanLySinhVien.md
│           └── SinhVien.md
├── img/
├── LICENSE
└── readme.md
```

## Yêu cầu môi trường

- Python `3.10+` khuyến nghị
- Terminal: PowerShell, CMD, Git Bash hoặc terminal trong VS Code

Kiểm tra Python:

```bash
python --version
```

Nếu máy dùng `python3`, thay `python` bằng `python3` trong các lệnh bên dưới.

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

## Danh sách file, chức năng và giải thích

> Bấm vào tên file để mở mã nguồn. Bấm vào `Giải thích` để xem mô tả chi tiết hàm và luồng xử lý trong từng file.

| File | Chức năng chính | Giải thích | Cách chạy nhanh |
|---|---|---|---|
| [`lab_01/Text_01.py`](lab_01/Text_01.py) | In thông tin cá nhân/nhóm | [`Giải thích`](lab_01/explain/Text_01.md) | `python lab_01/Text_01.py` |
| [`lab_01/ex01/Text_01.py`](lab_01/ex01/Text_01.py) | In thông tin cá nhân/nhóm | [`Giải thích`](lab_01/ex01/explain/Text_01.md) | `python lab_01/ex01/Text_01.py` |
| [`lab_01/ex02/ex02_01.py`](lab_01/ex02/ex02_01.py) | Nhập tên, tuổi và in lời chào | [`Giải thích`](lab_01/ex02/explain/ex02_01.md) | `python lab_01/ex02/ex02_01.py` |
| [`lab_01/ex02/ex02_02.py`](lab_01/ex02/ex02_02.py) | Tính diện tích hình tròn | [`Giải thích`](lab_01/ex02/explain/ex02_02.md) | `python lab_01/ex02/ex02_02.py` |
| [`lab_01/ex02/ex02_03.py`](lab_01/ex02/ex02_03.py) | Kiểm tra số chẵn/lẻ | [`Giải thích`](lab_01/ex02/explain/ex02_03.md) | `python lab_01/ex02/ex02_03.py` |
| [`lab_01/ex02/ex02_04.py`](lab_01/ex02/ex02_04.py) | Lọc số chia hết cho 7 và không chia hết cho 5 | [`Giải thích`](lab_01/ex02/explain/ex02_04.md) | `python lab_01/ex02/ex02_04.py` |
| [`lab_01/ex02/ex02_05.py`](lab_01/ex02/ex02_05.py) | Tính lương tuần, có tăng ca | [`Giải thích`](lab_01/ex02/explain/ex02_05.md) | `python lab_01/ex02/ex02_05.py` |
| [`lab_01/ex02/ex02_06.py`](lab_01/ex02/ex02_06.py) | Tạo ma trận theo X, Y | [`Giải thích`](lab_01/ex02/explain/ex02_06.md) | `python lab_01/ex02/ex02_06.py` |
| [`lab_01/ex02/ex02_07.py`](lab_01/ex02/ex02_07.py) | Nhập nhiều dòng và chuyển sang chữ hoa | [`Giải thích`](lab_01/ex02/explain/ex02_07.md) | `python lab_01/ex02/ex02_07.py` |
| [`lab_01/ex02/ex02_08.py`](lab_01/ex02/ex02_08.py) | Lọc số nhị phân chia hết cho 5 | [`Giải thích`](lab_01/ex02/explain/ex02_08.md) | `python lab_01/ex02/ex02_08.py` |
| [`lab_01/ex02/ex02_09.py`](lab_01/ex02/ex02_09.py) | Kiểm tra số nguyên tố | [`Giải thích`](lab_01/ex02/explain/ex02_09.md) | `python lab_01/ex02/ex02_09.py` |
| [`lab_01/ex02/ex02_10.py`](lab_01/ex02/ex02_10.py) | Đảo ngược chuỗi | [`Giải thích`](lab_01/ex02/explain/ex02_10.md) | `python lab_01/ex02/ex02_10.py` |
| [`lab_01/ex03/ex03_01.py`](lab_01/ex03/ex03_01.py) | Tính tổng các số chẵn trong dãy | [`Giải thích`](lab_01/ex03/explain/ex03_01.md) | `python lab_01/ex03/ex03_01.py` |
| [`lab_01/ex03/ex03_02.py`](lab_01/ex03/ex03_02.py) | Đảo ngược chuỗi bằng hàm | [`Giải thích`](lab_01/ex03/explain/ex03_02.md) | `python lab_01/ex03/ex03_02.py` |
| [`lab_01/ex03/ex03_03.py`](lab_01/ex03/ex03_03.py) | Chuyển list sang tuple | [`Giải thích`](lab_01/ex03/explain/ex03_03.md) | `python lab_01/ex03/ex03_03.py` |
| [`lab_01/ex03/ex03_04.py`](lab_01/ex03/ex03_04.py) | Lấy phần tử đầu/cuối của tuple | [`Giải thích`](lab_01/ex03/explain/ex03_04.md) | `python lab_01/ex03/ex03_04.py` |
| [`lab_01/ex03/ex03_05.py`](lab_01/ex03/ex03_05.py) | Đếm số lần xuất hiện của từng từ | [`Giải thích`](lab_01/ex03/explain/ex03_05.md) | `python lab_01/ex03/ex03_05.py` |
| [`lab_01/ex03/ex03_06.py`](lab_01/ex03/ex03_06.py) | Xóa key khỏi dictionary | [`Giải thích`](lab_01/ex03/explain/ex03_06.md) | `python lab_01/ex03/ex03_06.py` |
| [`lab_01/ex04/main.py`](lab_01/ex04/main.py) | Menu chính quản lý sinh viên | [`Giải thích`](lab_01/ex04/explain/main.md) | `cd lab_01/ex04 && python main.py` |
| [`lab_01/ex04/QuanLySinhVien.py`](lab_01/ex04/QuanLySinhVien.py) | Class xử lý nghiệp vụ sinh viên | [`Giải thích`](lab_01/ex04/explain/QuanLySinhVien.md) | Chạy qua `main.py` |
| [`lab_01/ex04/SinhVien.py`](lab_01/ex04/SinhVien.py) | Class lưu thông tin sinh viên | [`Giải thích`](lab_01/ex04/explain/SinhVien.md) | Chạy qua `main.py` |

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

Dự án phát hành theo giấy phép `MIT`. Xem chi tiết tại [`LICENSE`](LICENSE).
