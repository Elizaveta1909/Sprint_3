from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import lk_button, text_in_lk, head_make_a_burger, constructor, logo_burgers, logout, login_1


class TestAccount:
    def test_go_to_private_account(self, private):
        driver = private

        driver.find_element(By.XPATH, lk_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, text_in_lk)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_from_private_account_to_constructor(self, private):
        driver = private

        driver.find_element(By.XPATH, lk_button).click()
        driver.find_element(By.XPATH, constructor).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, head_make_a_burger)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_from_private_account_to_burgers_label(self, private):
        driver = private

        driver.find_element(By.XPATH, lk_button).click()
        driver.find_element(By.XPATH, logo_burgers).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, head_make_a_burger)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_sing_out_of_private_account(self, private):
        driver = private

        driver.find_element(By.XPATH, lk_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, text_in_lk)))
        driver.find_element(By.XPATH, logout).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, login_1)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'