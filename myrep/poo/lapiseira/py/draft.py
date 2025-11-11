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
        return "{self.__dureza}:{self.__calibre}:{self.__tamanho}"

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
            print("fail: primeiro remova o outro grafite")

    def remover(self):
        if self.bico != None:
        
        aux = 
        return self.bico 
    
    def escrever_folha(self):
        if self.grafite is None:
            print("fail: o bico está vazio")
            return
        aux = 

        if self.grafite <= 10:
            print("grafite insuficiente, retire o grafite")
            
    def pull(self): bool



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
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "init":
            calibre = args[1]
            bico = args[2]
            tambor = args[3]
            lapiseira = Lapiseira(bico, tambor)
        elif args[0] == "insert":
            lapiseira.inserir()
        elif args[0] == "remove":
            lapiseira.remover()
        elif args[0] == "write":
            lapiseira.escrever_folha()
        elif args[0] == "pull":
            lapiseira.pull()

        
main()