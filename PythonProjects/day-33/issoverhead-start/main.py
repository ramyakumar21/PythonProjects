import requests
from datetime import datetime
import smtplib

MY_LATITUDE = 33.748997
MY_LONGITUDE = -84.387985
MY_EMAIL = "abc123@gmail.com"
MY_PASSWORD = "abc123"

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5<= iss_longitude <= MY_LONGITUDE+5 :
        return True
    else:
        return False

def is_night_time():

    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset <= time_now.hour or time_now.hour <= sunrise:
        return True
    else:
        return False


if is_iss_overhead() and is_night_time():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:ISS is here!\n\nLook up!")
