from symbeam import beam
#from sympy.abc import L, E, I, P, M, q, x
import matplotlib.pyplot as plt
import numpy as np
import sys

E = 30000000
R = 1
I = np.pi/4*np.power(R,4)


shaft1y = beam(27)
# shaft1y.set_young(x_start, x_end, value)
shaft1y.set_young(0, 27, E)

# shaft1y.set_inertia(x_start, x_end, value)
shaft1y.set_inertia(0, 27, I)


# shaft1y.add_support(x_coord, type)
shaft1y.add_support(0, 'pin')
shaft1y.add_support(27, 'roller')

shaft1y.add_point_load(6, 37.14)
shaft1y.add_point_load(15, -55.33)
shaft1y.add_point_load(22, -49.98)


shaft1y.solve()


shaft1y.plot()
plt.savefig("pdfs/shaft1y.png")
#plt.title("Deflection in the y on shaft1")

#plt.show(block=True)

print("Begin Z stresses")
plt.clf()
shaft1z = beam(27)
# shaft1z.set_young(x_start, x_end, value)
shaft1z.set_young(0, 27, E)

# shaft1z.set_inertia(x_start, x_end, value)
shaft1z.set_inertia(0, 27, I)


# shaft1z.add_support(x_coord, type)
shaft1z.add_support(0, 'pin')
shaft1z.add_support(27, 'roller')

shaft1z.add_point_load(6, 83.10)
shaft1z.add_point_load(15, -123.78)
shaft1z.add_point_load(22, 53.44)


shaft1z.solve()

shaft1z.plot()
#plt.title("Deflection in the z on shaft1")
#plt.show(block=True)

plt.savefig("pdfs/shaft1z.png")