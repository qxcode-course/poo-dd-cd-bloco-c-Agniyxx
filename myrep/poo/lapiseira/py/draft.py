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
    
    def set_tamanho(self, tam_novo: int):
        self.__tamanho_mm = tam_novo

    def __str__(self):
        return "{self.__dureza}:{self.__calibre}:{self.__tamanho}mm"

class Lapiseira:
    gastos = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}
    tamanho_min = 10
    def __init__(self, calibre: float = 0.0):
        self.calibre = calibre
        self.tambor: list[Grafite] = []
        self.bico: Grafite | None = None

    def inserir(self, grafite: Grafite):
        if grafite.get_calibre() != self.calibre:
            print("fail: calibre incompativel")
            return
        self.tambor.append(grafite)

    def puxar(self):
        if self.bico is not None: 
            print("fail: primeiro remova o outro grafite")
            return
        if not self.tambor:
            print("fail: não a grafite no tambor")
            return
        self.bico = self.tambor.pop(0)

    def remover(self):
        if self.bico is None:
            print("fail: ")
            self.__bico = None
    
    def escrever_folha(self):
        if self.grafite is None:
            print("fail: o bico está vazio")
        
        
    def pull(self): 
        if self.bico is not None:
            return False
        if not self.tambor:
            return False
        self.bico = self.tambor.pop(0)
        return True

    def __str__(self):
        return f"Calibre: {self.calibre}, bico: {self.bico}, tambor: {self.tambor}"
    
def main():
    lapiseira = Lapiseira()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "init":
            calibre = args[1]
            tambor = args[2]
            bico = args[3]
            lapiseira = Lapiseira(calibre, tambor, bico)
        elif args[0] == "insert":
            lapiseira.inserir()
        elif args[0] == "remove":
            lapiseira.remover()
        elif args[0] == "write":
            lapiseira.escrever_folha()
        elif args[0] == "pull":
            lapiseira.pull()
        
main()