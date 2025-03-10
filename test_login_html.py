# automation testing selenium web driver + html test runner untuk visualisasi

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import HtmlTestRunner  # Tambahkan ini

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Setup WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")

        # Masukkan username
        driver.find_element(By.ID, "username").send_keys("tomsmith")

        # Masukkan password
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        # Klik tombol login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Tunggu 3 detik sebelum verifikasi pesan sukses
        time.sleep(3)

        # Verifikasi login berhasil
        success_message = driver.find_element(By.ID, "flash").text
        self.assertIn("You logged into a secure area!", success_message)

    def test_invalid_login(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")

        # Masukkan username yang salah
        driver.find_element(By.ID, "username").send_keys("wronguser")

        # Masukkan password yang salah
        driver.find_element(By.ID, "password").send_keys("wrongpassword")

        # Klik tombol login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Verifikasi login gagal
        error_message = driver.find_element(By.ID, "flash").text
        self.assertIn("Your username is invalid!", error_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/selenium-test/selenium-test-python/reports'))
