class Client:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__id = phone

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
        self.seats: list[Client] = [] * capacity

    def __search__(self, nome: str):
        for i, in range (len(Client)) (self.seats, start=1):
            if Client is not None and Client.get_id() == nome:
                return i
            return -1
        
    def __verifyIdex__(self, index: int):
        if index < 0:
            raise ValueError

    def reserve(self, id: str, phone: int, index: int):
        if self.seats[index] != None:
            print("fail: cadeira ocupada")
            return
        if self.__search__(id) != -1:
            raise ValueError
        self.seats[index] = Client(id, phone)

    def cancel(self, id: str):
        self.__search__(id)

    def getSeats(self):
        return self.seats

    def __str__(self):
        return f"[]"

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
            id = args[1]
            phone = args[2]
            cinema = Theater(id, phone)
        elif args[0] == "reserve":
            cinema.reserve()
        elif args[0] == "cancel":
            cinema.cancel()

main()