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
│   ├── ex01/
│   │   └── Text_01.py
│   ├── ex02/
│   │   ├── ex02_01.py
│   │   ├── ex02_02.py
│   │   ├── ex02_03.py
│   │   ├── ex02_04.py
│   │   ├── ex02_05.py
│   │   ├── ex02_06.py
│   │   ├── ex02_07.py
│   │   ├── ex02_08.py
│   │   ├── ex02_09.py
│   │   └── ex02_10.py
│   ├── ex03/
│   │   ├── ex03_01.py
│   │   ├── ex03_02.py
│   │   ├── ex03_03.py
│   │   ├── ex03_04.py
│   │   ├── ex03_05.py
│   │   └── ex03_06.py
│   └── ex04/
│       ├── main.py
│       ├── QuanLySinhVien.py
│       └── SinhVien.py
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

## Danh sách file và chức năng

> Có thể bấm vào tên file để mở trực tiếp mã nguồn trong GitHub/VS Code.

| File | Chức năng chính | Cách chạy nhanh |
|---|---|---|
| [`lab_01/Text_01.py`](lab_01/Text_01.py) | In thông tin cá nhân/nhóm | `python lab_01/Text_01.py` |
| [`lab_01/ex01/Text_01.py`](lab_01/ex01/Text_01.py) | In thông tin cá nhân/nhóm | `python lab_01/ex01/Text_01.py` |
| [`lab_01/ex02/ex02_01.py`](lab_01/ex02/ex02_01.py) | Nhập tên, tuổi và in lời chào | `python lab_01/ex02/ex02_01.py` |
| [`lab_01/ex02/ex02_02.py`](lab_01/ex02/ex02_02.py) | Tính diện tích hình tròn | `python lab_01/ex02/ex02_02.py` |
| [`lab_01/ex02/ex02_03.py`](lab_01/ex02/ex02_03.py) | Kiểm tra số chẵn/lẻ | `python lab_01/ex02/ex02_03.py` |
| [`lab_01/ex02/ex02_04.py`](lab_01/ex02/ex02_04.py) | Lọc số chia hết cho 7 và không chia hết cho 5 | `python lab_01/ex02/ex02_04.py` |
| [`lab_01/ex02/ex02_05.py`](lab_01/ex02/ex02_05.py) | Tính lương tuần, có tăng ca | `python lab_01/ex02/ex02_05.py` |
| [`lab_01/ex02/ex02_06.py`](lab_01/ex02/ex02_06.py) | Tạo ma trận theo X, Y | `python lab_01/ex02/ex02_06.py` |
| [`lab_01/ex02/ex02_07.py`](lab_01/ex02/ex02_07.py) | Nhập nhiều dòng và chuyển sang chữ hoa | `python lab_01/ex02/ex02_07.py` |
| [`lab_01/ex02/ex02_08.py`](lab_01/ex02/ex02_08.py) | Lọc số nhị phân chia hết cho 5 | `python lab_01/ex02/ex02_08.py` |
| [`lab_01/ex02/ex02_09.py`](lab_01/ex02/ex02_09.py) | Kiểm tra số nguyên tố | `python lab_01/ex02/ex02_09.py` |
| [`lab_01/ex02/ex02_10.py`](lab_01/ex02/ex02_10.py) | Đảo ngược chuỗi | `python lab_01/ex02/ex02_10.py` |
| [`lab_01/ex03/ex03_01.py`](lab_01/ex03/ex03_01.py) | Tính tổng các số chẵn trong dãy | `python lab_01/ex03/ex03_01.py` |
| [`lab_01/ex03/ex03_02.py`](lab_01/ex03/ex03_02.py) | Đảo ngược chuỗi bằng hàm | `python lab_01/ex03/ex03_02.py` |
| [`lab_01/ex03/ex03_03.py`](lab_01/ex03/ex03_03.py) | Chuyển list sang tuple | `python lab_01/ex03/ex03_03.py` |
| [`lab_01/ex03/ex03_04.py`](lab_01/ex03/ex03_04.py) | Lấy phần tử đầu/cuối của tuple | `python lab_01/ex03/ex03_04.py` |
| [`lab_01/ex03/ex03_05.py`](lab_01/ex03/ex03_05.py) | Đếm số lần xuất hiện của từng từ | `python lab_01/ex03/ex03_05.py` |
| [`lab_01/ex03/ex03_06.py`](lab_01/ex03/ex03_06.py) | Xóa key khỏi dictionary | `python lab_01/ex03/ex03_06.py` |
| [`lab_01/ex04/main.py`](lab_01/ex04/main.py) | Menu chính quản lý sinh viên | `cd lab_01/ex04 && python main.py` |
| [`lab_01/ex04/QuanLySinhVien.py`](lab_01/ex04/QuanLySinhVien.py) | Class xử lý nghiệp vụ sinh viên | Chạy qua `main.py` |
| [`lab_01/ex04/SinhVien.py`](lab_01/ex04/SinhVien.py) | Class lưu thông tin sinh viên | Chạy qua `main.py` |

