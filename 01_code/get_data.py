  
import os
import settings
import pandas as pd
import logging ,sys ,glob

#this sends the print statements to the log file
datestr = "%d/%m/%Y %I:%M:%S %p "
logging.basicConfig(level=logging.INFO , filename = r'logs/01_load_data.log',filemode="w", datefmt=datestr)
logger = logging.getLogger()
sys.stderr.write = logger.error
sys.stdout.write = logger.info

def read():
    directory = os.path.join(settings.main_path, settings.dir_data)
    print(directory)

    #data = pd.read_csv(os.path.join(settings.PROCESSED_DIR, "Acquisition.txt"))
    
    glued_data = pd.DataFrame()
    for file_name in glob.glob(directory+'*.csv'):
        print(file_name)
        x = pd.read_csv(file_name, low_memory=False)
        #print(x.head())
        glued_data = pd.concat([glued_data,x],axis=0)
    return glued_data     

if __name__ == "__main__":
    df = read()
    print(df.head())
    #performance_summary = count_performance_rows()
    #acquisition = annotate(acquisition, performance_summary)
    #write(acquisition)

