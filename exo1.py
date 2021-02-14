"""Exercice 2.4 Soient trois variables a , b et c (supposées du même type). Écrire les instruc-
tions permutant leurs valeurs, de sorte que la valeur de b passe dans a , celle de c dans b et
celle de a dans c . On utilisera une (et une seule) variable supplémentaire nommée d ."""

a = 1
b = 2
c = 3
print(["a", a], ["b", b], ["c", c])

d = a

a = b
b = c
c = d
print(["a", a], ["b", b], ["c", c])

"""
Exercice 2.5 En supposant que les variables n , p et q sont de type entier et qu’elles contiennent respectivement les valeurs 8, 13 et 29, déterminer les valeurs des expressions suivantes :"""

n, p, q = 8, 13, 29
print(n, p, q)
n + p / q # 8.44
n + q / p # 10.23
(n + q) / p #  2.84
n + p / n + p # 22.62
(n + p) / (n + p) #1
