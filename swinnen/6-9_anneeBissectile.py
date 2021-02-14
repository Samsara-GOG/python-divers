"""
6.9 
Déterminer si une année (dont le millésime est introduit par l’utilisateur) est bissextile ou non.
Une année A est bissextile si A est divisible par 4. Elle ne l’est cependant pas si A est un
multiple de 100, à moins que A ne soit multiple de 400."""

print("Détermination si une année est bissextile ou non")
print("Veuillez entrée une année (ex: 1999)")
a = eval(input())

if (a % 4 == 0) and ((a % 100 != 0) or (a % 400 == 0)):
    print(a, "est une année bissextile.")
else:
    print(a, "n'est pas une année bissextile.")