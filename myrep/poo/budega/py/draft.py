class Person:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name}"

class Market:
    def __init__(self, counters: list, waiting: str):
        self.counters = [None] 
        self.waiting = waiting
    
    def __str__(self):
        return f"Caixas: [{self.counters}]\Espera: [{self.waiting}]"
    

def main():
    mercado = Market(0, "")
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