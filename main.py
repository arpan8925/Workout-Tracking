import requests

NUTRITIONIX_APP_ID = "66ed0f84"
NUTRITIONIX_API_KEY = "6f006ad8bf02725d5b7a50d2443fc172"
MY_WEIGHT = "73"
MY_AGE = "22"

NUTRITIONIX_END = "https://trackapi.nutritionix.com/v2/natural/exercise"

request_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}

requst_param = {
    "query": "Ran 2 miles and walked for 3Km.",
    "weight_kg": MY_WEIGHT,
    "age": MY_AGE
}

request = requests.post(url=NUTRITIONIX_END, json=requst_param, headers=request_headers)

print(request.json())