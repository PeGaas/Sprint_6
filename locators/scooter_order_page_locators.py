from selenium.webdriver.common.by import By
from data_generator import generate_metro_station, generate_date, generate_rental_period, random_color_choice

# Кнопка заказать вверху страницы
BUTTON_ORDER_TOP = [By.XPATH, "//button[@class='Button_Button__ra12g']"]

# Кнопка заказать внизу страницы
BUTTON_ORDER_BOTTOM = [By.CSS_SELECTOR, ".Button_UltraBig__UU3Lp"]

# Поле ввода Имя
NAME_FIELD = [By.CSS_SELECTOR, "[placeholder='* Имя']"]

# Поле ввода Фамилия
SURNAME_FIELD = [By.CSS_SELECTOR, "[placeholder='* Фамилия']"]

# Поля ввода Адрес:куда привезти заказ
ADDRESS_FIELD = [By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']"]

# Поле выбора Станция метро
METRO_FIELD = [By.CSS_SELECTOR, "[placeholder='* Станция метро']"]

# Список выбора Станции метро
LIST_SUBWAY_STATIONS = [By.XPATH, f'//li[@data-value="{generate_metro_station()}"]']

# Поле ввода Телефон: на него позвонит курьер
PHONE_FIELD = [By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']"]

# Кнопа Далее
BUTTON_NEXT = [By.CSS_SELECTOR, '.Button_Middle__1CSJM']

# Логотип Самокат
SCOOTER_LOGO = [By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR"]

# Логотип Яндекс
YANDEX_LOGO = [By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"]

# Поле ввода Когда привести самокат
WHEN_BRING_SCOOTER = [By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']"]

# Выбор даты в календаре
DATE_CALENDAR = [By.CSS_SELECTOR, f".react-datepicker__day--{generate_date()}"]

# Поле ввода срок аренды
LEASE_TERM = [By.CSS_SELECTOR, ".Dropdown-placeholder"]

# Поле выбора срока аренды из выпадающего списка
RENTAL_PERIOD = [By.XPATH, f"//div[@class='Dropdown-menu']/div[{generate_rental_period()}]"]

# Цвет самоката
COLLOR_SCOOTER = [By.CSS_SELECTOR, f"[for='{random_color_choice()}']"]

# Поле ввода Комментарий для курьера
COMMENT_FOR_COURIER = [By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']"]

# Кнопка Заказать
ORDER_BUTTON = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

# Хотите оформить заказ ?
CONFIRM_ORDER_CREATION = [By.XPATH, "//button[.='Да']"]

# Модальное окно Заказ оформлен
ORDER_PLACED = [By.XPATH, '//div[@class="Order_Modal__YZ-d3"]/div[@class="Order_ModalHeader__3FDaJ"]']
