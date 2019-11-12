#include <stdio.h>

struct Noeud {
  int valeur;
  struct Noeud* suivant;
};

void afficher(struct Noeud *tete){
  printf("====MA LISTE====\n");
  struct Noeud *courant;
  courant = tete;
  while (courant != NULL){
    printf("%d|",courant->valeur);
    courant=courant->suivant;
  }
  printf("\n");
}

int main(void){
  struct Noeud n1;
  n1.valeur = 1;

  struct Noeud *tete = NULL;
  afficher(tete);


  struct Noeud n2;
  n2.valeur = 2;
  n2.suivant = NULL;

  n1.suivant = &n2;

  afficher(&n1);


  return 0;
}
