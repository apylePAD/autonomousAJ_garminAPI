# autonomousAJ_garminAPI/run.py
import inquirer
from autonomousAJ_garminAPI.data.activities_by_date_data import Activities_By_Date_Data
from autonomousAJ_garminAPI.data.full_name_data import Full_Name_Data
from autonomousAJ_garminAPI.data.user_summary_data import User_Summary_Data

def main_menu():
    questions = [
        inquirer.List("choice",
                      message="What type of data would you like to interact with?",
                      choices=["Activities_By_Date", "Full_Name", "User_Summary", "Exit"]),
    ]
    return inquirer.prompt(questions)["choice"]

def get_activities_by_date_input():
    activities_by_date_processor = Activities_By_Date_Data()
    activities_by_date_processor.get_and_process_data()

def get_full_name_input():
    full_name_processor = Full_Name_Data()
    full_name_processor.get_and_process_data()

def get_user_summary_input():
    user_summary_processor = User_Summary_Data()
    user_summary_processor.get_and_process_data()

def run():
    while True:
        choice = main_menu()
        if choice == "Activities_By_Date":
            get_activities_by_date_input()
        elif choice == "Full_Name":
            get_full_name_input()
        elif choice == "User_Summary":
            get_user_summary_input()
        elif choice == "Exit":
            break

if __name__ == "__main__":
    run()