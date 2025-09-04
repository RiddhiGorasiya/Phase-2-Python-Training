# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# def scrape_amazon_mobiles(search_query, pages=1):
#     # Setup Selenium WebDriver
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")   # Run in background
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
    
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     mobiles_data = []

#     # Loop through given number of pages
#     for page in range(1, pages + 1):
#         url = f"https://www.amazon.in/s?k=mobile&crid=3TR8VRHQALJKH&sprefix=mobile%2Caps%2C980&ref=nb_sb_noss_2"
#         driver.get(url)
#         time.sleep(3)  # wait for page to load

#         # Find all product containers
#         products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

#         for product in products:
#             try:
#                 name = product.find_element(By.TAG_NAME, "h2").text
#             except:
#                 name = "N/A"

#             try:
#                 price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
#             except:
#                 price = "N/A"

#             try:
#                 rating = product.find_element(By.CSS_SELECTOR, "span'a-icon-alt'").text
#             except:
#                 rating = "N/A"

#             mobiles_data.append({
#                 "Name": name,
#                 "Price": price,
#                 "Rating": rating
#             })

#     driver.quit()

#     # Save to JSON
#     with open("amazon_mobiles.json", "w", encoding="utf-8") as f:
#         json.dump(mobiles_data, f, indent=4, ensure_ascii=False)

#     print("Data saved to amazon_mobiles.json")

# Run the scraper
# scrape_amazon_mobiles("mobile", pages=2)

import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_amazon_mobiles(search_query="mobile", pages=1):
    # Setup Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")   # Run in background
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    mobiles_data = []

    # Loop through given number of pages
    for page in range(1, pages + 1):
        url = f"https://www.amazon.in/s?k={search_query}&page={page}"
        driver.get(url)
        time.sleep(4)  # wait for page to load

        # Find all product containers
        products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

        for product in products:
            try:
                name = product.find_element(By.TAG_NAME, "h2").text
            except:
                name = "N/A"

            try:
                price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
            except:
                price = "N/A"

            try:
                rating = product.find_element(By.CSS_SELECTOR, "span.a-icon-alt").icon
            except:
                rating = "N/A"

            mobiles_data.append({
                "Name": name,
                "Price": price,
                "Rating": rating
            })

    driver.quit()

    # Save to JSON
    with open("amazon_mobiles.json", "w", encoding="utf-8") as f:
        json.dump(mobiles_data, f, indent=4, ensure_ascii=False)

    print("Data saved to amazon_mobiles.json")

# Example usage
scrape_amazon_mobiles("mobile", pages=2)


