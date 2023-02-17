from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

user_input = input("Enter url: ")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(user_input)

soup = BeautifulSoup(driver.page_source, "html.parser")
book_titles = soup.find_all(class_="book-title")
print(book_titles)
book_author = soup.find_all(class_="book-author")
with open("books.txt", "w") as file:
    for i in range(len(book_titles)):
        file.write(f"{i+1}){book_titles[i].text} by {book_author[i].text}\n")
        print(f"{i+1}){book_titles[i].text} by {book_author[i].text}\n")