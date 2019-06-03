#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib as plt
import numpy as np

zhFont = matplotlib.font_manager.FontProperties(fname="SimHei.ttf")

class plot:
  def setTitle(self, title):
    plt.title(title, fontproperties=zhFont)

  def showPlot(self):
    plt.show()

  def
