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

import requests
from datetime import datetime
from google_play_scraper import app, Sort, reviews
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
# Replace 'com.cloudtradetech.sky' with the package name of the app you want to scrape.
app_id = 'com.cloudtradetech.sky'

# Specify language and country
language = 'en'
country = 'in'

 
# Specify start and end dates for filtering format date= yyyy-mm-dd
start_date_str = "2023-11-01"  # Replace with your desired start date
end_date_str = "2023-11-03"  # Replace with your desired end date



def full_filtered_review(start_date_str,end_date_str):
    
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
    return (reviews_result,filtered_reviews)

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

################################
#calculation of overall rating and separate rating based on  datetime interval

full_filtered=full_filtered_review(start_date_str,end_date_str)

overall_rating=0
interval_rating=0
for review in full_filtered[0]:
    overall_rating+=review['score']
overall_rating=overall_rating/len(full_filtered[0])

interval_rating = sum([
    review['score']
    for review in full_filtered[1]])/len(full_filtered[1])



###################################
#Enter the no of T minus days
T_minus_days=10

# Subtract days from the current datetime
#result_datetime = current_datetime - timedelta(days=T_minus_days)
#######################################################################################################

#######################################################################################################


def Trend_of_Tminus_days(T_minus_days):
    
    
    today_date=get_current_datetime().strftime("%Y-%m-%d")
    end_date=(current_datetime - timedelta(days=T_minus_days)).strftime("%Y-%m-%d")
    #full_filtered_review() takes string type date 
    trend_line_data=full_filtered_review(end_date,today_date)
    lis=[]
    required_date=(current_datetime - timedelta(days=T_minus_days)).strftime("%Y-%m-%d")
    def scoreSum_and_date(required_date):
        
        day_sum=[score['score'] for score in trend_line_data[0]
                 if score['at'].strftime("%Y-%m-%d")==required_date
                 ]
        return [sum(day_sum),required_date,len(day_sum)]
        
    while T_minus_days>0:
        required_date=(current_datetime - timedelta(days=T_minus_days)).strftime("%Y-%m-%d")
        lis.append(scoreSum_and_date(required_date))
        T_minus_days-=1
    lis = [
    [sublist[0] / sublist[2],sublist[1]] if sublist[2] != 0 else [0,sublist[1]]
    for sublist in lis
    ]
    return lis       
    

xx=Trend_of_Tminus_days(T_minus_days)
# Extract x and y values from the list
x_values = [pair[1] for pair in xx]
y_values = [pair[0] for pair in xx]

# Plot the line plot
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # 1 row, 2 columns, subplot 1
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot: xx[0] on Y-axis and xx[1] on X-axis')
plt.grid(True)

# Create a histogram
plt.subplot(1, 2, 2)  # 1 row, 2 columns, subplot 2
plt.hist2d(x_values, y_values, bins=(10, 10), cmap=plt.cm.Blues)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Histogram of X and Y values')
plt.colorbar()

# Show the plot
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()


for score in trend_line_data[0]:
        lis.append(score['score'])
        print(score['score'])
          
    
    while T_minus_days>=1:
        day_wise_reviews=[
            [trend_line_data[0][0]['score'],trend_line_data[0][0]['at']]
            for review in reviews_result
            if start_date <= review['at'] <= end_date
        ]
        
    
    
    return trend_line_data

    
trend_line_data=Trend_of_Tminus_days(T_minus_days)