## Chi tiết từng file

### [`lab_01/Text_01.py`](lab_01/Text_01.py)

Chức năng:

- In 3 dòng thông tin giới thiệu.
- Nội dung gồm tên cá nhân, nhóm WPCTeam và môn/bài thực hành.

Luồng xử lý:

1. Gọi `print()` để in tên và nhóm.
2. Gọi `print()` để in tên nhóm/khẩu hiệu.
3. Gọi `print()` để in thông tin môn học.

Hàm sử dụng:

- Không tự định nghĩa hàm.
- Dùng hàm có sẵn `print()` của Python để xuất dữ liệu ra màn hình.

---

### [`lab_01/ex01/Text_01.py`](lab_01/ex01/Text_01.py)

Chức năng:

- Bản trong thư mục `ex01`, nội dung giống `lab_01/Text_01.py`.
- Dùng để làm quen với lệnh xuất dữ liệu ra console.

Luồng xử lý:

1. In tên: `Tran Tan Dat - WPCTeam`.
2. In dòng: `White Promotion Code`.
3. In dòng: `BMTTNC - WPCTeam`.

Hàm sử dụng:

- Không tự định nghĩa hàm.
- Dùng `print()` để in chuỗi cố định.

---

### [`lab_01/ex02/ex02_01.py`](lab_01/ex02/ex02_01.py)

Chức năng:

- Nhập tên và tuổi từ bàn phím.
- In lời chào theo dữ liệu người dùng nhập.

Luồng xử lý:

1. `input("Nhap ten cua ban: ")` nhận tên.
2. `input("Nhap tuoi cua ban: ")` nhận tuổi.
3. Ghép chuỗi bằng toán tử `+`.
4. In lời chào bằng `print()`.

Hàm sử dụng:

- Không tự định nghĩa hàm.
- `input()` dùng để nhận dữ liệu kiểu chuỗi.
- `print()` dùng để hiển thị kết quả.

---

### [`lab_01/ex02/ex02_02.py`](lab_01/ex02/ex02_02.py)

Chức năng:

- Nhập bán kính hình tròn.
- Tính diện tích theo công thức `S = 3.14 * r * r`.
- Làm tròn kết quả 2 chữ số thập phân.

Luồng xử lý:

1. Nhận bán kính bằng `input()`.
2. Ép kiểu sang `float` để tính số thực.
3. Tính diện tích bằng biến `dien_tich`.
4. In kết quả đã làm tròn bằng `round(dien_tich, 2)`.

Hàm sử dụng:

- Không tự định nghĩa hàm.
- `float()` chuyển chuỗi nhập vào thành số thực.
- `round()` làm tròn kết quả.
- `print()` hiển thị diện tích.

Ghi chú:

- File có dòng comment gợi ý có thể dùng `math.pi` để chính xác hơn.

---

### [`lab_01/ex02/ex02_03.py`](lab_01/ex02/ex02_03.py)

Chức năng:

- Nhập một số nguyên.
- Kiểm tra số đó là chẵn hay lẻ.

Luồng xử lý:

1. Nhận dữ liệu bằng `input()`.
2. Ép kiểu sang `int`.
3. Dùng toán tử `%` để lấy phần dư khi chia cho `2`.
4. Nếu phần dư bằng `0` thì là số chẵn, ngược lại là số lẻ.

Hàm sử dụng:

- Không tự định nghĩa hàm.
- `int()` chuyển chuỗi sang số nguyên.
- `print()` in kết quả.

