"""
import math
r = 0.43


C = 2 * r * math.pi

A = math.pi * r ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
"""

# Selective Import

from math import radians
r = 192500


dist = r * radians(12)

print(dist)
