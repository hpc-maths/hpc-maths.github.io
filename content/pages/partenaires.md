title: Partenaires

## Lien avec des entreprises : Safran, SpaceX, CENAERO

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec vestibulum erat. Vivamus molestie metus ut laoreet finibus. Nunc ut ex pellentesque, suscipit tortor ut, aliquam lorem. Ut nunc dolor, pretium ut magna non, mollis cursus nisi. Proin egestas commodo ante vitae dictum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis lacinia magna eu metus egestas feugiat. Vestibulum blandit cursus magna. Proin quis augue lorem. Nulla consectetur et felis ac fermentum. Aenean vehicula lorem at tristique bibendum. Nullam sem leo, dictum sed libero id, convallis sodales risus. Vestibulum leo nulla, sodales et bibendum vitae, mattis id augue. Curabitur diam odio, sodales eu tortor sit amet, dignissim consectetur orci.

## NASA / ONERA / IFPEn / CEA

Donec lectus orci, hendrerit eu euismod non, molestie id libero. Vestibulum orci erat, facilisis nec erat in, lobortis consectetur metus. Nullam nunc elit, tristique eu sodales vel, feugiat sed felis. Pellentesque varius erat placerat consequat tristique. Cras sem lorem, malesuada vitae aliquet et, iaculis id tellus. Fusce quis ex vel diam iaculis bibendum. In ac tempus velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec ac justo et felis ultrices commodo. Cras quis nulla at justo sagittis mollis at in arcu. Sed rhoncus ante posuere neque tempor, non venenatis urna consequat. Aenean in metus ut eros dictum gravida sed sit amet ex.


## Partenaires internationaux VKI, UT Austin, ICME, Iowa State University, CTR Stanford, UTIAS

Maecenas vulputate facilisis elit, vitae facilisis urna rhoncus sit amet. Nam dignissim mi nunc, ac suscipit nibh maximus pretium. Integer dapibus, enim sed sodales placerat, neque libero pulvinar massa, id aliquam ligula neque in urna. Sed sed ornare tellus. Duis risus neque, feugiat ac neque ut, venenatis imperdiet diam. Etiam at commodo magna. Curabitur sollicitudin ante vitae mi aliquam accumsan. Nam facilisis, turpis et venenatis mattis, tortor mi vehicula eros, id porta nunc elit vitae velit. Cras sagittis, erat mollis blandit ultrices, eros est egestas leo, non malesuada diam quam eget odio. Nulla tincidunt nec elit eget malesuada. Etiam lacinia auctor sem, eget iaculis ligula pretium at. Donec facilisis gravida ligula, et fringilla odio cursus et. Morbi auctor vehicula feugiat. Quisque sed neque consectetur, dictum massa in, vehicula velit.

## QuantStack

QuantStack est une société basée à Paris et Berlin rassemblant les auteurs et mainteneurs de
logiciels de calcul scientifique Open Source. L'équipe comporte notamment cinq "core
contributors" du projet Jupyter, couvrant les principaux composants de l'écosystème
(JupyterHub, JupyterLab, Voilà, ipywidgets). En plus de Jupyter, le groupe a une grande
expertise en C++ scientifique.

L'initiative HPC@Maths et la société QuantStack ont des niveaux d’expertise dans des domaines très variés
et complémentaires. La collaboration scientifique permet d’enrichir les logiciels open source développés par QuantStack, de mettre à la disposition de la communauté de nouvelles méthodes numériques et de nouveaux algorithmes à la pointe des recherches actuelles, de répondre à des problématiques d’industriels faisant intervenir des mathématiques appliquées, ...

Cette collaboration scientifique s’articule autour des trois axes suivants:

### Logiciel d’algèbre linéaire moderne

Dans la plupart des thématiques abordées pour le CMAP, on retrouve l’utilisation de matrices
dites creuses du fait de la présence de nombreux zéros. Cette structure est liée aux méthodes
de discrétisation utilisées (différences finies, volumes finis, éléments finis, ...) pour représenter
des opérateurs différentiels intervenant dans les EDPs. Il existe différents formats (CSR, LIL,
COO, ...) plus ou moins efficaces selon les opérations effectuées. Une fois que l’on a une
structure de données pour représenter ces matrices, on résout généralement un système
linéaire qui peut être préconditionné. Les méthodes utilisées pour résoudre ces systèmes
peuvent être directes (LU, Cholesky, ...) ou itératives (CG, GMRES, ...). Les problèmes étudiés
peuvent être de grande taille (plusieurs centaines de millions d’inconnues) et il est alorsnécessaire d’avoir un parallélisme très efficace. Un certain nombre de logiciel existe déjà en
algèbre linéaire. Le plus connu est probablement PETSc qui permet d’appeler des librairies
externes implémentant certaines résolutions de système (mumps, superLU, Hypre, ...).
Nous travaillons ensemble sur l’élaboration d’une bibliothèque en algèbre linéaire
qui soit moderne, parallèle et facilement interfaçable avec des solveurs externes, des mailleurs,
des partitionneurs, ... en utilisant la philosophie de xtensor (système d’expressions, évaluation
paresseuse, ...).