---

### [`lab_01/ex02/ex02_04.py`](lab_01/ex02/ex02_04.py)

Chức năng:

- Tìm các số trong đoạn từ `2000` đến `3200`.
- Điều kiện: chia hết cho `7` và không chia hết cho `5`.
- In danh sách kết quả, ngăn cách bằng dấu phẩy.

Luồng xử lý:

1. Tạo list rỗng `j`.
2. Duyệt từng số bằng `for i in range(2000, 3201)`.
3. Kiểm tra điều kiện `(i % 7 == 0) and (i % 5 != 0)`.
4. Chuyển số hợp lệ sang chuỗi bằng `str(i)` rồi đưa vào list.
5. Dùng `",".join(j)` để ghép kết quả thành một dòng.

Hàm sử dụng:

- Không tự định nghĩa hàm.
- `range()` tạo dãy số cần duyệt.
- `append()` thêm phần tử vào list.
- `str()` chuyển số sang chuỗi.
- `join()` ghép các chuỗi trong list.

---

### [`lab_01/ex02/ex02_05.py`](lab_01/ex02/ex02_05.py)

Chức năng:

- Nhập số giờ làm mỗi tuần và lương mỗi giờ.
- Tính lương thực lĩnh.
- Giờ tiêu chuẩn là `44` giờ.
- Giờ vượt chuẩn được tính hệ số `1.5`.

Luồng xử lý:

1. Nhập `so_gio_lam` và `luong_gio`.
2. Gán `gio_tieu_chuan = 44`.
3. Tính giờ vượt chuẩn bằng `max(0, so_gio_lam - gio_tieu_chuan)`.
4. Tính lương: `gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5`.
5. Làm tròn và in kết quả.

Hàm sử dụng:

- Không tự định nghĩa hàm.
- `float()` chuyển input sang số thực.
- `max()` đảm bảo giờ vượt chuẩn không bị âm.
- `round()` làm tròn tiền lương.

---

### [`lab_01/ex02/ex02_06.py`](lab_01/ex02/ex02_06.py)

Chức năng:

- Nhập hai số `X` và `Y`.
- Tạo ma trận có `X` dòng, `Y` cột.
- Giá trị tại vị trí dòng `i`, cột `j` là `i * j`.

Luồng xử lý:

1. Nhập `X y` trên cùng một dòng, tách bằng `.split(" ")`.
2. Tạo list rỗng `listfinal`.
3. Duyệt từng dòng bằng `for i in range(int(input_str1))`.
4. Tạo từng dòng bằng list comprehension `[i*j for j in range(int(input_str2))]`.
5. Thêm dòng vào ma trận bằng `append()`.
6. In ma trận kết quả.

Hàm sử dụng:

- Không tự định nghĩa hàm.
- `split()` tách chuỗi nhập vào.
- `int()` chuyển `X`, `Y` sang số nguyên.
- `range()` tạo chỉ số dòng/cột.
- `append()` thêm từng dòng vào ma trận.

Ví dụ input:

```text
3 4
```

---

### [`lab_01/ex02/ex02_07.py`](lab_01/ex02/ex02_07.py)

Chức năng:

- Nhập nhiều dòng văn bản.
- Dừng nhập khi người dùng gõ `end`.
- In lại các dòng đã nhập ở dạng chữ in hoa.

Luồng xử lý:

1. Tạo list `lines` để lưu các dòng.
2. Dùng vòng lặp `while True` để nhập liên tục.
3. Nếu dòng nhập vào sau khi `.lower()` bằng `end` thì `break`.
4. Nếu chưa kết thúc, thêm dòng vào `lines`.
5. Duyệt list và in từng dòng bằng `text.upper()`.

Hàm sử dụng:

- Không tự định nghĩa hàm.
- `lower()` chuyển chuỗi về chữ thường để so sánh dễ hơn.
- `upper()` chuyển chuỗi sang chữ hoa.
- `append()` lưu dòng nhập vào list.

---

### [`lab_01/ex02/ex02_08.py`](lab_01/ex02/ex02_08.py)

Chức năng:

- Nhập các số nhị phân, phân tách bằng dấu phẩy.
- Lọc ra các số nhị phân có giá trị thập phân chia hết cho `5`.

