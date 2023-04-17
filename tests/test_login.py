from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import lk_button, sing_in_button_1, e_mail, password, login_1_1, login_lk, login_2, make_an_order, \
    recover_password


class TestLogin:
    def test_login_main_button(self, driver):

        driver.find_element(By.XPATH, login_lk).click()
        driver.find_element(By.XPATH, e_mail).send_keys("elizavetasmirnova08192@ya.ru")
        driver.find_element(By.XPATH, password).send_keys("123456")
        driver.find_element(By.XPATH, login_1_1).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, make_an_order)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_PrivateAccount_button(self, driver):

        driver.find_element(By.XPATH, lk_button).click()
        driver.find_element(By.XPATH, e_mail).send_keys("elizavetasmirnova08192@ya.ru")
        driver.find_element(By.XPATH, password).send_keys("123456")
        driver.find_element(By.XPATH, login_1_1).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, make_an_order)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_through_registration_button(self, driver):

        driver.find_element(By.XPATH, lk_button).click()
        driver.find_element(By.XPATH, sing_in_button_1).click()
        driver.find_element(By.XPATH, login_2).click()
        driver.find_element(By.XPATH, e_mail).send_keys("elizavetasmirnova08192@ya.ru")
        driver.find_element(By.XPATH, password).send_keys("123456")
        driver.find_element(By.XPATH, login_1_1).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, make_an_order)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_through_forgot_password_button(self, driver):

        driver.find_element(By.XPATH, login_lk).click()
        driver.find_element(By.XPATH, recover_password).click()
        driver.find_element(By.XPATH, login_2).click()
        driver.find_element(By.XPATH, e_mail).send_keys("elizavetasmirnova08192@ya.ru")
        driver.find_element(By.XPATH, password).send_keys("123456")
        driver.find_element(By.XPATH, login_1_1).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, make_an_order)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'