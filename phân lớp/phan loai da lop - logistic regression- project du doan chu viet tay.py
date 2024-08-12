import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

data = datasets.load_breast_cancer(return_X_y= True, as_frame= True)
#data = pd.concat([data[0], data[1]], axis = 1)
print(data[1])