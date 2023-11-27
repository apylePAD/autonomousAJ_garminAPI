# autonomousAJ_garminAPI/autonomousAJ_garminAPI/api/user_summary.py
# Endpoint: user_summary
# URL: nan
import requests
from .base import Garmin_API_Base

class User_Summary(Garmin_API_Base):
    def get_user_summary(self):
        app_id, access_token = self.get_garmin_client()

        url = "nan"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
                
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print("Locations:", data)
        else:
            print("Failed to retrieve locations. Status code:", response.status_code)
            print("Response:", response.text)

        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Error:", e)