# Repository Structure

```text
BMTTNC-WPCTeam-Pro/
|-- lab_01/
|   |-- Text_01.py
|   |-- ex01/
|   |-- ex02/
|   |-- ex03/
|   `-- ex04/
|-- lab_02/
|   |-- ex01/
|   `-- ex01_API/
|       |-- api.py
|       |-- cipher/
|       |   |-- caesar/
|       |   |-- playfair/
|       |   |-- railfence/
|       |   |-- transposition/
|       |   `-- vigenere/
|       |-- postman/
|       |-- static/
|       `-- templates/
|-- lab_03/
|   |-- api.py
|   |-- caesar_cipher.py
|   |-- ecc_cipher.py
|   |-- cipher/
|   |   |-- ecc/
|   |   `-- rsa/
|   |-- postman/
|   |   `-- api-cipher-rsa-ecc.postman_collection.json
|   |-- ui/
|   `-- platform/
|-- docs-en/
|-- img/
|-- AGENTS.md
|-- LICENSE
|-- requirements.txt
`-- readme.md
```

## Important Paths

| Path | Purpose |
|---|---|
| `lab_02/ex01_API/api.py` | Classic cipher Flask API and web UI |
| `lab_03/api.py` | RSA/ECC Flask API |
| `lab_03/cipher/rsa/rsa_cipher.py` | RSA crypto implementation |
| `lab_03/cipher/ecc/ecc_cipher.py` | ECC signature implementation |
| `lab_03/postman/api-cipher-rsa-ecc.postman_collection.json` | Latest Lab 03 Postman collection |
| `docs-en/` | Separate English supplemental documentation |
