"""
6.1
Écrivez un programme qui convertisse en mètres par seconde et en km/h une vitesse fournie
par l’utilisateur en miles/heure. (Rappel : 1 mile = 1609 mètres)
"""

oneMile = 1609
print("Veuillez entrer une vitesse mph (Miles per hour) pour la conversion en Km/h et en m/s :")
speedMileRaw = input()
speedMph = float(speedMileRaw)
speedKmph = speedMph * 1.609
speedMps = speedMph * oneMile/3600
print("La vitesse de %.2f" %speedMph, "mph vaut %.2f" %speedKmph, "km/h et %.2f" %speedMps, "m/s.")

