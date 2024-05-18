from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*element))

    def click_to_element(self, element):
        self.driver.find_element(*element).click()

    def get_text_from_element(self, element):
        return self.driver.find_element(*element).text

    def input_text(self, element, text):
        return self.driver.find_element(*element).send_keys(text)

    def find_element(self, element):
        return self.driver.find_element(*element)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_window_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_url_contains(self, url):
        Wait(self.driver, 10).until(EC.url_contains(url))
