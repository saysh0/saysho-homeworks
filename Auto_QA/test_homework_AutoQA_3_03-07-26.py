import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException


@pytest.fixture
def driver():
    firefox_service = Service(executable_path="./geckodriver.exe")
    driver = webdriver.Firefox(service=firefox_service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_itcareerhub_flow(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://itcareerhub.de/ru")
    logo_selector = "a[href*='itcareerhub'] img, img[src*='logo'], img[alt*='logo'], img[alt*='Logo']"
    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, logo_selector)))
    assert logo.is_displayed(), "Логотип ITCareerHub не отображается"
    def find_element_by_text_insensitive(text_to_find, tag_name="a"):
        try:
            elements = driver.find_elements(By.TAG_NAME, tag_name)
            matching_elements = []
            for elem in elements:
                try:
                    text = elem.get_attribute("textContent") or ""
                    if text_to_find.lower() in text.lower():
                        matching_elements.append(elem)
                except StaleElementReferenceException:
                    continue

            for elem in matching_elements:
                try:
                    if elem.is_displayed():
                        return elem
                except StaleElementReferenceException:
                    continue

            if matching_elements:
                return matching_elements[0]
        except Exception:
            pass
        return None

    expected_links = ["Программы", "Способы оплаты", "О нас", "Контакты", "Отзывы", "Блог"]
    for link_text in expected_links:
        elem = find_element_by_text_insensitive(link_text, tag_name="a")
        assert elem is not None, f"Ссылка '{link_text}' не найдена в структуре страницы"

        if link_text == "Контакты" and not elem.is_displayed():
            about_us_btn = find_element_by_text_insensitive("О нас", "a")
            if about_us_btn:
                ActionChains(driver).move_to_element(about_us_btn).perform()
                wait.until(lambda d: find_element_by_text_insensitive("Контакты", "a") is not None and
                                     find_element_by_text_insensitive("Контакты", "a").is_displayed())
                elem = find_element_by_text_insensitive(link_text, tag_name="a")

        assert elem.is_displayed(), f"Ссылка '{link_text}' скрыта от пользователя"

    lang_ru = find_element_by_text_insensitive("RU", "a") or find_element_by_text_insensitive("RU", "div")
    lang_de = find_element_by_text_insensitive("DE", "a") or find_element_by_text_insensitive("DE", "div")
    assert lang_ru is not None and lang_ru.is_displayed(), "Переключатель языка RU не найден"
    assert lang_de is not None and lang_de.is_displayed(), "Переключатель языка DE не найден"

    contacts_link = find_element_by_text_insensitive("Контакты", "a")
    if not contacts_link or not contacts_link.is_displayed():
        about_us_btn = find_element_by_text_insensitive("О нас", "a")
        if about_us_btn:
            ActionChains(driver).move_to_element(about_us_btn).perform()
            wait.until(lambda d: find_element_by_text_insensitive("Контакты", "a") is not None and
                                 find_element_by_text_insensitive("Контакты", "a").is_displayed())

    contacts_link = find_element_by_text_insensitive("Контакты", "a")
    contacts_link.click()

    def wait_for_callback_button(d):
        for tag in ["a", "button", "div", "span"]:
            btn = find_element_by_text_insensitive("Обратный звонок", tag)
            if btn and btn.is_displayed():
                return btn
        return False
    callback_btn = wait.until(wait_for_callback_button, message="Кнопка 'Обратный звонок' не появилась после перехода на страницу Контакты")
    driver.execute_script("arguments[0].click();", callback_btn)
    popup_selector = "[class*='popup'], [class*='modal'], .t-popup"
    popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, popup_selector)))
    expected_text = "Запишитесь на бесплатную карьерную консультацию"
    wait.until(lambda d: expected_text.lower() in popup.text.lower(), message=f"Текст '{expected_text}' не появился в модальном окне")