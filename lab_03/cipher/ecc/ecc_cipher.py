import hashlib
from pathlib import Path

import ecdsa


class ECCCipher:
    def __init__(self, key_dir=None):
        self.key_dir = Path(key_dir) if key_dir else Path(__file__).resolve().parent / 'keys'
        self.private_key_path = self.key_dir / 'privateKey.pem'
        self.public_key_path = self.key_dir / 'publicKey.pem'

    def generate_keys(self):
        private_key = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
        public_key = private_key.get_verifying_key()

        self.key_dir.mkdir(parents=True, exist_ok=True)
        self.private_key_path.write_bytes(private_key.to_pem())
        self.public_key_path.write_bytes(public_key.to_pem())

    def load_keys(self):
        try:
            private_key = ecdsa.SigningKey.from_pem(self.private_key_path.read_bytes())
            public_key = ecdsa.VerifyingKey.from_pem(self.public_key_path.read_bytes())
        except FileNotFoundError:
            raise
        except (ValueError, ecdsa.BadDigestError, ecdsa.MalformedPointError, ecdsa.der.UnexpectedDER) as exc:
            raise ValueError('ECC key files are invalid') from exc

        return private_key, public_key

    def sign(self, message, key):
        return key.sign_deterministic(message.encode('utf-8'), hashfunc=hashlib.sha256)

    def verify(self, message, signature, key):
        try:
            return key.verify(signature, message.encode('utf-8'), hashfunc=hashlib.sha256)
        except (ecdsa.BadSignatureError, ecdsa.BadDigestError):
            return False
