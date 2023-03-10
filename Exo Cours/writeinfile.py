x = int(input("Veuillez saisir un nombre: "))

with open("data.txt", "w") as f:
    for i in range(x):
        chaine = input("Veuillez saisir une chaine de caractères: ")
        f.write(chaine + "\n")

with open("data.txt", "r") as f:
    lignes = f.readlines()

for ligne in lignes:
    if "@" in ligne and ligne.endswith(".com"):
        print(f"{ligne} est un email valide.")
    else:
        print(f"{ligne} n'est pas un email valide.")