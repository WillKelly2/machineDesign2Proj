from symbeam import beam
#from sympy.abc import L, E, I, P, M, q, x
import matplotlib.pyplot as plt
import numpy as np


E = 30000000
R = .625
I = np.pi/2*np.power(R,4)

Wgear1 = 
Wgear2 = 
Wgear3 = 
print(I)

shaft1w = beam(27)
# shaft1w.set_young(x_start, x_end, value)
shaft1w.set_young(0, 27, E)

# shaft1w.set_inertia(x_start, x_end, value)
shaft1w.set_inertia(0, 27, I)


# shaft1w.add_support(x_coord, type)
shaft1w.add_support(0, 'pin')
shaft1w.add_support(27, 'roller')

shaft1w.add_point_load(6, 37.14)
shaft1w.add_point_load(15, -55.33)
shaft1w.add_point_load(22, -49.98)


shaft1w.solve()

shaft1w.plot()