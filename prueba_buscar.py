from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from openpyxl import load_workbook
import time

# ---------- 1. ABRIR NAVEGADOR ----------
driver = webdriver.Chrome()
driver.get("http://localhost:8000/iniciarSesion")

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("je2006")
password.send_keys("Manila2026")
password.send_keys(Keys.ENTER)



driver.get("http://localhost:8000/usuarios")

# ---------- 2. CARGAR EXCEL ----------
workbook = load_workbook("usuarios.xlsx")
sheet = workbook.active

# ---------- 3. RECORRER EXCEL ----------
for fila in range(2, sheet.max_row + 1):

    valor_busqueda = sheet.cell(row=fila, column=1).value

    if not valor_busqueda:
        break

    print(f"🔍 Buscando: {valor_busqueda}")

    # ---------- 4. BUSCAR ----------
    busqueda = driver.find_element(By.NAME, "buscador_Users")
    busqueda.clear()
    busqueda.send_keys(valor_busqueda)
    busqueda.send_keys(Keys.ENTER)

    # ---------- 5. ESPERAR RESULTADO ----------
    WebDriverWait(driver, 10).until(
    EC.url_contains("buscador_Users={valor_busqueda}".format(valor_busqueda=valor_busqueda))
) 
    time.sleep(20)  # Esperar a que los resultados se carguen
    

print("✅ Prueba de búsqueda terminada")
