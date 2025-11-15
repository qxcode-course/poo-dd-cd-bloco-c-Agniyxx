
class Slot: 
    def __init__(self):
        self.__nome: str = "empty"
        self.__qtd: int = 0
        self.__preço: int = 0.0 

    def get_nome(self):
        return self.__nome
    def get_qtd(self):
        return self.__qtd
    def get_preço(self):
        return self.__preço

    def __str__(self):
        return f"{self.__nome}:{self.__qtd}:{self.__preço}:"
    
class Machine:
    def __init__(self, slot: Slot): #cada espiral é um array
        self.slot = slot
        
  
    def __str__(self):
        return f"[   empty : 0 U : 0.00 RS]" 

def main():
    slot = Slot()
    while True:
        line = input()
        print(f"${line}")
        args = line.split

        if args[0] =="end":
            break
        if args[0] =="show":
            print(slot)
        if args[0] =="init":
            nome = args[1]
            qtd = args[2]
            preço = args[3]
            slot = Slot(nome, qtd, preço)