import heapq
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
    
    def __lt__(self, other):
        return self.__idade > -other.__idade

class Trampoline: 
    def __init__(self, counter: int = 0):
        self.playing: list[Kid] = []
        self.waiting: list[Kid] = []
        self.counter = counter

    def arrive(self, kid: Kid):
        heapq.heappush(self.waiting, kid)

    def enter(self):
        if not self.waiting:
            print("fail: ninguem na fila de espera")
            return
        kid = heapq.heappop(self.waiting)
        self.playing.append(kid)

    def leave(self):
        if not self.playing:
            print("fail: ninguem no pula-pula")
            return
        kid = self.playing.pop(0)
        heapq.heappush(self.waiting, kid)

    def removeKid(self, name: str): 
        for i, kid in enumerate(self.playing):
            if kid.get_name() == name:
                self.playing.pop(i)
                return
                
        temp_list = []
        found = False
        
        for kid in self.waiting:
            if kid.get_name() == name:
                found = True
            else:
                temp_list.append(kid)
                
        if found:
            self.waiting = temp_list  
            heapq.heapify(self.waiting)
            return     
        print(f"fail: {name} não esta no pula-pula")
        heapq.heappush(self.waiting, temp_list)
    
    def __str__(self):
        waiting_sorted = sorted(self.waiting, reverse=True)
        waiting_str = ", ".join(str(kid) for kid in waiting_sorted)
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