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


def titan22_login(driver, user, passwd):
    driver.get("https://titan22.com/account/login?return_url=\%2Faccount")
    print("Loggin in as user {}".format(user))
    driver.find_element(By.ID, "CustomerEmail").send_keys(user)
    time.sleep(0.5)
    driver.find_element(By.ID, "CustomerPassword").send_keys(passwd +
                                                             Keys.RETURN)
    time.sleep(0.5)
    print("Current URL: {}".format(driver.current_url))

    driver.find_element(By.XPATH, "/html/body/footer/div/section/div" +
                                  "/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    print("Current URL: {}".format(driver.current_url))
    time.sleep(0.5)


def write_message(driver, msg):
    if driver.current_url != "https://titan22.com/pages/contact-us":
        driver.get("https://titan22.com/pages/contact-us")
    driver.find_element(By.ID, "ContactFormMessage").send_keys(msg)
    time.sleep(2)


def main():
    driver = configure_driver()
    user = "kjahkasjkhbfkasj@outlook.com"
    passwd = "Password!"
    msg = "This is a test and is legal"
    titan22_login(driver, user, passwd)
    write_message(driver, msg)


if __name__ == "__main__":
    main()
