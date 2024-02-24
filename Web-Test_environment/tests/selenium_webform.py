import os
import func
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_webform(browser):
    # Определяем браузер
    driver = func.driver_chooser(browser)

    # Переходим на тестируемую страницу
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    driver.implicitly_wait(10)

    title = driver.title
    assert title == "Web form", "Title \"Web form\" not found"

    # Поиск основных элементов на странице
    text_box = driver.find_element(by=By.NAME, value="my-text")
    pass_box = driver.find_element(by=By.NAME, value="my-password")
    text_area = driver.find_element(by=By.NAME, value="my-textarea")
    test_select = driver.find_element(by=By.NAME, value="my-select")
    test_datalist = driver.find_element(by=By.NAME, value="my-datalist")
    test_file = driver.find_element(by=By.XPATH, value="/html/body/main/div/form/div/div[2]/label[3]/input")
    check_box1 = driver.find_element(by=By.ID, value="my-check-1")
    check_box2 = driver.find_element(by=By.ID, value="my-check-2")
    r_button1 = driver.find_element(by=By.ID, value="my-radio-1")
    r_button2 = driver.find_element(by=By.ID, value="my-radio-2")
    colpicker = driver.find_element(by=By.XPATH, value="/html/body/main/div/form/div/div[3]/label[1]/input")
    datepicker = driver.find_element(by=By.NAME, value="my-date")
    range1 = driver.find_element(by=By.CLASS_NAME, value="form-range")
    link1 = driver.find_element(by=By.LINK_TEXT, value="Return to index")

    # Взаимодействие с элементами
    text_box.send_keys("Test")
    pass_box.send_keys("123456")
    text_area.send_keys("Hello World!")
    Select(test_select).select_by_visible_text("Two")
    test_datalist.send_keys("Seattle")
    test_file.send_keys(f"{os.getcwd()}\\file.txt") # Для Windows
    # test_file.send_keys(f"{os.getcwd()}/file.txt") # Для *nix систем 
    check_box1.click()
    check_box2.click()
    r_button1.click()
    r_button2.click()
    func.color_picker(colpicker, "#7fff00", driver)
    func.range_mover(range1, 5, "left", 3)
    driver.implicitly_wait(20)
    datepicker.send_keys("11/20/2023")
    link1.click()

    # Переходим на другую страницу
    driver.implicitly_wait(20)

    title2 = driver.title
    assert title2 == "Index of Available Pages", "Title \"Index of Available Pages\" not found"

    link2 = driver.find_element(by=By.LINK_TEXT, value="web-form.html")
    link2.click()

    # Переходим на изначальную страницу    
    driver.implicitly_wait(10)

    assert title == "Web form", "Title \"Web form #2\" not found"

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    submit_button.click()

    # Переходим на другую страницу
    driver.implicitly_wait(10)

    message = driver.find_element(by=By.ID, value="message")
    assert message.text == "Received!", "Text \"Received!\" not found"

    driver.quit()
