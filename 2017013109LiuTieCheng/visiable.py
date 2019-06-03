#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import matplotlib
import numpy as np

class plot:
  def setTitle(self, title):
    plt.title(title)

  def showPlot(self):
    plt.show()

  def genHistogram(self, array, bins):
    a = np.array(array)
    plt.hist(a, bins)
