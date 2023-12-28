import os
import zipfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Общие функции
def archive_results(wrk_dir: str, arc_dir: str, arc_name: str, file_count: int):
    
    # Получаем список файлов в папке wrk_dir
    files = os.listdir(wrk_dir)
    
    # Если количество файлов больше file_count
    if len(files) >= file_count:
        # Создаем архив в папке arc_dir
        with zipfile.ZipFile(os.path.join(arc_dir, arc_name), 'w') as zip_file:
            # Добавляем в архив все файлы из папки wrk_dir
            for file in files:
                zip_file.write(os.path.join(wrk_dir, file), file)
        
        # Очищаем папку wrk_dir от файлов
        for file in files:
            os.remove(os.path.join(wrk_dir, file))

# Функции используемые в тестах
def driver_chooser(browser: str):
    if browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    return driver

def color_picker(path, color, driver):
    path.click()
    driver.execute_script("arguments[0].value = arguments[1]", path, color)
    assert path.get_attribute("value") == color, "Pick color is broken"

def range_mover(path, start, course: str, steps): # start = start value (int); course = "left"/"right"
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
