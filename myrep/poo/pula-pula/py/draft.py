class Kid:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade
        
    def get_name(self):
        return self.__nome

    def get_age(self):
        return self.__idade
    
    def set_name(self):
        return self.__nome
    
    def set_age(self):
        return self.__idade
    
    def __str__(self):
        return f"{self.__nome},{self.__idade}"

class Trampoline: 
    def __init__(self, counter: int):
        self.playing: Kid | None = []
        for _ in range(counter):
            self.playing = None
        self.waiting: Kid | None = []

    def arrive(self, kid: Kid):
        self.playing.append(self.waiting)

    def enter(self):

    def leave(self):

    def removeKid(self, name: str): Kid | None
        

    def __str__(self):
        return f"{self.playing} => {self.waiting}"

def main():
    pula_pula = Trampoline(0)
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print(pula_pula)
        if args[0] == "enter":

        if args[0] == "arrive":
            pula_pula.arrive(Kid)

main()