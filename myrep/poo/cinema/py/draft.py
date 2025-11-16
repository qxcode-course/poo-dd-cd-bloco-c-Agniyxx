class Client:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone

    def getPhone(self):
        return self.__phone
    def setPhone(self, phone: int):
        self.__phone = phone
    def getId(self):
        return self.__id

    def __str__(self):
        return f"{self.__id}:{self.__phone}"
        
class Theater:
    def __init__(self, capacity: int = 0):
        self.capacity = capacity
        self.seats: list[Client] = [None] * capacity

    def __search__(self, client_id: str):
        for i, client_ in enumerate (self.seats):
            if client_ is not None and client_.get_id() == client_id:
                return i
        return -1
        
    def reserve(self, id: str, phone: int, index: int):
        if index < 0 or index >= self.capacity:
            print("fail: assento inessistente")
            return
        if self.seats[index] is not None:
            print("fail: cadeira ocupada")
            return
        if self.__search__(id) != -1:
            print("fail: cliente ja esta reservado")
            return
        self.seats[index] = Client(id, phone)

    def cancel(self, client_id: str):
        index = self.__search__(client_id)
        if index == -1:
            print("fail: clite não esta no cinema")
            return
        self.seats[index] = None

    def getSeats(self):
        return self.seats

    def __str__(self):
        seats_str = " ".join(str(i) if i is not None else "-" for i in self.seats)
        return f"[{seats_str}]"

def main():
    cinema = Theater()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(cinema)
        elif args[0] == "init":
            capacity = int(args[1])
            cinema = Theater(capacity)
        elif args[0] == "reserve":
            client_id = args[1]
            phone = int(args[2])
            index = int(args[3])
            cinema.reserve(client_id, phone, index)
        elif args[0] == "cancel":
            client_id = args[1]
            cinema.cancel(client_id)


main()