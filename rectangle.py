class rectangle1() :
    def __init__(self):
         self.longeur=0
         self.largeur=0

    #def __init__(self,longeur,largeur):
        #self.longeur = longeur
        #self.largeur = largeur

    def __init__(self,yahya):
        self.longeur = yahya.longeur
        self.largeur = yahya.largeu

    def perimetre(self):
        return 2 * (self.longeur+self.largeur)

    def aire(self):
        return self.longeur * self.largeur

    def iscarre(self):
        if self.longeur == self.largeur:
           return "il sagit diun carre"
        else:
           return "il ne sagit pas dun carre"

    def afficherrectangle(self):
        print("longueur:",self.longeur)
        print("largeur:",self.largeur)
        print("perimetre:",self.perimetre())
        print("aire:",self.aire())
        print("iscarre:",self.iscarre())