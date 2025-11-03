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
        self.waiting: Person = []
    
    def __str__(self):
        return f"Caixas: [{self.counters}]\Espera: [{self.waiting}]"
    
    def arrive(slef, person: Person):


    def call(self, index: int):

    def finish(index:int): Person | None
    

def main():
    mercado = Market()
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
#