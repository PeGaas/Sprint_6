import allure
from locators.scooter_order_page_locators import NAME_FIELD, SURNAME_FIELD, ADDRESS_FIELD, \
    METRO_FIELD, PHONE_FIELD, BUTTON_NEXT, WHEN_BRING_SCOOTER, \
    LEASE_TERM, COMMENT_FOR_COURIER, ORDER_BUTTON, CONFIRM_ORDER_CREATION, \
    ORDER_PLACED
from pages.base_page import BasePage


class ScooterOrderPage(BasePage):

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнить поле Имя')
    def set_name(self, name):
        self.input_text(NAME_FIELD, name)

    @allure.step('Заполнить поле Фамилия')
    def set_surname(self, surname):
        self.input_text(SURNAME_FIELD, surname)

    @allure.step('Заполнить поле Адрес')
    def set_address(self, address):
        self.input_text(ADDRESS_FIELD, address)

    @allure.step('Заполнить поле Станция метро')
    def set_metro(self, metro_station):
        self.click_to_element(METRO_FIELD)
        self.click_to_element(metro_station)

    @allure.step('Заполнить поле Телефон')
    def set_phone_number(self, phone_number):
        self.input_text(PHONE_FIELD, phone_number)

    @allure.step('Нажать кнопку Далее для продолжения заполнения формы заказа самоката')
    def click_button_next(self):
        self.click_to_element(BUTTON_NEXT)

    @allure.step('Заполнить поля Для кого самокат')
    def fill_fields_for_scooter(self, name, surname, address, metro_station, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro_station)
        self.set_phone_number(phone_number)
        self.click_button_next()

    @allure.step('Выбрать дату Когда привезти самокат из календаря')
    def set_date_calendar(self, date_calendar):
        self.click_to_element(WHEN_BRING_SCOOTER)
        self.click_to_element(date_calendar)

    @allure.step('Выбрать срок аренды из выпадающего списка')
    def set_rental_period(self, rental_period):
        self.click_to_element(LEASE_TERM)
        self.click_to_element(rental_period)

    @allure.step('Выбрать цвет самоката')
    def choose_color_scooter(self, color):
        self.click_to_element(color)

    @allure.step('Заполнить поле Комментарий текстом')
    def set_comment(self, comment):
        self.input_text(COMMENT_FOR_COURIER, comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_button_order(self):
        self.click_to_element(ORDER_BUTTON)

    @allure.step('Нажать кнопку "Да" для подтверждения заказа')
    def click_button_confirm(self):
        self.click_to_element(CONFIRM_ORDER_CREATION)

    @allure.step('Заполнить поля Про аренду')
    def fill_fields_lease(self, date_calendar, rental_period, color, comment):
        self.set_date_calendar(date_calendar)
        self.set_rental_period(rental_period)
        self.choose_color_scooter(color)
        self.set_comment(comment)
        self.click_button_order()
        self.click_button_confirm()

    @allure.step('Проверить что на странице есть текст, "Заказ оформлен"')
    def get_text_order_placed(self):
        return self.get_text_from_element(ORDER_PLACED)
