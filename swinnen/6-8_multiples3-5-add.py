"""
6.8
Écrire un programme qui, étant données deux bornes entières a et b, additionne les nombres
multiples de 3 et de 5 compris entre ces bornes. Prendre par exemple a = 0, b = 32 ; le résultat
devrait être alors 0 + 15 + 30 = 45.

Modifier légèrement ce programme pour qu’il additionne les nombres multiples de 3 ou de 5
compris entre les bornes a et b. Avec les bornes 0 et 32, le résultat devrait donc être : 0 + 3 + 5
+ 6 + 9 + 10 + 12 + 15 + 18 + 20 + 21 + 24 + 25 + 27 + 30 = 225.
"""
print("\nTraitement de nombres entiers compris entre deux limites\n")
print("Veuillez entrer la limite inférieure :", end = " ")
a = eval(input())
print("Veuillez entrer la limite supérieure :", end = " ")
b = eval(input())

multiple3And5 = []
addition = 0
i = a
while i <= b:
    if (i % 3 == 0 and i % 5 == 0):
        multiple3And5.append(i)
        addition += i
    i += 1
print(multiple3And5)
print(addition)
