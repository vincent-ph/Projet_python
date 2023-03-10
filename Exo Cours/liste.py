liste = [17, 38, 10, 25, 72]

liste.sort()
print(liste)

liste.append(12)
print(liste)

liste.reverse()
print(liste)

indice = liste.index(17)
print(indice)

liste.remove(38)
print(liste)

sous_liste1 = liste[1:3]
print(sous_liste1)

sous_liste2 = liste[:2]
print(sous_liste2)

sous_liste3 = liste[2:]
print(sous_liste3)

sous_liste4 = liste[:]
print(sous_liste4)

message = "bonjour"
message_inverse = message[::-1]
if message == message_inverse:
    print("C'est un palindrome")