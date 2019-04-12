#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymongo

class mongo:
  def dbConnect(self, dbhost='localhost', dbport=27017):
    return pymongo.MongoClient(host=dbhost, port=dbport)

  def dbSelect(self, clientName, dbName):
    return clientName.dbName

  def selCollection(self, dbName, collectionName):
    return dbName.collectionName

  def dataInsert(self, collectionName, data):
    collectionName.insert_one(data)

  def dataSort(self, collectionName, orderby, order='ASCENDING'):
    if order == 'ASCENDING':
      collectionName.find().sort(orderby, pymongo.ASCENDING)
    else:
      collectionName.find().sort(orderby, pymongo.DESCENDING)