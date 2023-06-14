from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import platform
import csv
import os


def connect_to_linkedin(driver):
    # Navigate to the Linkedin login page
    driver.get("https://www.linkedin.com/login/en?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    time.sleep(3)


def login_to_linkedin(driver):
    email = os.environ["LINKEDIN_CLIENT_EMAIL"]
    password = os.environ["LINKEDIN_CLIENT_PASSWORD"]
    email_field = driver.find_element_by_xpath("//input[@name = 'session_key']")
    password_field = driver.find_element_by_xpath("//input[@name = 'session_password']")
    email_field.send_keys(email)
    password_field.send_keys(password)

    # Click the log in button
    submit = driver.find_element_by_xpath("//button[@type = 'submit']").click()
    time.sleep(2)


def load_jobs_page(driver, page_number):
    base_url = "https://www.linkedin.com/jobs/collections/recommended/?start="
    start = page_number * 24
    url = base_url + str(start)

    driver.get(url)
    time.sleep(5)  # Add a delay to allow the page to load
    driver.maximize_window()  # Maximize the browser window

    while True:
        print("Page:", page_number)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        job_cards = soup.select('.job-card-list__entity-lockup')
        write_company_details(job_cards)
        break


def write_company_details(job_cards):
    for card in job_cards:
        company_name = card.find(class_='job-card-container__company-name').get_text(strip=True)
        job_title = card.find(class_='job-card-list__title').get_text(strip=True)
        location = card.select('.job-card-container__metadata-item')[0].get_text(strip=True)

        try:
            workplace_type = card.select('.job-card-container__metadata-item--workplace-type')[0].get_text(strip=True)
        except IndexError:
            workplace_type = "N/A"  # Provide a default value when the selector doesn't find any elements

        print("Company Name:", company_name)
        print("Job Title:", job_title)
        print("Location:", location)
        print("Workplace Type:", workplace_type)
        print("-------------------------")


def attach_cv(driver, cv_path):
    # Implement code to detect and attach a CV to the application
    pass


def send_application(driver, company_details):
    # Implement code to send the application to each company
    pass


def close_session(driver):
    driver.get("https://www.linkedin.com/m/logout")
    time.sleep(2)  # Add a delay to ensure the logout page loads completely
    driver.quit()


def main():
    if platform.system() == "Windows":
        firefox_profile_path = os.path.expanduser(
            "~") + os.sep + 'AppData' + os.sep + 'Local' + os.sep + 'Mozilla' + os.sep + 'Firefox' + os.sep + 'Profiles' + os.sep + 'linkedin.default-release'
    else:
        firefox_profile_path = os.path.expanduser(
            "~") + "/snap/firefox/common/.cache/mozilla/firefox/linkedin.default-release"

    # Create a FirefoxOptions object with your profile path
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--profile')
    firefox_options.add_argument(firefox_profile_path)

    try:
        driver = webdriver.Firefox(options=firefox_options)
    except:
        print("ERROR")
        driver.quit()

    connect_to_linkedin(driver)

    login_to_linkedin(driver)

    num_pages = 9  # Example: load 10 pages
    for page_number in range(0, num_pages):
        load_jobs_page(driver, page_number)

    close_session(driver)


if __name__ == '__main__':
    load_dotenv()
    main()

