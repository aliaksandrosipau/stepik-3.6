import time

class TestBasket:

    def test_find_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        # time.sleep(30)
        try:
            browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
            result = True
        except:
            result = False
        assert result == True, "Can't find 'Add to basket' button"
