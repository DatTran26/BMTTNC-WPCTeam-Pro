from pathlib import Path

import rsa


class RSACipher:
    def __init__(self, key_dir=None, key_size=1024):
        self.key_dir = Path(key_dir) if key_dir else Path(__file__).resolve().parent / 'keys'
        self.key_size = key_size
        self.private_key_path = self.key_dir / 'privateKey.pem'
        self.public_key_path = self.key_dir / 'publicKey.pem'

    def generate_keys(self):
        public_key, private_key = rsa.newkeys(self.key_size)

        self.key_dir.mkdir(parents=True, exist_ok=True)
        self.public_key_path.write_bytes(public_key.save_pkcs1('PEM'))
        self.private_key_path.write_bytes(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        private_key = rsa.PrivateKey.load_pkcs1(self.private_key_path.read_bytes())
        public_key = rsa.PublicKey.load_pkcs1(self.public_key_path.read_bytes())

        return private_key, public_key

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('utf-8'), key)

    def decrypt(self, ciphertext, key):
        return rsa.decrypt(ciphertext, key).decode('utf-8')

    def sign(self, message, private_key):
        return rsa.sign(message.encode('utf-8'), private_key, 'SHA-256')

    def verify(self, message, signature, public_key):
        try:
            rsa.verify(message.encode('utf-8'), signature, public_key)
            return True
        except rsa.VerificationError:
            return False
