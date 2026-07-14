import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#task1
URL = "http://uitestingplayground.com/textinput"
INPUT_TEXT = "ITCH"
TIMEOUT = 10

@pytest.fixture
def get_driver():
    options = Options()
    options.add_argument("--headless")
    driver_instance = webdriver.Firefox(options=options)
    yield driver_instance
    driver_instance.quit()

def open_page(driver: webdriver.Firefox):
    driver.get(URL)

def text_input(driver: webdriver.Firefox):
    input_field = WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.ID, "newButtonName")))
    input_field.clear()
    input_field.send_keys(INPUT_TEXT)

def click_button(driver: webdriver.Firefox):
    button = WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.ID, "updatingButton")))
    button.click()

def test_verify_button_text(get_driver: webdriver.Firefox):
    open_page(get_driver)
    text_input(get_driver)
    click_button(get_driver)
    WebDriverWait(get_driver, TIMEOUT).until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), INPUT_TEXT))
    actual_text = get_driver.find_element(By.ID, "updatingButton").text
    assert actual_text == INPUT_TEXT, f"Ожидалось: '{INPUT_TEXT}', получено: '{actual_text}'"


#task2
URL2 = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
TIMEOUT2 = 15

@pytest.fixture
def get_driver2():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

def wait_for_images_to_load(driver, locator):
    WebDriverWait(driver, TIMEOUT2).until(lambda d: len(d.find_elements(*locator)) >= 5, message="<img> не появились в DOM за нужное время")
    WebDriverWait(driver, TIMEOUT2).until(lambda d: all(d.execute_script("return arguments[0].complete && arguments[0].naturalWidth > 0;",
                                                                         img) for img in d.find_elements(*locator)), message="Картинки не прогрузились полностью!")

def test_third_image(get_driver2):
    get_driver2.get(URL2)
    img_locator = (By.TAG_NAME, "img")
    wait_for_images_to_load(get_driver2, img_locator)
    images = get_driver2.find_elements(*img_locator)
    target_alt = images[3].get_attribute("alt")
    assert target_alt == "award", f"Ожидали alt='award', а получили '{target_alt}'"
