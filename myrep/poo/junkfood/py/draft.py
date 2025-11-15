
class Slot: 
    def __init__(self):
        self.__nome: str = "empty"
        self.__qtd: int = 0
        self.__preço: int = 0.0 

    def get_nome(self):
        return self.__nome
    def get_qtd(self):
        return self.__qtd
    def get_preço(self):
        return self.__preço
    def set_name(self):
        return self.__nome = nome
    def set_qtd(self):
        return self.__qtd = qtd
    def set_preço(self):
        return self.__preço = preço

    def __str__(self):
        return f"[   empty : 0 U : 0.00 RS]"
    
class Machine:
    def __init__(self, slot: Slot):
        self.slot = slot
