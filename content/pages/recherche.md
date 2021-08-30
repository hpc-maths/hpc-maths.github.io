title: Recherche

<section id="recherche" class="theme">
<div class="container" data-aos="fade-up">
    <h1 class="page_title">nos axes de recherche</h1>
    <div class="row justify-content-center">
    <div class="col-xl-10">
        <h2><span class="huge">I</span>ANALYSE ET MODÉLISATION MATHÉMATIQUE</h2>
        <ul class="theme-list">
        <li>
            <div data-bs-toggle="collapse" class="collapsed axe" href="#theme1">Modèles réduits pour les écoulements diphasique gaz-liquides<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme1" class="collapse"  data-bs-parent=".theme-list">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p> L'objectif est de proposer un nouvelle gamme de modèles unifiés pour l'injection diphasique (par exemple d'un carburant liquide dans une chambre de combustion) depuis l'injecteur jusqu'à la zone dispersée où va se produire évaporation et combustion, sachant que les régimes de combustion dépendent de la granulométrie des brouillards de gouttes produits et qu'il faut donc décire.</p>
                <p> Dans la lignée de plusieurs thèses (F. Drui, M. Essadki, P. Cordesse) et dans le cadre d'une collaboration forte avec l'ONERA, le CEA et IFPEN, deux thèses viennent d'être ou sont en cours de soutenance (R. Di Battista, A. Remigi - collaboration CORIA) et deux thèses ont démarré sur le sujet A. Loison et W. Haegeman. Il s'agit de construire des modèles de type phase séparées (multi-fluides) avec modélisation de sous-échelle impliquant des variables géométriques et de s'appuyer sur le principe de l'actions stationnaire, le second principe de la thermodynamique et des outils de géométrie algorithmique permettant des analyses de DNS d'écoulements interfaciaux (Code Mercru(v)e Ruben Di Battista). Il s'agit aussi d'étudier la structure mathématique des systèmes d'EDP produits par ces techniques afin d'en assurer le caractère bien posé. Cet axe de recherche est très présent dans le projet AID DGA MMEED (Pi. M. Massot) et permet une connexion entre tous ces acteurs. Une gamme de plusieurs code de calcul (Josiepy, CanoP, Mercur(v)e, SAMURAI - voir la section codes) et une articulation avec le code CEDRE de l'ONERA ont été développées. </p>
            </div>
            </div>
        </li>
        <li>
            <div data-bs-toggle="collapse" href="#theme2" class="collapsed axe">Méthodes de moments pour la modélisation des brouillards de gouttes polydispersés<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme2" class="collapse" data-bs-parent=".theme-list">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p> Décrire la polydispersion d'un brouillard de gouttes sphériques ou d'objets homéomorphes à une sphère dans un cadre fluide se fait en général par des techniques de méthodes de moments. Cela demande d'une part de clarifier la notion d'espace de moments et d'autre part d'être capable de reconstruire, à partir de la donnée d'un vecteur de moment, une densité de probabilité dont les moments correspondent, afin de pouvoir fermer les terms sources qui pilotent la dynamique du brouillard. Le méthodes de quadrature de moment (bien posées pour des distribution mono-variées, mais délicate en multi-varié) ou la maximisation de l'entropie de shannon permettent en général de mener à bien cette reconstruction mais le bord de l'espace des moments peut être problématique (Thèse M. Essadki, Post-Doctorat K. Ait-Ameur, Thèse A. Loison). Une connexion avec les technique d'apprentissage statistique peut ici être utile (J.B. Scoggins). Cet axe fait l'objet d'une collaboration avec IFPEN, le laboratoire EM2C et la Fédération de Mathématiques de CentraleSupélec. Là encore l'utilisation de simulations directe d'inclusions liquides et leur analyse par des outils de géometrie algorithmique peut être utile pour proposer des méthodes de moments innovantes et donner une signification physiques aux moments choisis. </p>
            </div>
            </div>
        </li>
        <li>
            <div data-bs-toggle="collapse" href="#theme3" class="collapsed axe">Méthodes de moments et modèles fluides pour les plasmas partiellement ionisés<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme3" class="collapse" data-bs-parent=".theme-list">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p> Le plasma est un état de la matière où diverses particules (éléctrons, ions ou neutres) peuvent se déplacer librement et intéragir entre eux par des effets collisionnels ou électromagnétiques. Si les fluides classiques sont classiquement représentés à l'équilibre thermodynamique menant à des équations fluides comme celles d'Euler, cette hypothèse d'équilibre s'avère fausse dans de nombreux régimes en plasmas. Pour modéliser ces régimes à une échelle fluide, on peut par exemple reprartir d'une description mesoscopique et faire l'hypothèse que la distribution des particules est donnée comme une perturbation de l'équilibre, c'est typiquement le cas pour la méthode de Grad. Or non seulement la construction de telles distributions peut s'avérer complexe, mais les équations fluides ou aux moments qui en résultent perdent souvent des propriétés mathématiques (hyperbolicité) essentielles. De plus, ces équations dégénèrent dans certains régimes et les méthodes numériques doivent être adaptées.</p>
                <p> Ces travaux sont au coeur du projet de thèse de Louis Reboul au CMAP, et sont en relation directe avec le LPP, notamment avec Alejandro Alvarez-Laguna. </p>
            </div>
            </div>
        </li>
        <li>
            <div data-bs-toggle="collapse" href="#theme4" class="collapsed axe">Réalisabilité, fermeture d'ordre élevé et méthodes de projection pour les modèles aux moments<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme4" class="collapse" data-bs-parent=".theme-list">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p> Dans un cadre générale, la méthode des moments peut être vue soit comme un changement d'échelle d'une description mésoscopique vers une description macroscopique d'un écoulement fluide, ou simplement comme une approximation numérique d'une fonction par rapport une variable et exploitant comme informations uniquement des intégrales pondérées, appelées moments, de cette fonction. Cette approximation est construite en résolvant le "problème des moments tronqués", c'est-à-dire en reconstruisant une fonction à partir de ses moments. Il faut donc choisir une telle reconstruction parmi toutes celles possibles. On peut alors imposer des contraintes supplémentaires à cette reconstruction, notamment sa positivité, afin d'imposer des propriétés mathématiques ou une précision dans certains régimes physiques au modèle obtenu.</p>
                <p> Cette étude se base sur une compréhension fine de la géométrie de l'espace des moments et des représentations possibles pour chaque vecteur de moments, notamment sur le bord du domaine de réalisabilité. L'objectif est double : 1-construire une fermeture d'ordre quelconque, et donc de construire une discrétisation d'ordre élevé par rapport à cette variable cinétique, 2-la contrainte de réalisabilité s'appliquant à la fois à l'inconnue continue et à sa discrétisation obtenue par un schéma numérique, l'étude de cette contrainte est également nécessaire pour la construction de schéma numérique d'ordre élevé pour ces équations aux moments. </p>
                <p> Cette thématique a été initiée par T. Pichard et s'applique à diverses autres projets autour des modèles aux moments. </p>
            </div>
            </div>
        </li>
        <li>
            <div data-bs-toggle="collapse" href="#theme5" class="collapsed axe">Conditions de bord pour les modèles aux moments (Application en transfert radiatif)<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme5" class="collapse" data-bs-parent=".theme-list">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p> Le principale problème derrière les modèles aux moments est celui de la fermeture. Partant d'un vecteur, on cherche à reconstruire une fonction dont les intégrales (pondérées par diverses fonctions poi ds) donne ce vecteur. Lorsqu'on appliqua cette méthode pour des simulations physiques, ce problème doit être résolu en tout point à l'intérieur du domaine spatial pour obtenir un système d'EDP aux moments. Or ce système a bien sûr également besoin d'une condition initiale et de conditions au bord du domaine spatial. Or la solution du problème de moment n'est pas adaptée pour construire une condition de bord entrante au bord du domaine dans le modèle aux moments. Une autre construction, par exemple basée sur la méthode des caractéristiques (lié au caractère hyperbolique de ces équations aux moments) est alors envisagée.</p>
                <p> Ce problème est général à tout les modèles aux moments en vitesse, mais est étudié ici pour des applications en transfert radiatif où la vitesse est supposée bornée.</p>
                <p> Ce projet a débuté en collaboration avec Clinton Groth et Joachim Sarr d'UTIAS Toronto lors de leur visite au CMAP avant le confinement de 2020 et permit par un financement Monge invité. </p>
            </div>
            </div>
        </li>
        <li>
            <div data-bs-toggle="collapse" href="#theme6" class="collapsed axe">Modélisation des écoulements gaz-particules turbulents<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme6" class="collapse" data-bs-parent=".theme-list">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p> Le but de cet axe est de développer un modèle "two-way coupled" à grande échelle d'écoulement de particules solides dans des écoulements turbulents en prenant en compte la physique de l'influence réciproque entre le gaz et les particules et l'intermittence naturellement présente dans ce type d'écoulement. Il s'agit en particulier de proposer des modèles stochastiques sur la base de processus non réguliers permettant de prédire tant dans la modélisation théorique que dans la simulation numérique efficace, cette intermittence à petite échelle. Ces résultats reposent sur une collaboration interdisciplinaire entre physicien de la turbulence (R. Zamansky, IMFT, A. Vié, CentraleSupélec) et des probabilistes (Alexandre Richard et Ludovic Goudenège, CentraleSupélec Fédé Maths) dans le cadre de la thèse de R. Letournel entre CMAP et la Fédé de Maths de CentraleSupélec (Projet DGA MMEED). </p>
            </div>
            </div>
        </li>
        </ul>
    </div>
    <div class="col-xl-10">
        <h2><span class="huge">II</span>ANALYSE NUMÉRIQUE ET DÉVELOPPEMENT DE SCHÉMAS</h2>
        <ul class="theme-list theme-listB">
        <li>
            <div data-bs-toggle="collapse" class="collapsed axe" href="#theme1B">Multirésolution adaptative<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme1B" class="collapse" data-bs-parent=".theme-listB">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p> Nous avons développé la capacité de développer des méthodes d'ordre élevée en temps couplées à de la multirésolution adaptative en espace permettant de mener à un contrôle de l'erreur globale avec des applications en combustion, physique des plasmas et génie biomédical (PhD Max Duarte) et en mécanique des fluides (Navier-Stokes incompressible et Low Mach / Combustion, PhD Marc-Arthur N'Guessan). Les techniques en temps peuvent être des intégrateurs de type DAE ordre élévé, RK implicite (RADAU5) ou des méthodes de séparation d'opérateur avec adaptation dynamique du pas de temps. Ces techniques font aussi l'objet d'une collaboration avec SpaceX. Ces techniques on été implémentées sur architecture many-coeurs en collaboration avec INTEL et l'ICJ (T. Dumont) et sont en cours d'implémentation dans le code SAMURAI.</p>
            </div>
            </div>
        </li>
        <li>
            <div data-bs-toggle="collapse" href="#theme2B" class="collapsed axe">Méthode de Boltzmann sur réseau<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme2B" class="collapse" data-bs-parent=".theme-listB">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p> Dans le cadre de la thèse de T. Bellotti et en collaboration avec B. Graille (IMO, Orsay), ainsi que dans le cadre du projet LBMHYPE (VKI, CENAERO, ESA), nosu développons une analyse et une vision nouvelle sur les méthodes de Boltzmann sur réseau, et le couplage de ce type de méthode avec de l'adaptation de maillage dans le cadre de la multiresolution adaptative (tout en préservant la capacité à utiliser la théorie des équations équivalentes). Le cadre est celui du code SAMURAI développé par l'équipe. </p>
            </div>
            </div>
        </li>
        <li>
            <div data-bs-toggle="collapse" href="#theme3B" class="collapsed axe">Méthode d'ordre élevé de type DG préservant un sous espace convexe<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme3B" class="collapse" data-bs-parent=".theme-listB">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p> La montée en ordre lors de la construction de schéma numérique permet certes d'agumenter la précision, mais elle mène également à de nouvelles difficultés. Deux d'entre elles sont liées à la préservation d'espace convexe~: d'abord la solution d'un système d'équations, comme les équations aux moments par exemple, est parfois bien définie uniquement dans un sous-ensemble (convexe). La solution numérique rendu par un schéma doit alors systématiquement appartenir à ce domaine, sans quoi la solution numérique n'est plus définie. Similairement, la stabilité d'un schéma numérique est souvent obtenue par ces mêmes raisonnements, typiquement via le principe du maximum en scalaire. Ces deux problématiques peuvent être résolue en cherchant à imposer à la solution numérique à rester dans un certain sous-espace convexe.</p>
                <p> On s'intéresse ici principalement aux schémas de type Galerkin Discontinu qui permettent une montée en ordre relativement simple et pour lesquels on peut imposer à la solution numérique d'apartenir au sous-espace convexe localement en des points de quadrature, plutôt qu'en tout point d'évaluation de la solution approchée. </p>
                <p> Cette problématique est étudié à travers le postdoc de Katia Ait-Ameur (financement Dim-Mathinov 2020-2021 puis DGA 2021-2022) en lien avec la thèse d'Arthur Loison (X-DGA). Et elle fait suite aux thèses de Florence Drui et Mohamed Essadki. </p>
            </div>
            </div>
        </li>
        <li>
            <div data-bs-toggle="collapse" href="#theme4B" class="collapsed axe">Méthode préservant l'asymptotique pour les systèmes hyperboliques et hyperboliques paraboliques et schéma numérique équilibre avec terme source<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme4B" class="collapse" data-bs-parent=".theme-listB">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p>De nombreux problèmes physiques font apparaitre plusieurs régimes régient par des modèles aux propriétés différentes. On s'intéresse typiquement à des modèles de transport avec des effets diffusifs (par exemple produit via des termes sources) qui peuvent être à la fois complêtement absents et prédominant dans une même simulation. Les équations dans les deux régimes ont des structures différentes (hyperbolique ou parabolique) et les schémas numériques classiques sont rarement précis dans les deux régimes.</p>
                <p> Cette dégénérence est souvent pilotée par un terme source dans les équations considérées couplant les différentes inconnues entre elles. La prise en compte de terme source dans un schéma numérique peut mener à des difficultés et doivent être adaptées aux régimes physiques considérés. </p>
                <p> Cette thématique a été initiée autour de la thèse de Louis Reboul pour des applications en physique des plasmas et en collaboration avec Alejandro Alvarez Laguna. Elle apparait également à travers l'étude des schémas LBM dans la thèse de Thomas Bellotti. </p>
            </div>
            </div>
        </li>
        <li>
            <div data-bs-toggle="collapse" href="#theme5B" class="collapsed axe">Méthodes de volumes finis et prise en compte de produits non-conservatifs<i class="bi bi-chevron-down icon-show"></i><i class="bi bi-chevron-up icon-close"></i></div>
            <div id="theme5B" class="collapse" data-bs-parent=".theme-listB">
            <div class="theme_content"> <img class="recherche_img" src="{{ SITEURL }}/theme/img/img_template.png" width="150" height="150" alt=""/>
                <p> Issu de la modélisation fluide des plasmas multi-composants hors équilibre thermique, des équations mixtes-hyperboliques paraboliques avec présence de produits non conservatifs sur l'énergie des électrons pose depuis longtemps des soucis en termes de définition des conditions de saut et des schémas numériques pour leur résolution. Une approche originale s'appuyant sur une dérivation détaillée à partir de la théorie cinétique des gaz dans un scaling mixte hyperbolique-parabolique, permet une évaluation des conditions de saut et la construction de schémas adaptés avec application en physique solaire (Collaboration NASA / VKI - PhD Q. Wargnier).</p>
            </div>
            </div>
        </li>
        </ul>
    </div>
    <div class="col-xl-10">
        <h2><span class="huge">III</span>CALCUL SCIENTIFIQUE ET CALCUL HAUTE PERFORMANCE (HPC)</h2>
        <ul class="list_item">
        Cet axe s'articule autour de deux stratégies :
        <li>le développement de code de calcul efficaces soit pour le prototypage rapide de modèles et de méthodes numériques (Collaboration Quantstack), soit des codes parallèles qui passent à l'échelle sur les architectures parallèles. </li>
        <li>l'intégration des modèles et méthodes numérique que nous développons dans des codes semi-industriels ou industriels de nos partenaires (ONERA / IFPEN / CEA / CERFACS / SAFRAN)</li>
        </ul>
        <p class="bandeau"> Les applications visées sont les chambres de combustion aéronautiques et automobiles, l'allumage et la dynamique diphasique des moteurs à propergol solide en propulsion solide des fusées, la propulsion liquide et hybride des moteurs fusée, la propulsion électrique pour les satellites, la modélisation des reconnexions magnétiques en physique solaire, ou le génie nucléaire, mais aussi en dynamique chimique non-linéaire et le génie biomédical.</p>
    </div>
    </div>
