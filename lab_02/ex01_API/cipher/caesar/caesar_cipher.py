from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def shift_char(self, char: str, key: int) -> str:
        if "A" <= char <= "Z":
            ascii_offset = ord("A")
        elif "a" <= char <= "z":
            ascii_offset = ord("a")
        else:
            return char

        return chr((ord(char) - ascii_offset + key) % len(self.alphabet) + ascii_offset)

    def encrypt_text(self, text: str, key: int) -> str:
        key = int(key)
        return "".join(self.shift_char(char, key) for char in text)

    def decrypt_text(self, text: str, key: int) -> str:
        key = int(key)
        return "".join(self.shift_char(char, -key) for char in text)
