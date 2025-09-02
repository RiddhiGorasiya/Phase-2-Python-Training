import urllib.request
from bs4 import BeautifulSoup

# File path where you want to save webpage
file_path = r"D:\Python Training\Phase-2-Python-Training\project\text_file.txt"

# Download and save the webpage
urllib.request.urlretrieve(
    "https://timesofindia.indiatimes.com/life-style/food-news/what-made-zigzag-vodka-a-global-winner-at-the-asia-world-spirits-competition-2025/articleshow/123569554.cms",
    file_path
)

# Open the saved file
with open(file_path, "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# Save extracted headlines + paragraphs
with open("test1.txt", "w", encoding="utf-8") as f:
    # Headlines (h1, h2, h3)
    for headline in soup.find_all(["h1", "h2", "h3"]):
        text = headline.get_text(strip=True)
        if text:
            f.write("HEADLINE: " + text + "\n\n")
            print("HEADLINE:", text)

    # Paragraphs (p tags)
    for data in soup.find_all("p"):
        text = data.get_text(strip=True)
        if text:
            f.write(text + "\n")
            print(text)