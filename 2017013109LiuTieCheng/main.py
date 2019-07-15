#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from randomGen import *
from db import *
from visiable import *

if __name__ == '__main__':
  maindb = mongo().dbSelect('localhost', 27017, 'maindb')
  collection = mongo().collectionSelect(maindb, 'mainColle')
  '''
  for i in dataGenerate().dGen():
    print("Inserting ", i)
    mongo().dataInsert(collection, i)
  '''
  """Generate histogram by birth year"""
  """
  arr = collection.find({}, {'birth': 1, '_id': 0})
  array = []
  for res in arr:
    array.append(int(res['birth']))
  bins = [1970, 1975, 1980, 1985, 1990, 1995, 2000]
  a = np.array(array)
  plt.hist(a, bins)
  plt.show()
  """
  adata = collection.find({}, {'A': 1, '_id': 0})
  bdata = collection.find({}, {'B': 1, '_id': 0})
  cdata = collection.find({}, {'C': 1, '_id': 0})
  aarr = []
  barr = []
  carr = []
  for res in adata:
    aarr.append(int(res['A']))
  for res in bdata:
    barr.append(int(res['B']))
  for res in cdata:
    carr.append(int(res['C']))

  ax = plot().draw3Dfig(aarr, barr, carr)
  plt.show()