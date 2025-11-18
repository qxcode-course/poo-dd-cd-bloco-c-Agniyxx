class Person:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name}"

class Market:
    def __init__(self, num_counters: int):
        self.counters: Person | None = ["-----"] * num_counters
        
        self.waiting: list[Person]= []
    
    def __str__(self):
        counters_str = ", ".join(str(i) if i is not None else "-----" for i in self.counters)
        waiting_str = ", ".join(str(i) for i in self.waiting)
        return f"Caixas: [{counters_str}]\nEspera: [{waiting_str}]"
    
    def arrive(self, person: Person):
        self.waiting.append(person)

    def call(self, index: int):
        if index < 0: 
            print("fail: caixa inexistente")
            return
        if index >= len(self.counters):
            print(" ")
            return
        if self.counters[index] is not None:
            print("fail: caixa {index} ocupado")
            return
        if not self.waiting:
            print("fail: sem cliente na fila de espera")
            return
        client = self.waiting.pop(0)
        self.counters[index] = client

    def finish(self, index: int):
        if index < 0 or index >= len(self.counters):
            print("fail: caixa inexistente")
            return
        person_leave = self.counters[index]
        if person_leave is None:
            print("fail: caixa vazuo")
            return
        self.counters[index] = None

def main():
    mercado = Market(0)
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(mercado)
        elif args[0] == "init":
            num_counters = int(args[1])
            mercado = Market(num_counters)
        elif args[0] == "arrive":
            name = args[1]
            mercado.arrive(Person(name))
        elif args[0] == "call":
            index = args[1]
            mercado.call(index)
        elif args[0] == "finish":
            index = args[1]
            mercado.finish(index)
            
main()

#
#join contrariio do split 
