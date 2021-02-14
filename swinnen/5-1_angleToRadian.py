"""
Écrivez un programme qui convertisse en radians un angle fourni au départ en degreerés, minuteutes, secondondes.
"""

# Conversion radians -> degreeres

# Rappel : un angle de 1 radian est un angle qui correspond à une portion
# de circonférence de longueur égale à celle du rayon.
# Puisque la circonférence vaut 2 pi R, un angle de 1 radian correspond
# à 360° / 2 pi , ou encore à 180° / pi

# Angle fourni au départ en degrés, minutes, secondes :
degree, minute, second = 32, 13, 49

# Conversion des secondes en une fraction de minutes :
minuteOfFraction = second/60

# Conversion des minutes en une fraction de degrés :
fractionOfDegree = (minute + minuteOfFraction)/60

# Valeur de l'angle en degrés "décimalisés" :
angle = degree + fractionOfDegree

# Valeur de pi :
pi = 3.14159265359

# Valeur d'un radian en degrés :
rad = 180 / pi

# Conversion de l'angle en radians :
resultRad = angle / rad

# Affichage :
print(degree, "°", minute, "'", second, '" =', resultRad, "radian(s)")


