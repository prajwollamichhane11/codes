import cmath
import math

AB = int(input())
BC = int(input())

A = complex(0, AB)
B = complex(0, 0)
C = complex(BC, 0)

MBC = int(round(math.degrees(cmath.phase(B + C + A))))
print(str(MBC) + "°")
