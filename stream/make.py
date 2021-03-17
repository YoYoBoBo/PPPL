import numpy as np
import pylab as pl
import matplotlib.gridspec as gridspec
from matplotlib import collections  as mc

u_raw = np.loadtxt( 'u.dat' )
v_raw = np.loadtxt( 'v.dat' )

x_data = []
y_data = []
u_data = []
v_data = []

xtemp = []
for x in range(0, 300):
    xtemp.append(x+1)

for x in range(0, 300):
    x_data.append(np.array(xtemp))

ytemp = []
for x in range(0, 300):
    ytemp.append(x+1)

for x in range(0, 300):
    y_data.append(np.array(ytemp))

for x in range(0, 300):
    temp = []
    for y in range(0,300):
        temp.append(u_raw[300*x + y])
    u_data.append(np.array(temp))

for x in range(0, 300):
    temp = []
    for y in range(0,300):
        temp.append(v_raw[300*x + y])
    v_data.append(np.array(temp))

y_numpy, x_numpy = np.mgrid[0:300, 0:300]
u_numpy = np.array(u_data)
v_numpy = np.array(v_data)

speedTemp = np.sqrt(u_numpy**2 + v_numpy**2)
'''
for i in range(len(speedTemp)):
    for j in range(len(speedTemp[i])):
        if speedTemp[i][j]>3:
            print(speedTemp[i][j])

print("\n\n")
'''
done = False
segments = []
speed = []

fig, ax0 = pl.subplots()
strm = ax0.streamplot(x_numpy, y_numpy, u_numpy, v_numpy, linewidth=speedTemp*10, cmap='autumn')
ax0.set_title('Data')
ax0.margins(0.1)

segs = strm.lines.get_segments()

lw = strm.lines.get_linewidths()
'''
print(lw)


out = open("lw.txt", "w")

for line in range(len(lw)):
    out.write(str(lw[line])+"\n")


'''

f = open("vertices.txt", "r")

while not done:
    line = str(f.readline())
    if line == "done":
        done = True
    else:
        line = line.replace('(', '')
        line = line.replace(')', '')

        nums = line.split(",")
        temp = [(nums[0], nums[1]), (nums[2], nums[3])]
        segments.append(temp)
        '''
        sx = int(float(nums[0]))
        sy = int(float(nums[1]))
        '''
        sx = int(round((float(nums[0])+float(nums[2]))/2))
        sy = int(round((float(nums[1])+float(nums[3]))/2))
    
        speed.append(speedTemp[sy][sx])
#print(speed)



for i in range(len(speed)):
    '''
    if speed[i]>3:
        print(speed[i])
        speed[i] = 1
    '''
    speed[i] = speed[i]*10


        
lc = mc.LineCollection(segments,  linewidths=lw)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)

pl.show()
