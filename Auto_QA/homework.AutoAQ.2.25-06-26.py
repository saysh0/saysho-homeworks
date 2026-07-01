"""
Скрипт для:
1. Открытия Firefox и перехода на https://itcareerhub.de/ru
2. Перехода в раздел "Способы оплаты"
3. Создания скриншота этой секции

Требования:
    pip install selenium Pillow
    geckodriver должен быть установлен и доступен в PATH
    Установка geckodriver: https://github.com/mozilla/geckodriver/releases
"""

import time
import io
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image


def take_element_screenshot(driver, element, filename: str) -> str:
    """
    Делает скриншот конкретного элемента на странице.
    Возвращает путь к сохранённому файлу.
    """
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.8)

    location = element.location
    size = element.size

    full_screenshot = driver.get_screenshot_as_png()
    image = Image.open(io.BytesIO(full_screenshot))
    device_pixel_ratio = driver.execute_script("return window.devicePixelRatio;") or 1

    left   = int(location["x"] * device_pixel_ratio)
    top    = int(location["y"] * device_pixel_ratio)
    right  = int((location["x"] + size["width"]) * device_pixel_ratio)
    bottom = int((location["y"] + size["height"]) * device_pixel_ratio)

    section_image = image.crop((left, top, right, bottom))
    section_image.save(filename)
    return filename


def find_payment_section(driver):
    """
    Ищет раздел 'Способы оплаты' только через CSS-селекторы и JavaScript.
    Возвращает найденный элемент или None.
    """

    css_selectors = [
        "[id*='payment']",
        "[id*='pay']",
        "[id*='оплат']",
        "[name*='payment']",
        "[data-section*='payment']",
        "[data-anchor*='payment']",
        "[class*='payment']",
        "[class*='pay-']",
    ]
    for selector in css_selectors:
        elements = driver.find_elements(By.CSS_SELECTOR, selector)
        if elements:
            print(f"   Найден через CSS: {selector}")
            return elements[0]

    element = driver.execute_script("""
        const keywords = ['Способы оплаты', 'способы оплаты'];

        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            null,
            false
        );

        let node;
        while ((node = walker.nextNode())) {
            const text = node.textContent.trim();
            if (keywords.some(kw => text.includes(kw))) {
                let el = node.parentElement;
                while (el && el !== document.body) {
                    const tag = el.tagName.toLowerCase();
                    if (tag === 'section') return el;
                    if (tag === 'div' && el.className &&
                        /section|block|container|wrap/i.test(el.className)) {
                        return el;
                    }
                    el = el.parentElement;
                }
                return node.parentElement;
            }
        }
        return null;
    """)

    if element:
        return element

    return None


def main():
    firefox_options = Options()
    from selenium.webdriver.firefox.service import Service
    service = Service("C:\\Users\\nikit\\PycharmProjects\\PythonProject\\Auto_QA\\geckodriver.exe")
    driver = webdriver.Firefox(service=service, options=firefox_options)

    # driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)

    try:
        print("1. Открываем https://itcareerhub.de/ru ...")
        driver.get("https://itcareerhub.de/ru")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)
        print(f"   Страница загружена: {driver.title}")
        print('Ищем раздел "Способы оплаты"')
        payment_section = find_payment_section(driver)
        if payment_section is None:
            raise RuntimeError(
                'Раздел "Способы оплаты" не найден. '
                "Проверь актуальную структуру сайта."
            )
        print("3. Делаем скриншот секции ...")
        output_path = Path("payment_section.png")
        take_element_screenshot(driver, payment_section, str(output_path))
        print(f"Скриншот сохранён: {output_path.resolve()}")

    except Exception as e:
        fallback_path = "error_screenshot.png"
        driver.save_screenshot(fallback_path)
        print(f"Ошибка: {e}")
        print(f"Полный скриншот для диагностики: {fallback_path}")
        raise

    finally:
        driver.quit()
        print("Браузер закрыт.")


if __name__ == "__main__":
    main()