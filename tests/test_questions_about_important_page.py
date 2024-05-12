import allure
from selenium import webdriver
from locators.base_locators import MAIN_URL
from pages.questions_about_important_page import QuestionsAboutImportantPage
from locators import questions_about_important_page_locators as QL


class TestQuestionsAboutImportantPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(MAIN_URL)

    @allure.title('Проверка блока "Сколько это стоит? И как оплатить?"')
    @allure.description('Когда нажимаем на стрелочку, открывается соответствующий текст')
    def test_open_cost_and_pay(self):
        questions_about_important_page = QuestionsAboutImportantPage(self.driver)
        questions_about_important_page.scroll_to_questions_about_importan()
        questions_about_important_page.click_to_question(QL.COST_AND_PAY)
        text_element = questions_about_important_page.get_text_on_question(QL.TEXT_COST_AND_PAY)

        assert text_element == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка блока "Хочу сразу несколько самокатов! Так можно?"')
    @allure.description('Когда нажимаем на стрелочку, открывается соответствующий текст')
    def test_open_several_scooters(self):
        questions_about_important_page = QuestionsAboutImportantPage(self.driver)
        questions_about_important_page.scroll_to_questions_about_importan()
        questions_about_important_page.click_to_question(QL.SEVERAL_SCOOTERS)
        text_element = questions_about_important_page.get_text_on_question(QL.TEXT_SEVERAL_SCOOTERS)

        assert text_element == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка блока "Как рассчитывается время аренды?"')
    @allure.description('Когда нажимаем на стрелочку, открывается соответствующий текст')
    def test_open_rental_time_calculated(self):
        questions_about_important_page = QuestionsAboutImportantPage(self.driver)
        questions_about_important_page.scroll_to_questions_about_importan()
        questions_about_important_page.click_to_question(QL.RENTAL_TIME_CALCULATED)
        text_element = questions_about_important_page.get_text_on_question(QL.TEXT_RENTAL_TIME_CALCULATED)

        assert text_element == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка блока "Можно ли заказать самокат прямо на сегодня?"')
    @allure.description('Когда нажимаем на стрелочку, открывается соответствующий текст')
    def test_open_order_scooter_today(self):
        questions_about_important_page = QuestionsAboutImportantPage(self.driver)
        questions_about_important_page.scroll_to_questions_about_importan()
        questions_about_important_page.click_to_question(QL.ORDER_SCOOTER_TODAY)
        text_element = questions_about_important_page.get_text_on_question(QL.TEXT_ORDER_SCOOTER_TODAY)

        assert text_element == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка блока "Можно ли продлить заказ или вернуть самокат раньше?"')
    @allure.description('Когда нажимаем на стрелочку, открывается соответствующий текст')
    def test_open_extend_order_or_return_scooter_earlier(self):
        questions_about_important_page = QuestionsAboutImportantPage(self.driver)
        questions_about_important_page.scroll_to_questions_about_importan()
        questions_about_important_page.click_to_question(QL.EXTEND_ORDER_OR_RETURN_SCOOTER_EARLIER)
        text_element = questions_about_important_page.get_text_on_question(QL.TEXT_EXTEND_ORDER_OR_RETURN_SCOOTER_EARLIER)

        assert text_element == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка блока "Вы привозите зарядку вместе с самокатом?"')
    @allure.description('Когда нажимаем на стрелочку, открывается соответствующий текст')
    def test_open_bring_charger_to_scooter(self):
        questions_about_important_page = QuestionsAboutImportantPage(self.driver)
        questions_about_important_page.scroll_to_questions_about_importan()
        questions_about_important_page.click_to_question(QL.BRING_CHARGER_TO_SCOOTER)
        text_element = questions_about_important_page.get_text_on_question(QL.TEXT_BRING_CHARGER_TO_SCOOTER)

        assert text_element == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка блока "Можно ли отменить заказ?"')
    @allure.description('Когда нажимаем на стрелочку, открывается соответствующий текст')
    def test_open_cancel_order(self):
        questions_about_important_page = QuestionsAboutImportantPage(self.driver)
        questions_about_important_page.scroll_to_questions_about_importan()
        questions_about_important_page.click_to_question(QL.CANCEL_ORDER)
        text_element = questions_about_important_page.get_text_on_question(QL.TEXT_CANCEL_ORDER)

        assert text_element == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка блока "Я жизу за МКАДом, привезёте?"')
    @allure.description('Когда нажимаем на стрелочку, открывается соответствующий текст')
    def test_open_outside_mkad(self):
        questions_about_important_page = QuestionsAboutImportantPage(self.driver)
        questions_about_important_page.scroll_to_questions_about_importan()
        questions_about_important_page.click_to_question(QL.OUTSIDE_MKAD)
        text_element = questions_about_important_page.get_text_on_question(QL.TEXT_OUTSIDE_MKAD)

        assert text_element == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()




