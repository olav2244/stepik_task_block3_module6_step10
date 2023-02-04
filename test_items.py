from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(30)
    try:
        button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    except NoSuchElementException:
        button = None
    assert button, "No button found"