Hàm chính:

#### `divi_5(so_nhi_phan)`

- Tham số: `so_nhi_phan` là chuỗi biểu diễn số nhị phân, ví dụ `1010`.
- Chuyển chuỗi nhị phân sang số thập phân bằng `int(so_nhi_phan, 2)`.
- Trả về `True` nếu số thập phân chia hết cho `5`, ngược lại `False`.

Luồng xử lý:

1. Nhập danh sách số nhị phân bằng `input()`.
2. Tách danh sách bằng `.split(",")`.
3. Dùng list comprehension để giữ lại số nào `divi_5(x)` trả về `True`.
4. In kết quả bằng `",".join(list_bina)`.

Ví dụ input:

```text
0100,0011,1010,1001
```

---

### [`lab_01/ex02/ex02_09.py`](lab_01/ex02/ex02_09.py)

Chức năng:

- Nhập một số nguyên.
- Kiểm tra số đó có phải số nguyên tố hay không.

Hàm chính:

#### `prime_number(n)`

- Tham số: `n` là số nguyên cần kiểm tra.
- Duyệt các số từ `2` đến `sqrt(n)`.
- Nếu `n` chia hết cho bất kỳ số nào trong đoạn đó thì trả về `False`.
- Nếu không chia hết và `n > 2` thì trả về `True`.

Luồng xử lý:

1. Nhập số nguyên bằng `input()`.
2. Ép kiểu sang `int`.
3. Gọi `prime_number(n)`.
4. Dùng biểu thức điều kiện để in thông báo là số nguyên tố hoặc không.

Hàm/kỹ thuật sử dụng:

- `int(n**0.5) + 1` giới hạn vòng lặp đến căn bậc hai của `n` để tối ưu.
- Toán tử `:=` vừa gán biến `n`, vừa dùng trong biểu thức in kết quả.

Ghi chú:

- Theo code hiện tại, số `2` sẽ được xem là không phải số nguyên tố vì điều kiện cuối là `n > 2`.

---

### [`lab_01/ex02/ex02_10.py`](lab_01/ex02/ex02_10.py)

Chức năng:

- Nhập một chuỗi.
- Đảo ngược chuỗi và in ra màn hình.

Hàm chính:

#### `reverse_str(chuoi)`

- Tham số: `chuoi` là chuỗi cần đảo.
- Trả về `chuoi[::-1]`.
- `[::-1]` là slicing trong Python, nghĩa là lấy toàn bộ chuỗi theo chiều ngược lại.

Luồng xử lý:

1. Nhập chuỗi bằng `input()`.
2. Gọi `reverse_str()`.
3. In chuỗi đã đảo bằng `print()`.

---

### [`lab_01/ex03/ex03_01.py`](lab_01/ex03/ex03_01.py)

Chức năng:

- Nhập một dãy số nguyên.
- Tính tổng các số chẵn trong dãy.

Hàm chính:

#### `sum_so_chan(lst)`

- Tham số: `lst` là danh sách/iterator các số nguyên.
- Dùng list comprehension `[x for x in lst if x % 2 == 0]` để lọc số chẵn.
- Dùng `sum()` để cộng các số chẵn.
- Trả về tổng tìm được.

Luồng xử lý:

1. Nhập dãy số, cách nhau bằng khoảng trắng.
2. Dùng `.split()` để tách thành list chuỗi.
3. Dùng `map(int, ...)` để chuyển thành số nguyên.
4. Gọi `sum_so_chan(number_list)`.
5. In tổng số chẵn.

Ví dụ input:

```text
1 2 3 4 5 6
```

---

### [`lab_01/ex03/ex03_02.py`](lab_01/ex03/ex03_02.py)

Chức năng:

- Nhập một chuỗi.
- Đảo ngược chuỗi bằng hàm riêng.

Hàm chính:

#### `dao_chuoi(chuoi)`

- Tham số: `chuoi` là chuỗi đầu vào.
- Trả về chuỗi đảo ngược bằng slicing `chuoi[::-1]`.

Luồng xử lý:

1. Nhập chuỗi từ bàn phím.
2. Gọi `dao_chuoi()`.
3. In kết quả sau khi đảo.

---

### [`lab_01/ex03/ex03_03.py`](lab_01/ex03/ex03_03.py)

