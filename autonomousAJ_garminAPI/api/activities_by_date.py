# autonomousAJ_garminAPI/autonomousAJ_garminAPI/api/activities_by_date.py
# Endpoint: activities_by_date
import datetime
import requests
from .base import Garmin_API_Base
from autonomousAJ_garminAPI.config import global_config

class Activities_By_Date(Garmin_API_Base):
    def get_activities_by_date(self):
        api = self.get_garmin_client()

        start_date = datetime.date(2021, 1, 1)
        end_date = datetime.date(2021, 5, 31)

        activities = api.get_activities_by_date(
                        start_date.isoformat(), end_date.isoformat(), 'running')
        
        for activity in activities:
            print(activity)
            activity_id = activity["activityId"]
            gpx_data = api.download_activity(
                activity_id, dl_fmt=api.ActivityDownloadFormat.GPX
                )
            
            output_file = f"{global_config.BASE_PATH}/data_files/written_files/activities_by_date/{str(activity_id)}.KML"
            with open(output_file, "wb") as fb:
                fb.write(gpx_data)