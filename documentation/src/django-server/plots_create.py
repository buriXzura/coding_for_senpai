#Imports
import os,sys,csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

##the directory where the result csv file is present and the plots are to be saved
directory = sys.argv[1]
##the address of results.csv
result = directory+"/results/result.csv"


with open(result,'r') as ft:
    ##one line from results.csv
    header = ft.readline()
    ##a list obtained on splitting 'header' by commas
    files = header.split(',')
    ##stores the resulting output after removing '\n' from the last column of the csv file
    files[len(files)-1] = files[len(files)-1].split('\n')[0] #remove '\n' form the last column of csv file

##stores results.csv into an np array
data = np.genfromtxt(result, dtype=float, delimiter=',', skip_header=1)

#if plot required for a few selected files only
#extacting the data from the result file corresponding to the selected files
if sys.argv[2]=='S':
    ##stores the data from the result file corresponding to the selected files
    my_dict = {}
    for i in range(len(files)):
        my_dict[files[i]] = i
    #sys.argv[3] gives the files selected(ie , subset of total files)
    files = sys.argv[3].split(',')
    a = np.empty([len(files),len(files)])
    for i in range(len(files)):
        for j in range(len(files)):
            a[i][j] = data[my_dict[files[i]]][my_dict[files[j]]]
    data = a

#creating x and y axis dimensions and grid
x = np.linspace(0, len(files), len(files))
y = np.linspace(0, len(files), len(files))
X, Y = np.meshgrid(x, y)

#make directory if does not exist already
if not os.path.exists(directory+"/plots"):
    os.makedirs(directory+"/plots")

#set figure dimensions
fig = plt.figure(figsize=(6,6))

#plotting the surface plot
ax1 = fig.add_subplot(111,projection='3d')
ax1.set_xlabel('filesMarkers')
ax1.set_zlabel("Similarity Measure")
my_col = cm.jet(data/np.amax(data))
surf = ax1.plot_surface(X, Y, data, cmap = cm.coolwarm, linewidth=0, antialiased=False)

ax1.set_zlim(0, 1)
ax1.zaxis.set_major_locator(LinearLocator(10))
ax1.zaxis.set_major_formatter('{x:.02f}')
fig.colorbar(surf,orientation="horizontal")
#saving plot to the provided address
plt.savefig(directory+"/plots/surfacePlot.png",dpi=120)
plt.close()

#plotting heat map (ses colour gradient to depict values)
fig = plt.figure(figsize=(4,4))
heatmap = plt.pcolor(data,cmap=cm.coolwarm)
fig.colorbar(heatmap)
#saving heat map to this provided location
plt.savefig(directory+"/plots/heatmap.png")
plt.close()

#write to a txt file the files corrosponding to the x marks in the graphs(i.e.) key to the plot axis markers
with open(directory+"/plots/markers.txt",'w') as Markers:
    for i in range(len(files)):
        Markers.write(str(i)+": "+files[i]+"\n")
