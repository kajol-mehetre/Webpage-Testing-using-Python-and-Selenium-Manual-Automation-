from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message
    driver.quit()

def test_invalid_username():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in message
    driver.quit()

def test_invalid_password():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in message
    driver.quit()

def test_empty_fields():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in message
    driver.quit()

def test_error_message_display():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text
    assert "invalid" in message.lower()
    driver.quit()

if __name__ == "__main__":
    test_valid_login()
    test_invalid_username()
    test_invalid_password()
    test_empty_fields()
    test_error_message_display()


