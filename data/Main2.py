from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://elitehubs.com/collections")
time.sleep(5)

collection_links = driver.find_elements(By.CLASS_NAME, "cat_grid_item__link")

for collection_link in collection_links:
    brand_url = collection_link.get_attribute("href")
    driver.get(brand_url)
    time.sleep(5)
    
    while True:
        try:
            load_more_button = driver.find_element(By.CLASS_NAME, "usf-load-more")
            ActionChains(driver).move_to_element(load_more_button).click(load_more_button).perform()
            time.sleep(5)
        except:
            break

    img_urls = set()
    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        src = img.get_attribute("src")
        if src:
            img_urls.add(src.replace("x553x", "600x"))

    pictures = driver.find_elements(By.TAG_NAME, "picture")
    for picture in pictures:
        sources = picture.find_elements(By.TAG_NAME, "source")
        for source in sources:
            srcset = source.get_attribute("srcset")
            if srcset:
                src_options = [src.strip().split()[0].replace("x553x", "600x") for src in srcset.split(",")]
                img_urls.update(src_options)

    brand_name = brand_url.split("/")[-1]
    os.makedirs(f"images/{brand_name}", exist_ok=True)

    for idx, url in enumerate(img_urls):
        response = requests.get(url)
        if response.status_code == 200:
            file_extension = url.split("?")[0].split(".")[-1]
            with open(f"images/{brand_name}/image_{idx}.{file_extension}", "wb") as file:
                file.write(response.content)
            print(f"Downloaded image {idx} for {brand_name} from {url}")
        else:
            print(f"Failed to download image for {brand_name} from {url}")

    driver.get("https://elitehubs.com/collections")
    time.sleep(5)

driver.quit()
