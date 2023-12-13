import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

video_url = "https://www.youtube.com/watch?v=IEuHpriOVzE"

try:
    driver.get(video_url)
    time.sleep(10)  # Wait for the page to load

    comment = driver.find_element(
        By.XPATH,
        '//ytd-comments[@id="comments"]//ytd-item-section-renderer[@id="sections"]',
    )
    comments = comment.text
    time.sleep(10)  # Wait for the page to load

    with open("comments.txt", "w", encoding="utf-8") as file:
        file.write(comments + "\n")

finally:
    # Close the browser
    driver.quit()
