import os,sys,csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

#os.system('python3 RKR_GST.py')


directory = sys.argv[1]
result = directory+"/results/result.csv"

with open(result,'r') as ft:
    header = ft.readline()
    files = header.split(',')
    files[len(files)-1] = files[len(files)-1].split('\n')[0]


data = np.genfromtxt(result, dtype=float, delimiter=',', skip_header=1) 


x = np.linspace(0, len(files), len(files))
y = np.linspace(0, len(files), len(files))
X, Y = np.meshgrid(x, y)


if not os.path.exists(directory+"/plots"):
    os.makedirs(directory+"/plots")


fig = plt.figure(figsize=(6,6))

ax1 = fig.add_subplot(111,projection='3d')

ax1.set_xlabel('filesMarkers')
ax1.set_zlabel("Similarity Measure")
my_col = cm.jet(data/np.amax(data))
surf = ax1.plot_surface(X, Y, data, cmap = cm.coolwarm, linewidth=0, antialiased=False)
#ax.view_init(elev=10., azim=180)
#surf = ax.contour3D(X, Y, data, 50, cmap='binary')
ax1.set_zlim(0, 1)
ax1.zaxis.set_major_locator(LinearLocator(10))
ax1.zaxis.set_major_formatter('{x:.02f}')

fig.colorbar(surf,orientation="horizontal")
plt.savefig(directory+"/plots/surfacePlot.png",dpi=120)
plt.close()

fig = plt.figure(figsize=(4,4))
heatmap = plt.pcolor(data,cmap=cm.coolwarm)
fig.colorbar(heatmap)
plt.savefig(directory+"/plots/heatmap.png")
plt.close()


with open(directory+"/plots/markers.txt",'w') as Markers:
    for i in range(len(files)):
        Markers.write(str(i)+": "+files[i]+"\n")
