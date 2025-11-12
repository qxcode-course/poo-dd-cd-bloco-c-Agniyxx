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
    def setId(self):
        self.__id = id

    def __str__(self):
        return f"{self.__id}:{self.__phone}"
        
class Theater:
    def __init__(self, capacity: int = 0):
        self.capacity = capacity
        self.seats 
        


def main():
    while True:
        cinema = Theater()
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        if args[0] =="show":
            print(cinema)