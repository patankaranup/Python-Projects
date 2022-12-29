import requests as r
import datetime as dt
from requests.auth import HTTPBasicAuth
import os
NAME = os.environ.get("NAME")
PASS_WORD = os.environ.get("PASS_WORD")
basic = HTTPBasicAuth(NAME, PASS_WORD)

SHEET_URL_ENDPOINT = "https://api.sheety.co/af83cb75ae27b470618f7721dc35b763/workoutTracking/workouts"
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
URL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Which exercise you did ?")
query_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 57,
    "height_cm": 165,
    "age": 21

}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = r.post(url=URL_ENDPOINT, json=query_params, headers=headers)
# print(response.json())

jsonify = response.json()
print(jsonify)

# GOOGLE SHEETS

date = dt.datetime.now()
time = dt.datetime.now()
TOKEN = os.environ.get("AUTH_TOKEN")
headers_s = {
    "Authorization": f"Bearer {TOKEN}"
}

for exercise in jsonify["exercises"]:

    formatted_date = date.strftime("%d/%m/%Y")
    formatted_time = time.strftime("%H:%M:%S")
    sheets_params = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

    # post_res = r.post(url=sheets_url,  json=sheets_params, auth=basic) # basic authentication using uname pwd
    post_res = r.post(url=SHEET_URL_ENDPOINT,  json=sheets_params, headers=headers_s
                      )  # bearer token auth
    print(post_res.text)
