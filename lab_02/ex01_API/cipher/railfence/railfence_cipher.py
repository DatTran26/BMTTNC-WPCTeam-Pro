class RailFenceCipher:
    def __init__(self, key):
        self.key = int(key)
        if self.key < 1:
            raise ValueError("Rail Fence key must be greater than 0")

    def encrypt(self, plain_text):
        if self.key == 1 or len(plain_text) <= 1:
            return plain_text

        rails = ["" for _ in range(self.key)]
        row = 0
        direction = 1

        for char in plain_text:
            rails[row] += char

            if row == 0:
                direction = 1
            elif row == self.key - 1:
                direction = -1
            row += direction

        return "".join(rails)

    def decrypt(self, cipher_text):
        if self.key == 1 or len(cipher_text) <= 1:
            return cipher_text

        pattern = self.create_rail_pattern(len(cipher_text))
        rail_lengths = [pattern.count(row) for row in range(self.key)]
        rails = []
        index = 0

        for length in rail_lengths:
            rails.append(list(cipher_text[index:index + length]))
            index += length

        rail_indexes = [0 for _ in range(self.key)]
        plain_text = []

        for row in pattern:
            plain_text.append(rails[row][rail_indexes[row]])
            rail_indexes[row] += 1

        return "".join(plain_text)

    def create_rail_pattern(self, text_length):
        pattern = []
        row = 0
        direction = 1

        for _ in range(text_length):
            pattern.append(row)

            if row == 0:
                direction = 1
            elif row == self.key - 1:
                direction = -1
            row += direction

        return pattern
