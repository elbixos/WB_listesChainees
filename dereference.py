def fonction1(tab):
    tab = [0,0,0]

def fonction2(tab):
    tab[1] = -4


tableau = [1,2,3]
print ("Tableau de depart")
print (tableau)

fonction1(tableau)
print ("Apres passage dans fonction1")
print (tableau)

fonction2(tableau)
print ("Apres passage dans fonction2")
print (tableau)