Chức năng:

- Nhập một dãy số nguyên.
- Chuyển list số nguyên sang tuple.

Hàm chính:

#### `tuple_list(lst)`

- Tham số: `lst` là list đầu vào.
- Dùng `tuple(lst)` để chuyển list thành tuple.
- Trả về tuple kết quả.

Luồng xử lý:

1. Nhập dãy số, cách nhau bằng khoảng trắng.
2. Chuyển dữ liệu nhập thành list số nguyên bằng `list(map(int, input().split()))`.
3. Gọi `tuple_list()`.
4. In tuple kết quả.

---

### [`lab_01/ex03/ex03_04.py`](lab_01/ex03/ex03_04.py)

Chức năng:

- Nhập một tuple.
- Lấy phần tử đầu tiên và phần tử cuối cùng.

Hàm chính:

#### `truy_cap_phan_tu(tuple_data)`

- Tham số: `tuple_data` là tuple đầu vào.
- Lấy phần tử đầu bằng `tuple_data[0]`.
- Lấy phần tử cuối bằng `tuple_data[-1]`.
- Trả về 2 giá trị: `first_element`, `last_element`.

Luồng xử lý:

1. Nhập tuple dạng `(1,2,545)`.
2. Dùng `eval()` để chuyển chuỗi nhập thành tuple Python.
3. Gọi `truy_cap_phan_tu()`.
4. Chuyển từng phần tử sang chuỗi và in ra.

Ghi chú:

- `eval()` chạy trực tiếp biểu thức Python, chỉ nên dùng khi input đáng tin cậy.

---

### [`lab_01/ex03/ex03_05.py`](lab_01/ex03/ex03_05.py)

Chức năng:

- Nhập danh sách các từ.
- Đếm số lần xuất hiện của từng từ.
- Trả kết quả dạng dictionary.

Hàm chính:

#### `count_elements(lst)`

- Tham số: `lst` là list các từ.
- Tạo dictionary rỗng `count_dict`.
- Duyệt từng `item` trong list.
- Nếu từ đã có trong dictionary thì tăng số đếm lên `1`.
- Nếu chưa có thì khởi tạo số đếm bằng `1`.
- Trả về dictionary kết quả.

Luồng xử lý:

1. Nhập các từ, cách nhau bằng khoảng trắng.
2. Dùng `.split()` để tạo list từ.
3. Gọi `count_elements()`.
4. In dictionary số lần xuất hiện.

Ví dụ input:

```text
python java python c python java
```

---

### [`lab_01/ex03/ex03_06.py`](lab_01/ex03/ex03_06.py)

Chức năng:

- Tạo dictionary mẫu.
- Xóa một key khỏi dictionary nếu key tồn tại.
- In dictionary sau khi xóa.

Hàm chính:

#### `del_implement(dictt, key)`

- Tham số `dictt`: dictionary cần xử lý.
- Tham số `key`: key cần xóa.
- Nếu `key in dictt`, dùng `del dictt[key]` để xóa.
- Nếu key không tồn tại, in thông báo không tìm thấy.

Luồng xử lý:

1. Tạo dictionary `my_dict = {"a": 1, "b": 2, "c": 3}`.
2. Gán `key_to_delete = "b"`.
3. Gọi `del_implement(my_dict, key_to_delete)`.
4. In dictionary sau khi xóa.

---

### [`lab_01/ex04/SinhVien.py`](lab_01/ex04/SinhVien.py)

Chức năng:

- Định nghĩa class `SinhVien` để lưu thông tin một sinh viên.
- Đây là model dữ liệu được dùng bởi `QuanLySinhVien.py`.

Class chính:

#### `SinhVien`

Thuộc tính:

- `_id`: mã sinh viên tự tăng
- `_name`: họ tên sinh viên
- `_sex`: giới tính
- `_major`: chuyên ngành
- `_diemTB`: điểm trung bình
- `_hocLuc`: học lực, ban đầu là chuỗi rỗng

Hàm chính:

#### `__init__(self, id, name, sex, major, diemTB)`

- Hàm khởi tạo object sinh viên.
- Nhận dữ liệu từ `QuanLySinhVien.themSinhVien()`.
- Gán từng tham số vào thuộc tính tương ứng của object.

