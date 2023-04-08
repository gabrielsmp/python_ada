# > LISTAS

# Antes

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com Lista

notas = [7.9, 9.7, 8.2]

# Criando Listas

lista = []
lista = list()
lista = [26, 'gabriel', 1.68, True]
lista_de_listas = [22, [1, 2, 3]]



# Indexação e Slices (fatiamento)

lista = [10, 'gabriel', 1.68, False]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])


# Slices 

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

# > Interação com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)
    
# 2. Utilizando índices

print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])
    



# > MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]


# append

print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)

# insert

lista.insert(2, 10)

print('Depois do insert: ', lista)

# extend

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend: ', lista)

# pop

lista.pop()

print('Lista após o pop: ', lista)

lista.pop(0)

print('Lista após o pop:', lista)

# remove

lista.remove(3)

print('Depois do remove: ', lista)


# count

print('Quantidade de 2 na lista: ', lista.count(2))

# index 

print('índice do elemento 12: ', lista.index(12))

# sort

lista.sort(reverse=True)

print(lista)

# > FUNÇÕES PARA  LISTAS

# len

print(len(lista))

# sum

print(sum(lista))

# max

print('Maior elemento da lista: ', max(lista))

# min

print('Menor elemento da lista: ', min(lista))