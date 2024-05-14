import allure
import pytest
from locators.scooter_home_page_locators import EXTEND_ORDER_OR_RETURN_SCOOTER_EARLIER, \
    TEXT_EXTEND_ORDER_OR_RETURN_SCOOTER_EARLIER, BRING_CHARGER_TO_SCOOTER, TEXT_BRING_CHARGER_TO_SCOOTER, CANCEL_ORDER, \
    TEXT_CANCEL_ORDER, OUTSIDE_MKAD, TEXT_OUTSIDE_MKAD, COST_AND_PAY, TEXT_COST_AND_PAY, SEVERAL_SCOOTERS, \
    TEXT_SEVERAL_SCOOTERS, RENTAL_TIME_CALCULATED, TEXT_RENTAL_TIME_CALCULATED, ORDER_SCOOTER_TODAY, \
    TEXT_ORDER_SCOOTER_TODAY
from pages.scooter_home_page import ScooterHomePage


@allure.title('Открыть вопрос и проверить его ответ')
@allure.description('Проверка когда нажимаешь на стрелочку, открывается соответствующий текст')
@pytest.mark.parametrize('question, answer, text_answer', [
    [COST_AND_PAY, TEXT_COST_AND_PAY, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
    [SEVERAL_SCOOTERS, TEXT_SEVERAL_SCOOTERS,
     'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
    [RENTAL_TIME_CALCULATED, TEXT_RENTAL_TIME_CALCULATED,
     'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
    [ORDER_SCOOTER_TODAY, TEXT_ORDER_SCOOTER_TODAY, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
    [EXTEND_ORDER_OR_RETURN_SCOOTER_EARLIER, TEXT_EXTEND_ORDER_OR_RETURN_SCOOTER_EARLIER,
     'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
    [BRING_CHARGER_TO_SCOOTER, TEXT_BRING_CHARGER_TO_SCOOTER,
     'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
    [CANCEL_ORDER, TEXT_CANCEL_ORDER,
     'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
    [OUTSIDE_MKAD, TEXT_OUTSIDE_MKAD, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']])
def test_open_questions_and_check_text(firefox_driver, question, answer, text_answer):
    scooter_home_page = ScooterHomePage(firefox_driver)
    scooter_home_page.scroll_to_questions_about_importan()
    scooter_home_page.click_to_question(question)
    text_element = scooter_home_page.get_text_answer(answer)

    assert text_element == text_answer
