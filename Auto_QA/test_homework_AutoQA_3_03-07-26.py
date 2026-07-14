import pytest
import shutil
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# ---------------------------------------------------------------------------
# Хелперы
# ---------------------------------------------------------------------------

def find_by_text(driver, text, tag="a"):
    """Находит видимый элемент по частичному совпадению текста (регистронезависимо)."""
    for elem in driver.find_elements(By.TAG_NAME, tag):
        if text.lower() in (elem.get_attribute("textContent") or "").lower():
            if elem.is_displayed():
                return elem
    return None


def hover_and_wait_visible(driver, wait, hover_target_text, target_text, tag="a"):
    """Наводит мышь на hover_target_text и ждёт появления target_text."""
    trigger = find_by_text(driver, hover_target_text, tag)
    assert trigger is not None, f"Элемент '{hover_target_text}' для hover не найден"
    ActionChains(driver).move_to_element(trigger).perform()
    wait.until(
        lambda d: find_by_text(d, target_text, tag) is not None,
        message=f"Элемент '{target_text}' не появился после наведения на '{hover_target_text}'"
    )


def click_contacts_link(driver, wait):
    """
    Кликает по ссылке 'Контакты' в дропдауне 'О нас'.
    Контакты ведут на отдельную страницу (/contact-us), поэтому после клика
    ждём загрузки новой страницы через смену URL.
    """
    contacts = find_by_text(driver, "Контакты")
    if contacts is None or not contacts.is_displayed():
        hover_and_wait_visible(driver, wait, "О нас", "Контакты")

    contacts = find_by_text(driver, "Контакты")
    assert contacts is not None, "Ссылка 'Контакты' не найдена"
    current_url = driver.current_url
    driver.execute_script("arguments[0].click();", contacts)

    # Ждём смены URL — признак что новая страница загружается
    wait.until(
        lambda d: d.current_url != current_url,
        message="URL не изменился после клика по 'Контакты' — страница не загрузилась"
    )


# ---------------------------------------------------------------------------
# Фикстуры
# ---------------------------------------------------------------------------

@pytest.fixture(scope="function")
def driver():
    gecko_path = shutil.which("geckodriver") or "./geckodriver.exe"
    service = Service(executable_path=gecko_path)
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def opened_site(driver):
    """Открывает главную страницу и возвращает (driver, wait)."""
    driver.get("https://itcareerhub.de/ru")
    wait = WebDriverWait(driver, 10)
    return driver, wait


# ---------------------------------------------------------------------------
# 1. Логотип
# ---------------------------------------------------------------------------

def test_logo_is_visible(opened_site):
    """Логотип ITCareerHub отображается на главной странице."""
    driver, wait = opened_site
    logo_selector = "a[href*='itcareerhub'] img, img[src*='logo'], img[alt*='logo'], img[alt*='Logo']"
    logo = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, logo_selector)),
        message="Логотип ITCareerHub не отображается"
    )
    assert logo.is_displayed()


# ---------------------------------------------------------------------------
# 2. Навигационные ссылки
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("link_text", [
    "Программы",
    "Способы оплаты",
    "О нас",
    "Отзывы",
    "Блог",
])
def test_nav_link_visible(opened_site, link_text):
    """Навигационная ссылка отображается в меню."""
    driver, wait = opened_site
    wait.until(
        lambda d: find_by_text(d, link_text) is not None,
        message=f"Ссылка '{link_text}' не найдена на странице"
    )
    elem = find_by_text(driver, link_text)
    assert elem.is_displayed(), f"Ссылка '{link_text}' скрыта от пользователя"


def test_contacts_link_visible_after_hover(opened_site):
    """Ссылка 'Контакты' становится видима после наведения на 'О нас'."""
    driver, wait = opened_site
    contacts = find_by_text(driver, "Контакты")
    if contacts is None or not contacts.is_displayed():
        hover_and_wait_visible(driver, wait, "О нас", "Контакты")
    contacts = find_by_text(driver, "Контакты")
    assert contacts is not None and contacts.is_displayed(), \
        "Ссылка 'Контакты' не отображается даже после hover на 'О нас'"


# ---------------------------------------------------------------------------
# 3. Переключатели языка
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("lang", ["RU", "DE"])
def test_language_switcher_visible(opened_site, lang):
    """Переключатель языка RU/DE отображается на странице."""
    driver, wait = opened_site
    wait.until(
        lambda d: find_by_text(d, lang, "a") is not None
                  or find_by_text(d, lang, "div") is not None,
        message=f"Переключатель языка '{lang}' не найден"
    )
    elem = find_by_text(driver, lang, "a") or find_by_text(driver, lang, "div")
    assert elem is not None and elem.is_displayed(), \
        f"Переключатель языка '{lang}' не отображается"


# ---------------------------------------------------------------------------
# 4. Переход на страницу Контакты
# ---------------------------------------------------------------------------

def test_contacts_page_opens(opened_site):
    """Клик по 'Контакты' открывает страницу с кнопкой 'Обратный звонок'."""
    driver, wait = opened_site

    click_contacts_link(driver, wait)

    wait.until(
        lambda d: find_by_text(d, "Обратный звонок", "a")
                  or find_by_text(d, "Обратный звонок", "button")
                  or find_by_text(d, "Обратный звонок", "div")
                  or find_by_text(d, "Обратный звонок", "span"),
        message="Страница 'Контакты' не загрузилась: кнопка 'Обратный звонок' не найдена"
    )


# ---------------------------------------------------------------------------
# 5. Попап «Обратный звонок»
# ---------------------------------------------------------------------------

def test_callback_popup_opens(opened_site):
    """Клик по 'Обратный звонок' открывает модальное окно с нужным текстом."""
    driver, wait = opened_site

    click_contacts_link(driver, wait)

    wait.until(
        lambda d: find_by_text(d, "Обратный звонок", "a")
                  or find_by_text(d, "Обратный звонок", "button")
                  or find_by_text(d, "Обратный звонок", "div")
                  or find_by_text(d, "Обратный звонок", "span"),
        message="Кнопка 'Обратный звонок' не появилась"
    )

    callback_btn = (
            find_by_text(driver, "Обратный звонок", "a")
            or find_by_text(driver, "Обратный звонок", "button")
            or find_by_text(driver, "Обратный звонок", "div")
            or find_by_text(driver, "Обратный звонок", "span")
    )
    driver.execute_script("arguments[0].click();", callback_btn)

    popup_selector = "[class*='popup'], [class*='modal'], .t-popup"
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, popup_selector)),
        message="Модальное окно не открылось"
    )

    expected_text = "Запишитесь на бесплатную карьерную консультацию"
    # Берём текст заново каждую итерацию, чтобы не словить stale reference на popup
    wait.until(
        lambda d: expected_text.lower() in (
            d.find_element(By.CSS_SELECTOR, popup_selector).text.lower()
        ),
        message=f"Текст '{expected_text}' не появился в модальном окне"
    )
    assert expected_text.lower() in driver.find_element(By.CSS_SELECTOR, popup_selector).text.lower()
