from locators.questions_about_important_page_locators import TITLE_QUESTIONS_ABOUT_IMPORTAN


class QuestionsAboutImportantPage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_questions_about_importan(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*TITLE_QUESTIONS_ABOUT_IMPORTAN))

    def click_to_question(self, element):
        self.driver.find_element(*element).click()

    def get_text_on_question(self, element):
        return self.driver.find_element(*element).text


