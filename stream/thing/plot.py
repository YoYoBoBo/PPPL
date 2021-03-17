import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.collections as collections
import pylab as pl
from netCDF4 import Dataset
import sys

w = 300
Y, X = np.mgrid[0:1080, 0:1440]
U = Dataset('ssu.nc', "r").variables['ssu'].__array__()
V = Dataset('ssv.nc', "r").variables['ssv'].__array__()
U = np.delete(U, 1440, axis=2)
V = np.delete(V, 1080, axis=1)
speed = np.sqrt(U[0]**2 + V[0]**2)


fig, ax = pl.subplots()
lw = speed / speed.max()
ax.streamplot(X, Y, U[0], V[0], linewidth = 10*lw)
ax.autoscale()
ax.margins(0.1)

pl.show()