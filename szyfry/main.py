class Data:
    data: object

    def __init__(self, data, cipher):
        self.data = data
        self.cipher = cipher
        self.encoded = False
        if self.cipher in ["caesars", "atbash"]:
            if self.cipher == "caesars":
                self.data = self.caesars_cipher_encode()
            else:
                self.data = self.atbash_cipher_encode()

    def caesars_cipher_encode(self):
        result = ""
        if self.encoded:
            return self.data
        alphabet = "xyzabcdefghijklmnopqrstuvwxyz"
        for i in range(len(self.data)):
            char = self.data[i]
            char = char.lower()
            try:
                idx = alphabet.index(char)
            except ValueError:
                result += " "
            else:
                result += alphabet[idx - 3]
        self.encoded = True
        return result

    def atbash_cipher_encode(self):
        result = ""
        if self.encoded:
            return self.data
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        reverse_alphabet = alphabet[::-1]
        for i in range(len(self.data)):
            char = self.data[i]
            char = char.lower()
            try:
                idx = alphabet.index(char)
            except ValueError:
                result += " "
            else:
                result += reverse_alphabet[idx]
        self.encoded = True
        return result

    def caesars_cipher_decode(self):
        result = ""
        if not self.encoded:
            return self.data
        for i in range(len(self.data)):
            ch = self.data[i]
            ch = ch.lower()
            if ch == " ":
                result += " "
            else:
                result += chr((ord(ch) + 3 - 97) % 26 + 97)
        self.encoded = False
        self.data = result
        return result

    def atbash_decode(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        atbash_map = {alphabet[i]: alphabet[25 - i] for i in range(26)}
        if not self.encoded:
            return self.data
        result = ''
        for char in self.data:
            if char.lower() in alphabet:
                result += atbash_map[char.lower()]
            else:
                result += " "
        self.encoded = False
        self.data = result
        return result


def main():
    dane = Data("sprawdzam czemu to nie jest jak ma byc", "atbash")
    print(dane.data)
    dane.caesars_cipher_decode()
    print(dane.data)


if __name__ == '__main__':
    main()


