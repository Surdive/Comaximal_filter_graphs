from Filters_in_RL import est_filtre
from Set_filters import subsets_with_n
from attributes import prelinear
from attributes import divisible
from attributes import involutive
from attributes import idempotent
from prog import DataStore

def liste_filtres(t,l,n):
    f=[]
    for i in range(len(t)):
        h = []
        for x in subsets_with_n(n):
            if est_filtre(l, t[i]._leq, t[i]._mult, x):
             h.append(x)
        f.append(h)

    return f


ds = DataStore()
it=ds.residuated_lattices(10)
a=list(it)
l=[0,1,2,3,4,5,6,7,9]

T=[x for x in a if prelinear(x)==True]
#H = [x for x in subsets_with_n(5) if est_filtre(l, T[0]._leq, T[0]._mult, x) == True]
#print(len(t))
#print(liste_filtres(T,l,5))
#print(len(liste_filtres(T,l,5)))
#print(liste_filtres(T,l,5)[0])

def filtrer_elements(L):
    sous_liste_resultat = []

    # Parcourir chaque élément de L (chaque élément est une liste de listes)
    for element in L:

        # Vérifier qu'il y a au moins deux éléments dans cette sous-liste (pour avoir un avant-dernier élément)
        if len(element) < 2:
            continue  # Si l'élément n'a pas d'avant-dernier élément, on le passe

        # L'avant-dernier élément de la liste de listes
        avant_dernier = element[-2]

        # Vérifier qu'il existe une sous-liste dans cet élément pour laquelle
        # il existe une sous-liste qui n'est pas un sous-ensemble de l'avant-dernier élément
        condition_satisfaite = True
        for sub_liste in element[:-1]:
            if not is_subset(sub_liste, avant_dernier):
                # Si la sous-liste n'est pas un sous-ensemble de l'avant-dernier, on continue
                condition_satisfaite = True
                print(T[L.index(element)]._leq)
                print(T[L.index(element)]._mult)
                break
        else:
            condition_satisfaite = False

        if condition_satisfaite:
            sous_liste_resultat.append(element)

    return sous_liste_resultat


def is_subset(sub_liste, liste):
    """Vérifie si une sous-liste est un sous-ensemble de la liste donnée."""
    return all(item in liste for item in sub_liste)


# Exemple d'utilisation
#L = [
 #   [[1, 2], [3, 4], [5, 6]],  # Premier élément
  #  [[7, 8], [9, 10], [1, 2]],  # Deuxième élément
  #  [[11, 12], [13, 14], [15, 16]],  # Troisième élément
   # [[1, 2], [3, 4]]  # Quatrième élément
#]

# Appel de la fonction
resultat = filtrer_elements(liste_filtres(T,l,9))

# Affichage du résultat
print(resultat)
print(len(resultat))
