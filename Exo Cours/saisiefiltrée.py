valid = False
a = 0
while valid is False:
    a = int(input("Veuillez saisir un nombre entre 1 et 10 : "))
    if a < 1 or a > 10:
        print("Saisie invalide, veuillez réessayer.")
    else:
        valid = True
print("Vous avez saisi le nombre :", a)
