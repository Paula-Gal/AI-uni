

import matplotlib.pyplot as plt

# get data from .tsp file
from utils.library import *

# citire
file = 'data/kroA100.tsp'
tsp_data = readData(file)

# afisare header fisier tsp
displayData(tsp_data)