</div>
</section>

<!-- ## Analyse et modélisation mathématique

### Modéles réduits pour les écoulements diphasique gaz-liquides

L'objectif est de proposer un nouvelle gamme de modèles unifiés pour l'injection diphasique (par exemple d'un carburant liquide dans une chambre de combustion) depuis l'injecteur jusqu'à la zone dispersée où va se produire évaporation et combustion, sachant que les régimes de combustion dépendent de la granulométrie des brouillards de gouttes produits et qu'il faut donc décire.

Dans la lignée de plusieurs thèses (F. Drui, M. Essadki, P. Cordesse) et dans le cadre d'une collaboration forte avec l'ONERA, le CEA et IFPEN, deux thèse viennent d'être ou sont en cours de soutenance (R. Di Battista, A. Remigi - collaboration CORIA) et deux thèses ont démarré sur le sujet A. Loison et W. Haegeman. Il s'agit de construire des modèles de type phase séparées (multi-fluides) avec modélisation de sous-échelle impliquant des variables géométriques et de s'appuyer sur le principe de l'actions stationnaire, le second principe de la thermodynamique et des outils de géométrie algorithmique permettant des analyses de DNS d'écoulements interfaciaux.
Il s'agit aussi d'étudier la structure mathématique des systèmes d'EDP produits par ces techniques afin d'en assurer le caractère bien posé.
Cet axe de recherche est très présent dans le projet AID DGA MMEED (Pi. M. Massot) et permet une connexion entre tous ces acteurs. Une gamme de plusieurs code de calcul (Josiepy, CanoP, Mercur(v)e, SAMURAI - lien codes) et une articulation avec le code CEDRE de l'ONERA ont été développées.

(film / image Pierre / Ruben)

### Méthodes de moments pour la modélisation des brouillards de gouttes polydispersés

Décrire la polydispersion d'un brouillard de gouttes sphériques ou d'objets homéomorphes à une sphère dans un cadre fluide se fait en général par des techniques de méthodes de moments. Cela demande d'une part de clarifier la notion d'espace de moments et d'autre part d'être capable de reconstruire, à partir de la donnée d'un vecteur de moment, une densité de probabilité dont les moments correspondent, afin de pouvoir fermer les terms sources qui pilotent la dynamique du brouillard. Le méthodes de quadrature de moment (bien posées pour des distribution mono-variées, mais délicate en multi-varié) ou la maximisation de l'entropie de shannon permettent en général de mener à bien cette reconstruction mais le bord de l'espace des moments peut être problématique (Thèse M. Essadki, Post-Doctorat K. Ait-Ameur, Thèse A. Loison). Une connexion avec les technique d'apprentissage statistique peut ici être utile (J.B. Scoggins).
Cet axe fait l'objet d'une collaboration avec IFPEN, le laboratoire EM2C et la Fédération de Mathématiques de CentraleSupélec. Là encore l'utilisation de simulations directe d'inclusions liquides et leur analyse par des outils de géometrie algorithmique peut être utile pour proposer des méthodes de moments innovantes et donner une signification physiques aux moments choisis.

(figure espace des moments)

### Méthodes de moments et modèles fluides pour les plasmas partiellement ionisés

Le plasma est un état de la matière où diverses particules (éléctrons, ions ou neutres) peuvent se déplacer librement et intéragir entre eux par des effets collisionnels ou électromagnétiques. Si les fluides classiques sont classiquement représentés à l'équilibre thermodynamique menant à des équations fluides comme celles d'Euler, cette hypothèse d'équilibre s'avère fausse dans de nombreux régimes en plasmas. Pour modéliser ces régimes à une échelle fluide, on peut par exemple reprartir d'une description mesoscopique et faire l'hypothèse que la distribution des particules est donnée comme une perturbation de l'équilibre, c'est typiquement le cas pour la méthode de Grad. Or non seulement la construction de telles distributions peut s'avérer complexe, mais les équations fluides ou aux moments qui en résultent perdent souvent des propriétés mathématiques (hyperbolicité) essentielles. De plus, ces équations dégénèrent dans certains régimes et les méthodes numériques doivent être adaptées.

Ces travaux sont au coeur du projet de thèse de Louis Reboul au CMAP, et sont en relation directe avec le LPP, notamment avec Alejandro Alvarez Laguna.

### Réalisabilité, fermeture d'ordre élevé et méthodes de projection pour les modèles aux moments

Dans un cadre générale, la méthode des moments peut être vue soit comme un changement d'échelle d'une description mésoscopique vers une description macroscopique d'un écoulement fluide, ou simplement comme une approximation numérique d'une fonction par rapport une variable et exploitant comme informations uniquement des intégrales pondérées, appelées moments, de cette fonction. Cette approximation est construite en résolvant le "problème des moments tronqués", c'est-à-dire en reconstruisant une fonction à partir de ses moments. Il faut donc choisir une telle reconstruction parmi toutes celles possibles. On peut alors imposer des contraintes supplémentaires à cette reconstruction, notamment sa positivité, afin d'imposer des propriétés mathématiques ou une précision dans certains régimes physiques au modèle obtenu.

Cette étude se base sur une compréhension fine de la géométrie de l'espace des moments et des représentations possibles pour chaque vecteur de moments, notamment sur le bord du domaine de réalisabilité. L'objectif est double : 1-construire une fermeture d'ordre quelconque, et donc de construire une discrétisation d'ordre élevé par rapport à cette variable cinétique, 2-la contrainte de réalisabilité s'appliquant à la fois à l'inconnue continue et à sa discrétisation obtenue par un schéma numérique, l'étude de cette contrainte est également nécessaire pour la construction de schéma numérique d'ordre élevé pour ces équations aux moments.

Cette thématique a été initiée par T. Pichard et s'applique à diverses autres projets autour des modèles aux moments.

### Conditions de bord pour les modèles aux moments (application en transfert radiatif)

Le principale problème derrière les modèles aux moments est celui de la fermeture. Partant d'un vecteur, on cherche à reconstruire une fonction dont les intégrales (pondérées par diverses fonctions poi
ds) donne ce vecteur. Lorsqu'on appliqua cette méthode pour des simulations physiques, ce problème doit être résolu en tout point à l'intérieur du domaine spatial pour obtenir un système d'EDP aux moments. Or ce système a bien sûr également besoin d'une condition initiale et de conditions au bord du domaine spatial. Or la solution du problème de moment n'est pas adaptée pour construire une condition de bord entrante au bord du domaine dans le modèle aux moments. Une autre construction, par exemple basée sur la méthode des caractéristiques (lié au caractère hyperbolique de ces équations aux moments) est alors envisagée.

