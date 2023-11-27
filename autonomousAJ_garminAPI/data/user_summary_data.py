# autonomousAJ_garminAPI/autonomousAJ_garminAPI/data/user_summary_data.py
# Endpoint: user_summary
# URL: {'proper_name': 'User_Summary', 'url': nan}
import pandas as pd
from autonomousAJ_garminAPI.api.user_summary import User_Summary
from autonomousAJ_garminAPI.config import global_config

class User_Summary_Data:
    def __init__(self):
        self.user_summary = User_Summary()

    def get_and_process_data(self):
        data = self.user_summary.get_user_summary()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
