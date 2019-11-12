def afficher(tete):
    print ("======= MA LISTE ========")
    courant = tete
    while not courant == None:
        print (courant.value, " / ", end="")
        courant = courant.next
    print()



class Noeud():
  def __init__(self,value):
      self.value = value
      self.next = None

n1 = Noeud("tete de noeud")
n2 = Noeud(5)
n3 = Noeud(-2.5)

n1.next = n2
n2.next = n3

afficher(n1)
afficher(n2)
afficher(n3)
