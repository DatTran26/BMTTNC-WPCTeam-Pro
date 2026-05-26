class PlayfairCipher:
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    def __init__(self, key):
        self.key = self.normalize_text(key)
        if not self.key:
            raise ValueError("Playfair key must contain at least one letter")
        self.matrix = self.generate_matrix()

    def normalize_text(self, text):
        return "".join(
            char.upper().replace("J", "I")
            for char in str(text)
            if "A" <= char.upper() <= "Z"
        )

    def generate_matrix(self):
        matrix = []
        used_chars = set()

        for char in self.key + self.alphabet:
            if char not in used_chars and char in self.alphabet:
                matrix.append(char)
                used_chars.add(char)

        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def encrypt(self, plaintext):
        pairs = self.create_pairs(self.normalize_text(plaintext))
        return "".join(self.encrypt_pair(pair) for pair in pairs)

    def decrypt(self, ciphertext):
        text = self.normalize_text(ciphertext)
        if len(text) % 2 != 0:
            text += "X"

        pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
        decrypted_text = "".join(self.decrypt_pair(pair) for pair in pairs)
        return self.remove_padding(decrypted_text)

    def create_pairs(self, text):
        pairs = []
        i = 0

        while i < len(text):
            first = text[i]
            second = text[i + 1] if i + 1 < len(text) else ""

            if not second:
                pairs.append(first + self.filler_for(first))
                i += 1
            elif first == second:
                pairs.append(first + self.filler_for(first))
                i += 1
            else:
                pairs.append(first + second)
                i += 2

        return pairs

    def filler_for(self, char):
        return "Q" if char == "X" else "X"

    def encrypt_pair(self, pair):
        pos1 = self.find_position(pair[0])
        pos2 = self.find_position(pair[1])

        if pos1[0] == pos2[0]:
            return (
                self.matrix[pos1[0]][(pos1[1] + 1) % 5]
                + self.matrix[pos2[0]][(pos2[1] + 1) % 5]
            )
        if pos1[1] == pos2[1]:
            return (
                self.matrix[(pos1[0] + 1) % 5][pos1[1]]
                + self.matrix[(pos2[0] + 1) % 5][pos2[1]]
            )
        return self.matrix[pos1[0]][pos2[1]] + self.matrix[pos2[0]][pos1[1]]

    def decrypt_pair(self, pair):
        pos1 = self.find_position(pair[0])
        pos2 = self.find_position(pair[1])

        if pos1[0] == pos2[0]:
            return (
                self.matrix[pos1[0]][(pos1[1] - 1) % 5]
                + self.matrix[pos2[0]][(pos2[1] - 1) % 5]
            )
        if pos1[1] == pos2[1]:
            return (
                self.matrix[(pos1[0] - 1) % 5][pos1[1]]
                + self.matrix[(pos2[0] - 1) % 5][pos2[1]]
            )
        return self.matrix[pos1[0]][pos2[1]] + self.matrix[pos2[0]][pos1[1]]

    def remove_padding(self, text):
        cleaned_text = []
        i = 0

        while i < len(text):
            if (
                i + 2 < len(text)
                and text[i] == text[i + 2]
                and text[i + 1] == self.filler_for(text[i])
            ):
                cleaned_text.append(text[i])
                i += 2
            else:
                cleaned_text.append(text[i])
                i += 1

        if cleaned_text and cleaned_text[-1] in ("X", "Q"):
            cleaned_text.pop()

        return "".join(cleaned_text)

    def find_position(self, char):
        for row_index, row in enumerate(self.matrix):
            if char in row:
                return row_index, row.index(char)
        raise ValueError(f"Character {char!r} not found in Playfair matrix")
