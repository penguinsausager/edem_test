import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://едем.рф'

try:
    # Открытие браузера на полный экран
    driver.get(url)
    driver.maximize_window()
    # Неявное ожидание
    driver.implicitly_wait(15)

    # Клик по кнопке входа
    driver.find_element(By.CSS_SELECTOR, '.header_auth-box_sign :nth-child(2)').click()

    # Ожидание, пока поле для ввода телефона станет активным
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '//input[@name="phone"]')))

    # Ввод телефонного номера
    phone_number_input = driver.find_element(By.XPATH, '//input[@name="phone"]')
    phone_number_input.click()
    phone_number_input.send_keys('70000000001')

    # Ввод пароля
    password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
    password_input.click()
    password_input.send_keys('test123456')

    # Нажатие на кнопку входа
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Ожидание прогрузки страницы (когда можно будет кликнуть по "+Создать поездку")
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '//a[@class="profile-user"]')))

    # Переход на вкладку "+Создать поездку"
    driver.find_element(By.CSS_SELECTOR, '.header_tour > .link-tour_create').click()

    # Ввод места отправления
    city_from = driver.find_element(By.XPATH, '//input[@data-name="fromCityId"]')
    city_from.click()
    city_from.send_keys('Екатеринбург')
    # Ожидание выпадающего окна
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '//div[@class="form-dropdown-title"]')))
    city_from.send_keys(Keys.ENTER)

    # Ввод улицы/района отправления
    from_address = driver.find_element(By.XPATH, '//input[@name="fromAddress"]')
    from_address.click()
    from_address.send_keys('Южный автовокзал')

    # Ввод места прибытия
    to_city = driver.find_element(By.XPATH, '//input[@data-name="toCityId"]')
    to_city.click()
    to_city.send_keys('Пермь')
    # Ожидание выпадающего окна
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.form-to .form-dropdown')))
    to_city.send_keys(Keys.ENTER)

    # Ввод улицы/района прибытия
    to_address = driver.find_element(By.XPATH, '//input[@name="toAddress"]')
    to_address.click()
    to_address.send_keys('Ленина, 28')

    # Клик по кнопке "ДАЛЕЕ"
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Выбор даты отправления
    driver.find_element(By.XPATH, '//input[@data-name="createdDate"]').click()
    driver.find_element(By.XPATH, '//div[@data-action="next"]').click()
    driver.find_element(By.XPATH, '(//div[@data-date="1"])[1]').click()

    # Выбор времени отправления
    driver.find_element(By.XPATH, '//input[@name="createdTime"]').click()
    # Выставляется 16 часов (Отсчет с 00, индексация с 1)
    driver.find_element(By.CSS_SELECTOR, '.clockpicker-dial :nth-child(17)').click()
    # Ожидание минутных часов
    time.sleep(0.5)
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.clockpicker-minutes')))
    # Выставляется 15 минут
    driver.find_element(By.CSS_SELECTOR, '.clockpicker-minutes > div:nth-child(4)').click()

    # Клик по кнопке "ДАЛЕЕ"
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Ввод бренда авто
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '//input[@data-name="brandId"]')))
    car_brand_input = driver.find_element(By.XPATH, '//input[@data-name="brandId"]')
    car_brand_input.send_keys('Toyota')
    time.sleep(1)
    car_brand_input.send_keys(Keys.ENTER)
    # Ожидание, пока поле выбора модели авто не станет активным
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '//input[@data-name="modelId"]')))
    # Ввод модели авто
    car_model_input = driver.find_element(By.XPATH, '//input[@data-name="modelId"]')
    car_model_input.click()
    car_model_input.send_keys('Supra')
    car_model_input.send_keys(Keys.ENTER)
    # Ожидание переключения на следующее поле
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '//input[@name="year"]')))
    # Ввод года выпуска авто
    year_car = driver.find_element(By.XPATH, '//input[@name="year"]')
    year_car.click()
    year_car.send_keys('1998')
    # Ожидание переключения на следующее поле
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '//input[@name="plateNumber"]')))
    # Ввод номера авто
    plate_number = driver.find_element(By.XPATH, '//input[@name="plateNumber"]')
    plate_number.click()
    plate_number.send_keys('x000xx')
    # Выбор цвета авто
    driver.find_element(By.XPATH, '//span[@style="background: #FFC0CB;"]').click()
    # Нажатие на кнопку "ДАЛЕЕ"
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Нажатие на кнопку "ДАЛЕЕ"
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '//span[@class="js-checkbox"]')))
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Нажатие на кнопку "ДАЛЕЕ" в разделе стоимость
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '//input[@data-name="cost0"]')))
    driver.find_element(By.CSS_SELECTOR, '.button-blue').click()

    # Выбор оплаты
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.ways-middle_text-primary')))
    driver.find_element(By.XPATH, '(//div[@class="ways-middle_text-primary"])[3]').click()
    # Нажатие на кнопку "ДАЛЕЕ"
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Подтверждение оплаты
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.form-checkbox_caption')))
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Клик по первому пункту в промо акциях
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.route-promo')))
    driver.find_element(By.XPATH, '//div[@class="route-promo_name "]').click()

    # Клик по клавише "Перейти к поездкам"
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Клик по "Детали поездки"
    driver.find_element(By.CSS_SELECTOR, '.button-md').click()

    # Клик по клавише "Редактировать"
    driver.find_element(By.CSS_SELECTOR, '.form-button.button-trans-lg').click()

    # Клик по клавише "Удалить поездку"
    driver.find_element(By.CSS_SELECTOR, '.js-account-routes-remove-handler').click()

    # Подтверждение удаления
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
