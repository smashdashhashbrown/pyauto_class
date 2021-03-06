#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
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


def main():
    driver = configure_driver()
    driver.get("http://automated.pythonanywhere.com/")

    # Alternative 'find_element':
    # element = driver.find_element(by="xpath",
    #           value="/html/body/div[1]/div/h1[2]")

    time.sleep(2)  # Allow website to get temperature
    element = driver.find_element(By.ID, 'displaytimer')
    temperature = extract_temp(element.text)
    print("Calculated avg world temp: {}".format(temperature))


if __name__ == "__main__":
    main()
