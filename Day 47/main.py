from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import pandas
import gspread
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from gspread.exceptions import APIError

current_price = float(soup.find(id="price_inside_buybox").get_text().split("$")[1][:-1])
title = soup.find(id="productTitle").text
time = datetime.now()
price_dataframe = pandas.DataFrame({
    "Price": current_price,
    "Date": time.strftime("%b %d %Y"),
    "Time": time.strftime("%H:%M:%S"),
},index=[0])

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file('amazon-price-tracker-372111-121dcf37a74c.json', scopes=scopes)
gc = gspread.authorize(credentials)
gauth = GoogleAuth()
drive = GoogleDrive(gauth)
gs = gc.open_by_url("https://docs.google.com/spreadsheets/d/1HdDSXu0AZtqm80NTNP-T-PTAs8r3RI0jb0Ly16oLAp4/edit#gid=0")
try:
    worksheet = gs.add_worksheet(title=f"{title[:int(len(title)/3)]}", rows=1, cols=1)
    print(worksheet.col_values(2), "try output test")
except APIError:
    worksheet = f"{title[:int(len(title)/3)]}"
df_values = price_dataframe.values.tolist()
gs.values_append(f'{title[:int(len(title)/3)]}', {'valueInputOption': 'RAW'}, {'values': df_values})
data = gs.worksheet(worksheet)
print()
if current_price < float(min(data.col_values(1))) :
    print(f"Lowest price yet at go to |{user_input}| to make a purchase!")
