# API And Postman Guide

## Postman Collections

| Area | Collection |
|---|---|
| Lab 02 classic ciphers | `lab_02/ex01_API/postman/api-cipher.postman_collection.json` |
| Lab 03 latest full collection | `lab_03/postman/api-cipher-rsa-ecc.postman_collection.json` |

## Lab 02 Classic Cipher API

Base URL:

```text
http://127.0.0.1:5000/api
```

Route pattern:

```text
POST /api/<algorithm>/<action>
```

Supported algorithms: `caesar`, `vigenere`, `playfair`, `railfence`, `transposition`.

Supported actions: `encrypt`, `decrypt`, `details`.

Typical encrypt body fields:

```text
plain_text: Hello World
key: 3
```

Typical decrypt body fields:

```text
encrypted_text: Khoor Zruog
key: 3
```

## Lab 03 RSA API

| Method | Endpoint | Purpose |
|---:|---|---|
| GET | `/api/rsa/generate_keys` | Generate RSA key pair |
| POST | `/api/rsa/encrypt` | Encrypt text with public key |
| POST | `/api/rsa/decrypt` | Decrypt ciphertext with private key |
| POST | `/api/rsa/sign` | Sign a message with private key |
| POST | `/api/rsa/verify` | Verify a signature with public key |

RSA encrypt body fields:

```text
message: HUTECH University
key_type: public
```

RSA decrypt body fields:

```text
ciphertext: {{rsa_ciphertext}}
key_type: private
```

## Lab 03 ECC API

| Method | Endpoint | Purpose |
|---:|---|---|
| GET | `/api/ecc/generate_keys` | Generate ECC key pair |
| POST | `/api/ecc/sign` | Sign a message with private key |
| POST | `/api/ecc/verify` | Verify a signature with public key |

ECC sign body fields:

```text
message: HUTECH University
```

ECC verify body fields:

```text
message: HUTECH University
signature: {{ecc_signature}}
```

## Recommended Postman Flow

1. Import `lab_03/postman/api-cipher-rsa-ecc.postman_collection.json`.
2. Run `RSA / Generate Keys`, then RSA encrypt/decrypt/sign/verify.
3. Run `ECC / Generate Keys`, then ECC sign/verify.
4. For classic ciphers, run encrypt before decrypt so collection variables are populated.

## Collection Variables

- `base_url`
- `caesar_cipher_text`
- `vigenere_cipher_text`
- `playfair_cipher_text`
- `railfence_cipher_text`
- `transposition_cipher_text`
- `rsa_ciphertext`
- `rsa_signature`
- `ecc_signature`
