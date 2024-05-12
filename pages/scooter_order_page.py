from locators.scooter_order_page_locators import BUTTON_ORDER_BOTTOM, NAME_FIELD, SURNAME_FIELD, ADDRESS_FIELD, \
    METRO_FIELD, PHONE_FIELD, SCOOTER_LOGO, YANDEX_LOGO, LIST_SUBWAY_STATIONS, BUTTON_NEXT, WHEN_BRING_SCOOTER, \
    DATE_CALENDAR, LEASE_TERM, RENTAL_PERIOD, BLACK_PEARL, COMMENT_FOR_COURIER, ORDER_BUTTON, CONFIRM_ORDER_CREATION, \
    ORDER_PLACED


class ScooterOrderPage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_button_order_bottom(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*BUTTON_ORDER_BOTTOM))

    def click_to_button_order(self, element):
        self.driver.find_element(*element).click()

    def set_name(self, name):
        self.driver.find_element(*NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*ADDRESS_FIELD).send_keys(address)

    def set_metro(self):
        self.driver.find_element(*METRO_FIELD).click()
        self.driver.find_element(*LIST_SUBWAY_STATIONS).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*PHONE_FIELD).send_keys(phone_number)

    def click_button_next(self):
        self.driver.find_element(*BUTTON_NEXT).click()

    def click_to_logo_scooter(self):
        self.driver.find_element(*SCOOTER_LOGO).click()

    def click_to_logo_yandex(self):
        self.driver.find_element(*YANDEX_LOGO).click()

    def fill_fields_for_scooter(self, name, surname, address, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro()
        self.set_phone_number(phone_number)
        self.click_button_next()

    def set_date_calendar(self):
        self.driver.find_element(*WHEN_BRING_SCOOTER).click()
        self.driver.find_element(*DATE_CALENDAR).click()

    def set_rental_period(self):
        self.driver.find_element(*LEASE_TERM).click()
        self.driver.find_element(*RENTAL_PERIOD).click()

    def choose_color_scooter(self):
        self.driver.find_element(*BLACK_PEARL).click()

    def set_comment(self, comment):
        self.driver.find_element(*COMMENT_FOR_COURIER).send_keys(comment)

    def click_button_order(self):
        self.driver.find_element(*ORDER_BUTTON).click()

    def click_button_confirm(self):
        self.driver.find_element(*CONFIRM_ORDER_CREATION).click()

    def get_text_order_placed(self):
        return self.driver.find_element(*ORDER_PLACED).text

    def fill_fields_lease(self, comment):
        self.set_date_calendar()
        self.set_rental_period()
        self.choose_color_scooter()
        self.set_comment(comment)
        self.click_button_order()
        self.click_button_confirm()

