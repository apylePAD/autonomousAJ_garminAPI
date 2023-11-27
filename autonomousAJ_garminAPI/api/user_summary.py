# autonomousAJ_garminAPI/autonomousAJ_garminAPI/api/user_summary.py
# Endpoint: user_summary
# URL: nan
import requests
from datetime import datetime, timedelta
from .base import Garmin_API_Base

class User_Summary(Garmin_API_Base):
    def get_user_summary(self):
        api = self.get_garmin_client()

        today = datetime.now()
        user_summary = api.get_user_summary(today.isoformat())

        return user_summary