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


'''
#LES EXPLICATIONS

## Fonction1

En fait, python ne travaille qu'avec des references des variables (un peu comme des pointeurs)

Au moment de l'appel de la fonction1, la variable tableau du pg principal et la variable tab dans la fonction1, réferencent le meme tableau (c'est un passage par référence)

Quand, dans la fonction1, on fait tab = [0,0,0,0],
tab ne "pointe" plus sur le tableau du pg principal, mais
sur un nouveau tableau ([0,0,0,0])

Mais la variable tableau, elle, est restée "pointée" sur le tableau original. Donc a la sortie de la fonction, on n'a rien changé

## Fonction2

Notez bien que je n'ai jamais, dans cette fonction, de "tab=XXX".
Du coup, tab, en lui meme, ne change pas.

En fait, chaque case de tableau référence une valeur.
Quand on fait tab[1]= -4, la case 1 de tab (et donc de tableau)
arretent de référencer la valeur 2, et "pointent" maintenant sur une case de valeur -4.

Quand on sort de la fonction2, le contenu des cases de tableau
a changé (mais tableau n'a pas changé, il "pointe" toujours la meme zone. Seule la case 1 de tableau ne "pointe" plus sur la meme chose qu'avant)

'''
