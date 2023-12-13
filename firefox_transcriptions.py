import time
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

video_url = "https://www.youtube.com/watch?v=drQK8ciCAjY"

try:
    driver.get(video_url)
    time.sleep(10)  # Wait for the page to load

    more_button = driver.find_element(By.XPATH, '//tp-yt-paper-button[@id="expand"]')
    more_button.click()

    transcript_button = driver.find_element(
        By.XPATH,
        '//ytd-structured-description-content-renderer[@id="structured-description"]//ytd-video-description-transcript-section-renderer[@class="style-scope ytd-structured-description-content-renderer"]//div[@class="yt-spec-touch-feedback-shape__fill"]',
    )
    transcript_button.click()
    time.sleep(10)  # Wait for the page to load

    transcript_element = driver.find_element(
        By.XPATH,
        '//ytd-transcript-segment-list-renderer[@class="style-scope ytd-transcript-search-panel-renderer"]',
    )
    transcript = transcript_element.text

    with open("transcriptions.txt", "w", encoding="utf-8") as file:
        file.write(transcript + "\n")

finally:
    # Close the browser
    driver.quit()
