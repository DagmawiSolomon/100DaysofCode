from bs4 import BeautifulSoup
import requests
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
# anchor_tags = soup.find_all(name="a")
# for tag in anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading )

response = requests.get("https://news.ycombinator.com/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
title = soup.find(name="title")
print(title.text)
story_links = soup.find_all(class_="titleline")
for links in story_links:
    print(links.find(name="a").text)
    print(links.get("href"))

