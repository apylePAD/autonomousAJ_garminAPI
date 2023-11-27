# autonomousAJ_garminAPI/autonomousAJ_garminAPI/api/full_name.py
# Endpoint: full_name
# URL: nan
import requests
from .base import Garmin_API_Base

class Full_Name(Garmin_API_Base):
    def get_full_name(self):
        api = self.get_garmin_client()

        full_name = api.get_full_name()
        
        return full_name