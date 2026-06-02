# Project Overview

## Purpose

`BMTTNC-WPCTeam-Pro` is a Python learning project for basic programming
exercises and cryptography practice. It is organized into three labs.

## Labs

| Lab | Scope | Main Entry Points |
|---|---|---|
| Lab 01 | Basic Python syntax, data structures, functions, and student management CLI | `lab_01/` |
| Lab 02 | Classic cipher implementations with Flask API and web UI | `lab_02/ex01_API/api.py` |
| Lab 03 | PyQt5 clients and asymmetric crypto API for RSA/ECC | `lab_03/api.py`, `lab_03/caesar_cipher.py`, `lab_03/ecc_cipher.py` |

## Technology

- Python 3.10 or newer recommended
- Flask for HTTP APIs and the Lab 02 web UI
- PyQt5 for desktop UI clients
- `rsa` for RSA encryption/signature operations
- `ecdsa` for ECC signatures
- Postman collections for API testing

## Current API Collections

- Lab 02 classic ciphers: `lab_02/ex01_API/postman/api-cipher.postman_collection.json`
- Lab 03 classic ciphers + RSA + ECC: `lab_03/postman/api-cipher-rsa-ecc.postman_collection.json`

## Generated Files To Avoid Committing

- `__pycache__/`
- `*.pyc`
- `.tmp-*.log`
- `lab_03/cipher/rsa/keys/`
- `lab_03/cipher/ecc/keys/`
