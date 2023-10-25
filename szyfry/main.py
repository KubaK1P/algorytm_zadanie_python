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

    def atbash_cipher_decode(self):
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
    working = True
    lista = []
    print("1. Dodaj do bazy \n2. Usuń z bazy \n3.Odszyfruj \n4.Pokaz baze \n5.Wyjdz")
    while working:
        try:
            choice = int(input("Podaj opcje: "))
        except ValueError:
            print("PodajPrawidłową watrość")
            continue
        if choice == 1:
            dane = str(input("Podaj dane do zaszyfrowania: "))
            szyfr = str(input("Jaki szyfr: "))
            if szyfr == "caesars":
                lista.append(Data(dane, "caesars"))
                print(lista[-1].data)
                continue
            elif szyfr == "atbash":
                lista.append(Data(dane, "atbash"))
                print(lista[-1].data)
                continue
            else:
                print("Podałeś zły szyfr")
                continue
        elif choice == 2:
            idx = int(input("Podaj miejsce do usuniecia: "))
            try:
                lista.pop(idx-1)
                print("Usunięto")
            except IndexError:
                print("Index nie jest w liście")
                continue
        elif choice == 3:
            idx1 = int(input("Podaj miejsce do odszyfrowania: "))
            szyfr1 = str(input("Jaki szyfr: "))
            try:
                if szyfr1 in ["caesars", "atbash"]:
                    if szyfr1 == "caesars":
                        lista[idx1-1].caesars_cipher_decode()
                        print(lista[idx1-1].data)
                    else:
                        lista[idx1-1].atbash_cipher_decode()
                    print(lista[idx1-1].data)
                    continue
            except IndexError:
                print("Index nie w liście")
        elif choice == 4:
            for i in lista:
                print(f'{i.data}', end="\n")
                continue
        elif choice == 5:
            working = False

if __name__ == '__main__':
    main()