from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver,  10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, locator):
        self.wait_and_find_element(locator).click()

    def set_input(self, locator, value):
        element = self.wait_and_find_element(locator)
        element.clear()
        element.send_keys(value)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url


