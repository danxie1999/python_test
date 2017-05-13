#!/usr/bin/env python3

from collections import namedtuple

Colour=namedtuple('Colour',['red','blue','yellow'])

color=Colour(55,45,75)

#print(Colour.__doc__)

Point=namedtuple('Point',['x','y'])
p=Point(3,2)
print(p.x)
print(Point.__doc__)

