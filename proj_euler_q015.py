# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?
from math import factorial

lengthUnits = 20
breadthUnits = 20

totalPerimeter = lengthUnits + breadthUnits

totalRoutes = factorial(totalPerimeter)/(factorial(lengthUnits)*factorial(breadthUnits))

print ("Total routes for the 20x20 grid are %d" %(totalRoutes))