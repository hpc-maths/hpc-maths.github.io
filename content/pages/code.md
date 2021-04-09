title: Codes développés

### Samurai

L'objectif principal de Samurai est de fournir une nouvelle structure de données basée sur les intervalles et l'algèbre d'ensembles pour traiter efficacement les méthodes de raffinement de maillage adaptatif basées sur une grille cartésienne. Une telle approche doit être suffisamment polyvalente pour traiter les méthodes AMR et multi-résolution.

La plupart des structures de données existantes utilisées à cette fin sont basées sur la construction d'un arbre (quadtree en 2d ou octree en 3d).

Le principal avantage de l'utilisation d'une structure de données sous forme d'arbre est que l'ajout ou la suppression de noeuds peut être réalisé très rapidement une fois que l'on sait où ils se trouvent ou où les ajouter. Mais la recherche d'un noeud donné dans l'arbre peut prendre beaucoup de temps. Pour améliorer ce temps de recherche, une façon habituelle est d'utiliser une courbe de remplissage de l'espace pour localiser les noeuds de façon linéaire (voir [p4est](https://www.p4est.org/) pour un exemple reposant sur la z-curve - Courbe de Lebesgue en français). Une telle approche peut garantir que le voisinage d'un noeud donné est toujours proche de ce noeud à l'intérieur de la structure de données. Elle est particulièrement importante pour la résolution des EDP utilisant des méthodes numériques telles que les méthodes de volumes finis, d'éléments finis sur le maillage adaptatif.

Cela signifie qu'un opérateur discret faisant intervenir un stencil doit évaluer diverses cellules de voisinage ou potentiellement les reconstruire pour la structure d'arbre, et cela doit être fait rapidement. Afin d'améliorer l'efficacité de l'arbre / remplissage de l'espace, la nouvelle structure de données proposée s'appuie sur la représentation du maillage sous forme d'intervalles à différents niveaux de résolution. La plupart des opérations sur le maillage sont effectuées par des opérations utilisant une algèbre d'ensembles. L'approche vise à combiner trois objectifs:

- améliorer l'efficacité de la manipulation du maillage par rapport à la combinaison construction d'un arbre / courbes de remplissage d'espace,
- découpler l'évolution du maillage des méthodes numériques utilisées pour résoudre les EDP et rendre particulièrement intuitive l'implémentation d'un nouveau schéma,
- introduire une approche qui aura de bonnes propriétés pour le calcul parallèle distribué.

Pour plus d'informations:

- code: <https://github.com/hpc-maths/samurai>
- documentation: <https://hpc-math-samurai.readthedocs.io>

### pylbm

pylbm est un logiciel open source écrit en Python. Il propose une implémentation flexible de la méthode Lattice Boltzmann pour les problèmes 1D/2D/3D et a été créé pour s'adresser à diverses communautés:

- Les mathématiciens : Il offre un environnement très agréable pour tester de nouveaux schémas, comprendre leurs propriétés mathématiques, telles que la stabilité et la consistance, et ouvrir à de nouvelles frontières dans le domaine, telles que le raffinement du maillage, les équations équivalentes...
- Physiciens : pylbm offre un cadre idéal pour mener des expériences numériques pour différents niveaux de modélisation et de schémas, sans avoir à se plonger dans la machinerie mathématique des schémas LBM. Les algorithmes proposés peuvent également permettre d'aller au-delà du premier essai et de réaliser facilement des simulations à grande échelle grâce à sa capacité parallèle.
- Les informaticiens : dans pylbm, la méthode Lattice Boltzmann n'est pas codée en dur. Des outils avancés de génération de code, basés sur un large ensemble de bibliothèques d'algèbre informatique récemment développées, permettent à l'utilisateur d'entrer à un haut niveau la définition du schéma et les conditions aux limites. Le logiciel pylbm génère ensuite le code numérique résultant. Il est donc possible de modifier les noyaux de construction du code pour tester les performances et l'optimisation du code sur différentes architectures (AA pattern et Pull and Push algorithms); le code peut également être généré dans différents langages (C, C++, openCL, ...).

La principale caractéristique de pylbm est sa grande flexibilité en termes de schémas LBM et d'implémentations de code numérique. De plus, il possède d'excellentes capacités parallèles et utilise MPI pour le calcul distribué et openCL pour les GPU.

Le cadre généralisé de d'Humières est utilisé pour décrire les schémas. Il est alors facile de définir votre schéma lattice Boltzmann en fournissant les vitesses, les valeurs d'équilibre et les paramètres de relaxation, ... De plus, vous pouvez avoir plusieurs schémas $D_dQ_q$ pour votre simulation où $d$ est la dimension et $q$ le nombre de vitesses. C'est généralement le cas lorsque vous voulez simuler par exemple des écoulements de fluides thermodynamiques comme dans le cas test de Rayleigh-Benard. Mais vous pouvez également expérimenter de nouveaux types de schémas de lattice Boltzmann comme les schémas vectorisés ou avec des vitesses relatives.

Pour plus d'information:

- code: <https://github.com/pylbm/pylbm>
- documentation: <https://pylbm.readthedocs.io/>