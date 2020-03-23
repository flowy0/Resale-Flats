  
import os
import settings
import pandas as pd

def read():
    
    data = pd.read_csv(os.path.join(settings.PROCESSED_DIR, "Acquisition.txt"))
    return data

if __name__ == "__main__":
    df = read()
    #performance_summary = count_performance_rows()
    #acquisition = annotate(acquisition, performance_summary)
    #write(acquisition)