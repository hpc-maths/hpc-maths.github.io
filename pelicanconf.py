#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import math

AUTHOR = "Marc Massot"
SITENAME = "HPC@Maths"
SITEURL = "/site"
# SITEURL = 'http://localhost:8000'

PATH = "content"

TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "fr"

OUTPUT_PATH = "public/"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites", "code_directive"]

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
I18N_TEMPLATES_LANG = "fr"

# Theme
THEME = "themes/hpc_math_theme"

HIDE_SIDEBAR = True
BANNER = "images/banner.jpg"
BANNER_ALL_PAGES = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

DATE_FORMATS = {"fr": ""}
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SLUGIFY_SOURCE = "basename"

MENUITEMS = [
    ("Présentation", "/index.html"),
    ("Codes", "/pages/codes.html"),
    ("Enseignements", "/pages/enseignements.html"),
    ("Recherche", "/pages/recherche.html"),
    ("Événements", "/pages/events.html"),
    ("Partenaires", "/pages/partenaires.html"),
    ("Ressources", "/pages/ressources.html"),
]

PARTNERS = {
    "entreprises": {
        "title": "Nos liens avec des entreprises de pointe à fort potentiel d'innovation",
        "description": """
                    Nous développons des interactions fortes avec des entreprises positionnées à la pointe au niveau technologique pour lesquelles nos  contributions au développement de nouvelles générations de méthodes mathématiques et méthodes numériques, voire des implémentations novatrices sur diverses architectures de calcul, aide de manière essentielle à soutenir l’innovation.
                """,
        "list": {
            "Air Liquide": {
                "description": "Leader mondial des gaz, technologies et services pour l’industrie et la santé",
                "url": "https://www.airliquide.com/fr",
                "img": "../images/partenaires/entreprises/AirLiquide.png",
            },
            "Cenaero": {
                "description": "Centre de recherche appliquée privé qui fournit des méthodes et des outils de simulation numérique",
                "url": "https://www.cenaero.be/",
                "img": "../images/partenaires/entreprises/Cenaero.png",
            },
            "Lockheed": {
                "description": "Première entreprise américaine et mondiale de défense et de sécurité",
                "url": "https://www.lockheedmartin.com/",
                "img": "../images/partenaires/entreprises/Lockheed.png",
            },
            "Safran": {
                "description": "Groupe international opérant dans les domaines de l'aéronautique, de l'espace et de la défense",
                "url": "https://www.safran-group.com/",
                "img": "../images/partenaires/entreprises/Safran.png",
            },
        },
    },
    "instituts": {
        "title": "Nos coopérations avec des instituts de recherche stratégiques",
        "description": """
                    L’innovation dans le domaine des « Computational Sciences » est aussi très active dans diverse organes de recherche stratégiques de la recherche française et internationale. Nous coopérons donc naturellement avec un ensemble d’institutions pour lesquelles notre spécificité en mathématiques et analyse numérique est importante.
                """,
        "list": {
            "CEA": {
                "description": "Commissariat à l'énergie atomique et aux énergies alternatives",
                "url": "https://www.cea.fr/",
                "img": "../images/partenaires/entites_gouvernementales/Cea.png",
            },
            "DGA": {
                "description": "Direction Générale de l'Armement",
                "url": "https://www.defense.gouv.fr/dga",
                "img": "../images/partenaires/entites_gouvernementales/DGA.png",
            },
            "ESA": {
                "description": "European Space Agency",
                "url": "https://www.esa.int/",
                "img": "../images/partenaires/entites_gouvernementales/Esa.png",
            },
            "IFPEN": {
                "description": "IFP énergies nouvelles",
                "url": "https://www.ifpenergiesnouvelles.fr",
                "img": "../images/partenaires/entites_gouvernementales/Ifpen.jpg.png",
            },
            "NASA": {
                "description": "National Aeronautics and Space Administration",
                "url": "https://www.nasa.gov",
                "img": "../images/partenaires/entites_gouvernementales/Nasa.png",
            },
            "ONERA": {
                "description": "Office national d'études et de recherches aérospatiales",
                "url": "https://www.onera.fr/fr",
                "img": "../images/partenaires/entites_gouvernementales/Onera.png",
            },
            "JAXA": {
                "description": "Japan Aerospace Exploration Agency",
                "url": "https://global.jaxa.jp",
                "img": "../images/partenaires/entreprises/Jaxa.png",
            },
        },
    },
    "labos": {
        "title": "NOS PARTENAIRES UNIVERSITAIRES en france et à l'international",
        "description": """
                    Le domaine à l’interface entre les mathématiques appliquées et le calcul haute performance est présent dans diverses Laboratoires de recherche au sein de nombreuses universités françaises et à l’étranger et nous avons construit un ensemble de partenariats avec un certain nombre d’entre eux au cours de ces dernières années.
                """,
        "list": {
            "Centrale Supélec": {
                "description": "Centrale Supélec",
                "url": "https://www.centralesupelec.fr/",
                "img": '../images/partenaires/universites/CentraleSupelec.png"',
            },
            "ICME": {
                "description": "Institute for Computational & Mathematical Engineering",
                "url": "https://icme.stanford.edu/",
                "img": '../images/partenaires/universites/ICME.png"',
            },
            "INP-Toulouse": {
                "description": "Institut national polytechnique de Toulouse",
                "url": "https://www.inp-toulouse.fr/",
                "img": '../images/partenaires/universites/Inpt.png"',
            },
            "Institut Camille Jordan": {
                "description": "Institut Camille Jordan",
                "url": "http://math.univ-lyon1.fr/",
                "img": '../images/partenaires/universites/ICJ.png"',
            },
            "Institut Maths Bordeaux": {
                "description": "Institut de Mathématiques de Bordeaux",
                "url": "https://www.math.u-bordeaux.fr",
                "img": '../images/partenaires/universites/Imb.jpg.png"',
            },
            "Institut de Mécanique des fluide Toulouse": {
                "description": "Institut de Mécaniques des Fluides de Toulouse",
                "url": "https://www.imft.fr",
                "img": '../images/partenaires/universites/Imft.png"',
            },
            "IOWA state University": {
                "description": "Iowa State University",
                "url": "https://www.iastate.edu/",
                "img": '../images/partenaires/universites/Iowa.png"',
            },
            "Mathématiques Orsay": {
                "description": "Institut de Mathématiques d'Orsay",
                "url": "https://www.imo.universite-paris-saclay.fr",
                "img": '../images/partenaires/universites/IMO.png"',
            },
            "Oden Institute": {
                "description": "Oden Institute for Computational Engineering & Sciences",
                "url": "https://www.oden.utexas.edu",
                "img": '../images/partenaires/universites/Oden_Institute_wm.png"',
            },
            "POLITECHNICO MILANO": {
                "description": "Politechnico Milano",
                "url": "https://www.polimi.it",
                "img": '../images/partenaires/universites/Politecnico.png"',
            },
            "STANFORD": {
                "description": "Stanford University",
                "url": "https://www.stanford.edu/",
                "img": '../images/partenaires/universites/Stanford.png"',
            },
            "Université Côte d'Azur": {
                "description": "Université Côte d'Azur",
                "url": "https://univ-cotedazur.fr/",
                "img": '../images/partenaires/universites/Uca.png"',
            },
            "University of Toronto": {
                "description": "University of Toronto",
                "url": "https://www.utoronto.ca",
                "img": '../images/partenaires/universites/Utias.png"',
            },
            "Von Karman Institute": {
                "description": "Von Karman Institute for Fluid Dynamics",
                "url": "https://www.utoronto.ca",
                "img": '../images/partenaires/universites/Vki.png"',
            },
        },
    },
}


# LOGOS = os.listdir('content/images/logo')
# LOGOS.sort()
# LOGOS_NCOLS = 3
# LOGOS_NROWS = math.ceil(len(LOGOS)/LOGOS_NCOLS)
# print(len(LOGOS))
# print(LOGOS)
