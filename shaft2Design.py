from symbeam import beam
#from sympy.abc import L, E, I, P, M, q, x
import matplotlib.pyplot as plt
import numpy as np


E = 30000000
R = .5
I = np.pi/2*np.power(R,4)
L = 13
print(I)

shaft2y = beam(L)
# shaft2y.set_young(x_start, x_end, value)
shaft2y.set_young(0, L, E)

# shaft2y.set_inertia(x_start, x_end, value)
shaft2y.set_inertia(0, L, I)


# shaft2y.add_support(x_coord, type)
shaft2y.add_support(0, 'pin')
shaft2y.add_support(L, 'roller')

shaft2y.add_point_load(10, 55.33)

shaft2y.solve()

shaft2y.plot()
plt.savefig("pdfs/shaft2y.png")
#plt.title("Deflection in the y on shaft1")

#plt.show(block=True)

print("Begin Z stresses")
plt.clf()
shaft2z = beam(L)
# shaft2z.set_young(x_start, x_end, value)
shaft2z.set_young(0, L, E)

# shaft2z.set_inertia(x_start, x_end, value)
shaft2z.set_inertia(0, L, I)


# shaft2z.add_support(x_coord, type)
shaft2z.add_support(0, 'pin')
shaft2z.add_support(L, 'roller')

shaft2z.add_point_load(10, 123.78)



shaft2z.solve()

shaft2z.plot()
plt.savefig("pdfs/shaft2z.png")
#plt.title("Deflection in the z on shaft1")
#plt.show(block=True)

#plt.savefig("beam.pdf")