from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Acer Aspire 7 amazon link
urlPrice = 'https://www.amazon.in/Acer-i5-1035G1-Graphics-Charcoal-A315-57G/dp/B08HR3CYGQ/ref=sr_1_3?dchild=1&keywords' \
           '=acer+aspire+7&qid=1605507187&s=computers&sr=1-3 '
# Accu weather website
urlTemp = 'https://www.accuweather.com/en/in/hyderabad/202190/current-weather/202190'

# PewDiePie subscriber count
urlTube = "https://socialblade.com/youtube/user/pewdiepie/realtime"

# your user agent
ua = {
    "User-Agent": 'Write your user agent here!!!'}  # write your user agent here


# function to get details from respective websites
def checkstatus():
    page1 = requests.get(urlPrice, headers=ua)
    page2 = requests.get(urlTemp, headers=ua)
    page3 = requests.get(urlTube, headers=ua)

    p1 = BeautifulSoup(page1.content, 'html.parser')
    p2 = BeautifulSoup(page2.content, 'html.parser')
    p3 = BeautifulSoup(page3.content, 'html.parser')

    ans1 = p1.find(id="priceblock_ourprice").get_text()
    ans2 = p2.find_all(class_="display-temp")
    ans3 = p3.find(id="rawCount").get_text()

    for row in ans2:
        ans22 = (row.get_text())
    ans = (ans1, ans22, ans3)   # make tuple and return
    return ans


@app.route("/")
def home():
    a1, a2, a3 = checkstatus()
    return render_template("scrapperFrontE.html", t1=a1, t2=a2, t3=a3)  # render the web page


if __name__ == "__main__":
    app.run(debug=True)
