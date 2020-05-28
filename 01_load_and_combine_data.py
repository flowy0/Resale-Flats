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
import os
print(os.getcwd())

raw_dir = "data/raw"
processed_dir = "data/processed"
#main_path = os.getcwd()


#print(directory)
#%%
#https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py

print(os.getcwd()+raw_dir)
os.chdir(os.getcwd()+raw_dir)

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

#combine all files in the list
#combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
#combined_csv.to_csv( processed_dir+"combined_csv", index=False, encoding='utf-8-sig')


#%%


#%%