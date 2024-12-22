from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np
from matplotlib import cm

fig ,ax = plt.subplots(figsize=(5,5),subplot_kw ={'projection':'3d'})

def update(num):
    plot[0].remove()
    Z =c[num]* np.sinh(u)
    zmin, zmax = ax.get_zlim()
    if Z[0,0] <= zmin:
        ax.set_zlim(2*zmin, 2*zmax)
    plot[0] = ax.plot_surface(X, Y, Z, cmap=cm.viridis)

u = np.linspace(-3,3,100)
v = np.linspace(0, 2 * np.pi, 100)
u,v = np.meshgrid(u,v)

a=1
b=1
c=np.linspace(0,10,100)

X =a* np.cosh(u)*np.cos(v)
Y =b* np.cosh(u)*np.sin(v)
Z =c[0]* np.sinh(u)

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_zlim(-10,10)
#ax.set_aspect('equal')
ax.view_init(elev=15, azim=-60)

plot= [ax.plot_surface(X, Y, Z,alpha=0.8, cmap=cm.viridis)]

ani = animation.FuncAnimation(fig, update, 100, interval=100)
for i in range(10) :
    plt.show()
    plt.savefig("temp{}.png".format(i))

#dpi=100
#ani.save('hyperboloid_extend.mp4', writer="ffmpeg",dpi=dpi)
