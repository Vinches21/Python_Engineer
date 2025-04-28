import io
import time

import allure
import pytest
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("headless")
    options.add_argument("no-sandbox")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver




@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)  # сохраняем отчет в item



def take_full_page_screenshot(driver):
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")
    viewport_width = driver.execute_script("return window.innerWidth")
    stitched_image = Image.new("RGB", (viewport_width, total_height))

    offset_y = 0
    while offset_y < total_height:
        driver.execute_script(f"window.scrollTo(0, {offset_y})")
        time.sleep(0.5)  # Задержка для обновления страницы

        screenshot = driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screenshot))

        # Обрезаем изображение, если оно больше высоты страницы
        if offset_y + viewport_height > total_height:
            crop_height = viewport_height - (offset_y + viewport_height - total_height)
            image = image.crop((0, viewport_height - crop_height, viewport_width, viewport_height))

        stitched_image.paste(image, (0, offset_y))
        offset_y += viewport_height

    img_byte_arr = io.BytesIO()
    stitched_image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

@pytest.fixture(scope="function")
def take_screenshot(driver, request):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        print("Тест упал, делаю скриншот полной страницы...")
        screenshot = take_full_page_screenshot(driver)
        allure.attach(
            screenshot,
            name="Full page screenshot on failure",
            attachment_type=allure.attachment_type.PNG
        )