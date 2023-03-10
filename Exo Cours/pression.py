# declare les variables seuil
pSeuil = 2.3
vSeuil = 7.41

# saisie la pression et le volume
pressure = float(input("Entrer la pression "))
volumeRoom = float(input("Entrer le volume courant de l'enceinte "))

# vérifie les seuils
if pressure > pSeuil and volumeRoom > vSeuil:
    print("Arrêt immédiat !")
elif pressure > pSeuil:
    print("Veuillez augmenter le volume de l'enceinte !")
elif volumeRoom > vSeuil:
    print("veuillez diminuer le volume de l'enceinte !")
else:
    print("Tout va bien !")


