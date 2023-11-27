# autonomousAJ_garminAPI/autonomousAJ_garminAPI/data/activities_by_date_data.py
# Endpoint: activities_by_date
# URL: {'proper_name': 'Activities_By_Date', 'url': nan}
import pandas as pd
from autonomousAJ_garminAPI.api.activities_by_date import Activities_By_Date
from autonomousAJ_garminAPI.config import global_config

class Activities_By_Date_Data:
    def __init__(self):
        self.activities_by_date = Activities_By_Date()

    def get_and_process_data(self):
        data = self.activities_by_date.get_activities_by_date()
        print(data)

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
