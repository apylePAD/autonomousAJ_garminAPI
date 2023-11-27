# autonomousAJ_garminAPI/autonomousAJ_garminAPI/auth.py
import os
from dotenv import load_dotenv
from garminconnect import Garmin

load_dotenv()

class Get_Garmin_Client:
    def __init__(self):
        self.username = os.getenv("GARMIN_USERNAME")
        self.password = os.getenv("GARMIN_PASSWORD")

    def get_garmin_client(self):
        username = self.username
        password = self.password

        api = Garmin(username, password)
        api.login()
        
        return api

garmin_client = Get_Garmin_Client()