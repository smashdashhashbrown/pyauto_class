#!/usr/bin/env python3

from selenium import webdriver


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


def main():
    driver = configure_driver()
    driver.get("http://automated.pythonanywhere.com/")
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    print(element.text)


if __name__ == "__main__":
    main()
