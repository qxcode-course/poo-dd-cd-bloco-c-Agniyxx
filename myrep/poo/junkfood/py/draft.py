class Slot: 
    def __init__(self, nome: str = "empty", qtd: int = 0, preço: float = 0.0):
        self.__nome = nome
        self.__qtd = qtd
        self.__preço = preço

    def __str__(self):
        return f"{self.__nome}:{self.__qtd}:{self.__preço:.2f} RS"
    
class Machine:
    def __init__(self, slots: int, capacity: int = 0): 
        self.slots = [Slot for _ in range(slots)]
        self.dinheiro_inserido = 0.0
        self.capacity = capacity
        
    def __str__(self):
        for i, produto in enumerate(self.slots):
            nome_str = " : ".join(str(i) if i is not None else "empty" for i in self.slots)
            qtd_str = " : ".join(str(i) for i in self.qtd)
            preço_str = " : ".join(str(i) for i in self.preço)
            return f"{i}[   {nome_str}{qtd_str}{preço_str} RS]" 
    
    def setSlot(self, index: int, nome: str, qtd: int = 0, preço: float = 0.0):

        self.slots[index] = Slot(nome, qtd, preço)

    def clearSlots(self, index: int):
        if not index <= 0 or index < len(self.slots):
            print("fail: indice invalido")
            return
        self.slots[index] = Slot()

    def insertCash(self):

    def withdrawCash(self):

    def getCash(self):

    def Profit(self):

    def buyItem(self, index: int):


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
            qtd = int(args[2])
        if args[0] == "set":
            nome = args[1]
            qtd = int(args[2])
            preço = int(args[3])
            slot = Slot(nome, qtd, preço)

main()