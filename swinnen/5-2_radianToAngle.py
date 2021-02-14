"""
Écrivez un programme qui convertisse en degrés, minutes, secondes un angle fourni au départ en radians.
"""

# Conversion degrés -> radians
# Rappel : un angle de 1 radian est un angle qui correspond à une portion
# de circonférence de longueur égale à celle du rayon.
# Puisque la circonférence vaut 2 pi R, un angle de 1 radian correspond
# à 360° / 2 pi , ou encore à 180° / pi

# Angle fourni au départ en radian :
resultRad = 0.5625244660546206

# Valeur de pi :
pi = 3.14159265359

# Valeur d'un radian en degrés :
rad = 180 / pi

# Calcul de l'angle :
#resultRad = angle / rad
angle = resultRad * rad
print("\n", resultRad, "radian(s) est égal à", end = " ")
minutes,seconds = divmod(angle*3600,60)
degrees,minutes = divmod(minutes,60)
print(round(degrees),"°", round(minutes), "\'", round(seconds), "\"")

"""
def decdeg2dms(dd):
    negative = dd < 0
    dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60)
    degrees,minutes = divmod(minutes,60)
    if negative:
        if degrees > 0:
            degrees = -degrees
        elif minutes > 0:
            minutes = -minutes
        else:
            seconds = -seconds
    return (round(degrees), round(minutes), round(seconds))

print(decdeg2dms(65.56))
"""