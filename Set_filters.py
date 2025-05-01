import itertools

from Filters_in_RL import est_filtre


def subsets_with_n(n):
    # Création de la liste L = [0, 1, 2, ..., n]
    L = list(range(n + 1))

    # Liste pour stocker les sous-ensembles contenant n
    result = []

    # Parcourir toutes les tailles possibles de sous-ensembles (de 0 à len(L))
    for r in range(len(L) + 1):
        # Obtenir tous les sous-ensembles de taille r
        subsets = itertools.combinations(L, r)

        # Ajouter à result uniquement ceux qui contiennent l'élément n
        for subset in subsets:
            if n in subset:
                result.append(list(subset))

    return result


# Exemple d'utilisation
#n = 3
#result = subsets_with_n(n)
#print(result)
