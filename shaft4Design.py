from symbeam import beam
#from sympy.abc import L, E, I, P, M, q, x
import matplotlib.pyplot as plt
import numpy as np
import sys

E = 30000000
R = 1
I = np.pi/4*np.power(R,4)
L = 12


shaft4y = beam(L)
# shaft4y.set_young(x_start, x_end, value)
shaft4y.set_young(0, L, E)

# shaft4y.set_inertia(x_start, x_end, value)
shaft4y.set_inertia(0, L, I)


# shaft4y.add_support(x_coord, type)
shaft4y.add_support(0, 'pin')
shaft4y.add_support(L, 'roller')

shaft4y.add_point_load(3,49.98)

shaft4y.solve()

shaft4y.plot()
plt.savefig("pdfs/shaft4y.png")
#plt.title("Deflection in the y on shaft1")

#plt.show(block=True)

print("Begin Z stresses")
plt.clf()
shaft4z = beam(L)
# shaft4z.set_young(x_start, x_end, value)
shaft4z.set_young(0, L, E)

# shaft4z.set_inertia(x_start, x_end, value)
shaft4z.set_inertia(0, L, I)


# shaft4z.add_support(x_coord, type)
shaft4z.add_support(0, 'pin')
shaft4z.add_support(L, 'roller')

shaft4z.add_point_load(3, -53.44)



shaft4z.solve()

shaft4z.plot()
plt.savefig("pdfs/shaft4z.png")
#plt.title("Deflection in the z on shaft1")
#plt.show(block=True)

#plt.savefig("beam.pdf")