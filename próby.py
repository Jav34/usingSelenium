from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time


def to_translate():
    content = input("Insert text: ")
    print("Initializing...")
    time.sleep(1)

    def spanish():
        driver = webdriver.Chrome()
        driver.minimize_window()
        driver.get("https://www.deepl.com/translator")
        assert "DeepL" in driver.title
        message = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[2]/div/textarea")
        message.send_keys(content)
        time.sleep(5)
        not_empty = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div[3]/div[1]/textarea")
        assert not_empty
        element = driver.find_elements_by_css_selector("#dl_translator > div.lmt__sides_container > "
                                                       "div.lmt__side_container.lmt__side_container--target > "
                                                       "div.lmt__textarea_container > div.lmt__translations_as_text > "
                                                       "p:nth-child(3) > button.lmt__translations_as_text__text_btn")
        element2 = driver.find_elements_by_css_selector("#dl_translator > div.lmt__sides_container > "
                                                        "div.lmt__side_container.lmt__side_container--target > "
                                                        "div.lmt__textarea_container > div.lmt__translations_as_text")

        for element in element:
            print("element: ", element.text)

        for element2 in element2:
            print("element2: ", element2.text)

    spanish()


to_translate()
