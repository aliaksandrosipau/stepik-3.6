from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestBasket:

    def test_find_basket_button(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        driver.get(link)
        try:
            basket_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-baske"]'))
            )
        except TimeoutException:
            print("Can't find 'Add to basket' button")

