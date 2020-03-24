# load_and_combine_data.py 
#%%
#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype
import glob

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
#%%

#%%
data_dir = "data"
import os
main_path = "/Users/g/Dropbox/DS_Notebooks/Exploring Resale Flat/"
directory = os.path.join(main_path,"data_dir")

print(directory)
#%%

#%%
glued_data = pd.DataFrame()
for file_name in glob.glob(directory+'*.csv'):
    print(file_name)
    x = pd.read_csv(file_name, low_memory=False)
    print(x.head())
    glued_data = pd.concat([glued_data,x],axis=0)

print(glued_data.head())
#%%