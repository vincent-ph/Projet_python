# saisir l'email
email = input("Entrer votre mail ")
valid = False
com = ""
for i in range(len(email)):
    if email[i] == "@":
        for j in range(len(email)-4, len(email)):
            com += email[j]
            if com == ".com":
                valid = True

if valid:
    print("Cette adresse e-mail est valide.")
else:
    print("Cette adresse e-mail n'est pas valide.")