#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymongo

class mongo:
  """class mongo:
  This class is used to perform operations on a specific database.

  No attributes needed.
  """

  def dbSelect(self, host, port, dbName):
    """First connect to Mongo on host:port, then select the dbName database"""
    client = pymongo.MongoClient(host=host, port=port)
    db = client.dbName
    return db

  def collectionSelect(self, dbName, collectionName):
    """Select a collection called collectionName in database dbName"""
    collection = dbName.collectionName
    return collection

  def dataInsert(self, collectionName, data):
    """
    Insert a data into collection collectionName
    Return an InsertOneResult object
    """
    result = collectionName.insert(data)
    return result

  def dataFind(self, collectionName, catagory, data):
    """
    Find a data by appointing a catagory and a data
    Return a dict including _id.
    """
    result = collectionName.find_one({catagory: data})
    return result

  def dataCount(self, collectionName):
    """
    Count the data in collection collectionName
    Return the count
    """
    count = collectionName.find().count()
    return count

  def dataCountBy(self, collectionName, catagory, data):
    """
    Find the data by appointing catagory and data first, then count
    Return the count
    """
    count = collectionName.find({catagory: data}).count()
    return count

  def dataSort(self, collectionName, catagory, method='ASCENDING'):
    """
    Sort the data by catagory, method can be specified.
    Return the sorted collection
    """
    if method == 'ASCENDING':
      results = collectionName.find().sort(catagory, pymongo.ASCENDING)
    elif method == 'DESCENDING':
      results = collectionName.find().sort(catagory, pymongo.DESCENDING)
    return results

  def dataUpdate(self, collectionName, findCat, findData, updateCat, updateData):
    """
    Update a specific data after finding it
    Return an UpdateResult
    """
    condition = {findCat: findData}
    findRes = collectionName.find_one(condition)
    findRes[updateCat] = updateData
    result = collectionName.update(condition, findRes)
    return result

  def dataDelete(self, collectionName, catagory, data):
    """
    Delete a data
    Return a DeleteResult
    """
    result = collectionName.delete_one({catagory: data})
    return result
