import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

load_url = "https://hypixel.net/threads/all-bedwars-weekly-item-rotations.5284358/#:~:text=Chicken%20Turret%20%2B%20Throwable-,TNT,-(Week%2019)"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
print(soup)