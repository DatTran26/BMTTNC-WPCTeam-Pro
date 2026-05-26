# Huong dan dung Postman cho API Cipher

## 1. Chay Flask API

Mo terminal tai thu muc goc project:

```bash
cd lab_02/ex01_API
python api.py
```

Mac dinh server chay tai:

```text
http://127.0.0.1:5000/api
```

Neu port `5000` bi trung, doi port khi chay Flask va sua collection variable `base_url` trong Postman.

## 2. Import collection vao Postman

1. Mo Postman.
2. Bam `Import`.
3. Chon file:

```text
lab_02/ex01_API/postman/api-cipher.postman_collection.json
```

4. Sau khi import se thay collection `API Cipher`.
5. Cau truc collection:

```text
API Cipher
|-- Caesar
|   |-- POST Encrypt
|   |-- POST Decrypt
|   `-- POST Details / Matrix
|-- Vigenere
|   |-- POST Encrypt
|   |-- POST Decrypt
|   `-- POST Details / Matrix
|-- Playfair
|   |-- POST Encrypt
|   |-- POST Decrypt
|   `-- POST Details / Matrix
|-- Rail Fence
|   |-- POST Encrypt
|   |-- POST Decrypt
|   `-- POST Details / Matrix
`-- Transposition
    |-- POST Encrypt
    |-- POST Decrypt
    `-- POST Details / Matrix
```

## 3. Cach test nhanh

1. Chon request `Encrypt` cua thuat toan can test.
2. Bam `Send`.
3. Postman se tu luu ket qua ma hoa vao collection variable.
4. Chon request `Decrypt` cung folder.
5. Bam `Send` de giai ma lai.
6. Chon request `Details / Matrix`.
7. Bam `Send` de xem bang/ma tran/thong tin lien quan.

Vi du `Caesar/Encrypt`:

```json
{
  "plain_text": "Hello World",
  "key": "3"
}
```

Ket qua:

```json
{
  "action": "encrypt",
  "algorithm": "caesar",
  "encrypted_text": "Khoor Zruog",
  "result": "Khoor Zruog"
}
```

## 4. Xem ma tran trong Postman

Request `Details / Matrix` dung chung endpoint:

```text
POST /<algorithm>/details
```

Body mau:

```json
{
  "plain_text": "Hello World",
  "key": "KEY"
}
```

Ket qua nam trong field `details`.

| Thuat toan | Details tra ve |
|---|---|
| Caesar | `alphabet`, `shift`, `normalized_shift`, `mapping` |
| Vigenere | `matrix` tabula recta 26x26, `formatted_key`, `key_shifts`, `key_stream` |
| Playfair | `matrix` 5x5, `normalized_key`, `normalized_text`, `pairs`, `position_map`, `rules` |
| Rail Fence | `matrix` zigzag, `rail_count`, `pattern`, `rails` |
| Transposition | `matrix`, `key_row`, `column_order`, `ordered_columns`, `padded_text` |

Trong Postman, chon tab `Body` cua response va de che do `Pretty` + `JSON` de nhin ma tran ro hon.

## 5. Danh sach endpoint

| Thuat toan | Encrypt | Decrypt | Details |
|---|---|---|---|
| Caesar | `POST /caesar/encrypt` | `POST /caesar/decrypt` | `POST /caesar/details` |
| Vigenere | `POST /vigenere/encrypt` | `POST /vigenere/decrypt` | `POST /vigenere/details` |
| Playfair | `POST /playfair/encrypt` | `POST /playfair/decrypt` | `POST /playfair/details` |
| Rail Fence | `POST /railfence/encrypt` | `POST /railfence/decrypt` | `POST /railfence/details` |
| Transposition | `POST /transposition/encrypt` | `POST /transposition/decrypt` | `POST /transposition/details` |

## 6. Body mau

Encrypt:

```json
{
  "plain_text": "Hello World",
  "key": "KEY"
}
```

Decrypt:

```json
{
  "encrypted_text": "Rijvs Uyvjn",
  "key": "KEY"
}
```

Details:

```json
{
  "plain_text": "Hello World",
  "key": "KEY"
}
```

## 7. Luu y

- `Caesar` va `Rail Fence` dung key dang so.
- `Vigenere`, `Playfair`, `Transposition` dung key dang chuoi.
- `Playfair` chuyen chuoi ve chu hoa, bo khoang trang, doi `J` thanh `I`.
- `Transposition` tu them ky tu dem `X` khi do dai chuoi khong chia het cho do dai key.
- Neu doi host/port, vao collection `API Cipher` -> `Variables` -> sua `base_url`.
