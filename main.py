import requests
from requests.auth import HTTPBasicAuth
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

MY_WEIGHT = "73"
MY_AGE = "22"

date_extract = datetime.datetime.now()




Excersise = input("What Excersise you did today?: ")



request_headers = {
    "x-app-id": os.getenv("NUTRITIONIX_APP_ID"),
    "x-app-key": os.getenv("NUTRITIONIX_API_KEY"),
    "x-remote-user-id": "0"
}

requst_param = {
    "query": Excersise,
    "age": MY_AGE,
    "weight_kg": MY_WEIGHT
}

request = requests.post(url=os.getenv("NUTRITIONIX_END"), json=requst_param, headers=request_headers)

data = request.json()["exercises"][0]


excersize_name = data["name"].title()

duration_minit = data["duration_min"]

calories = data["nf_calories"]


print(f"Excersize: {excersize_name}\n\nTime: {duration_minit}\n\nCalories Burned: {calories}\n\n")









sheety_header = {
    "Authorization": os.getenv("SHEETY_AUTH")
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


add_row = requests.post(url=os.getenv("SHEETY_POST_END"), json=add_row, headers=sheety_header)

print(add_row.text)