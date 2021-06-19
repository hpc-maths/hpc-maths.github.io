title: Enseignement

Un ensemble d'enseignements a été créé afin de former les étudiants au domaine de l'analyse numérique et du HPC dans le but de les amener au plus près des compétences nécessaires à l'innovation dans ce domaine riche et en pleine évolution. 

## MAP412 - Cours de 2A d'ingénieurs
### Introduction à l'Analyse Numérique : des fondements mathématiques à l’expérimentation avec Jupyter

Lorsque l’on souhaite modéliser et simuler un problème réel (qu’il s’agisse de dynamique des populations en écologie, de la croissance tumorale en ingénierie biomédicale, de la dynamique de la combustion dans les nouvelles générations de moteurs fusées – par exemple à SpaceX, de la prédiction des tempêtes solaires et des phénomènes de reconnexion magnétique en physique solaire, de la simulation de la turbulence et de la combustion turbulente en mécanique des fluides) l’ingénieur ou le chercheur en mathématiques appliquées ou en « computational science » doit faire appel à une palette de méthodes numériques qu’il doit savoir analyser mathématiquement, évaluer en termes de qualité et d’efficacité computationnelle et, finalement, implémenter.

Ce cours propose une introduction à l’analyse numérique, partant des fondements mathématiques sur lesquels les méthodes numériques reposent et allant jusqu’à l’implémentation et l’emploi de ces méthodes sur la base de notebooks [Jupyter](https://jupyter.org/) en passant par la compréhension de leur efficacité numérique. Le lien est fait avec les applications afin de comprendre l’étendue de l’utilisation de ce type de méthode d’un point de vue pratique. Les implémentations de ces méthodes dans des bibliothèques numériques existantes sont aussi documentées.

Ce cours est porté par  M. Massot en collaboration avec L. Séries, M. Breden, T. Pichard (CMAP).



## MAP551 - Cours de 3A / Master 1
### Systèmes dynamiques pour la modélisation et la simulation des milieux réactifs multi-échelles

Dans un nombre croissant d’applications scientifiques et industrielles, la modélisation et la simulation numérique jouent un rôle clef pour comprendre et analyser les phénomènes physiques complexes mis en jeu. Un élément commun à ces systèmes énergétiques, spatiaux, biologiques, mécaniques, fluides, etc... tourne autour de la notion de systèmes dynamiques. En mathématiques, un système dynamique est la donnée d’un système et d’une loi décrivant l’évolution de ce système dans le temps. Ces systèmes sont particulièrement multi-échelles, c’est-à-dire qu’ils impliquent une très large variété d’échelles en temps, voire d’espace. Ils posent alors de nombreuses difficultés si l’on veut les analyser et en faire une résolution numérique précise afin de disposer d’outils fiables de prédiction de leur dynamique.

Dans le champ mathématique, l’étude des systèmes dynamiques est un domaine particulièrement riche et passionnant depuis les travaux d’H. Poincaré jusqu’aux travaux plus récents sur les systèmes dynamiques chaotiques en passant par l’étude des points critiques, de leur stabilité et l’analyse des bifurcations qui touche à la géométrie différentielle.

Ce cours a été conçu pour donner une base tant au niveau de la modélisation (compréhension de ce qu’est une hiérarchie de modèles à différentes échelles), que de l’analyse théorique et de l’analyse numérique. Il s’agit de maîtriser un ensemble d’outils et d’être capable de conduire une analyse complète de systèmes dynamiques issus d’un vaste champ d’applications. Nous proposons d’identifier les enjeux en termes mathématiques afin de comprendre et d’analyser la dynamique de ces systèmes en dimension finie, voire d’en proposer une simulation précise, fiable et prédictive.

Nous étudierons des exemples dans de nombreux domaines d’application comme la combustion, la mécanique des fluides, la dynamique des populations, la dynamique chimique non-linéaire, le génie biomédical ou la physique des plasmas, que l’on rassemble sous le vocable de “milieux réactifs" (un milieu impliquant plusieurs “espèces" qui “réagissent" entre elles avec un certain niveau de complexité impliquant un large spectre d’échelles de temps, voire d’espace).

Les domaines sur lesquels le cours donnera une expertise sont : analyse mathématique, schémas numériques pour les systèmes d’équations différentielles, analyse de la stabilité des systèmes - bifurcation, implémentation numérique et bibliothèques de programmes permettant la simulation numérique ou l’analyse de bifurcations. Des applications sur machines permettent une analyse de la dynamique mais aussi une compréhension des schémas numériques à la base d’une simulation précise et robuste, ainsi qu’une ouverture sur les enjeux du calcul haute performance. L’ensemble des petites classes se fait au moyen de notebooks Jupyter, ce qui permet une familiarisation avec les concepts et les méthodes numériques particulièrement efficace, puis d’analyser les résultats en termes des applications. L’ensemble des techniques proposées sera illustré sur des exemples simples mais symptomatiques des enjeux des systèmes complexes rencontrés dans les véritables applications. Un mini-projet permet de mettre en œuvre les notions et méthodes enseignées et de se confronter à des systèmes appliqués dans un large spectre de domaines applicatifs.

Ce cours est porté par M. Massot, M. Breden et L. Séries (CMAP).

 
## MAP586 - Enseignement d'approfondissement de 3A
### Algorithmes et principes de conception logicielle pour les mathématiques appliquées en C++ moderne

La recherche en mathématiques appliquées a connu des avancées majeures ces dernières années grâce à l'évolution rapide des moyens informatiques (GPUs, multi-coeurs, architectures massivement parallèles). Cela implique une adaptation quasi continue des structures de données et des algorithmes afin d’exploiter pleinement les ressources à disposition. Ces évolutions répondent au besoin de simuler et de prédire le comportement de systèmes de plus en plus complexes, au plus proche de la réalité et ce dans de nombreux domaines scientifiques. Ces avancées contribuent également à l’innovation dans le domaine industriel et en particulier dans les PME et les start-up.

Par ailleurs, les logiciels et les infrastructures sur lesquelles ils sont déployés deviennent de plus en plus stratégiques pour les entreprises et les laboratoires de recherche. De ce fait, l'ingénieur/chercheur d'aujourd'hui ne peut plus se contenter d'implémenter des algorithmes pour ses seuls besoins, indépendamment des objectifs de l'entité au sein de laquelle il évolue. Il doit être capable d'intégrer rapidement de nouvelles briques logicielles dans une architecture complexe tout en assurant sa maintenabilité, sa portabilité et son évolutivité. Ceci nécessite d'acquérir non seulement des bases en algorithmie et en programmation, mais aussi de solides connaissances en conception de logiciels.

L'originalité de ce module d'enseignement est de partir de problèmes concrets que nous retrouvons dans les codes industriels et Open Source de calcul scientifique pour ensuite remonter aux algorithmes et à leurs implémentations. Ces problèmes permettront d'illustrer un ensemble de méthodes numériques (analyse numérique des EDPs, apprentissage statistique, calcul stochastique, etc, dont les bases mathématiques ont été présentées dans les cours de deuxième année essentiellement (MAP412 et MAP433)) qui requièrent le choix d’algorithmes avancés et d'en présenter une implémentation élégante, modulaire et performante en C++ moderne. Ce cours sera très interactif et permettra d'expérimenter différentes améliorations des solutions existantes tout en analysant leur intégration potentielle au sein de systèmes complexes.

Pour ce faire, nous nous appuierons dans un premier temps sur [Jupyter](https://jupyter.org/) et le kernel [xeus-cling](https://github.com/jupyter-xeus/xeus-cling) permettant d'écrire du C++ dans des notebooks, puis nous passerons à une structuration de projet plus traditionnelle permettant d'illustrer l'architecture d'un logiciel (arborescence, création de librairies et d'exécutables, etc).

A la fin du cours, des connaissances solides en algorithmie permettront aux étudiants d'appréhender plus facilement l'implémentation de nouvelles méthodes numériques. Grâce à leur connaissance du C++, ils seront à même de lire la plupart des codes écrits dans ce langage et d'envisager sereinement toutes les potentialités de celui-ci. Enfin, les notions de génie logiciel abordées leur permettront de comprendre les architectures logicielles complexes que l’on trouve tant dans le domaine de la recherche que dans les industries de pointe. Les aspects de programmation paralléle pourront être abordés pendant ce cours et faire l'objet de projets conclusifs.

Ce cours est porté par L. Gouarin (CMAP) et Y. Mabile (Quantstack)



## AMS X02 - Cours de Master 2
### Méthodes numériques avancées et calcul haute performance pour la simulation de phénomènes complexes

Dans un nombre croissant d’applications, scientifiques ou industrielles, la simulation
numérique joue un rôle clef pour comprendre et analyser les phénomènes
physiques complexes. Elle permet aussi de prédire le fonctionnement de dispositifs
comme les chambres de combustion aéronautiques dans l’optique
d’une conception avancée. La complexité des systèmes et la taille des simulations
multi-dimensionnelles rendent l’utilisation du calcul haute performance nécessaire.
Ce cours propose dans un premier temps une présentation des enjeux que
pose la modélisation des systèmes complexes pour les méthodes numériques et la
simulation et un état de l’art des nouvelles architectures de calcul et des modèles
de programmation parallèle. Après avoir rappelé les bases de l’analyse numérique
des EDP pour les problèmes multi-échelles, nous proposons d’explorer quelques
méthodes numériques avancées conçues pour traiter la raideur présente dans ces
modèles complexes tout en tirant le meilleur parti des nouvelles architectures
de calcul. Ces méthodes s’appuient sur une combinaison efficace entre analyse
numérique, modélisation et calcul scientifique. Des séances de mise en oeuvre sur
machines en lien avec le mésocentre de calcul de l’Ecole polytechnique seront
proposées.

Ce cours est porté par L. Séries (CMAP) et M. Massot (CMAP)

## Research Course
### [Introduction to Solving PDEs with Machine Learning](https://jbscoggi.github.io/website/talks/2020-01-27-short_course/) 

Solving partial differential equations is an engineer’s bread and butter. Classical discretization techniques such as finite-difference or finite-volume are powerful methods for the numerical solution of PDEs, however, their reliance on robust and efficient mesh generation often presents difficulties in solution convergence or necessitates enormous computational resources to obtain an accurate solution. In this lecture, an alternative method based on a statistical machine learning approach will be presented, which yields a continuous, differentiable, and meshless representation of the hidden PDE solution. The topics covered will include machine learning basics, foundations in neural networks, and PDE solution techniques with neural networks. Following the lecture, a practical session on solving PDEs will be presented using the Tensorflow library and Jupyter notebooks with Google Colab. All lecture slides and Jupyter notebooks will be available after the lecture.

Ce cours est porté par J.B. Scoggins (CMAP/NASA) 

## Research Course
### [Moment Closure Methods for Kinetic Equations of Complex Transport Phenomena and their Numerical Solution](http://arrow.utias.utoronto.ca/~groth/moment-closure-course/index.html) 

Moment closure methods are considered for kinetic equations governing a range of complex transport phenomena, including non-equilibrium, rarefied, gaseous flow phenomena as described by the Boltzmann kinetic equation, multi-phase poly-disperse spray behaviour described by the Williams-Boltzmann equation, and radiative heat transfer in non-gray, participating media as described by the radiative transfer equation. Moment closure methods offer a means of significant complexity reduction when constructing approximate solutions to such high-dimensional equations, providing a good compromise between computational efficiency and accuracy for many practical engineering applications. Closure techniques based on classical Grad-type methods, maximum-entropy considerations, as well as quadrature formulations will all be considered. The numerical solution of the resulting systems of hyperbolic moment equations that result from the moment closure strategy will also be examined.

## Autres cours 


Plusieurs autres cours sont portés par des membres de l'initiative à divers niveaux. Un Cours de Master 1 (AMS CS1) en collaboration avec CentraleSupélec porte sur les "Méthodes de Moments dérivées d’une équation cinétique". Un cours de 2A de bachelor (MAA208) sur "Numerical linear algebra" est porté par T. Pichard en particulier. T. Pichard participe aussi aux MODAL MAP471A
"Problem solving en mathématiques appliquées" et 
MODAL MAP472A "Modélisation mathématique par la démarche expérimentale". Une implication sur les "Projet scientifique collaboratif (PSC)" est aussi coordonnée par T. Pichard et des projets sont proposés dans le cadre de l'intiative.

