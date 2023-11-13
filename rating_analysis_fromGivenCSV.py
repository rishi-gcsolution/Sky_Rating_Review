# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 17:28:44 2023

@author: asus
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:35:03 2023

@author: asus
"""
import os
import pandas as pd
import requests
from datetime import datetime
from google_play_scraper import app, Sort, reviews
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
from docx import Document

# Replace 'com.cloudtradetech.sky' with the package name of the app you want to scrape.
app_id = 'com.cloudtradetech.sky'

# Specify language and country
language = 'en'
country = 'in'

 
# Specify start and end dates for filtering format date= yyyy-mm-dd
start_date_str = "2023-11-01"  # Replace with your desired start date
end_date_str = "2023-11-03"  # Replace with your desired end date
T_minus_days=10

##################################
# Current datetime module
##################################
#Replace 'your_file.csv' with the actual file path
file_path_csv = r'C:\Users\asus\Desktop\HDFC Work Related\excel_files\Daily rating distribution _ 2023-10-15 - 2023-11-11.csv'

# Read the CSV file into a DataFrame
df_csv = pd.read_csv(file_path_csv)


def get_current_datetime():
    try:
        response = requests.get("http://worldtimeapi.org/api/ip")
        response.raise_for_status()  # Raise an exception for bad responses

        data = response.json()
        current_datetime_str = data['datetime']
        # Convert the datetime string to a datetime object
        current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%dT%H:%M:%S.%f%z")

        return current_datetime

    except requests.exceptions.RequestException as e:
        print(f"Error fetching current datetime: {e}")
        return None
    

   
