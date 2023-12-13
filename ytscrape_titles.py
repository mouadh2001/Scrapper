from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://www.youtube.com/")

# Wait for the video descriptions to be present on the page
titles = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, '//yt-formatted-string[@class="style-scope ytd-rich-grid-media"]')
    )
)

# Open a file in write mode
with open("titles.txt", "w", encoding="utf-8") as file:
    for title in titles:
        # Write each description to the file
        file.write(title.text + "\n")

driver.quit()
