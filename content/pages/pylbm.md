title: pylbm

<section id="code_pylbm" class="page code">
    <div class="container" data-aos="fade-up" data-aos-delay="100">
    <h1 class="page_title">Logiciel pylbm</h1>
    </div>
<div class="container" data-aos="fade-up">
    <div class="row">
    <div class="col-lg-6 pt-4 pt-lg-0 content d-flex flex-column" data-aos="fade-up" data-aos-delay="100">
<h2 class="section_title">Un logiciel polyvalent</h2>
        <p><span class="glossary_link">Pylbm</span> est un logiciel open source écrit en Python. Il propose une implémentation flexible de la méthode Lattice Boltzmann pour les problèmes 1D/2D/3D et a été créé pour s'adresser à diverses communautés:</p>
        <h3 class="subtitle">Pour les mathématiciens</h3>
        <p>Ce logiciel offre un environnement très agréable pour tester de nouveaux schémas, comprendre leurs propriétés mathématiques, telles que la stabilité et la consistance, et ouvrir à de nouvelles frontières dans le domaine, telles que le raffinement du maillage, les équations équivalentes... </p>
        <h3 class="subtitle">Pour les physiciens</h3>
        <p>Pyblm offre un cadre idéal pour mener des expériences numériques pour différents niveaux de modélisation et de schémas, sans avoir à se plonger dans la machinerie mathématique des schémas LBM. Les algorithmes proposés peuvent également permettre d'aller au-delà du premier essai et de réaliser facilement des simulations à grande échelle grâce à sa capacité parallèle.</p>
        <h3 class="subtitle">Pour les informaticiens</h3>
        <p> Dans Pylbm, la méthode Lattice Boltzmann n'est pas codée en dur. Des outils avancés de génération de code, basés sur un large ensemble de bibliothèques d'algèbre informatique récemment développées, permettent à l'utilisateur d'entrer à un haut niveau la définition du schéma et les conditions aux limites. Le logiciel pylbm génère ensuite le code numérique résultant. Il est donc possible de modifier les noyaux de construction du code pour tester les performances et l'optimisation du code sur différentes architectures (AA pattern et Pull and Push algorithms); le code peut également être généré dans différents langages (C, C++, openCL, ...)</p>
    </div>
    <div class="col-lg-6"  data-aos="zoom-in" data-aos-delay="100"> <img src="../images/codes/pylbm/logo_pylbm.png" class="img-fluid img_logo_code" alt="">
        <div class="codes_link">
        <div class="codedoc"> <a href="https://github.com/pylbm/pylbm" class="github"> <i class="bi bi-github float-lg-start"></i>
            <div > <span class="title">Code</span><br>
            <span class="url">https://github.com/pylbm/pylbm</span> </div>
            </a> </div>
        <div class="codedoc"> <a href="https://pylbm.readthedocs.io" class="readdoc"><i class="bi bi-file-text-fill float-lg-start"></i>
            <div class=""> <span class="title">Documentation</span><br>
            <span class="url">https://pylbm.readthedocs.io</span> </div>
            </a> </div>
        </div>
    </div>
    </div>
    <hr class="separateur">
</div>
<div class="container">
    <div class="row">
    <div class="col-lg-6" data-aos="zoom-out" data-aos-delay="100"> <img src="../images/codes/pylbm/picture_pyblm.png" class="img-fluid picture" alt=""> </div>
    <div class="col-lg-6" data-aos="fade-left" data-aos-delay="100">
        <h2 class="section_title">Les caractéristiques essentielles</h2>
        <p>La principale caractéristique de pylbm est sa grande flexibilité en termes de schémas LBM et d'implémentations de code numérique. De plus, il possède d'excellentes capacités parallèles et utilise MPI pour le calcul distribué et openCL pour les GPU.</p>
        <p>Le cadre généralisé de d'Humières est utilisé pour décrire les schémas. Il est alors facile de définir votre schéma lattice Boltzmann en fournissant les vitesses, les valeurs d'équilibre et les paramètres de relaxation, ... De plus, vous pouvez avoir plusieurs schémas $D_dQ_q$ pour votre simulation où $d$ est la dimension et $q$ le nombre de vitesses. C'est généralement le cas lorsque vous voulez simuler par exemple des écoulements de fluides thermodynamiques comme dans le cas test de Rayleigh-Benard. Mais vous pouvez également expérimenter de nouveaux types de schémas de lattice Boltzmann comme les schémas vectorisés ou avec des vitesses relatives. </p>
    </div>
    </div>
</div>
</section>

<section id="autresCodes" class="section-bg">
<div class="container">
    <p class="well"  data-aos="fade-down">Les autres codes proposés</p>
    <div class="row justify-content-center">
        <a href="josiepy.html" class="code-thumb row">
            <div class="code-title col">
                <h1>
                    josiepy
                </h1>
                <h2>
                    Méthodes volumes finis en Python
                </h2>
            </div>
            <div class="code-image col">
                <img class="img-fluid" src="../images/codes/josiepy/logo_josiepy.png" alt=""/>
            </div>
        </a>
        <a href="mercurve.html"  class="code-thumb row">
            <div class="code-title col">
                <h1>
                    mercurve
                </h1>
                <h2>
                    Outils de post-traitement
                </h2>
            </div>
            <div class="code-image col">
                <img class="img-fluid" src="../images/codes/mercurve/logo_mercurve.png" alt=""/>
            </div>
        </a>
        <!-- <a href="pylbm.html" class="code-thumb row">
            <div class="code-title col">
                <h1>
                    pylbm
                </h1>
                <h2>
                    Lattice Boltzmann methods
                </h2>
            </div>
            <div class="code-image col">
                <img class="img-fluid" src="../images/codes/pylbm/logo_pylbm.png" alt=""/>
            </div>
        </a> -->
        <a href="samurai.html"  class="code-thumb row">
            <div class="code-title col">
                <h1>
                    samurai
                </h1>
                <h2>
                    Adaptation de maillage
                </h2>
            </div>
            <div class="code-image col">
                <img class="img-fluid" src="../images/codes/samurai/logo_samurai.png" alt=""/>
            </div>
        </a>
    </div>
</div>
</section>
