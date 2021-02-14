"""
Écrivez un programme qui affiche la suite de symboles suivante :
*
**
***
****
*****
******
*******
"""

count, star = 1, "*"

while count <= 7:
    print(star)
    star += "*"
    count += 1