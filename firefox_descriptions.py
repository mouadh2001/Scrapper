import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

video_url = "https://www.youtube.com/watch?v=kqtD5dpn9C8&t=5s"

try:
    driver.get(video_url)
    time.sleep(10)  # Wait for the page to load

    more_button = driver.find_element(By.XPATH, '//tp-yt-paper-button[@id="expand"]')
    more_button.click()

    description = driver.find_element(By.XPATH, '//div[@id="description-inner"]')
    descriptions = description.text

    with open("descriptions.txt", "w", encoding="utf-8") as file:
        file.write(descriptions + "\n")

finally:
    # Close the browser
    driver.quit()
