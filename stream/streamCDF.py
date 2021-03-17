import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math

from netCDF4 import Dataset
from ncscan import ncscan
import sys

from matplotlib.collections import LineCollection

'''
Importing data and creating the streamplot/histogram
'''

#creates a 1440x1080 grid
Y, X = np.mgrid[0:1080, 0:1440]

#sets up 2D arrays for U and V components
U = [[]for i in range(1440)]
V = [[]for i in range(1080)]
counter = 0; #to keep track of the index within the array

try:
    uFile = sys.argv[1]
    vFile = sys.argv[2]
except:
    uFile = 'ssu.nc'
    vFile = 'ssv.nc'

#import ssu.nc
u = Dataset(uFile,"r")
ssu = u.variables["ssu"]

v = Dataset(vFile,"r")
ssv = v.variables["ssv"]

print(ssu)
print(ssv)

#converts into numpy arrays
U = ssu.__array__();
V = ssv.__array__();

U = np.delete(U, 1440, axis=2)
V = np.delete(V, 1080, axis=1)

print(U[0][14][1])
print(V[1][80][1])

yes = 0;

for i in range(len(U)):
    for j in range(len(U[0])):
        for k in range(len(U[0][0])):
            if U[i][j][k] >= (10**20):
                U[i][j][k] = 0;
                yes = 1;

for i in range(len(V)):
    for j in range(len(V[0])):
        for k in range(len(V[0][0])):
            if U[i][j][k] >= (10**20):
                U[i][j][k] = 0;

speedTemp = np.sqrt(U[0]**2 + V[0]**2) #calculate magnitude of vector at each point

            

print("yes"+str(yes));
#quit();
        
#Streamline Graph
scale = 10
fig, ax0 = plt.subplots()
strm = ax0.streamplot(X, Y, U[0], V[0], linewidth=1)#speedTemp*scale)
ax0.set_title('Streamline Graph')
ax0.autoscale()
ax0.margins(0.1)

plt.show()

#to make a 1D array of the magnitudes for the histogram
spd=[]
for i in range(len(speedTemp)):
    for j in range(len(speedTemp[0])):
        spd.append(speedTemp[i][j])

#Histogram
fig, ax1 = plt.subplots()
#ax1.set_xlim(0,1)
ax1.hist(spd, bins = 10)
plt.yscale('log')

'''
Exporting streamplot data
'''

#export line segment vertices
segs = strm.lines.get_segments()
out = open("vertices.txt", "w")
for line in range(len(segs)):
    #formatted as '(0,1),(2,3)' each line, each line is a line segment
    out.write("(" + str(segs[line][0][0]) + "," + str(segs[line][0][1]) + "),(" + str(segs[line][1][0]) + "," + str(segs[line][1][1]) + ")\n")
out.close()

#export line widths of each segment
lwTemp = strm.lines.get_linewidths()
out = open("lw.txt", "w")
for line in range(len(lwTemp)):
    out.write(str(lwTemp[line]/scale)+"\n") #divides by scale to get original magnitudes
out.close()

'''
Recreating streamplot with the exported data
'''

#importing the vertices
l = open("vertices.txt", "r")
ls = [] #list of line segment vertices
for line in l:
    #changes line to '0,1,2,3'
    line = line.replace('(','').replace(')','')

    #makes a list [0,1,2,3]
    nums = line.split(',')

    #converts to float and stores nums in tuples (0,1) (2,3)
    start = (float(nums[0]),float(nums[1]))
    end = (float(nums[2]),float(nums[3]))

    ls.append([start, end])
l.close()

lws = [] #list of line width for each segment
f_lw = open("lw.txt", "r")
for line in f_lw:
    lws.append(float(line))
f_lw.close()

lws = np.array(lws)

#creates linecollection for plotting
lc = LineCollection(ls, linewidth=lws*scale) #scale = 10

fig, ax = plt.subplots()

ax.add_collection(lc)
ax.set_title('Reproduced Streamplot')
ax.autoscale()

plt.show()



