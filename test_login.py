import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(browser):
    browser.get("https://bispb.odoo.com/web/login?redirect=%2Fodoo%3F")

    wait = WebDriverWait(browser, 10)

    email_input = wait.until(EC.visibility_of_element_located((By.NAME, "login")))
    email_input.clear()
    email_input.send_keys("bishnupb008@gmail.com")


    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_input.clear()
    password_input.send_keys("Bishnu@9040%")

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in')]")))
    login_button.click()
    time.sleep(5)

    crm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='result_app_3']")))
    crm_button.click()
    time.sleep(2)

    new_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'New')]")))
    assert new_button.is_displayed()
    new_button.click()
    time.sleep(5)

    gen_leads = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='action_generate_leads']")))
    assert gen_leads.is_displayed()
    gen_leads.click()
    time.sleep(5)

    close = wait.until(EC.visibility_of_element_located((By.XPATH, "// header/button[@class='btn-close']")))
    close.click()
    time.sleep(5)

    wait.until(EC.url_contains("/odoo"))
    assert "/odoo" in browser.current_url
