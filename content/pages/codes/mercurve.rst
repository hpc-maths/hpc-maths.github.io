:title: Mercurve
:subtitle: Outils de post-traitement
:date: 2023-01-01
:category: code
:logo: ../images/codes/mercurve/logo_mercurve.png
:source: https://gitlab.com/rubendibattista/mercurve
:documentation: https://docs.mercurve.rdb.is
:description: <span class="glossary_link">Mercurve</span> est une librairie en C++ qui permet d'effectuer le post-traitement de simulations DNS diphasiques. Mercurve effectue une triangulation de l'interface entre les deux phases de l'écoulement, il calcule des propriétés géométriques comme la courbure moyenne et la courbure de Gauss avec une approche qui préserve certains invariants topologiques, en donnant la possibilité d'obtenir plus d'information à travers ces simulations qui sont après utilisées pour le développement de modèles réduits.

.. title:: Mercurve en quelques mots

**Mercurve** est une librairie en C++ qui permet d'effectuer le post-traitement de simulations DNS diphasiques.

**Mercurve** effectue une triangulation de l'interface entre les deux phases de l'écoulement, il calcule des propriétés géométriques comme la courbure moyenne et la courbure de Gauss avec une approche qui préserve certains invariants topologiques, en donnant la possibilité d'obtenir plus d'information à travers ces simulations qui sont après utilisées pour le développement de modèles réduits.

Le code C++ est modulaire et permet potentiellement d'intégrer différentes façons de calculer les propriétés géométriques, différents type de fichier en entrée et sortie et plus.
