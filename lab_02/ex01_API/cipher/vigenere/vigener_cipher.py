class VigenereCipher:
    def __init__(self, key: str):
        self.key = self.format_key(key)
        if not self.key:
            raise ValueError("Vigenere key must contain at least one letter")

    def format_key(self, key: str) -> str:
        return "".join(char.lower() for char in str(key) if "a" <= char.lower() <= "z")

    def shift_char(self, char: str, shift: int) -> str:
        if "A" <= char <= "Z":
            ascii_offset = ord("A")
        elif "a" <= char <= "z":
            ascii_offset = ord("a")
        else:
            return char

        return chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        key_length = len(self.key)
        key_index = 0

        for char in plaintext:
            if "a" <= char.lower() <= "z":
                shift = ord(self.key[key_index % key_length]) - ord("a")
                ciphertext += self.shift_char(char, shift)
                key_index += 1
            else:
                ciphertext += char

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        key_length = len(self.key)
        key_index = 0

        for char in ciphertext:
            if "a" <= char.lower() <= "z":
                shift = ord(self.key[key_index % key_length]) - ord("a")
                plaintext += self.shift_char(char, -shift)
                key_index += 1
            else:
                plaintext += char

        return plaintext
