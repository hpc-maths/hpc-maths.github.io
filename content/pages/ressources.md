title: Ressources

### Mésocentre Cholesky

La connaissance des architectures de calcul les plus récentes est un point-clef dans le développement de nouveaux schémas numériques. En effet, en plus de posséder de bonnes propriétés mathématiques, un schéma numérique doit aussi savoir tirer parti des machines sur lesquelles il s'execute. Ainsi, lors de la conception de nouveaux schémas, l'accès simple à des plateformes de calcul est un atout important pour tester et montrer l'efficacité des schémas.

A l'echelle de l'école Polytechnique, le développement d'un mésocentre est la bonne cible d'équipement à viser.
En effet, un mésocentre propose une machine de quelques milliers de coeurs mutualisées à l’échelle de plusieurs laboratoires, voire de plusieurs établissements. Il offre l'intérêt, pour les laboratoires, de mutualiser l’acquisition des serveurs et permet de tester de nouveaux algorithmes parallèles et de préparer le passage à l’échelle des codes et constituent un tremplin vers les centres nationaux et européens.
Dans le cadre de l'initiative, un soutien a été apporté pour renouveler une machine déjà mutualisé entre les laboratoire CMAP, CMLS, CPHT et LPP. Cette nouvelle machine de plus de 1600 coeurs de calcul et équipé de plusieurs cartes GPU de dernière génération est opérationnelle depuis avril 2021. Sa puissance de calcul devrait rapidement augmenter avec l'intégation d'autres partenaires de l'école et de l'IP-PARIS (LMS, l'UMA de l'ENSTA).

Les recrutements réalisés dans le cadre de l'initiative ont permis de mettre en place une unité de service dont la mission est de mettre en place et assurer le fonctionnement d’un socle technique de haut niveau sur lequel doivent s’appuyer des projets structurants de l'école. Ainsi, l'administration et le bon fonctionnement de la machine du mésocentre est assuré par les ingénieurs système et réseau de l'unité et l'accompagnement des chercheurs pour son utilisation optimale est la mission des ingénieurs calcul de l'unité. 


### JupyterHub

Jupyter est une application web permettant de réaliser des documents contenant à la fois du texte formatté (en markdown), des images ou des vidéos, du code directement exécutable. Grâce au caractère interactif que lui confère la possibilité de visualiser du code et de l’exécuter dans la même interface utilisateur, le projet Jupyter connaît un engouement croissant auprès de la communauté scientifique, de la communauté des enseignants et de la communauté industrielle.

Pour l'enseignement, l'intérêt de Jupyter reside dans l'interactivité de l'outil. L’élève n’est plus passif. Il peut reprendre le notebook et tester le code fourni par l’enseignant. Il peut ainsi changer les paramètres de la simulation, changer la méthode numérique, représenter les résultats d’une autre façon.

Pour la recherche, Jupyter peut répondre à la problématique de la reproductibilité des résultats obtenus par un nouvel méthode numérique dans un papier de recherche. Grâce aux notebooks, il est possible de présenter un schéma numérique comme dans une publication classique mais aussi d'accompagner sa description de som implémentation directement executable. Jupyter devient alors nouvel outil pour diffuser des travaux de recherche en particulier dans l'analyse numérique.

Jupyter est une application de type client serveur. Pour executer un notebook, la même machine peut tenir les rôles du client et du serveur mais il est également possible d’utiliser un serveur distant pour le serveur. Dans ce cas, l'utilisateur exécute le code contenu dans le notebook sur le serveur distant et le résultat s'afiche sur sa machine. C’est le principe d’un JupyterHub qui est en train d’être mis en place à l'école Polytechnique. Dans le cadre de l'initiative, plusieurs études ont été menés pour mettre à disposition ce type de service dont les conclusions sont :
- de s'adresser à une fournisseur de services "cloud" pour la partie enseignement (discussion en cours avec OVHcloud);
- de participer à un cloud institutionelle déjà en service pour la partie recherche (discussion avec le mesocentre DataCenter@UPSud pour étendre l'infrastructure cloud : https://www.mesocentre.u-psud.fr/services/cloud.html).