Ce problème est général à tout les modèles aux moments en vitesse, mais est étudié ici pour des applications en transfert radiatif où la vitesse est supposée bornée.

Ce projet a débuté en collaboration avec Clinton Groth et Joachim Sarr d'UTIAS Toronto lors de leur visite au CMAP avant le confinement de 2020 et permit par un financement Monge invité.

### Modélisation des écoulements gaz-particules turbulents

Roxane - Aymeric - DGA
Collaboration CentraleSupélec Fédé Maths Alexandre Richard et Ludovic Goudenège

## Analyse numérique et développement de schémas

### Multirésolution adaptative

Marc-Arthur - code Python - film NS

### Méthode de Boltzmann sur réseau

Thomas - Lien SAMURAI

### Méthode d'ordre élevé de type DG préservant un sous espace convexe

La montée en ordre lors de la construction de schéma numérique permet certes d'agumenter la précision, mais elle mène également à de nouvelles difficultés. Deux d'entre elles sont liées à la préservation d'espace convexe~: d'abord la solution d'un système d'équations, comme les équations aux moments par exemple, est parfois bien définie uniquement dans un sous-ensemble (convexe). La solution numérique rendu par un schéma doit alors systématiquement appartenir à ce domaine, sans quoi la solution numérique n'est plus définie. Similairement, la stabilité d'un schéma numérique est souvent obtenue par ces mêmes raisonnements, typiquement via le principe du maximum en scalaire. Ces deux problématiques peuvent être résolue en cherchant à imposer à la solution numérique à rester dans un certain sous-espace convexe (à définir au cas par cas).

