class Polygon(object):
    """docstring for ."""

    def __init__(self, sides, name):
        self.sides = sides
        self.name = name

square = Polygon(4, "square")
pentagon = Polygon(5, "pentagon")
