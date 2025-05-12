# Comaximal_filter_graphs
In the _subset_ library, the _liste_filtres_ function determines the list of non-local residuated lattices. It therefore takes as input the residuated lattice in question, the list of elements used to construct the residuated lattice, and the number of elements in the residuated lattice, i.e., _liste_filtres_(t, l, n).

To implement this function, we need to import the following libraries:
From _Filters_in_RL_ import _est_filtre_
From _Set_filters_ import _subsets_with_n_
From _attributes_ import _prelinear_
From _attributes_ import _divisible_
From _attributes_ import _involutive_
From _attributes_ import _idempotent_
From _prog_ import _DataStore_

Note that the _attributes.py_ and _prog.py_ libraries come from Jens Kotters' GitHub account (https://github.com/koetters/residuated_lattices).

In the _Filters_in_RL.py_ library, the function _est_filtre.py_ checks whether a subset of the elements of the residuated lattice is a filter.

In the _Set_filters.py_ library, the function _subsets_with_n.py_ generates all the subsets of a given finite ordered set that contain the largest element of the set.

Example

When n = 7, after importing all the listed libraries, execute the following commands based on Jens Kotters code:

ds = DataStore()
it = ds.residuated_lattices(7)
a = list(it)
l = [0, 1, 2, 3, 4, 5, 6]

If we want to obtain all the residuated lattices with 7 elements that are prelinear (i.e., the MTL-algebras), we define the following list:

T = [x for x in a if prelinear(x) == True]

Next, the _filtrer_elements(L)_ function, which takes as input the list of filter elements from T, will return the list of elements from T that have more than one maximal filter.
