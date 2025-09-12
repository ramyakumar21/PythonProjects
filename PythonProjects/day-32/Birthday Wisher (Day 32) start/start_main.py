import pandas
import smtplib
import datetime as dt
import random

my_email = "email@yahoo.com"
my_email2 = "email@gmail.com"
password_gmail = "abc@123"
password_yahoo = "abc@123"

to_email = "email@yahoo.com"



now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 4:
    #method 1:
    with open("quotes.txt") as data:
        quotes = data.readlines()
        quote = random.choice(quotes)
    # method 2:
    # data = pandas.read_csv("quotes.txt", header=None)
    # quotes = data.to_dict(orient="records")
    # rand_choice = random.choice(quotes)
    #
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email2, password=password_gmail)
        connection.sendmail(from_addr=my_email2, to_addrs=to_email,msg=f"Subject:Today's Quote\n\n{quote}")


