import rsa
from flask import Flask, jsonify, request

if __package__:
    from .cipher.rsa import RSACipher
else:
    from cipher.rsa import RSACipher

app = Flask(__name__)

# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher()


def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code


def get_json_data():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return None, error_response('Request body must be valid JSON')
    return data, None


def get_required_text(data, field_name):
    value = data.get(field_name)
    if not isinstance(value, str) or not value.strip():
        return None, error_response(f'Missing or empty field: {field_name}')
    return value.strip(), None


def load_rsa_keys():
    try:
        return rsa_cipher.load_keys(), None
    except FileNotFoundError:
        return None, error_response('RSA keys not found. Call /api/rsa/generate_keys first')
    except ValueError:
        return None, error_response('RSA key files are invalid. Generate keys again')


def decode_hex_value(value, field_name):
    try:
        return bytes.fromhex(value), None
    except ValueError:
        return None, error_response(f'Field {field_name} must be hexadecimal text')


@app.route("/api/rsa/generate_keys", methods=["GET"])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})


@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data, error = get_json_data()
    if error:
        return error

    message, error = get_required_text(data, 'message')
    if error:
        return error

    key_type, error = get_required_text(data, 'key_type')
    if error:
        return error

    if key_type != 'public':
        return error_response('RSA encryption must use key_type public')

    keys, error = load_rsa_keys()
    if error:
        return error

    _private_key, public_key = keys

    try:
        encrypted_message = rsa_cipher.encrypt(message, public_key)
    except OverflowError:
        return error_response('Message is too long for this RSA key size')

    encrypted_hex = encrypted_message.hex()

    return jsonify({'encrypted_message': encrypted_hex})


@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data, error = get_json_data()
    if error:
        return error

    ciphertext_hex = data.get('ciphertext') or data.get('encrypted_message')
    if not isinstance(ciphertext_hex, str) or not ciphertext_hex.strip():
        return error_response('Missing or empty field: ciphertext')
    ciphertext_hex = ciphertext_hex.strip()

    key_type, error = get_required_text(data, 'key_type')
    if error:
        return error

    if key_type != 'private':
        return error_response('RSA decryption must use key_type private')

    ciphertext, error = decode_hex_value(ciphertext_hex, 'ciphertext')
    if error:
        return error

    keys, error = load_rsa_keys()
    if error:
        return error

    private_key, _public_key = keys

    try:
        decrypted_message = rsa_cipher.decrypt(ciphertext, private_key)
    except rsa.DecryptionError:
        return error_response('Ciphertext cannot be decrypted with the current private key')

    return jsonify({'decrypted_message': decrypted_message})


@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign_message():
    data, error = get_json_data()
    if error:
        return error

    message, error = get_required_text(data, 'message')
    if error:
        return error

    keys, error = load_rsa_keys()
    if error:
        return error

    private_key, _public_key = keys

    signature = rsa_cipher.sign(message, private_key)
    signature_hex = signature.hex()

    return jsonify({'signature': signature_hex})


@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify_signature():
    data, error = get_json_data()
    if error:
        return error

    message, error = get_required_text(data, 'message')
    if error:
        return error

    signature_hex, error = get_required_text(data, 'signature')
    if error:
        return error

    signature, error = decode_hex_value(signature_hex, 'signature')
    if error:
        return error

    keys, error = load_rsa_keys()
    if error:
        return error

    _private_key, public_key = keys
    is_verified = rsa_cipher.verify(message, signature, public_key)

    return jsonify({'is_verified': is_verified})


# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
