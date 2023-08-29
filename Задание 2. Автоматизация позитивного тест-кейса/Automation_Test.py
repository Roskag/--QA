from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

successful_tests = 0
unsuccessful_tests = 0

try:
    driver.get("https://www.avito.ru/sankt-peterburg/avtomobili/volkswagen_golf_plus_1.4_amt_2007_114388km_2990663791")

    favorite_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.desktop-p6xjn6")))
    favorite_button.click() 

    driver.get("https://www.avito.ru/favorites")

    time.sleep(3)

    added_ad = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-marker='toggle-favorite-icon']")))
    print("Сценарий 1: Успешно")
    successful_tests += 1

except Exception as e:
    print(f"Ошибка: {e}")
    unsuccessful_tests += 1

finally:
    driver.quit()
    print(f"Всего выполнено сценариев: {successful_tests + unsuccessful_tests}")
    print(f"Успешных сценариев: {successful_tests}")
    print(f"Неуспешных сценариев: {unsuccessful_tests}")
