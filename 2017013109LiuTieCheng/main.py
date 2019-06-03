#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from randomGen import *
from db import *
from visiable import *

if __name__ == '__main__':
  maindb = mongo().dbSelect('localhost', 27017, 'maindb')
  collection = mongo().collectionSelect(maindb, 'mainColle')
  for i in dateGenerate().dGen():
    mongo().dataInsert(collection, i)

  """Generate histogram by birth year"""
