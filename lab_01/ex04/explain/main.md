# Giải thích `main.py`

## Chức năng

- Là file chạy chính của mini project quản lý sinh viên.
- Hiển thị menu CLI và gọi các hàm trong `QuanLySinhVien`.

## Luồng xử lý

1. Import class `QuanLySinhVien`.
2. Tạo object `qlsv = QuanLySinhVien()`.
3. Dùng vòng lặp `while True` để menu chạy liên tục.
4. In menu lựa chọn từ `1` đến `7`, và `0` để thoát.
5. Nhận lựa chọn bằng `input()` rồi ép kiểu `int`.
6. Dùng `if/elif/else` để xử lý từng chức năng.

## Danh sách chức năng trong menu

| Phím | Chức năng | Hàm được gọi |
|---|---|---|
| `1` | Thêm sinh viên | `qlsv.themSinhVien()` |
| `2` | Cập nhật sinh viên theo ID | `qlsv.updateSinhVien(ID)` |
| `3` | Xóa sinh viên theo ID | `qlsv.deleteByID(ID)` |
| `4` | Tìm kiếm sinh viên theo tên | `qlsv.findByName(name)` |
| `5` | Sắp xếp theo điểm trung bình | `qlsv.sortByDiemTB()` |
| `6` | Sắp xếp theo tên | `qlsv.sortByName()` |
| `7` | Hiển thị danh sách | `qlsv.showSinhVien(...)` |
| `0` | Thoát chương trình | `break` |

## Ghi chú

- Trước các thao tác cần dữ liệu, chương trình kiểm tra `qlsv.soLuongSinhVien() == 0` để báo danh sách rỗng.
- File này không tự định nghĩa hàm, chủ yếu điều phối menu và gọi nghiệp vụ từ `QuanLySinhVien`.

## Cách chạy

```bash
cd lab_01/ex04
python main.py
```
