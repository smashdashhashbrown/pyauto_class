#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
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
    if driver.current_url != "http://automated.pythonanywhere.com/":
        driver.get("http://automated.pythonanywhere.com/")

    time.sleep(2)  # Allow website to get temperature
    element = driver.find_element(By.ID, 'displaytimer')
    temperature = extract_temp(element.text)
    print("Calculated avg world temp: {}".format(temperature))
    return temperature


def py_anywhere_login(driver, user, passwd):
    driver.get("http://automated.pythonanywhere.com/login/")
    print("Loggin in as user {}".format(user))
    driver.find_element(By.ID, "id_username").send_keys(user)
    time.sleep(0.1)
    driver.find_element(By.ID, "id_password").send_keys(passwd +
                                                        Keys.RETURN)
    time.sleep(0.1)
    print("Current URL: {}".format(driver.current_url))

    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    print("Current URL: {}".format(driver.current_url))


def init_csv():
    file = open("files/temps.csv", "w")
    file.write("datetime,temp\n")
    return file


def main():
    file = init_csv()
    driver = configure_driver()
    user = "automated"
    passwd = "automatedautomated"

    py_anywhere_login(driver, user, passwd)

    try:
        while True:
            temp = scrape_temp(driver)
            line = "{},{}\n".format(datetime.now(), temp)
            print(line)
            file.write(line)
    except KeyboardInterrupt:
        print("Ending program.")
        file.close()


if __name__ == "__main__":
    main()
