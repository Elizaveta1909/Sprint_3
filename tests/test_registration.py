from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import lk_button, name, sing_in_button_1, e_mail, password, sing_in_button_2, login_1, wrong_password, \
    make_an_order

faker = Faker()


class TestRegistration:
    def test_registration(self, driver):
        email = faker.email()
        print(email)

        driver.find_element(By.XPATH, lk_button).click()
        driver.find_element(By.XPATH, sing_in_button_1).click()
        driver.find_element(By.XPATH, name).send_keys("Elizaveta")
        driver.find_element(By.XPATH, e_mail).send_keys(email)
        driver.find_element(By.XPATH, password).send_keys("123456")
        driver.find_element(By.XPATH, sing_in_button_2).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, login_1)))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(By.XPATH, e_mail).send_keys(email)
        driver.find_element(By.XPATH, password).send_keys("123456")
        driver.find_element(By.XPATH, login_1).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, make_an_order)))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_registration_wrong_password(self, driver):
        email = faker.email()
        print(email)

        driver.find_element(By.XPATH, lk_button).click()
        driver.find_element(By.XPATH, sing_in_button_1).click()
        driver.find_element(By.XPATH, name).send_keys("Elizaveta")
        driver.find_element(By.XPATH, e_mail).send_keys(email)
        driver.find_element(By.XPATH, password).send_keys("1234")
        driver.find_element(By.XPATH, sing_in_button_2).click()
        WebDriverWait(driver, 4).until(
            expected_conditions.visibility_of_element_located((By.XPATH, wrong_password)))

        assert driver.find_element(By.XPATH, wrong_password).text == 'Некорректный пароль'
