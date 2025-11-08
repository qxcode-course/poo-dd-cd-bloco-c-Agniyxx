class Foo:
    def __init__(self, num: int):
        self.num = num

    def __str__(self):
        return self.num
    
lista_vazia: list[int] = []
print(lista_vazia)

lista_num: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista_num)
tam_lista_num = len(lista_num)
print(tam_lista_num)
lista_num.insert(0, 0)
print(lista_num)

n = 10
num_aleatorios = list(range(n + 1)) 
print(num_aleatorios)

for i in num_aleatorios:
    range(len(num_aleatorios))
    print(f"indice {i} => {num_aleatorios[i]}")

x = 2
for num in num_aleatorios:
    if num == x:
        print(num)
    elif x not in num_aleatorios:
        print("numero não encontrado")

for num_pares in num_aleatorios:
    if num_pares % 2 == 0:
        print(num_pares)


print()
lista = []
print(lista)

lista.append('agne')
print(lista)

lista.append(8)
print(lista)

lista.append('serra')
print(lista)

tamanho = len(lista)
print(tamanho)

if 8 in lista:
    lista.remove('agne')
    print(lista)

lista.pop()
print(lista)




