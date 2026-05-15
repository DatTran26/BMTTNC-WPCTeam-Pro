# Giải thích `QuanLySinhVien.py`

## Chức năng

- Chứa class `QuanLySinhVien`.
- Quản lý danh sách sinh viên và các nghiệp vụ thêm, sửa, xóa, tìm kiếm, sắp xếp, hiển thị.

## Class chính

### `QuanLySinhVien`

Thuộc tính:

- `listSinhVien`: list lưu các object `SinhVien`.

## Các hàm chính

### `generateID(self)`

- Tạo ID mới cho sinh viên.
- Nếu danh sách rỗng, trả về `1`.
- Nếu đã có sinh viên, tìm ID lớn nhất rồi cộng thêm `1`.

### `soLuongSinhVien(self)`

- Trả về số lượng sinh viên hiện có.
- Dùng `self.listSinhVien.__len__()`.

### `themSinhVien(self)`

- Nhập tên, giới tính, chuyên ngành, điểm trung bình.
- Tạo object `SinhVien` mới.
- Gọi `xepLoaiHocLuc()` để gán học lực.
- Thêm sinh viên vào `listSinhVien`.

### `updateSinhVien(self, ID)`

- Tìm sinh viên theo ID bằng `findByID()`.
- Nếu tìm thấy, nhập lại thông tin mới và cập nhật object.
- Sau khi cập nhật điểm, gọi lại `xepLoaiHocLuc()`.
- Nếu không tìm thấy, in thông báo lỗi.

### `xepLoaiHocLuc(self, sv)`

- Xếp loại học lực dựa trên `_diemTB`.
- Từ `9`: Xuất sắc.
- Từ `8`: Giỏi.
- Từ `7`: Khá.
- Từ `5`: Trung bình.
- Dưới `5`: Yếu.

### `sortByID(self)`

- Sắp xếp danh sách sinh viên theo `_id` tăng dần.

### `sortByName(self)`

- Sắp xếp danh sách sinh viên theo `_name` tăng dần.

### `sortByDiemTB(self)`

- Sắp xếp danh sách sinh viên theo `_diemTB` giảm dần.

### `findByID(self, ID)`

- Duyệt danh sách sinh viên.
- Nếu sinh viên có `_id` trùng ID cần tìm thì trả về sinh viên đó.
- Nếu không tìm thấy thì trả về `None`.

### `findByName(self, keyword)`

- Tìm sinh viên có tên chứa từ khóa.
- Trả về list sinh viên phù hợp.

### `deleteByID(self, ID)`

- Tìm sinh viên theo ID.
- Nếu tìm thấy thì xóa khỏi list bằng `remove()`.
- Trả về `True` nếu xóa thành công, `False` nếu không tìm thấy.

### `showSinhVien(self, listSV)`

- In bảng danh sách sinh viên.
- Hiển thị các cột: `ID`, `Name`, `Sex`, `Major`, `DiemTB`, `HocLuc`.
- Dùng `format()` để căn chỉnh cột.

### `getListSinhVien(self)`

- Trả về toàn bộ danh sách sinh viên hiện tại.
- Được `main.py` dùng khi cần hiển thị hoặc sắp xếp.

## Cách chạy

File này không chạy độc lập. Chạy thông qua:

```bash
cd lab_01/ex04
python main.py
```
