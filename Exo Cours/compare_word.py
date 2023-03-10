def main():
    # saisir les mots
    word1 = input("Entrer le premier mot ")
    word2 = input("Entrer le deuxième mot ")

    # comparer les deux mots et retourner le plus peit
    if word1 < word2:
        print(word1, "est le plus petit")
    elif word2 < word1:
        print(word2, "est le plus petit mot")
    else:
        print("Les mots sont identiques")


if __name__ == '__main__':
    main()
