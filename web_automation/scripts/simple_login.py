#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def configure_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
                                    ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    return driver


def extract_temp(text):
    """Extracts temperature value from scraped text"""
    return float(text.split(": ")[1])


def scrape_temp(driver):
    driver.get("http://automated.pythonanywhere.com/")

    # Alternative 'find_element':
    # element = driver.find_element(by="xpath",
    #           value="/html/body/div[1]/div/h1[2]")

    time.sleep(2)  # Allow website to get temperature
    element = driver.find_element(By.ID, 'displaytimer')
    temperature = extract_temp(element.text)
    print("Calculated avg world temp: {}".format(temperature))


def main():
    driver = configure_driver()
    user = "automated"
    passwd = "automatedautomated"

    driver.get("http://automated.pythonanywhere.com/login/")
    print("Loggin in as user {}".format(user))
    element = driver.find_element(By.ID, "id_username").send_keys(user)
    time.sleep(0.1)
    element = driver.find_element(By.ID, "id_password").send_keys(passwd + 
              Keys.RETURN)
    time.sleep(0.1)
    print("Current URL: {}".format(driver.current_url))

    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    print("Current URL: {}".format(driver.current_url))


if __name__ == "__main__":
    main()
