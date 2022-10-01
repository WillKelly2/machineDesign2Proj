from symbeam import beam
#from sympy.abc import L, E, I, P, M, q, x
import matplotlib.pyplot as plt
import numpy as np


E = 30000000
R = .441
I = np.pi/2*np.power(R,4)


print(I)

shaft1w = beam(12)
# shaft1w.set_young(x_start, x_end, value)
shaft1w.set_young(0, 12, E)

# shaft1w.set_inertia(x_start, x_end, value)
shaft1w.set_inertia(0, 12, I)


# shaft1w.add_support(x_coord, type)
shaft1w.add_support(0, 'pin')
shaft1w.add_support(12, 'roller')

shaft1w.add_point_load(3, -2.689)
#shaft1w.add_point_load(15, -.9120)
#shaft1w.add_point_load(22, -6.0512)


shaft1w.solve()

