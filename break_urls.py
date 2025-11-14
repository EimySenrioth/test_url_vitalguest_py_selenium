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

    # 1. Query param raro
    driver.get(f"{base}/dashboard/delegations?debug=true")
    time.sleep(1)
    print("8) query param raro, url:", driver.current_url)
    print("8) Título:", driver.title)
    with open(os.path.join(result_dir, "resultado_Query.html"), "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open(os.path.join(result_dir, "resultado_Query.txt"), "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot(os.path.join(result_dir, "resultado_Query.png"))
    # 2. Mayúsculas en ruta
    driver.get(f"{base}/dashboard/DELEGATIONS")
    time.sleep(1)
    print("10) mayúsculas en ruta, url:", driver.current_url)
    print("10) Título:", driver.title)
    with open(os.path.join(result_dir, "resultado_Mayusculas.html"), "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open(os.path.join(result_dir, "resultado_Mayusculas.txt"), "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot(os.path.join(result_dir, "resultado_Mayusculas.png"))
    # 3. Punto y coma en ruta
    driver.get(f"{base}/dashboard/delegations;")
    time.sleep(1)
    print("11) punto y coma en ruta, url:", driver.current_url)
    print("11) Título:", driver.title)
    with open(os.path.join(result_dir, "resultado_punto_coma.html"), "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    with open(os.path.join(result_dir, "resultado_punto_coma.txt"), "w", encoding="utf-8") as f:
        f.write(driver.find_element(By.TAG_NAME, "body").text)
    driver.save_screenshot(os.path.join(result_dir, "resultado_punto_coma.png"))


finally:
    driver.quit()