On s'intéresse ici principalement aux schémas de type Galerkin discontinu qui permettent une montée en ordre relativement simple et pour lesquels on peut imposer à la solution numérique d'apartenir au sous-espace convexe localement en des points de quadrature, plutôt qu'en tout point d'évaluation de la solution approchée.

Cette problématique est étudié à travers le postdoc de Katia Ait-Ameur (financement Dim-Mathinov 2020-2021 puis DGA 2021-2022) en lien avec la thèse d'Arthur Loison (X-DGA). Et elle fait suite aux thèses de Florence Drui et Mohamed Essadki.

### Méthode préservant l'asymptotique pour les systèmes hyperboliques et hyperboliques paraboliques et schéma numérique équilibre avec terme source

De nombreux problèmes physiques font apparaitre plusieurs régimes régient par des modèles aux propriétés différentes. On s'intéresse typiquement à des modèles de transport avec des effets diffusifs (par exemple produit via des termes sources) qui peuvent être à la fois complêtement absents et prédominant dans une même simulation. Les équations dans les deux régimes ont des structures différentes (hyperbolique ou parabolique) et les schémas numériques classiques sont rarement précis dans les deux régimes.

Cette dégénérence est souvent pilotée par un terme source dans les équations considérées couplant les différentes inconnues entre elles. La prise en compte de terme source dans un schéma numérique peut mener à des difficultés et doivent être adaptées aux régimes physiques considérés.

Cette thématique a été initiée autour de la thèse de Louis Reboul pour des applications en physique des plasmas et en collaboration avec Alejandro Alvarez Laguna. Elle apparait également à travers l'étude des schémas LBM dans la thèse de Thomas Bellotti.

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

Film Florence - film Louis - film Quentin -->
