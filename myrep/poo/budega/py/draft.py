class Person:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name}"

class Market:
    def __init__(self, num_counters: int):
        self.counters: Person | None = [] 
        for _ in range(num_counters):
            self.counters = None
        self.waiting: Person |None = []
    
    def __str__(self):
        return f"Caixas: [{self.counters}]\Espera: [{self.waiting}]"
    
    def arrive(self, person: Person):
        self.counters.append(self.waiting)

    def call(self, index: int):
        if self.counters is None:
            print("fail: niguem no caixa")
            return
        if self.waiting is None:
            print("fail: sem cliente")
            return
        else:
            print("fail: caixa ocupado")

    def finish(self, index:int): Person | None
            print("fail: caixa inexistente")
            print("fail: caixa vazio")
        self.counters = Person
        self.counters = None

def main():
    mercado = Market(0)
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print(mercado)
        if args[0] == "init":
            counters = args[1]
            waiting = args[2]
            mercado = Market(counters, waiting)
            
main()

#.append() cria  a lista 
#join contrariio do split 
