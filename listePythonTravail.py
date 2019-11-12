def afficher(tete):
    courant = tete
    print ("=====MA Liste=====")
    while courant != None:
        print (courant.valeur, end="/")
        courant = courant.suivant
    print()

def AjoutDebut(tete, valeur):
    new = Noeud(valeur)
    new.suivant = tete
    return new

def AjoutPos(tete, valeur,pos):
    courant = tete
    for i in range(pos-1):
        courant = courant.suivant

    new = Noeud(valeur)
    new.suivant = courant.suivant
    courant.suivant = new

    if pos == 0 or tete==None:
        return new
    return tete


def append(tete, valeur):
    courant = tete
    if tete != None:
        while courant.suivant != None:
            courant = courant.suivant

        new = Noeud(valeur)
        courant.suivant = new
        return tete
    else :
        new = Noeud(valeur)
        return new


class Noeud():
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None


tete = None
tete = append(tete, "tete de noeud")
tete = append(tete, 5)
tete = append(tete, -2.5)
tete = append(tete, "petit dernier")

tete = AjoutDebut(tete, "youhou")
afficher(tete)

tete = AjoutPos(tete, "moi",2)

tete = AjoutPos(tete, "biten",0)

afficher(tete)
