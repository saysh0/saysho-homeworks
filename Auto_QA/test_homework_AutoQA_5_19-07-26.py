import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

#task1 Проверка наличия текста в iframe
PAGE_URL = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
TARGET_TEXT = "semper posuere integer et senectus justo curabitur."

def get_firefox_options():
    options = Options()
    options.add_argument("--headless")
    return options

@pytest.fixture
def driver():
    firefox = webdriver.Firefox(options=get_firefox_options())
    yield firefox
    firefox.quit()

class TestIframeText:
    def test_text_inside_iframe(self, driver):
        driver.get(PAGE_URL)
        wait = WebDriverWait(driver, timeout=10)
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        driver.switch_to.frame(iframe)
        all_elements = driver.find_elements(By.CSS_SELECTOR, "*")
        matching_element = None
        for element in all_elements:
            element_text = element.get_attribute("innerText") or ""
            if TARGET_TEXT.lower() in element_text.lower():
                matching_element = element
                break
        assert matching_element is not None, (f"Элемент '{TARGET_TEXT}' не найден в iframe")
        assert matching_element.is_displayed(), ("Элемент нашелся, но не отображается на странице")
        element_text = matching_element.get_attribute("innerText") or ""
        assert TARGET_TEXT.lower() in element_text.lower(), (f"Текст элемента не совпадает.\nОжидалось: '{TARGET_TEXT}'\nПолучено:  '{element_text}'")


#task2 Тестирование Drag & Drop (Перетаскивание изображения в корзину)
PAGE_URL = "https://www.globalsqa.com/demo-site/draganddrop/"

def get_firefox_options():
    options = Options()
    options.set_preference("network.proxy.type", 0)
    return options

@pytest.fixture
def driver():
    firefox = webdriver.Firefox(options=get_firefox_options())
    firefox.maximize_window()
    yield firefox
    firefox.quit()

def close_gdpr_popup(driver):
    try:
        WebDriverWait(driver, timeout=7).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        buttons = driver.find_elements(By.TAG_NAME, "button")
        agree_button = None
        for button in buttons:
            text = button.text.strip()
            if text in ("Соглашаюсь", "Agree", "Accept", "OK"):
                agree_button = button
                break
        if agree_button:
            agree_button.click()
            WebDriverWait(driver, timeout=5).until(EC.staleness_of(agree_button))
    except Exception:
        pass

def find_demo_iframe(driver):
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    for iframe in iframes:
        src = iframe.get_attribute("src") or ""
        if "photo-manager" in src:
            return iframe
    return None

class TestDragAndDrop:
    def test_dragged_photo_to_trash(self, driver):
        driver.get(PAGE_URL)
        wait = WebDriverWait(driver, timeout=15)
        close_gdpr_popup(driver)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        demo_iframe = wait.until(lambda d: find_demo_iframe(d))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", demo_iframe)
        time.sleep(1)
        driver.switch_to.frame(demo_iframe)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gallery li")))
        first_photo = driver.find_element(By.CSS_SELECTOR, "#gallery li:first-child")
        trash = driver.find_element(By.CSS_SELECTOR, "#trash")
        photos_before = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
        assert len(photos_before) == 4, (f"Ожидалось 4 фото, получили: {len(photos_before)}")
        source_loc = first_photo.location
        source_size = first_photo.size
        target_loc = trash.location
        target_size = trash.size
        start_x = source_loc["x"] + source_size["width"] // 2
        start_y = source_loc["y"] + source_size["height"] // 2
        end_x = target_loc["x"] + target_size["width"] // 2
        end_y = target_loc["y"] + target_size["height"] // 2
        steps = 10
        step_x = (end_x - start_x) / steps
        step_y = (end_y - start_y) / steps
        ActionChains(driver).click_and_hold(first_photo).perform()
        time.sleep(0.3)
        for _ in range(steps):
            ActionChains(driver).move_by_offset(step_x, step_y).perform()
            time.sleep(0.05)
        ActionChains(driver).release().perform()
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3)
        photos_in_gallery = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
        photos_in_trash = driver.find_elements(By.CSS_SELECTOR, "#trash li")
        assert len(photos_in_gallery) == 3, (f"В галерее должно быть 3 фото, осталось: {len(photos_in_gallery)}")
        assert len(photos_in_trash) == 1, (f"В корзине должно быть 1 фото, найдено: {len(photos_in_trash)}")
        