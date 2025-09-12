
import datetime as dt
import random
import smtplib
import pandas

TO_REPLACE = "[NAME]"
FROM_ADDR = "email@gmail.com"
PASSWORD = "abc@123"

# 1. Update the birthdays.csv with your friends & family's details. 

# 2. Check if today matches a birthday in the birthdays.csv

today = dt.datetime.today()
today_date = (today.month, today.day)

birthday_data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_data.iterrows()}

if today_date in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    birthday_person = birthdays_dict.get(today_date) # or name = birthdays_dict[today_date]
    template_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(template_path, mode="r") as letter:
        letter_temp = letter.read()
        name = birthday_person["name"] # or name = birthdays_dict[today_date]["name"]
        mail_body = letter_temp.replace(TO_REPLACE, name)

# 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=FROM_ADDR, password=PASSWORD)
        connection.sendmail(from_addr=FROM_ADDR, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{mail_body}")



