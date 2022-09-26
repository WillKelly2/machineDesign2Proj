from symbeam import beam
#from sympy.abc import L, E, I, P, M, q, x
import matplotlib.pyplot as plt
import numpy as np


E = 30000000
R = .5
I = np.pi/2*np.power(R,4)
L = 7
print(I)

shaft3y = beam(L)
# shaft3y.set_young(x_start, x_end, value)
shaft3y.set_young(0, L, E)

# shaft3y.set_inertia(x_start, x_end, value)
shaft3y.set_inertia(0, L, I)


# shaft3y.add_support(x_coord, type)
shaft3y.add_support(0, 'pin')
shaft3y.add_support(L, 'roller')

shaft3y.add_point_load(3, -37.14)

shaft3y.solve()

shaft3y.plot()
#plt.title("Deflection in the y on shaft1")

plt.show(block=True)

print("Begin Z stresses")
shaft3z = beam(L)
# shaft3z.set_young(x_start, x_end, value)
shaft3z.set_young(0, L, E)

# shaft3z.set_inertia(x_start, x_end, value)
shaft3z.set_inertia(0, L, I)


# shaft3z.add_support(x_coord, type)
shaft3z.add_support(0, 'pin')
shaft3z.add_support(L, 'roller')

shaft3z.add_point_load(3, -83.10)



shaft3z.solve()

shaft3z.plot()
#plt.title("Deflection in the z on shaft1")
plt.show(block=True)

#plt.savefig("beam.pdf")