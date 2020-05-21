import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_dir = "." + os.sep + "rotation_curves" + os.sep # set data directory
filename = "rc4536.dat" # choose file to draw
df = pd.read_csv(data_dir + filename, delimiter='\s+', names=['radius', 'velocity']) # import
df.plot(kind='line', x='radius', y='velocity') # plot graph
plt.ylabel("velocity")
plt.show()
