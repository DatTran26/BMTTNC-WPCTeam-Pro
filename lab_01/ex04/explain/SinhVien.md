# Giải thích `SinhVien.py`

## Chức năng

- Định nghĩa class `SinhVien` để lưu thông tin một sinh viên.
- Đây là model dữ liệu được dùng bởi `QuanLySinhVien.py`.

## Class chính

### `SinhVien`

Thuộc tính:

- `_id`: mã sinh viên tự tăng.
- `_name`: họ tên sinh viên.
- `_sex`: giới tính.
- `_major`: chuyên ngành.
- `_diemTB`: điểm trung bình.
- `_hocLuc`: học lực, ban đầu là chuỗi rỗng.

## Hàm chính

### `__init__(self, id, name, sex, major, diemTB)`

- Hàm khởi tạo object sinh viên.
- Nhận dữ liệu từ `QuanLySinhVien.themSinhVien()`.
- Gán từng tham số vào thuộc tính tương ứng của object.

## Cách chạy

File này không chạy độc lập. Chạy thông qua:

```bash
cd lab_01/ex04
python main.py
```
