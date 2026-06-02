# Setup And Run Guide

## Requirements

- Python 3.10+
- PowerShell, CMD, Git Bash, or VS Code terminal
- Dependencies from `requirements.txt`

## Install Dependencies

Run from the repository root:

```bash
python -m pip install -r requirements.txt
```

## Run Lab 02 Flask API And Web UI

```bash
cd lab_02/ex01_API
python api.py
```

Open:

```text
http://127.0.0.1:5000
```

API base URL:

```text
http://127.0.0.1:5000/api
```

## Run Lab 03 RSA/ECC API

Run from the repository root:

```bash
python lab_03/api.py
```

API base URL:

```text
http://127.0.0.1:5000/api
```

## Run Lab 03 PyQt5 Clients

Caesar UI, with the Lab 02 API running in another terminal:

```bash
python lab_03/caesar_cipher.py
```

ECC UI, with the Lab 03 API running in another terminal:

```bash
python lab_03/ecc_cipher.py
```

## Syntax Check

```bash
python -m compileall lab_01 lab_02 lab_03
```

## Notes

- Lab 02 and Lab 03 both default to port `5000`; run one API server at a time unless you change ports.
- RSA and ECC key files are generated locally and ignored by Git.
