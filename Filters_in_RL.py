def est_filtre(L, I, M, F):
    """
    Vérifie si F est un filtre de L dans un treillis résidué (avec min et max comme opérations)

    L : liste d'entiers de 0 à n
    F : sous-ensemble de L (filtre)
    """

    # Vérifier que F est bien un sous-ensemble de L
    for f in F:
        if f not in L:
            return False  # Si un élément de F n'est pas dans L, ce n'est pas un filtre

    # Vérification de la fermeture sous l'opération inférieure (rencontre, min)
    for x in F:
        for y in F:
            # Vérifier que la rencontre (min) de x et y est dans F
            if M[x][y] not in F:
                return False

    # Vérification de la condition d'inclusion : Si x dans F, alors tous les éléments supérieurs à x dans F
    for x in F:
        for l in L:
            if I[x][l]==1 and l not in F:
                return False  # Si un élément supérieur à x n'est pas dans F, ce n'est pas un filtre

    return True  # Si toutes les conditions sont respectées, F est un filtre de L


# Exemple d'utilisation :

L = [0, 1, 2]
I=[[1,1,1],[0,1,1],[0,0,1]]
M=[[0,0,0],[0,1,1],[0,1,2]]
F = [1, 2]

# Vérification si F est un filtre de L
resultat = est_filtre(L, I, M, F)
print(resultat)  # Cela retournera 'True' si F est un filtre, sinon 'False'
