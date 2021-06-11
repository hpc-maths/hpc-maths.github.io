title: Recherches
## Analyse et modélisation mathématique

### Modéles réduits pour les écoulements diphasique gaz-liquides

L'objectif est de proposer un modèle unifié pour l'injection diphasique (par exemple d'un carburant liquide dans une chambre de combustion) depuis l'injecteur jusqu'à la zone dispersée où va se produire évaporation et combustion, sachant que les régimes de combustion dépendent de la granulométrie des brouillards de gouttes produits et qu'il faut donc décire. 

Dans la lignée de plusieurs thèse (F. Drui, M. Essadki, P. Cordesse) et dans le cadre d'une collaboration forte avec l'ONERA, le CEA et IFPEN, deux thèse viennent d'être ou sont en cours de soutenance (R. Di Battista, A. Remigi - collaboration CORIA) et deux thèses ont démarré sur le sujet A. Loison et W. Haegeman. Il s'agit de construire des modèles de type phase séparées (multi-fluides) avec modélisation de sous-échelle impliquant des variables géométriques et de s'appuyer sur le principe de l'actions stationnaire, le second principe de la thermodynamique et des outils de géométrie algorithmique permettant des analyses de DNS d'écoulements interfaciaux.
Cet axe de recherche est très présent dans le projet AID DGA MMEED (Pi. M. Massot) et permet une connexion entre tous ces acteurs. Une gamme de plusieurs code de calcul (Josiepy, CanoP, Mercur(v)e, SAMURAI - lien codes) et une articulation avec le code CEDRE de l'ONERA ont été développées. 

(film / image Pierre / Ruben)


### Méthodes de moments pour la modélisation des brouillards de gouttes polydispersés

Décrire la polydispersion d'un brouillard de gouttes sphériques ou d'objets homéomorphe à une sphère dans un cadre fluide se fait en général par des techniques de méthodes de moments. Cela demande d'une part de clarifier la notion d'espace de moments et d'autre part d'être capable de reconstruire, à partir de la donnée d'un vecteur de moment, une densité de probabilité dont les moments correspondent, afin de pouvoir fermer les terms sources qui pilotent la dynamique du brouillard. Le méthodes de quadrature de moment (bien posées pour des distribution mono-variées, mais délicate en multi-varié) ou la maximisation de l'entropie de shannon permettent en général de mener à bien cette reconstruction mais le bord de l'espace des moments peut être problématique (Thèse M. Essadki, Post-Doctorat K. Ait-Ameur, Thèse A. Loison). Une connexion avec les technique d'apprentissage statistique peut ici être utile (J.B. Scoggins). Cet axe fait l'objet d'une collaboration avec IFPEN, le laboratoire EM2C et la Fédération de Mathématiques de CentraleSupélec.

(figure espace des moments)

### Méthodes de moments et modèles fluides pour les plasmas partiellement ionisés



Louis - Alejandro - Teddy


### Modélisation des écoulements gaz-particules turbulents

Roxane - Aymeric - DGA
Collaboration CentraleSupélec Fédé Maths Alexandre Richard et Ludovic Goudenège


### Réalisabilité / Fermeture d'ordre élevé / méthodes de projection pour les modèles aux moments

Teddy


### Conditions de bord pour les modèles aux moments

Teddy
Collaboration UTIAS Joachim - Clinton


### Modeles cinétique et aux moments en transfert radiatif (application en radiothérapie)

Teddy


## Analyse numérique et développement de schémas

### Multirésolution adaptative

Marc-Arthur - code Python - film NS


### Méthode de Boltzmann sur réseau

Thomas - Lien SAMURAI


### Méthode d'ordre élevé de type DG préservant un sous espace convexe

Katia - Teddy


### Méthode préservant l'asymptotique pour les systèmes hyperboliques et hyperboliques paraboliques

Louis - Alejandro - Teddy


### Schéma numérique avec terme source / Well-balanced

Louis - Alejandro - Teddy


### Méthodes de volumes finis et prise en compte de produits non-conservatifs

Quentin


### Méthode d'apprentissage pour la modélisation et la simulations d'équations aux dérivées partielles

JB


### Géométrie algorithmique et reconstruction de propriétés géométriques d'une interface (courbure)

film Mercru(v)e Ruben


### Schéma Lagrange-projection pour les écoulements diphasiques

Samuel - Katia - Marica - Teddy


## Calcul scientifique et Calcul haute performance (HPC)

### ONERA CEDRE - diphasique

image Pierre


### ONERA CEDRE - allumage

Laurent François


### ONERA Couplage de codes

Allumage Laurent François


### développement de structures de données pour la MR adaptative

Collaboration INTEL, ICJ pour l'implémentation sur arcthitecture many-coeurs - code z-code (lien), puis algèbre d'ensembles - code SAMURAI (lien code) + image


### couplage adaptation temporelle et adaptation en espace avec contrôle d'erreur

exemple Max - BZ idéalement avec SAMURAI


### Développement d'un plateforme pour la simulation de modèles fluides avec adapatation de maillage (cell-based AMR) massivement parallèle CanoP (codes)

CanoP - p4est - CEA - Maison de la Simulation
Application plasmas partiellement ionisé (NASA / VKI), Ecoulements diphasiques pour les moteurs à combustion interne et génie nucléaire (IFPEN / CEA) et la propulsion électrique (LPP)

Film Florence - film Louis - film Quentin
