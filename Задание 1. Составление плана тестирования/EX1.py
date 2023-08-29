from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Инициализация веб-драйвера (вам может потребоваться указать путь к драйверу)
driver = webdriver.Chrome()

successful_tests = 0
unsuccessful_tests = 0

try:
    # Добавление трех объявлений через переход по ссылкам
    ads_urls = [
        "https://www.avito.ru/sankt-peterburg/avtomobili/volkswagen_golf_plus_1.4_amt_2007_114388km_2990663791",
        "https://www.avito.ru/sankt-peterburg/kvartiry/2-k._kvartira_53m_824et._3342286436",
        "https://www.avito.ru/sankt-peterburg/odezhda_obuv_aksessuary/rubashka_lnyanaya_tommy_hilfiger_2854886423"
    ]

    for url in ads_urls:
        driver.get(url)
        favorite_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.desktop-p6xjn6")))
        favorite_button.click()
        time.sleep(3)
        driver.get("https://www.avito.ru/favorites")
        time.sleep(3)
        successful_tests += 1

    # Удаление всех объявлений из 'Избранного'
    try:
        # Шаг удаления всех объявлений из "Избранного"
        driver.get("https://www.avito.ru/favorites")
        time.sleep(3)

        # CSS-селектор для кнопки удаления объявлений
        delete_buttons = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".withFavorites-heart_fill-InZcS")))

        for button in delete_buttons:
            button.click()
            time.sleep(3)

        print("Все объявления успешно удалены из 'Избранного'")
        successful_tests += 1

    except Exception as e:
        print(f"Ошибка при удалении: {e}")
        unsuccessful_tests += 1

    # Добавление трех объявлений через поисковые запросы
    queries = [
        "Volkswagen Golf Plus 1.4 AMT, 2007, 114 388 км",
        "2-к. квартира, 53 м², 8/24 эт.",
        "Рубашка льняная Tommy Hilfiger"
    ]

    for query in queries:
        driver.get("https://www.avito.ru/sankt-peterburg")
        time.sleep(3)
        search_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'][data-marker='search-form/suggest']")))
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        first_ad_fav_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-marker='favorites-add'][data-state='empty']")))
        first_ad_fav_button.click()
        time.sleep(3)
        driver.get("https://www.avito.ru/favorites")
        time.sleep(3)
        successful_tests += 1

except Exception as e:
    print(f"Ошибка: {e}")
    unsuccessful_tests += 1

finally:
    driver.quit()
    print(f"Всего протестировано сценариев: {successful_tests + unsuccessful_tests}")
    print(f"Успешных тестов: {successful_tests}")
    print(f"Не успешных тестов: {unsuccessful_tests}")
