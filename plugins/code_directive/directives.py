import locale
from docutils.parsers.rst import directives, Directive
from docutils.parsers.rst.directives.parts import Contents
from docutils.transforms import frontmatter
from docutils.statemachine import StringList
from docutils import io, nodes
import dateutil.parser
from pelican import readers
from pelican.readers import PelicanHTMLTranslator

import re
from jinja2 import Environment, FileSystemLoader
import os
import logging

logger = logging.getLogger(__name__)

class title_element(nodes.General, nodes.Element):
    """ code element """

class subtitle_element(nodes.General, nodes.Element):
    """ code element """

class break_element(nodes.General, nodes.Element):
    """ code element """

class Break(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = False

    def run(self):
        return [break_element()]

class Title(Directive):
    required_arguments = 1
    final_argument_whitespace = True
    optional_arguments = 0
    has_content = False

    def run(self):
        node = title_element()
        node['text'] = self.arguments[0]
        return [node]

class SubTitle(Directive):
    required_arguments = 1
    final_argument_whitespace = True
    optional_arguments = 0
    has_content = False

    def run(self):
        node = subtitle_element()
        node['text'] = self.arguments[0]
        return [node]

class myHTMLTranslator(PelicanHTMLTranslator):
    """Extend default translator"""

    def __init__(self, *args, **kwargs):
        # Pre-loading Jinja2 templates
        super().__init__(*args, *kwargs)

    def visit_break_element(self, node):
        self.body.append('<break>')

    def depart_break_element(self, node):
        pass

    def visit_title_element(self, node):
        self.body.append(f'<h2 class="section_title text-left">{node["text"]}</h2>')

    def depart_title_element(self, node):
        pass

    def visit_subtitle_element(self, node):
        self.body.append(f'<h3 class="subtitle">{node["text"]}</h3>')

    def depart_subtitle_element(self, node):
        pass

# Overwrite default translator so that extensions can be chained
readers.PelicanHTMLTranslator = myHTMLTranslator

def register():
    directives.register_directive('break', Break)
    directives.register_directive('title', Title)
    directives.register_directive('subtitle', SubTitle)
