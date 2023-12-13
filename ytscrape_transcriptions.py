import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace 'path/to/msedgedriver.exe' with the actual path to Edge WebDriver
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

# Replace 'your_video_url' with the actual YouTube video URL
video_url = "https://www.youtube.com/watch?v=kqtD5dpn9C8&t=5s"

try:
    driver.get(video_url)
    time.sleep(10)  # Wait for the page to load

    # Click the "More" button to expand transcript
    more_button = driver.find_element(By.XPATH, '//tp-yt-paper-button[@id="expand"]')
    more_button.click()
    time.sleep(10)  # Wait for the page to load

    # Click the "Open transcript" option
    transcript_button = driver.find_element(
        By.XPATH,
        '//ytd-structured-description-content-renderer[@id="structured-description"]//ytd-video-description-transcript-section-renderer[@class="style-scope ytd-structured-description-content-renderer"]//div[@class="yt-spec-touch-feedback-shape__fill"]',
    )
    transcript_button.click()
    time.sleep(10)  # Wait for the page to load

    # Extract the transcript
    transcript_element = driver.find_element(
        By.XPATH,
        '//ytd-transcript-segment-list-renderer[@class="style-scope ytd-transcript-search-panel-renderer"]',
    )
    transcript = transcript_element.text
    time.sleep(10)  # Wait for the page to load

    # Print or save the transcript as needed

    with open("transcriptions.txt", "w", encoding="utf-8") as file:
        # Write each description to the file
        file.write(transcript + "\n")


finally:
    # Close the browser
    driver.quit()
