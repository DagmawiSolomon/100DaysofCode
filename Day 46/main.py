from bs4 import BeautifulSoup
import requests

year = input("Enter year: ")


hot_100 = requests.get(url=f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs/")
hot_100_data = hot_100.text

soup = BeautifulSoup(hot_100_data, "html.parser")
music_titles = [title.text for title in soup.find_all(class_="c-title")]
print(music_titles)

user_id = "b24f5e6cde8440ac86edf8e02352847c"
endpoint_url = f"https://api.spotify.com/v1/users/{user_id}"
spotify_api = requests.get(endpoint_url)
print(spotify_api.text)