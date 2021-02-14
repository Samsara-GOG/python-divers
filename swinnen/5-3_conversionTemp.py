"""
Écrivez un programme qui convertisse en degrés Celsius une température exprimée au départ
en degrés Fahrenheit, ou l’inverse.
La formule de conversion est : Tf = Tc × 1,8 + 32 
"""
#Conversion de temperature en °F en °C
tempFahr = 68
tempCelcius = (tempFahr - 32) / 1.8
print(tempFahr, "°F est égal à ", tempCelcius, "°C", end = " ")
print ("ou", end = " ")

#Conversion de température en °C en °F
tempCelcius2 = 20
tempFahr2 = tempCelcius2 * 1.8 + 32
print(tempCelcius2, "°C est à égal à", tempFahr2, "°F")