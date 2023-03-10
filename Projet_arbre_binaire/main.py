from model.AB import AB

A1 = AB()
print("A1 est vide:", A1.estVide())  # retourne true

A2 = AB(5)
print("A2 est vide:", A2.estVide())  # retourne false

A3 = AB(3)
A2.set_left(A3)
print("A2:", A2)  # retourne [3][5]None

Atest = AB(10, AB(5, AB(3), AB(8)), AB(12))
print("Atest:", Atest)  # retourne [3][5][8][10][12]
print("Atest est vide:", Atest.estVide())  # retourne False
print("Taille Atest", Atest.taille())  # retourne 5
# 10. Methode Atest est récursive

print("Préfixe:" + Atest.prefixe())  # retourne Préfixe:[10][5][3][8][7]
print("Postfixe:" + Atest.postfixe())  # retourne Postfixe:[3][8][5][7][10]
print("Infixe:" + Atest.infixe())  # retourne Infixe:[3][5][8][10][7]
print("Hauteur Atest:", Atest.hauteur())  # retourne 2

A12 = AB(5, AB(3), AB(8))
print("A12:", A12)
print("Hauteur A12", A12.hauteur())
print("Atest est équilibré:", Atest.estABR())
print("ABR:", A12.estABR())
print("Atest est ABR:", Atest.estEquilibre())

A13 = AB(5, AB(3, AB(8)))
print("A13:", A13)
print("A13 est equilibré:", A13.estEquilibre())

A14 = AB(107, AB(), AB(133, AB(), AB(167, AB(151), AB(183))))
print("A14:", A14)
print("A14 est ABR:", A14.estABR())
print("A14 est equilibré:", A14.estEquilibre())

print("A12:", A12)
A15 = A12.rotD()
print("Rotation droite de A12:", A15)
print(A15.root)
A13 = AB(1, AB(2), AB(5))
print("A13:", A13)
A16 = A13.rotG()
print("Rotation gauche de A13:", A16)
print(A16.root)
