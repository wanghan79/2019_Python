#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymongo

class mongo:
  def dbConnect(self, clientName='client'):
    clientName = pymongo.MongoClient(host='localhost', port=27017)

  def dbSelect(self, clientName='client', dbName='testDB'):
    pass

