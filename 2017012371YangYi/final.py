import matplotlib.pyplot as plt

import numpy as np

from pymongo import MongoClient

from data_generate import Generate

from run_mongo import mongo

from visualization import matplot



if __name__ == '__main__':

    mongo.build()

    matplot.picture()
