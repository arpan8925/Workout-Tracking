import requests
from requests.auth import HTTPBasicAuth
import datetime

NUTRITIONIX_APP_ID = "66ed0f84"
NUTRITIONIX_API_KEY = "6f006ad8bf02725d5b7a50d2443fc172"
MY_WEIGHT = "73"
MY_AGE = "22"

date_extract = datetime.datetime.now()




Excersise = input("What Excersise you did today?: ")

NUTRITIONIX_END = "https://trackapi.nutritionix.com/v2/natural/exercise"

request_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}
requst_param = {
    "query": Excersise,
    "age": MY_AGE,
    "weight_kg": MY_WEIGHT
}

request = requests.post(url=NUTRITIONIX_END, json=requst_param, headers=request_headers)
data = request.json()["exercises"][0]


excersize_name = data["name"].title()

duration_minit = data["duration_min"]

calories = data["nf_calories"]


print(f"Excersize: {excersize_name}\n\nTime: {duration_minit}\n\nCalories Burned: {calories}\n\n")




SHEETY_POST_END = "https://api.sheety.co/7dd323f370a1fa5581a130fb15e4a412/myWorkouts/workouts"


sheety_header = {
    "Authorization": "Basic YXJwYW44OTI1OkFycGFuODkyNSQjJCM="
}

date = date_extract.strftime("%x")

current_time = date_extract.strftime("%I:%M:%S %p")


add_row = {
    "workout": {
        "date": date,
        "time": current_time,
        "exercise": excersize_name,
        "duration": duration_minit,
        "calories": calories
    }
}


add_row = requests.post(url=SHEETY_POST_END, json=add_row, headers=sheety_header)

print(add_row.text)