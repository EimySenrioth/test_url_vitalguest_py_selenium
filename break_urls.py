from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import os
import time


base = "https://vitalgest.vercel.app"  
result_dir = r"C:\Users\veronicob\Desktop\test_result_vitalguest"
os.makedirs(result_dir, exist_ok=True)
usuario = "adminseed@vitalgest.mx"
password = "Asdf1234@"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # LOGIN
    driver.get(f"{base}/login")
    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys(usuario)
    driver.find_element(By.NAME, "password").send_keys(password)
    # Buscar el botón por texto visible 'Iniciar Sesión'
    botones = driver.find_elements(By.TAG_NAME, "button")
    for boton in botones:
        if boton.text.strip().lower() == "iniciar sesión":
            boton.click()
            break
    else:
        raise Exception("Botón 'Iniciar Sesión' no encontrado")
    time.sleep(2)
    # 1. Añadir / al final
    driver.get(f"{base}/dashboard/delegations/")
    time.sleep(1)
    print("5) / al final, url:", driver.current_url)
    print("5) Título:", driver.title)
    with open(os.path.join(result_dir, "resultado_5.html"), "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open(os.path.join(result_dir, "resultado_5.txt"), "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot(os.path.join(result_dir, "resultado_5.png"))

    # 2. Añadir ID falso
    driver.get(f"{base}/dashboard/delegations/123")
    time.sleep(1)
    print("6) ID falso, url:", driver.current_url)
    print("6) Título:", driver.title)
    with open(os.path.join(result_dir, "resultado_6.html"), "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open(os.path.join(result_dir, "resultado_6.txt"), "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot(os.path.join(result_dir, "resultado_6.png"))

    # 3. Path traversal en delegations
    driver.get(f"{base}/dashboard/delegations/../users")
    time.sleep(1)
    print("7) path traversal delegations, url:", driver.current_url)
    print("7) Título:", driver.title)
    with open(os.path.join(result_dir, "resultado_7.html"), "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open(os.path.join(result_dir, "resultado_7.txt"), "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot(os.path.join(result_dir, "resultado_7.png"))

    # 4. Query param raro
    driver.get(f"{base}/dashboard/delegations?debug=true")
    time.sleep(1)
    print("8) query param raro, url:", driver.current_url)
    print("8) Título:", driver.title)
    with open(os.path.join(result_dir, "resultado_8.html"), "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open(os.path.join(result_dir, "resultado_8.txt"), "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot(os.path.join(result_dir, "resultado_8.png"))

    # 5. Hash raro
    driver.get(f"{base}/dashboard/delegations#admin")
    time.sleep(1)
    print("9) hash raro, url:", driver.current_url)
    print("9) Título:", driver.title)
    with open(os.path.join(result_dir, "resultado_9.html"), "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open(os.path.join(result_dir, "resultado_9.txt"), "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot(os.path.join(result_dir, "resultado_9.png"))

    # 6. Mayúsculas en ruta
    driver.get(f"{base}/dashboard/DELEGATIONS")
    time.sleep(1)
    print("10) mayúsculas en ruta, url:", driver.current_url)
    print("10) Título:", driver.title)
    with open(os.path.join(result_dir, "resultado_10.html"), "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open(os.path.join(result_dir, "resultado_10.txt"), "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot(os.path.join(result_dir, "resultado_10.png"))

    # 7. Punto y coma en ruta
    driver.get(f"{base}/dashboard/delegations;")
    time.sleep(1)
    print("11) punto y coma en ruta, url:", driver.current_url)
    print("11) Título:", driver.title)
    with open(os.path.join(result_dir, "resultado_11.html"), "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open(os.path.join(result_dir, "resultado_11.txt"), "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot(os.path.join(result_dir, "resultado_11.png"))



finally:
    driver.quit()
