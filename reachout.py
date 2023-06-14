from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from dotenv import load_dotenv
import platform
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


def load_jobs_page(driver):
    driver.get("https://www.linkedin.com/jobs/collections/recommended")


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

    # service = Service(log_path=os.devnull)

    # Create a new Firefox driver with your options
    try:
        # driver = webdriver.Firefox(options=firefox_options, service=service)
        driver = webdriver.Firefox(options=firefox_options)
    except:
        print("ERROR")
        driver.quit()

    connect_to_linkedin(driver)

    login_to_linkedin(driver)

    load_jobs_page(driver)


if __name__ == '__main__':
    load_dotenv()
    main()
