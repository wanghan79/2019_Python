import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient
from Random_number import Generate
from import_mongo import mongo
from matplotlib_operation import matplot

if __name__ == '__main__':
    mongo.build()
    matplot.picture()