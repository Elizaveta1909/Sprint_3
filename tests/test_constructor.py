from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import buns_button, buns_text, sauses_button, sauses_text, filling_button, filing_text


class TestConstructor:
    def test_go_to_bulki(self, private):
        driver = private

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, buns_button)))
        driver.find_element(By.XPATH, buns_button)
        current_title = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, buns_text)))

        assert current_title.text == "Булки"

    def test_go_to_souses(self, private):
        driver = private

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, sauses_button)))
        driver.find_element(By.XPATH, sauses_button)
        current_title = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, sauses_text)))

        assert current_title.text == "Соусы"

    def test_go_to_nachinki(self, private):
        driver = private

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, filling_button)))
        driver.find_element(By.XPATH, filling_button)
        current_title = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, filing_text)))

        assert current_title.text == "Начинки"