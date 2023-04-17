import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = "https://stellarburgers.nomoreparties.site/"

faker = Faker()


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1200,800")

    browser = webdriver.Chrome(options=options, executable_path="./chromedriver")
    browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def private(driver):
    driver.find_element(By.XPATH, "//button[contains(.,'Войти в аккаунт')]").click()
    driver.find_element(By.XPATH, "//label[contains(.,'Email')]/following-sibling::input").send_keys("elizavetasmirnova08192@ya.ru")
    driver.find_element(By.XPATH, "//label[contains(.,'Пароль')]/following-sibling::input").send_keys("123456")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()
    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))

    return driver