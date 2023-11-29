import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

def main():
    firefox = "firefox"
    chrome = "chrome"
    edge = "edge"

    print(f"Test 01: {test_webform(firefox)}")
    quit()

def test_webform(driver: str):

    # Определяем браузер
    if driver == "firefox":
        driver = webdriver.Firefox()
    elif driver == "chrome":
        driver = webdriver.Chrome()
    elif driver == "edge":
        driver = webdriver.Edge()

    assert_count = 0

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form", "Title \"Web form\" not found"
    assert_count += 1

    driver.implicitly_wait(10)

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
    datefield = driver.find_element(by=By.NAME, value="my-date")
    range1 = driver.find_element(by=By.CLASS_NAME, value="form-range")
    link1 = driver.find_element(by=By.LINK_TEXT, value="Return to index")

    # Взаимодействие с элементами
    text_box.send_keys("Test")
    pass_box.send_keys("123456")
    text_area.send_keys("Hello World!")
    dropdown1 = Select(test_select)
    dropdown1.select_by_visible_text("Two")
    test_datalist.send_keys("Seattle")
    test_file.send_keys(f"{os.getcwd()}\\test.txt") # Для Windows
#    test_file.send_keys(f"{os.getcwd()}/test.txt") # Для *nix систем
    check_box1.click()
    check_box2.click()
    r_button1.click()
    r_button2.click()
    color_picker(colpicker, "#7fff00", driver)
    assert_count += 1
    range_mover(range1, 5, "left", 3)
    assert_count += 1
    driver.implicitly_wait(20)
    date_picker(datefield, "11/20/2023")
    assert_count += 1
    link1.click()

    driver.implicitly_wait(20)

    title2 = driver.title
    assert title2 == "Index of Available Pages", "Title \"Index of Available Pages\" not found"
    assert_count += 1
    link2 = driver.find_element(by=By.LINK_TEXT, value="web-form.html")
    link2.click()
    
    driver.implicitly_wait(10)

    assert title == "Web form", "Title \"Web form\" not found"
    assert_count += 1

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!", "Text \"Received!\" not found"
    assert_count += 1
    driver.quit()

    if assert_count == 7:
        tpass = "PASSED"
    else: tpass = "FAILED"

    return tpass

# Используемые функции

# Взаимодействие с элементом Color Picker
def color_picker(path, color: str, driver):
    path.click()
    driver.execute_script("arguments[0].value = arguments[1]", path, color)
    assert path.get_attribute("value") == color, "Pick color is broken"

# Взаимодействие с элементом Date Picker
def date_picker(path, date: str):
    path.send_keys(date)
    assert path.get_attribute("value") == date, "Pick date is broken"

# Взаимодействие с элементом Range
def range_mover(path, start: int, course: str, steps: int): # start = start value (int); course = "left"/"right"
    if course == "left":
        course = Keys.LEFT
        mv_value = str(start - steps)
    elif course == "right":
        course = Keys.RIGHT
        mv_value = str(start + steps)

    path.click()
    for i in range(steps):
        path.send_keys(course)
    assert path.get_attribute("value") == mv_value, "Range mover is broken"


if __name__ == "__main__":
    main()