import allure
import pytest
from selenium import webdriver

from data_generator import generate_name, generate_surname, generate_address, generate_phone_number, generate_comment
from locators.base_locators import MAIN_URL, DZEN_URL
from locators import scooter_order_page_locators as SL
from pages.scooter_order_page import ScooterOrderPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait


class TestScooterOrderPage:
    driver = None

    def setup_method(self):
        with allure.step('Открываем браузер Firefox'):
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
            self.driver.get(MAIN_URL)

    @allure.title('Заказать самокат через кнопку "Заказать" вверху страницы')
    @allure.description('Проверка позитивного сценария заказа самоката с случайным наборам данных')
    @pytest.mark.parametrize('name, surname, address, phone_number, comment', [
        [generate_name(), generate_surname(), generate_address(), generate_phone_number(), generate_comment()]])
    def test_button_order_top(self, name, surname, address, phone_number, comment):
        scooter_order_page = ScooterOrderPage(self.driver)
        scooter_order_page.click_to_button_order(SL.BUTTON_ORDER_TOP)
        scooter_order_page.fill_fields_for_scooter(name, surname, address, phone_number)
        scooter_order_page.fill_fields_lease(comment)
        text = scooter_order_page.get_text_order_placed()

        assert "Заказ оформлен" in text

    @allure.title('Заказать самокат через кнопку "Заказать" внизу страницы')
    @allure.description('Проверка позитивного сценария заказа самоката с случайным наборам данных')
    @pytest.mark.parametrize('name, surname, address, phone_number, comment', [
        [generate_name(), generate_surname(), generate_address(), generate_phone_number(), generate_comment()]])
    def test_button_order_bottom(self, name, surname, address, phone_number, comment):
        scooter_order_page = ScooterOrderPage(self.driver)
        scooter_order_page.scroll_to_button_order_bottom()
        scooter_order_page.click_to_button_order(SL.BUTTON_ORDER_BOTTOM)
        scooter_order_page.fill_fields_for_scooter(name, surname, address, phone_number)
        scooter_order_page.fill_fields_lease(comment)
        text = scooter_order_page.get_text_order_placed()

        assert "Заказ оформлен" in text

    @allure.title('Кликнуть на логотип Самокат')
    @allure.description('Проверка что после клика на логотип "Самокат",попадаешь на главную страницу "Самокат"')
    def test_click_logo_scooter(self):
        scooter_order_page = ScooterOrderPage(self.driver)
        scooter_order_page.click_to_logo_scooter()

        assert self.driver.current_url == MAIN_URL

    @allure.title('Кликнуть на логотип Яндекс')
    @allure.description('Проверка что после клика на логотип "Яндекс",попадаешь на главную страницу "Дзен"')
    def test_click_logo_yandex(self):
        scooter_order_page = ScooterOrderPage(self.driver)
        scooter_order_page.click_to_logo_yandex()
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait(self.driver, 10).until(EC.url_contains(DZEN_URL))

        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true&is_autologin_ya=true'

    def teardown_method(self):
        with allure.step('Открываем браузер Firefox'):
            self.driver.quit()
