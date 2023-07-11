# ----- Ex 1 -----
print('----- Ex 1 -----')

a = 1
b = 2
c = 12.5
d = 'variabila'
e = False
print(a)
print(b)
print(c)
print(d)
print(e)

# ----- Ex 2 -----
print('----- Ex 2 -----')
print(a + b)
print(a - b)
print(a * b)

# ----- Ex 3 -----
print('----- Ex 3 -----')
if a > b:
    print(a)
else:
    print(b)

# ----- Ex 4 -----
print('----- Ex 4 -----')
if e == True:
    print(d + 'adev vtm')
else:
    print("nu se poate asa ceva")

# ----- Ex 5 -----
print('----- Ex 5 -----')
lista = [34, 62, 13, 53, 21]
print(lista)
lista.sort(reverse=True)
print(lista)
lista.pop(2)
print(lista)

# ----- Ex 6 ----
print('----- Ex 6 -----')
f = 22
lista.append(f)
print(lista)
# BONUS
print('------BONUS-----')
lista.insert(1, 99)

print(lista)
