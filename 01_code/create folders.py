
#create folder structures
import os 
import logging ,sys

def create_folders(list):
    for i in list:
        if not os.path.exists(i):
            os.makedirs(i)
            print("folder is created:" + i)

folder_log = ["logs"]
create_folders(folder_log)


#this sends the print statements to the log file
datestr = "%d/%m/%Y %I:%M:%S %p "
logging.basicConfig(level=logging.INFO , filename = r'logs/00_create_folders.log',filemode="w", datefmt=datestr)
logger = logging.getLogger()
sys.stderr.write = logger.error
sys.stdout.write = logger.info


folder_list = ['data','models','logs']
create_folders(folder_list)



folder_data = ["raw","processed"]
os.chdir('data')
create_folders(folder_data)
