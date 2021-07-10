from bs4 import BeautifulSoup
import requests

my_url = requests.get(
    'https://weather.com/weather/tenday/l/96f2f84af9a5f5d452eb0574d4e4d8a840c71b05e22264ebdc0056433a642c84#detailIndex5')
# url of a specific city from weather.com, can use any city just replace the above url with city you want info from
soup = BeautifulSoup(my_url.content, 'html.parser')  # html parse the provided url
week = soup.find(class_="DailyForecast--DisclosureList--yscmv")  # finds the div that contains the entire week's info
day_summary = week.find_all(
    class_='Disclosure--themeList--1K20m')  # finds all div's that contain the corresponding day's info
high_and_low_temps = week.find_all(
    class_='DetailsSummary--temperature--35t70')  # finds the div/span that contain the high temp and low temp
description = week.find_all(
    class_='DetailsSummary--condition--33r6t')  # finds the div that contains the short description that day
precip = week.find_all(
    class_='DetailsSummary--precip--lnKqZ')  # finds the div that contains the precipitation chance that day
winds_info = week.find_all(
    class_='DetailsSummary--wind--3-8Xm DetailsSummary--extendedData--MEMw7')  # finds the div that contains the wind strength and direction

day = [i.find(class_='DetailsSummary--daypartName--3C7r4').get_text() for i in
       day_summary]  # returns all day names in list
high_temp = [i.find("span", {'data-testid': 'TemperatureValue'}).get_text() for i in
             high_and_low_temps]  # returns all high temps in list
low_temp = [i.find(class_='DetailsSummary--lowTempValue--2wKBA').get_text() for i in
            high_and_low_temps]  # returns all low temps in list
day_description = [i.find(class_='DetailsSummary--extendedData--MEMw7').get_text() for i in
                   description]  # returns short descr for the day in list
precipitation = [i.find("span", {'data-testid': 'PercentageValue'}).get_text() for i in
                 precip]  # returns the precipitation chance for the day in a list
wind = [i.find(class_='Wind--windWrapper--Ps7cP undefined').get_text() for i in
        winds_info]  # returns wind info per day in list

for j in range(len(day)):
    print(day[j] + "\nHigh Temp: " + high_temp[j] + "\nLow Temp: " + low_temp[j] + "\nDay Outlook: " + day_description[
        j] + "\nChance of precipitation: " + precipitation[j] + "\nWind: " + wind[j] + "\n\n")

