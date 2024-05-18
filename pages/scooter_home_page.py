import allure
from locators.scooter_home_page_locators import TITLE_QUESTIONS_ABOUT_IMPORTAN
from locators.scooter_order_page_locators import BUTTON_ORDER_TOP, BUTTON_ORDER_BOTTOM, SCOOTER_LOGO, YANDEX_LOGO
from pages.base_page import BasePage


class ScooterHomePage(BasePage):

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Пролистать страницу вниз до "Вопросы о важном"')
    def scroll_to_questions_about_importan(self):
        self.scroll_to_element(TITLE_QUESTIONS_ABOUT_IMPORTAN)

    @allure.step('Кликнуть на стрелочку чтобы открыть ответ на вопрос')
    def click_to_question(self, element):
        self.click_to_element(element)

    @allure.step('Получить текст ответа на вопрос')
    def get_text_answer(self, element):
        return self.get_text_from_element(element)

    @allure.step('Кликнуть на кнопку "Заказать" вверху страницы')
    def click_to_button_order_top(self):
        self.click_to_element(BUTTON_ORDER_TOP)

    @allure.step('Кликнуть на кнопку "Заказать" внизу страницы')
    def click_to_button_order_bottom(self):
        self.click_to_element(BUTTON_ORDER_BOTTOM)

    @allure.step('Переходим к кнопки "Заказать" внизу страницы')
    def scroll_to_button_order_bottom(self):
        self.scroll_to_element(BUTTON_ORDER_BOTTOM)

    @allure.step('Кликнуть на логотип Самокат')
    def click_to_logo_scooter(self):
        self.click_to_element(SCOOTER_LOGO)

    @allure.step('Кликнуть на логотип Яндекс')
    def click_to_logo_yandex(self):
        self.click_to_element(YANDEX_LOGO)

