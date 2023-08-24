from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/Users/roskag/Downloads/chromedriver-mac-arm64')

driver.get('https://www.avito.ru/favorites')

try:
    driver.find_element_by_xpath('//div[contains(@class, "item")][1]//button[contains(@class, "icon-star")]').click()
    driver.find_element_by_xpath('//button[contains(text(), "Добавить в избранное")]').click()
    print("Тест 1: Объявление успешно добавлено в избранное.")
except Exception as e:
    print(f"Тест 1: Ошибка - {str(e)}")

try:
    driver.find_element_by_xpath('//div[contains(@class, "item")][1]//button[contains(@class, "icon-star-filled")]').click()
    driver.find_element_by_xpath('//button[contains(text(), "Удалить из избранного")]').click()
    print("Тест 2: Объявление успешно удалено из избранного.")
except Exception as e:
    print(f"Тест 2: Ошибка - {str(e)}")

driver.quit()
