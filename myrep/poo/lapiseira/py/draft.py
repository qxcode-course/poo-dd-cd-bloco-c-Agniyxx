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
        return "{self.__dureza},{self.__calibre},{self.__tamanho}"

class Lapiseira:
    def __init__(self, calibre: float = 0):
        self.calibre = calibre
        self.tambor: list[int] = None
        self.bico = []

    def inserir(self):
        if self.get_grafite() != self.get_calibre():
            print("fail: grafite não compativel")

    def puxar(self):
        if self.bico is not None: 
            print(" fail: primeiro remova o outro grafite")

    def remover(self):
        return self.bico 
    
    def escrever_folha(self):
        if self.grafite is None:
            print("fail: o bico está vazio")
            return
        if self.grafite 

    def __str__(self):
        return f"Calibre: {self.calibre}, bico: {self.bico}, tambor: {self.tambor}"
    
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
        if args[0] == "init":
            calibre = args[1]
            bico = args[2]
            tambor = args[3]
            lapiseira = Lapiseira(bico, tambor)
        
main()