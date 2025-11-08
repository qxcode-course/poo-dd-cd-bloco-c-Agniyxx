class Grafite:
    def __init__(self, dureza: str, calibre: float, tamanho__mm: int):
        self.__dureza = dureza
        self.__calibre = calibre
        self.__tamanho_mm = tamanho__mm

    def get_dureza(self):
        return self.__dureza
    def get_calibre(self):
        return self.__calibre
    def get_tamanho(self):
        return self.__tamanho_mm

    def __str__(self):
        return f"{self.__dureza}mm,{self.__calibre}, {self.__tamanho}mm"

class Lapiseira:
    def __init__(self, calibre: float = 0):
        self.calibre = calibre
        self.tambor: list[int] = None
        self.bico = []

    def inserir(self):
        if self.get_grafite() =! self.:

    def __str__(self):
        return f" "
    
def main():
    while True:
        lapiseira = Lapiseira()
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print(lapiseira)
        

