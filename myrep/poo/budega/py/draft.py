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
        counters_str = ", ".join(str(i) if i is None else "vazio" for i in self.counters)
        waiting_str = ", ".join(str(i) for i in self.waiting)
        return f"Caixas: [{counters_str}]\Espera: [{waiting_str}]"
    
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

    def finish(self, index: int):
        if index < 0 or index >= len(self.counters):
            print("fail: caixa inexistente")
            return
        if self.counters[index] is not None:
            print("fail: caixa vazio")
            return
        if not self.waiting:
            print("fail: sem clientes na fila de espera")
        client = self.waiting.pop(0)
        self.counters[index] = client
        print(f"ok: {client.get_name()} foi para o caixa {index}")

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
