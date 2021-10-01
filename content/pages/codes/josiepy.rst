:title: josiepy
:subtitle: Méthodes volumes finis en Python
:category: code
:logo: ../images/codes/josiepy/logo_josiepy.png
:source: https://gitlab.com/rubendibattista/josiepy
:documentation: https://josiepy.rdb.is
:description: <span class="glossary_link">Josiepy</span> est une librairie en Python qui permet de mettre en place des simulations pour des problèmes qui sont gouvernés par des EDP avec simplicité avec la méthode des volumes finis. Tous les aspects d'un problème sont codé directement en Python, en évitant les difficultés que très souvent on rencontre dans des autres codes dans lesquels les configurations se font avec des DSL très limités

.. title:: qu'est-ce que josiepy?

**Josiepy** est une librairie en Python qui permet de mettre en place des simulations pour des problèmes qui sont gouvernés par des EDP avec simplicité avec la méthode des volumes finis. Tous les aspects d'un problème sont codé directement en Python, en évitant les difficultés que très souvent on rencontre dans des autres codes dans lesquels les configurations se font avec des DSL très limités.

.. title:: notre approche

L'idée fondamentale du projet est de fournir une boîte à outils très facile à utiliser pour rapidement tester des idées : développement de schémas, conception de conditions au bord particulières, équations constitutives exotiques, etc... dans des cas 1D, 2D et dans le futur proche 3D. La structure très modulaire de la librairie permet de s'occuper de ces elements constituants un cas à simuler de façon individuelle, en abstrayant le plus possible la façon d'opérer du reste du code. Le code est basé sur l'API de NumPy, qui fournit les structures des données sous-jacentes.

.. break::

.. title:: l'offre actuelle

- Une série de solveurs
- Équations d'Euler
- Équations de Navier-Stokes compressibles
- Équation de la Chaleur
- Équations de Baer-Nunziato pour un système diphasiques
- Schéma d'ordre 2 MUSCL
- Un mailleur simplifié basé sur le transfinite interpolation, codable directement avec l'API Python, qui permet de générer des maillages structurés rapidement et d'intégrer le script de génération du maillage directement dans le code du cas test
- Support pour I/O sur fichiers XDMF
- Sous-système pour génerer des visualisations très rapidement dans le code Python avant d'effectuer des post-processing plus poussés avec des outils externes
- Une installation très facile, qui ne nécessite pas de compiler des modules, et qui est basée sur les conventions de packaging offert par l'ecosystème de Python

.. break::

.. title:: notre vision pour le futur

La vision du projet pour le futur est d'offrir un outil très simple à utiliser, depuis Python, sans devoir renoncer à une performance acceptable, avec la possibilité d'exploiter des architectures modernes de calcul comme les GPU. Dans ce sens, les points suivants sont envisagés pour le futur

.. highlights::

    - Amélioration du mailleur intégré pour arriver à offrir la possibilité de générer des maillages structurés par blocs, possiblement avec des générations hyperboliques ou elliptiques
    - Puisque le code exploite l'API de NumPy, permettre le calcul sur GPU devient un développement naturel avec la librairie cupy
    - Intégration de schémas d'ordre élevé avec la méthode Galerkin Discontinu
    - Une interopérabilité avec le code **Samurai** pour pouvoir traiter aussi des maillages adaptatifs