Afin de valider l’implémentation, nous nous focaliserons sur les problèmes étudiés au sein du
CMAP.

### Optimisation et paradigme parallèle pour xtensor

La bibliothèque xtensor est de plus en plus utilisé par la communauté et permet réellement de
gagner du temps et de la lisibilité pour les noyaux de calcul. Néanmoins, certaines
implémentations dans xtensor ne sont pas encore très optimisées. C’est le cas par exemple
lorsque l’on écrit des algorithmes faisant intervenir certaines vues. Nous définissons un
certain nombre de benchmarks sur des algorithmes bien connues des mathématiques
appliquées (équation de la chaleur avec des différences finies, ensembles de Julia, problèmes à
N corps, ...) qui serviront de référence.

Le fait que xtensor décrive des expressions mathématiques de manière paresseuse (sans
écrire de boucles) est un réel atout pour les personnes qui débutent et qui ne sont pas
forcément familiers avec la programmation bas niveau comme le C++. Un autre avantage est
que la partie optimisation du noyau de calcul est cachée à l’utilisateur. A partir du graphe
d’exécution, nous pouvons analyser finement et découper le noyau de calcul afin de faire
certaines opérations sur des accélérateurs si ils sont disponibles (GPU par exemple). Nous
pouvons également avoir un parallélisme distribué.

Nous proposons donc ici de réfléchir à des optimisations simples validant l’implémentation des
différentes briques de xtensor, puis de réfléchir à l’élaboration de graphes de tâches et à leur
manipulation afin d’optimiser des noyaux de calcul sur différentes architectures.

### Représentation de données

Une bibliothèque scientifique sera utilisée par la communauté si son interface utilisateur est
simple, si la documentation est bien faite mais également s’il est facile de représenter ses
données. L’utilisation des notebooks Jupyter simplifie grandement la description et la mise en
place d’une expérience ainsi que l’analyse des données recueillies. QuantStack a une grande
expérience dans la création de widgets permettant d’interagir plus facilement avec son calcul.
Néanmoins, la visualisation de grandes masses de données pendant ou après le calcul reste
encore un problème ouvert.

Dans cette collaboration, nous souhaitons d’une part avoir des widgets spécialisés
permettant de visualiser rapidement les données des problèmes mathématiques étudiés
(champs sur une surface, maillage adapté, ...) et ce dans différents langages (Python, Julia,
C++, ...), et d’autres part avoir la possibilité d'interroger en temps réel un calcul HPC effectué
sur un cluster de calcul sans écriture des données sur un disque.

### L'enseignement

Depuis 2017, le département de Mathématiques Appliquées, sous l’impulsion de l’initiative
HPC@Maths, a mis en place une offre de cours allant du Bachelor au Master 2 en passant par
des cours d'amphithéâtre de 2A et des cours plus spécialisés de 3A dans le domaine de
l’analyse numérique et des sciences computationnelles reposant sur une utilisation intensive de
Jupyter. Par ailleurs, en lien avec la communauté des élèves, une journée Jupyter ayant eu un
succès important auprès des élèves a eu lieu en mars 2018, déjà en lien avec Quantstack et la
communauté autour de Jupyter.
L’idée est de profiter de la présente collaboration pour aller plus loin. Trois points sont ici
concernés:

1. Aide à la découverte de Jupyter / Journées Jupyter avec les élèves / Binet Réseau
(prolonger l’idée de la journée de Mars 2018 mais en lien avec les initiatives locale des
départements - Physique/Mécanique/Biologie...),

2. Proposer une initiation à Jupyter et son environnement en début d’année pour les élèves
de 3A et leur faire découvrir l’univers du projet Jupyter,

3. Proposer des stages en lien avec l’initiative et les activités de Quantstack et du présent
projet pour faire le lien avec la communauté des élèves.