from bs4 import BeautifulSoup
import requests
import csv

site = requests.get(url="https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century")


data = site.text


soup = BeautifulSoup(data, "html.parser")
movies_list = [movie.text for movie in soup.find_all(name="strong")]
f = open("100moviesofalltime1.csv", "w")
write = csv.writer(f)
for movie in movies_list[0:-3]:
    if len(movie) > 3 :
        write.writerow(movie)

f.close()


