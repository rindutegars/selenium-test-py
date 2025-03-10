import unittest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@allure.feature("Login Feature")
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    @allure.story("Valid Login")
    def test_valid_login(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")

        with allure.step("Masukkan username"):
            driver.find_element(By.ID, "username").send_keys("tomsmith")

        with allure.step("Masukkan password"):
            driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        with allure.step("Klik tombol login"):
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(3)

        with allure.step("Verifikasi login berhasil"):
            success_message = driver.find_element(By.ID, "flash").text
            assert "You logged into a secure area!" in success_message

    @allure.story("Invalid Login")
    def test_invalid_login(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")

        with allure.step("Masukkan username salah"):
            driver.find_element(By.ID, "username").send_keys("wronguser")

        with allure.step("Masukkan password salah"):
            driver.find_element(By.ID, "password").send_keys("wrongpassword")

        with allure.step("Klik tombol login"):
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        with allure.step("Verifikasi login gagal"):
            error_message = driver.find_element(By.ID, "flash").text
            assert "Your username is invalid!" in error_message

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
