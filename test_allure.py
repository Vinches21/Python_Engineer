import allure
import pytest

from UI_Selenium.pages.base_class import BaseClass


# @allure.title("Проверка равенства")
# @allure.description("Этот тест проверяет, что x > y")
# def test_positive_one():
#     x = 2
#     y = 3
#     assert x < y, "Не вверно"
#
# @allure.title("Проверка сложения")
# @allure.description("Этот тест проверяет сумму")
# def test_positive_two():
#     x = 2
#     y = 3
#     res = x + y
#     assert res == 5, "Не вверно"
#
#
# @allure.title("Специально созданный негативный тест")
# @allure.description("Этот тест проверяет что тест проваливается")
# def test_negative():
#     x = 2
#     y = 3
#     assert x > y, "Не вверно"

@pytest.mark.open
def test_open_yandex(driver):
    base_class = BaseClass(driver)
    base_class.open("https://ya.ru")