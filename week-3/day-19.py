# Fetch HTML Content
# import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/india/did-not-deboard-when-putin-offered-a-lift-to-dear-friend-pm-modi-the-story-behind-the-picture/articleshow/123630790.cms"

fetchAndSaveToFile(url, r"D:\Python Training\Phase-2-Python-Training\week-3\data\news.html")

# Parse HTML with BeautifulSoup
import requests
from bs4 import BeautifulSoup

with open(r"D:\Python Training\Phase-2-Python-Training\week-3\data\simple.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

print(soup.prettify())
print(soup.title)
print(soup.title.name)  
print(soup.title.string)
print(soup.find_all("div"))

for link in soup.find_all("a"):
    print(link.get("href"))
    print(link.get_text())

print(soup.select("div.italic"))
print(soup.select("span#italic"))
print(soup.span["class"])

for child in soup.find(class_="container").children:
    print(child)

for parent in soup.find(class_="box").parents:
    print(parent)

cont = soup.find(class_="container") # modification
cont.name = "span"
cont["class"] = "new-class"
cont.string = "i am a string now"
print(cont)

how to insert a new tag inside div with class container
cont = soup.find(class_="container")

ulTag = soup.new_tag("ul")

liTag1 = soup.new_tag("li")
liTag1.string = "home"
ulTag.append(liTag1)

liTag1 = soup.new_tag("li")
liTag1.string = "about"
ulTag.append(liTag1)

soup.html.body.insert(0, ulTag)
with open(r"D:\Python Training\Phase-2-Python-Training\week-3\data\modified.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

cont = soup.find(class_="container") # how to check if a tag has a specific attribute
print(cont.has_attr("id"))
print(cont.has_attr("class"))

def has_class_but_no_id(tag):  # beautifulsoup custom filter function
    return tag.has_attr("class") and not tag.has_attr("id")
results = soup.find_all(has_class_but_no_id)
for res in results:
    print(res)