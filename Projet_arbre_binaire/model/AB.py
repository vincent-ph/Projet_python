class AB:
    def __init__(self, root=None, left=None, right=None):
        if root is None:
            self.root = [None]
        else:
            self.root = [root]
        self.left = left
        self.right = right

    def set_root(self, root):
        self.root = root

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.root)
        else:
            return str(self.left) + str(self.root) + str(self.right)

    def estVide(self):
        return self.root == [None]

    def taille(self):
        if self.estVide():
            return 0
        else:
            size_left = 0
            size_right = 0
            if self.left is not None:
                size_left = self.left.taille()
            if self.right is not None:
                size_right = self.right.taille()
        return 1 + size_left + size_right

    def prefixe(self):
        prefixe = ""
        prefixe += str(self.root)
        if self.left is not None:
            prefixe += str(self.left.prefixe())
        if self.right is not None:
            prefixe += str(self.right.prefixe())
        return prefixe

    def postfixe(self):
        postfixe = ""
        if self.left is not None:
            postfixe += str(self.left.postfixe())
        if self.right is not None:
            postfixe += str(self.right.postfixe())
        postfixe += str(self.root)
        return postfixe

    def infixe(self):
        infixe = ""
        if self.left is not None:
            infixe += str(self.left.infixe())
        infixe += str(self.root)
        if self.right is not None:
            infixe += str(self.right.infixe())
        return infixe

    def hauteur(self):
        if self.estVide():
            return -1
        else:
            hauteur_left = -1
            hauteur_right = -1
            if self.left is not None:
                hauteur_left = self.left.hauteur()
            if self.right is not None:
                hauteur_right = self.right.hauteur()
            return 1 + max(hauteur_left, hauteur_right)

    def estABR(self):
        if self.estVide():
            return True
        if self.left is not None and self.left.root[0] is not None and self.root[0] > self.left.root[0]:
            return True
        if self.right is not None and self.right.root[0] is not None and self.root[0] < self.right.root[0]:
            return True
        if self.left is not None and self.left.root is not None and self.left.estABR():
            return True
        if self.right is not None and self.right.root is not None and self.right.estABR():
            return True
        return False

    def estEquilibre(self):
        if self.estVide():
            return True
        hauteur_left = -1
        hauteur_right = -1
        if self.left is not None:
            hauteur_left = self.left.hauteur()
        if self.right is not None:
            hauteur_right = self.right.hauteur()
        delta = abs(hauteur_left - hauteur_right)
        if delta > 1 or delta < -1 and not self.left.estEquilibre() and not self.right.estEquilibre():
            return False
        return True

    """
    Pivot     = Racine→CO
    Racine→CO = Pivot→CR
    Pivot→CR  = Racine
    Racine    = Pivot
    """

    def rotD(self):
        if self.left is None:
            return self

        pivot = self.left
        self.left = pivot.right
        pivot.right = self
        return pivot

    def rotG(self):
        if self.right is None:
            return self

        pivot = self.right
        self.right = pivot.left
        pivot.left = self
        return pivot
