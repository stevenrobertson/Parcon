
"""
This module provides various classes for specifying what a particular syntax
diagram (a.k.a. railroad diagram) should look like.

The actual drawing of diagrams created with classes in this module is left up
to other modules included with Parcon in order to allow railroad diagrams that
look different to be created. The main one of these is the submodule raildraw,
which is a from-scratch railroad diagram drawing engine that can take a
railroad diagram as specified by classes in this module and convert it to a PNG
image.

Here's a really simple example that uses raildraw to draw a syntax diagram:

from parcon import First
from parcon.railroad import create_railroad
from parcon.railroad.raildraw import draw_to_png
# Create a parser to draw
some_parser = "Hello, " + First("world", "all you people")
# Then draw a diagram of it.
draw_to_png(create_railroad(some_parser, {}), "test.png")
"""

PRODUCTION = 1
TEXT = 2
ANYCASE = 3
DESCRIPTION = 4

class Component(object):
    pass


class Nothing(Component):
    pass


class Then(Component):
    def __init__(self, *constructs):
        self.constructs = list(constructs)


class Or(Component):
    def __init__(self, *constructs):
        self.constructs = list(constructs)


class Token(Component):
    def __init__(self, type, text):
        assert type >= 1 and type <= 4
        self.type = type
        self.text = text


class Loop(Component):
    def __init__(self, component, delimiter):
        self.component = component
        self.delimiter = delimiter


class Railroadable(object):
    def create_railroad(self, options):
        raise NotImplementedError


def create_railroad(value, options):
    if not isinstance(value, Railroadable):
        raise Exception("Trying to create a railroad diagram for an object of "
                        "class " + str(type(value)) + " but that type is not a "
                        "subclass of Railroadable, so this is not allowed.")
    return value.create_railroad(options)



