---

### [`lab_01/ex04/QuanLySinhVien.py`](lab_01/ex04/QuanLySinhVien.py)

Chức năng:

- Chứa class `QuanLySinhVien`.
- Quản lý danh sách sinh viên và các nghiệp vụ thêm, sửa, xóa, tìm kiếm, sắp xếp, hiển thị.

Class chính:

#### `QuanLySinhVien`

Thuộc tính:

- `listSinhVien`: list lưu các object `SinhVien`.

Các hàm chính:

#### `generateID(self)`

- Tạo ID mới cho sinh viên.
- Nếu danh sách rỗng, trả về `1`.
- Nếu đã có sinh viên, tìm ID lớn nhất rồi cộng thêm `1`.

#### `soLuongSinhVien(self)`

- Trả về số lượng sinh viên hiện có.
- Dùng `self.listSinhVien.__len__()`.

#### `themSinhVien(self)`

- Nhập tên, giới tính, chuyên ngành, điểm trung bình.
- Tạo object `SinhVien` mới.
- Gọi `xepLoaiHocLuc()` để gán học lực.
- Thêm sinh viên vào `listSinhVien`.

#### `updateSinhVien(self, ID)`

- Tìm sinh viên theo ID bằng `findByID()`.
- Nếu tìm thấy, nhập lại thông tin mới và cập nhật object.
- Sau khi cập nhật điểm, gọi lại `xepLoaiHocLuc()`.
- Nếu không tìm thấy, in thông báo lỗi.

#### `xepLoaiHocLuc(self, sv)`

- Xếp loại học lực dựa trên `_diemTB`.
- Từ `9`: Xuất sắc.
- Từ `8`: Giỏi.
- Từ `7`: Khá.
- Từ `5`: Trung bình.
- Dưới `5`: Yếu.

#### `sortByID(self)`

- Sắp xếp danh sách sinh viên theo `_id` tăng dần.

#### `sortByName(self)`

- Sắp xếp danh sách sinh viên theo `_name` tăng dần.

#### `sortByDiemTB(self)`

- Sắp xếp danh sách sinh viên theo `_diemTB` giảm dần.

#### `findByID(self, ID)`

- Duyệt danh sách sinh viên.
- Nếu sinh viên có `_id` trùng ID cần tìm thì trả về sinh viên đó.
- Nếu không tìm thấy thì trả về `None`.

#### `findByName(self, keyword)`

- Tìm sinh viên có tên chứa từ khóa.
- Trả về list sinh viên phù hợp.

#### `deleteByID(self, ID)`

- Tìm sinh viên theo ID.
- Nếu tìm thấy thì xóa khỏi list bằng `remove()`.
- Trả về `True` nếu xóa thành công, `False` nếu không tìm thấy.

#### `showSinhVien(self, listSV)`

- In bảng danh sách sinh viên.
- Hiển thị các cột: `ID`, `Name`, `Sex`, `Major`, `DiemTB`, `HocLuc`.
- Dùng `format()` để căn chỉnh cột.

#### `getListSinhVien(self)`

- Trả về toàn bộ danh sách sinh viên hiện tại.
- Được `main.py` dùng khi cần hiển thị hoặc sắp xếp.

---

### [`lab_01/ex04/main.py`](lab_01/ex04/main.py)

Chức năng:

- Là file chạy chính của mini project quản lý sinh viên.
- Hiển thị menu CLI và gọi các hàm trong `QuanLySinhVien`.

Luồng xử lý:

1. Import class `QuanLySinhVien`.
2. Tạo object `qlsv = QuanLySinhVien()`.
3. Dùng vòng lặp `while True` để menu chạy liên tục.
4. In menu lựa chọn từ `1` đến `7`, và `0` để thoát.
5. Nhận lựa chọn bằng `input()` rồi ép kiểu `int`.
6. Dùng `if/elif/else` để xử lý từng chức năng.

Danh sách chức năng trong menu:

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

Ghi chú:

- Trước các thao tác cần dữ liệu, chương trình kiểm tra `qlsv.soLuongSinhVien() == 0` để báo danh sách rỗng.
- File này không tự định nghĩa hàm, chủ yếu điều phối menu và gọi nghiệp vụ từ `QuanLySinhVien`.

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
