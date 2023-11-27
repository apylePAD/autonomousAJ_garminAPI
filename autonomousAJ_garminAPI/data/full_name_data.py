# autonomousAJ_garminAPI/autonomousAJ_garminAPI/data/full_name_data.py
# Endpoint: full_name
# URL: {'proper_name': 'Full_Name', 'url': nan}
import pandas as pd
from autonomousAJ_garminAPI.api.full_name import Full_Name
from autonomousAJ_garminAPI.config import global_config

class Full_Name_Data:
    def __init__(self):
        self.full_name = Full_Name()

    def get_and_process_data(self):
        data = self.full_name.get_full_name()
        print(data)

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
