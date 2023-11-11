# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:35:03 2023

@author: asus
"""

import requests
from datetime import datetime
from google_play_scraper import app, Sort, reviews
from datetime import datetime,timedelta

# Replace 'com.cloudtradetech.sky' with the package name of the app you want to scrape.
app_id = 'com.cloudtradetech.sky'

# Specify language and country
language = 'en'
country = 'in'

# Specify start and end dates for filtering format date= yyyy-mm-dd
start_date_str = "2023-11-01"  # Replace with your desired start date
end_date_str = "2023-11-03"  # Replace with your desired end date

#Convert start and end dates to datetime objects
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

# Fetch the reviews sorted by date in descending order
reviews_result, _ = reviews(
    app_id,
    lang=language,
    country=country,
    sort=Sort.NEWEST,
    count=10000,  # Number of reviews to retrieve (adjust as needed)
)

# Filter reviews based on date range given as start date and end date
filtered_reviews = [
    review
    for review in reviews_result
    if start_date <= review['at'] <= end_date
]

##################################
# Current datetime module
##################################



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

#fetching the current datetime
current_datetime = get_current_datetime()

if current_datetime:
    print(f"Current Datetime: {current_datetime}")
else:
    print("Failed to fetch current datetime.")

############################
#Enter the no of T minus days
T_minus_days=2

# Subtract days from the current datetime
result_datetime = current_datetime - timedelta(days=T_minus_days)

################################
#calculation of overall rating and separate rating based on  datetime interval
overall_rating=0
interval_rating=0
for review in reviews_result:
    overall_rating+=review['score']
overall_rating=overall_rating/len(reviews_result)

interval_rating = sum([
    review['score']
    for review in filtered_reviews])/len(filtered_reviews)









