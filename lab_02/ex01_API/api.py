from flask import Flask, jsonify, render_template, request

from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ALGORITHMS = [
    {"id": "caesar", "name": "Caesar", "keyLabel": "Shift key", "keyType": "number", "defaultKey": "3"},
    {"id": "vigenere", "name": "Vigenere", "keyLabel": "Text key", "keyType": "text", "defaultKey": "KEY"},
    {"id": "playfair", "name": "Playfair", "keyLabel": "Text key", "keyType": "text", "defaultKey": "KEY"},
    {"id": "railfence", "name": "Rail Fence", "keyLabel": "Rail count", "keyType": "number", "defaultKey": "3"},
    {"id": "transposition", "name": "Transposition", "keyLabel": "Column key", "keyType": "text", "defaultKey": "ZEBRAS"},
]


@app.get("/")
def index():
    return render_template("index.html", algorithms=ALGORITHMS)


@app.post("/api/<algorithm>/<action>")
def run_algorithm(algorithm, action):
    if algorithm not in {item["id"] for item in ALGORITHMS}:
        return error_response("Algorithm is not supported", 404)
    if action == "details":
        return show_algorithm_details(algorithm)
    if action not in ("encrypt", "decrypt"):
        return error_response("Action must be encrypt, decrypt, or details", 404)

    data = request.get_json(silent=True) or {}
    text_field = "plain_text" if action == "encrypt" else "encrypted_text"
    input_text = data.get(text_field, data.get("text", ""))
    key = data.get("key", "")

    try:
        result = dispatch_cipher(algorithm, action, input_text, key)
    except ValueError as error:
        return error_response(str(error))

    result_field = "encrypted_text" if action == "encrypt" else "decrypted_text"
    return jsonify({"algorithm": algorithm, "action": action, "result": result, result_field: result})


def show_algorithm_details(algorithm):
    data = request.get_json(silent=True) or {}
    try:
        details = build_cipher_details(algorithm, data)
    except ValueError as error:
        return error_response(str(error))
    return jsonify({"algorithm": algorithm, "details": details})


def dispatch_cipher(algorithm, action, input_text, key):
    if algorithm == "caesar":
        cipher = CaesarCipher()
        return cipher.encrypt_text(input_text, key) if action == "encrypt" else cipher.decrypt_text(input_text, key)
    cipher_map = {
        "vigenere": VigenereCipher,
        "playfair": PlayfairCipher,
        "railfence": RailFenceCipher,
        "transposition": TranspositionCipher,
    }
    cipher = cipher_map[algorithm](key)
    return cipher.encrypt(input_text) if action == "encrypt" else cipher.decrypt(input_text)


def build_cipher_details(algorithm, data):
    text = data.get("plain_text") or data.get("encrypted_text") or data.get("text", "")
    key = data.get("key", "")
    detail_builders = {
        "caesar": lambda: build_caesar_details(key),
        "vigenere": lambda: build_vigenere_details(text, key),
        "playfair": lambda: build_playfair_details(text, key),
        "railfence": lambda: build_railfence_details(text, key),
        "transposition": lambda: build_transposition_details(text, key),
    }
    return detail_builders[algorithm]()


def build_caesar_details(key):
    shift = int(key)
    normalized_shift = shift % len(ALPHABET)
    return {
        "has_matrix": False,
        "alphabet": list(ALPHABET),
        "shift": shift,
        "normalized_shift": normalized_shift,
        "mapping": [
            {"plain": char, "cipher": ALPHABET[(index + normalized_shift) % len(ALPHABET)]}
            for index, char in enumerate(ALPHABET)
        ],
    }


def build_vigenere_details(text, key):
    cipher = VigenereCipher(key)
    return {
        "has_matrix": True,
        "matrix_name": "Vigenere tabula recta",
        "formatted_key": cipher.key.upper(),
        "key_shifts": [{"key_char": char.upper(), "shift": ord(char) - ord("a")} for char in cipher.key],
        "key_stream": build_vigenere_key_stream(text, cipher.key),
        "matrix": [list(ALPHABET[index:] + ALPHABET[:index]) for index in range(len(ALPHABET))],
    }


def build_vigenere_key_stream(text, key):
    key_stream = []
    key_index = 0
    for index, char in enumerate(str(text)):
        if "a" <= char.lower() <= "z":
            key_char = key[key_index % len(key)]
            key_stream.append({
                "text_index": index,
                "text_char": char,
                "key_char": key_char.upper(),
                "shift": ord(key_char) - ord("a"),
            })
            key_index += 1
    return key_stream


def build_playfair_details(text, key):
    cipher = PlayfairCipher(key)
    normalized_text = cipher.normalize_text(text)
    return {
        "has_matrix": True,
        "matrix_name": "Playfair 5x5 key matrix",
        "normalized_key": cipher.key,
        "normalized_text": normalized_text,
        "pairs": cipher.create_pairs(normalized_text),
        "matrix": cipher.matrix,
        "position_map": {
            char: {"row": row_index, "column": column_index}
            for row_index, row in enumerate(cipher.matrix)
            for column_index, char in enumerate(row)
        },
        "rules": [
            "Same row: move one column to the right when encrypting.",
            "Same column: move one row down when encrypting.",
            "Rectangle: swap columns between the pair positions.",
        ],
    }


def build_railfence_details(text, key):
    cipher = RailFenceCipher(key)
    text = str(text)
    pattern = cipher.create_rail_pattern(len(text))
    matrix = [["" for _ in text] for _ in range(cipher.key)]
    for column_index, char in enumerate(text):
        matrix[pattern[column_index]][column_index] = char
    return {
        "has_matrix": True,
        "matrix_name": "Rail Fence zigzag matrix",
        "rail_count": cipher.key,
        "input_text": text,
        "pattern": pattern,
        "matrix": matrix,
        "rails": ["".join(char or " " for char in row) for row in matrix],
    }


def build_transposition_details(text, key):
    cipher = TranspositionCipher(key)
    padded_text = cipher.pad_text(str(text), len(cipher.key))
    matrix = [list(padded_text[index:index + len(cipher.key)]) for index in range(0, len(padded_text), len(cipher.key))]
    column_order = cipher.column_order()
    return {
        "has_matrix": True,
        "matrix_name": "Columnar transposition matrix",
        "key": cipher.key,
        "key_row": list(cipher.key),
        "padding_char": cipher.padding_char,
        "padded_text": padded_text,
        "matrix": matrix,
        "column_order": [
            {"read_order": order_index + 1, "column_index": column_index, "key_char": cipher.key[column_index]}
            for order_index, column_index in enumerate(column_order)
        ],
        "ordered_columns": [
            {
                "read_order": order_index + 1,
                "column_index": column_index,
                "column_values": [row[column_index] for row in matrix],
            }
            for order_index, column_index in enumerate(column_order)
        ],
    }


def error_response(message, status=400):
    return jsonify({"error": message}), status


def run_server():
    print("Cipher API is starting at http://127.0.0.1:5000")
    print("API root: http://127.0.0.1:5000/api")
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

if __name__ == "__main__":
    run_server()
