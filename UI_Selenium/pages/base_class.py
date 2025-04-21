import locale
import random
import time

import allure
from selenium import webdriver
from selenium.common import TimeoutException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
from datetime import datetime, timedelta


class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    """Метод потока"""
    def bypass(self, url):
        th = Thread(target=self.driver.get, args=(url,))
        th.start()


    """Открыть страницу в браузере"""
    def open(self, url):
        self.driver.get(url)


    """Метод для получения текущего url"""
    def get_current_url(self):
        return self.driver.current_url


    """Метод перехода на новую вкладку(последнюю)"""
    def swith_to_new_window(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])


    """Метод перехода на первоначальную вкладку"""
    def swith_to_old_window(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])



    """Метод по ожиданию элемента"""
    def element_is_visible(self, locator, timeout=60):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))



    """Метод по ожиданию элементов"""
    def element_all_visible(self, locator, timeout=60):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))


    """Метод по нахождению элемента в DOM"""
    def element_is_present(self, locator, timeout=60):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))



    """Метод по нахождению элементов в DOM"""
    def element_all_present(self, locator, timeout=60):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))


    """Метод по клику на элемент"""
    def element_is_clickable(self, locator, timeout=60):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))



    """Метод по переключению на iframe"""
    def element_is_available_and_switch_to_it(self, locator, timeout=60):
        return wait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))


    """Метод скролл до элемента"""
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    """Метод клик до элемента"""
    def click_to_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)



    """Ввод текста если не работает стандартный метод"""
    def input_text(self, element, value):
        ActionChains(self.driver).move_to_element(element).click(element).send_keys(value).perform()


    """Скролиинг"""
    def scroll(self, col):
        self.driver.execute_script(f'window.scrollTo(0, {col})')


    def scroll_to_element_click(self, element):
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).pause(1).click(element).perform()


    """Другое"""
    def alert_wait(self, timeout=10):
        return wait(self.driver, timeout).until(EC.alert_is_present())


    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")


    """Скриншот"""
    def screen(self):
        self.driver.save_screenshot(f"UI/CMS/utilities/screens/screenshot_{datetime.now().strftime('%d_%b_%y_%H_%M_%S')}.png ")


    """Скрин всей области"""
    def screen_full(self):
        element = self.driver.find_element(By.TAG_NAME, 'body')
        element.screenshot(f"UI/CMS/utilities/screens/screenshot_full_{datetime.now().strftime('%d_%b_%y_%H_%M_%S')}.png")


    """Перевод даты"""
    def format_date_(self):
        locale.setlocale(locale.LC_TIME, 'ru_RU')
        now = datetime.now()
        formatted_date = now.strftime('%d %b %Y')
        return formatted_date[0:6].strip()


    """Выбор рандомного значения в Селекте(Открывает селект и выбирает значение)"""
    def click_on_react_select(self, data_test_id, text=None):

        self.element_is_clickable((By.CSS_SELECTOR,
                                   f"[data-testid={data_test_id}] .bcp-select__control:not(.bcp-select__control--is-disabled")).click()
        time.sleep(1)
        if text is None:
            items = self.element_all_present((By.CSS_SELECTOR, f"[data-testid={data_test_id}] .bcp-select__option"))
            random_el = random.randint(1, len(items))
            self.element_is_present(
                 (By.CSS_SELECTOR, f"[data-testid={data_test_id}] .bcp-select__option:nth-child({random_el})")).click()
        else:
            self.click_to_element(
                self.element_is_present(
                (By.XPATH, f"//div[@data-testid='categories-select']//span[text() = '{text}']")))


    """Ввод текста в селект и выбор значения"""
    def input_on_react_select(self, data_test_id, text):
        self.element_is_visible((By.CSS_SELECTOR,
                                   f"[data-testid={data_test_id}] .bcp-select__control input")).send_keys(text)
        time.sleep(1)
        items = self.element_all_present((By.CSS_SELECTOR, f"[data-testid={data_test_id}] .bcp-select__option"))
        random_el = random.randint(1, len(items))
        self.click_to_element(self.element_is_present(
            (By.CSS_SELECTOR, f"[data-testid={data_test_id}] .bcp-select__option:nth-child({random_el})")))


    """Выбор рандомного актива в файлпикере"""
    def click_to_asset(self, data_test_id="asset-chooser-loader", element=None):
        if element is None:
            items = self.element_all_visible((By.CSS_SELECTOR, f"[data-testid={data_test_id}] .AssetPreview_card__fPONE"))
            random_el = random.randint(1, len(items))
            elem = (By.CSS_SELECTOR, f"[data-testid={data_test_id}] .AssetPreview_card__fPONE:nth-child({random_el}) > div:nth-of-type(1)")
        else:
            elem = (By.CSS_SELECTOR, f"[data-testid={data_test_id}] .AssetPreview_card__fPONE:nth-child(1) > div:nth-of-type(1)")
        self.element_is_clickable(elem).click()

    """Ввод в поиске значения и выбор актива"""
    def asset_chooser_search(self, text, data_test_id="asset-chooser-loader"):
        self.element_is_visible((By.CSS_SELECTOR, "input[data-testid='asset-chooser-search']")).send_keys(text)
        items = self.element_all_visible((By.CSS_SELECTOR, f"[data-testid={data_test_id}] .AssetPreview_card__fPONE"))
        random_el = random.randint(1, len(items))
        elem = (By.CSS_SELECTOR, f"[data-testid={data_test_id}] .AssetPreview_card__fPONE:nth-child({random_el}) > div")
        self.element_is_clickable(elem).click()


    """Метод по сохранению компонента в сайдбаре"""
    def save_component_in_sidebar(self):
        # self.element_is_clickable((By.XPATH, "(//span[text()='Сохранить'])[2]")).click()
        # self.click_to_element(self.element_is_present((By.XPATH, '(//button[.//span[text()="Сохранить"]])[2]')))
        self.click_to_element(self.element_is_present(("xpath", fr"(//span[text()='Сохранить'])[2]")))





    # """Выбор инстанса"""
    # def click_on_instance(self, instance):
    #     self.click_to_element(self.element_is_present((By.CSS_SELECTOR, "button[title='Сменить фронтовый инстанс']")))
    #     self.element_is_present((By.CSS_SELECTOR, "div[role='modal'] .bcp-select__value-container")).click()
    #     self.click_to_element(self.element_is_visible(
    #         (By.CSS_SELECTOR, f"div[role='modal'] .bcp-select__option:nth-child({instance})")))


    """Метод по добавлению скриншота в отчет allure"""
    def add_screenshot_for_allure(self):
        allure.attach(
        self.driver.get_screenshot_as_png(),
        name="Screenshot after opening page",
        attachment_type=allure.attachment_type.JPG)


    """Возвращение респонсов"""
    def get_response(self):
        sl = []
        for request in self.driver.requests:
            sl.append(request.url)
            print(request.url, request.response.status_code)
        print(sl)
        return sl