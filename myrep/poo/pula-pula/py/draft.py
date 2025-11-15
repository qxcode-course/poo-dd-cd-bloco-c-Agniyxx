class Kid:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade
        
    def get_name(self):
        return self.__nome

    def get_age(self):
        return self.__idade
    
    def __str__(self):
        return f"{self.__nome}:{self.__idade}"

class Trampoline: 
    def __init__(self, counter: int = 0):
        self.playing: list[Kid] = []
        self.waiting: list[Kid] = []
        self.count = counter

    def arrive(self, kid: Kid):
        self.waiting.insert(0, kid)

    def enter(self):
        if not self.waiting:
            print("fail: ninguem na fila de espera")
            return
        kid = self.waiting.pop(0)
        self.playing.append(kid)

    def leave(self):
        if not self.playing:
            print("fail: ninguem no pula-pula")
            return
        kid = self.playing.pop(0)
        self.waiting.append(kid)


    def removeKid(self, name: str): 
        for lista in [self.waiting, self.playing]:
            for i, kid in enumerate(lista):
                if kid.get_name() == name:
                    lista.pop(i)
                    return     
        print(f"fail: {name} não encontrado")
    
    def __str__(self):
        waiting_str = ", ".join(str(kid) for kid in self.waiting)
        playing_str = ", ".join(str(kid) for kid in self.playing)
        return f"[{waiting_str}] => [{playing_str}]"

def main():
    pula_pula = Trampoline(0)
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pula_pula)
        elif args[0] == "arrive":
            nome = args[1]
            idade = int(args[2])
            pula_pula.arrive(Kid(nome, idade))
        elif args[0] == "enter":
            pula_pula.enter()
        elif args[0] =="leave":
            pula_pula.leave()
        elif args[0] =="remove":
            nome = args[1]
            pula_pula.removeKid(nome)

main()