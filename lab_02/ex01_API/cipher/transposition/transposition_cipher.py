class TranspositionCipher:
    def __init__(self, key, padding_char="X"):
        self.key = str(key).strip()
        self.padding_char = str(padding_char or "X")[0]

        if not self.key:
            raise ValueError("Transposition key must not be empty")

    def encrypt(self, plain_text):
        column_count = len(self.key)
        padded_text = self.pad_text(str(plain_text), column_count)
        rows = [
            padded_text[index:index + column_count]
            for index in range(0, len(padded_text), column_count)
        ]

        return "".join(
            row[column_index]
            for column_index in self.column_order()
            for row in rows
        )

    def decrypt(self, cipher_text):
        cipher_text = str(cipher_text)
        column_count = len(self.key)

        if len(cipher_text) % column_count != 0:
            raise ValueError("Cipher text length must be divisible by key length")

        row_count = len(cipher_text) // column_count
        columns = [""] * column_count
        index = 0

        for column_index in self.column_order():
            columns[column_index] = cipher_text[index:index + row_count]
            index += row_count

        plain_text = "".join(
            columns[column_index][row_index]
            for row_index in range(row_count)
            for column_index in range(column_count)
        )

        return plain_text.rstrip(self.padding_char)

    def column_order(self):
        return sorted(
            range(len(self.key)),
            key=lambda index: (self.key[index].lower(), index),
        )

    def pad_text(self, text, column_count):
        padding_length = (-len(text)) % column_count
        return text + self.padding_char * padding_length
