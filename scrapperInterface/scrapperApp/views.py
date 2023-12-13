# views.py

from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .models import Request

def home(request):
    return render(request, 'scrapperApp/home.html')

def process_request(request_id, video_url):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

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
        time.sleep(5)  # Wait for the page to load

        transcript_element = driver.find_element(
            By.XPATH,
            '//ytd-transcript-segment-list-renderer[@class="style-scope ytd-transcript-search-panel-renderer"]',
        )
        transcript = transcript_element.text

        with open("transcriptions.txt", "w", encoding="utf-8") as file:
            file.write(transcript + "\n")

        # Update the status and result of the request in the database
        update_request_status(request_id, 'completed', transcript)

    except Exception as e:
        # Handle exceptions and update the status in the database
        update_request_status(request_id, 'error', str(e))

    finally:
        # Close the browser
        driver.quit()

def update_request_status(request_id, status, result=''):
    # Update the status and result of the request in the database
    request_instance = Request.objects.get(id=request_id)
    request_instance.status = status
    request_instance.result = result
    request_instance.save()

def enqueue_request(video_url):
    # Insert a new request into the database with 'waiting' status
    request_instance = Request.objects.create(url=video_url, status='waiting')

    # Get the request_id of the newly inserted request
    request_id = request_instance.id

    return request_id

def result(request):
    result_text = None
    message = None

    if request.method == 'POST':
        video_url = request.POST.get('videoUrl', '')

        # Check if a URL was submitted
        if video_url:
            # Enqueue the request and get the request_id
            request_id = enqueue_request(video_url)

            # Process the request asynchronously
            process_request(request_id, video_url)

    # Fetch the latest request from the database if a URL was submitted
    if request.method == 'POST' and video_url:
        latest_request = Request.objects.order_by('-timestamp').first()

        # Check the status of the latest request
        if latest_request and latest_request.status == 'completed':
            result_text = latest_request.result
        else:
            message = 'No transcript available.'

    return render(request, 'scrapperApp/result.html', {'result': result_text, 'message': message})
