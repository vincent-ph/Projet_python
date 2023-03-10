import math
def main():

    # saisir un flottant
    x = float(input("Entrer un flottant"))
    # véification si le nombre est positif ou nul
    if x >= 0:
        # calcul racine carrée
        square = math.sqrt(x)
        # affichage de la racine
        print("La racine carrée de", x, "est", square)
    else:
        # affichage du message d'erreur
        print("Erreur : le nombre doit être positif ou nul.")

if __name__ == '__main__':
    main()