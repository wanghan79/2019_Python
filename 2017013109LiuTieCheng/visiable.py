#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import matplotlib
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class plot:
  def setTitle(self, title):
    plt.title(title)

  def showPlot(self):
    plt.show()

  def genHistogram(self, array, bins):
    a = np.array(array)
    plt.hist(a, bins)

  def draw3Dfig(self, x, y, z):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, y, z)
    return ax

  def set3DfigLabel(self, ax, xname, yname, zname):
    ax.set_xlabel(xname)
    ax.set_ylabel(yname)
    ax.set_zlabel(zname)