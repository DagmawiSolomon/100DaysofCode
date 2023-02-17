import gspread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, date
from google.oauth2.service_account import Credentials
from gspread.exceptions import APIError
import pandas
from twilio.rest import Client
account_sid = "AC4aa59b263bd38ca010bd2fdd6f280cd8"
auth_token = "a83c46a61f31c1a922a8d911b46e1e02"
client = Client(account_sid, auth_token)

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

link = "https://www.amazon.com/Skullcandy-Hesh-Wireless-Over-Ear-Headphone/dp/B075749KHR/ref=sr_1_13?qid=1671540858" \
       "&refinements=p_36%3A1253505011&rnid=172541&s=electronics&sr=1-13 "


class PriceTracker:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(link)
        price_element = self.driver.find_element(By.CSS_SELECTOR, '#corePrice_desktop > div > table > tbody > '
                                                                  'tr:nth-child(2) > '
                                                                  'td.a-span12 > span.a-price.a-text-price.a-size'
                                                                  '-medium.apexPriceToPay > '
                                                                  'span:nth-child(2)')
        product_title_element = self.driver.find_element(By.ID, "productTitle")
        self.product_title = product_title_element.text
        self.price = float(price_element.text.split('$')[1])
        self.data_dict = {}
        self.credentials = Credentials.from_service_account_file('amazon-price-tracker-372111-121dcf37a74c.json',
                                                            scopes=scopes)
        self.client = gspread.authorize(self.credentials)
        self.sheet = self.client.open_by_url("https://docs.google.com/spreadsheets/d/1HdDSXu0AZtqm80NTNP-T"
                                   "-PTAs8r3RI0jb0Ly16oLAp4/edit#gid=0")
        self.min_price = 0

    def save_data(self):
        self.data_dict['Price'] = self.price
        time_now = datetime.now()
        self.data_dict['Time'] = time_now.strftime("%H:%M:%S")
        current_date = date.today()
        self.data_dict['Date'] = current_date.strftime("%b %d %Y")
        data_dataframe = pandas.DataFrame(self.data_dict, index=[0])
        title = self.product_title
        try:
            worksheet = self.sheet.add_worksheet(title=f"{title[:int(len(title) / 3)]}", rows=1, cols=1)
            print(worksheet.col_values(2), "try output test")
        except APIError:
            self.min_price = float(min(self.sheet.worksheet(f"{self.product_title[:int(len(self.product_title) / 3)]}").col_values(1)[:-1]))
        df_values = data_dataframe.values.tolist()
        self.sheet.values_append(f'{title[:int(len(title) / 3)]}', {'valueInputOption': 'RAW'}, {'values': df_values})


    def check_data(self):

        data = self.sheet.worksheet(f"{self.product_title[:int(len(self.product_title) / 3)]}")
        print(data, "data")
        current_price = self.price
        print(current_price, "current price")
        print(self.min_price, "min price")
        if float(current_price) < self.min_price:
            print(f"{self.product_title}' is at it's lowest price.\nGo to {link} to make a purchase.")
            msg = client.messages.create(
                body=f"{self.product_title}' is at it's lowest price.\nGo to {link} to make a purchase.",
                from_="+15628372242",
                to="+251912677537"
            )
            print(msg.sid)




price_tracker = PriceTracker()
price_tracker.save_data()
price_tracker.check_data()




