import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://your-proxy-ip:port",
    "https": "http://your-proxy-ip:port",
}

url = "https://www.amazon.in/s?k=iphone&crid=B8VZBM7M9WXN&sprefix=iphone%2Caps%2C614&ref=nb_sb_noss_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

spans = soup.select("span.a-size-medium a-color-base a-text-normal")
price = soup.select("span.a-price-whole")
for span in spans:
    print(span.string)

for price in price:
    print(price.string)

print(soup.title)
print(soup.title.name) 