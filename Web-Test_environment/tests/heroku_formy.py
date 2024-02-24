import func
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_formy(browser):
    # Определяем браузер
    driver = func.driver_chooser(browser)

    # Переходим на тестируемую страницу
    driver.get("https://formy-project.herokuapp.com/form")

    driver.implicitly_wait(10)

    pagename = driver.find_element(by=By.XPATH, value="/html/body/div/h1")
    assert pagename.text == "Complete Web Form", "Text \"Complete Web Form\" not found"

    # Поиск основных элементов на странице
    firstname = driver.find_element(by=By.ID, value="first-name")
    lastname = driver.find_element(by=By.ID, value="last-name")
    jobtitle = driver.find_element(by=By.ID, value="job-title")
    rbutton1 = driver.find_element(by=By.ID, value="radio-button-1")
    checkbox1 = driver.find_element(by=By.ID, value="checkbox-1")
    select_years = driver.find_element(by=By.ID, value="select-menu")
    datepicker = driver.find_element(by=By.ID, value="datepicker")
    sub_button = driver.find_element(by=By.CLASS_NAME, value="btn")

    # Взаимодействие с элементами
    firstname.send_keys("John")
    lastname.send_keys("Jameson")
    jobtitle.send_keys("Redaction Chief")
    rbutton1.click()
    checkbox1.click()
    Select(select_years).select_by_value("2")
    datepicker.send_keys("12/11/2023")
    sub_button.click()

    # Переходим на другую страницу
    driver.implicitly_wait(10)

    thanks = driver.find_element(by=By.CLASS_NAME, value="alert")
    assert thanks.text == "The form was successfully submitted!", "Text \"The form was successfully submitted!\" not found"

    driver.quit()
