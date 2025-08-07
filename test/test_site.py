from itertools import product

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    # self.browser.get("https://www.demoblaze.com/index.html")
    homepage.click_monitor()
    # monitor_link = browser.find_element(By.CSS_SELECTOR , """[onclick="byCat('monitor')"]""")
    # monitor_link.click()
    time.sleep(4)
    homepage.check_prod_count(2)
    # monitors = browser.find_elements(By.CSS_SELECTOR, ".card-img-top.img-fluid")
    # assert  len(monitors) == 2

