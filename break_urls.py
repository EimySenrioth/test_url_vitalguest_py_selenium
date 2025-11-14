from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


base = "https://vitalgest.vercel.app"  
usuario = "adminseed@vitalgest.mx"
password = "Asdf1234@"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:

    # LOGIN
    # 1. Añadir / al final
    driver.get(f"{base}/dashboard/delegations/")
    time.sleep(1)
    print("5) / al final, url:", driver.current_url)
    print("5) Título:", driver.title)
    with open("resultado_5.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open("resultado_5.txt", "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot("resultado_5.png")

    # 2. Añadir ID falso
    driver.get(f"{base}/dashboard/delegations/123")
    time.sleep(1)
    print("6) ID falso, url:", driver.current_url)
    print("6) Título:", driver.title)
    with open("resultado_6.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open("resultado_6.txt", "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot("resultado_6.png")

    # 3. Path traversal en delegations
    driver.get(f"{base}/dashboard/delegations/../users")
    time.sleep(1)
    print("7) path traversal delegations, url:", driver.current_url)
    print("7) Título:", driver.title)
    with open("resultado_7.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open("resultado_7.txt", "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot("resultado_7.png")

    # 4. Query param raro
    driver.get(f"{base}/dashboard/delegations?debug=true")
    time.sleep(1)
    print("8) query param raro, url:", driver.current_url)
    print("8) Título:", driver.title)
    with open("resultado_8.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open("resultado_8.txt", "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot("resultado_8.png")

    # 5. Hash raro
    driver.get(f"{base}/dashboard/delegations#admin")
    time.sleep(1)
    print("9) hash raro, url:", driver.current_url)
    print("9) Título:", driver.title)
    with open("resultado_9.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open("resultado_9.txt", "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot("resultado_9.png")

    # 6. Mayúsculas en ruta
    driver.get(f"{base}/dashboard/DELEGATIONS")
    time.sleep(1)
    print("10) mayúsculas en ruta, url:", driver.current_url)
    print("10) Título:", driver.title)
    with open("resultado_10.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open("resultado_10.txt", "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot("resultado_10.png")

    # 7. Punto y coma en ruta
    driver.get(f"{base}/dashboard/delegations;")
    time.sleep(1)
    print("11) punto y coma en ruta, url:", driver.current_url)
    print("11) Título:", driver.title)
    with open("resultado_11.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open("resultado_11.txt", "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot("resultado_11.png")



finally:
    driver.quit()
