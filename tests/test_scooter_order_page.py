import allure
import pytest
from data_generator import generate_name, generate_surname, generate_address, generate_phone_number, generate_comment
from data_static import MAIN_URL, DZEN_URL
from locators.scooter_order_page_locators import LIST_SUBWAY_STATIONS, DATE_CALENDAR, RENTAL_PERIOD, COLLOR_SCOOTER
from pages.scooter_home_page import ScooterHomePage
from pages.scooter_order_page import ScooterOrderPage


@allure.title('Заказать самокат через кнопку "Заказать" вверху страницы')
@allure.description('Проверка позитивного сценария заказа самоката с случайным наборам данных')
@pytest.mark.parametrize(
    'name, surname, address, metro_station, phone_number, date_calendar, rental_period, color, comment', [
        [generate_name(), generate_surname(), generate_address(), LIST_SUBWAY_STATIONS, generate_phone_number(),
         DATE_CALENDAR, RENTAL_PERIOD, COLLOR_SCOOTER, generate_comment()]])
def test_button_order_top(firefox_driver, name, surname, address, metro_station, phone_number, date_calendar,
                          rental_period, color, comment):
    scooter_home_page = ScooterHomePage(firefox_driver)
    scooter_home_page.click_to_button_order_top()

    scooter_order_page = ScooterOrderPage(firefox_driver)
    scooter_order_page.fill_fields_for_scooter(name, surname, address, metro_station, phone_number)
    scooter_order_page.fill_fields_lease(date_calendar, rental_period, color, comment)
    text = scooter_order_page.get_text_order_placed()

    assert "Заказ оформлен" in text


@allure.title('Заказать самокат через кнопку "Заказать" внизу страницы')
@allure.description('Проверка позитивного сценария заказа самоката с случайным наборам данных')
@pytest.mark.parametrize(
    'name, surname, address, metro_station, phone_number, date_calendar, rental_period, color, comment', [
        [generate_name(), generate_surname(), generate_address(), LIST_SUBWAY_STATIONS, generate_phone_number(),
         DATE_CALENDAR, RENTAL_PERIOD, COLLOR_SCOOTER, generate_comment()]])
def test_button_order_bottom(firefox_driver, name, surname, address, metro_station, phone_number, date_calendar,
                             rental_period, color, comment):
    scooter_home_page = ScooterHomePage(firefox_driver)
    scooter_home_page.scroll_to_button_order_bottom()
    scooter_home_page.click_to_button_order_bottom()

    scooter_order_page = ScooterOrderPage(firefox_driver)
    scooter_order_page.fill_fields_for_scooter(name, surname, address, metro_station, phone_number)
    scooter_order_page.fill_fields_lease(date_calendar, rental_period, color, comment)
    text = scooter_order_page.get_text_order_placed()

    assert "Заказ оформлен" in text


@allure.title('Кликнуть на логотип Самокат')
@allure.description('Проверка что после клика на логотип "Самокат",попадаешь на главную страницу "Самокат"')
def test_click_logo_scooter(firefox_driver):
    scooter_home_page = ScooterHomePage(firefox_driver)
    scooter_home_page.click_to_logo_scooter()

    assert scooter_home_page.get_current_url() == MAIN_URL


@allure.title('Кликнуть на логотип Яндекс')
@allure.description('Проверка что после клика на логотип "Яндекс",попадаешь на главную страницу "Дзен"')
def test_click_logo_yandex(firefox_driver):
    scooter_home_page = ScooterHomePage(firefox_driver)
    scooter_home_page.click_to_logo_yandex()
    scooter_home_page.switch_to_window_next_tab()
    scooter_home_page.wait_url_contains(DZEN_URL)

    assert scooter_home_page.get_current_url() == 'https://dzen.ru/?yredirect=true&is_autologin_ya=true'
