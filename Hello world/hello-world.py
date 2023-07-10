print('hello world')

# -----------------------------

a = 10  # int
b = 20.0  # float
c = 'caine'  # string
d = '10'  # string

lista = [a, b, c, d]

print(lista)

print(a + b)
print(c + d)

# --------------------------------
#               0  1   2   3  4  5  6  7      indecsi
lista_numere = [1, 19, 10, 2, 3, 4, 7, 12]
print(max(lista_numere))
print(min(lista_numere))

print(lista_numere[1])  # 19
lista_numere.sort()  # [1, 2, 3, 4, 7, 10, 12, 19]
print(lista_numere)
print(lista_numere[1])  # 2

print(lista_numere.pop())  # 19
print(lista_numere)  # [1, 2, 3, 4, 7, 10, 12]

# ----------------------------------------

a = 10
b = 20
if a > b:
    print('a mai mare decat b')
    print('caca')
    print('pipi')
else:
    print('b mai mare decat a')

for i in range(10):
    print(i)
