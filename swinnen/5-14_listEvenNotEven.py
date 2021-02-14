"""5.14 
Écrivez un programme qui analyse un par un tous les éléments d’une numbers de nombres (par
exemple celle de l’exercice précédent) pour générer deux nouvelles numberss. L’une contiendra
seulement les nombres pairs de la numbers initiale, et l’autre les nombres impairs. 
Par exemple, si la numbers initiale est celle de l’exercice précédent, le programme devra 
construire une numbers pairs qui contiendra [32, 12, 8, 2] , et une numbers impairs qui contiendra 
[5, 3, 75, 15]. 
Astuce : pensez à utiliser l’opérateur modulo (%) déjà cité précédemment.
"""

numbers = [32, 5, 12, 8, 3, 75, 2, 15]
print("numbers non-triée:", numbers)
even = []
notEven = []

i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even.append(numbers[i])    
    else:
        notEven.append(numbers[i])
    i += 1

print("Nombres pairs:", even)
print("Nombres impairs:", notEven)