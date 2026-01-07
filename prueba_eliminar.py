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
for row in range(2, sheet.max_row + 1):

    valor_busqueda = sheet.cell(row=row, column=1).value

    if not valor_busqueda:
        break

    print(f"🔍 Buscando: {valor_busqueda}")

    busqueda = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "buscador_Users"))
    )

    busqueda.clear()
    busqueda.send_keys(str(valor_busqueda))
    busqueda.send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(
        EC.url_contains(str(valor_busqueda))
    )

    filas = driver.find_elements(
        By.XPATH,
        f"//tr[td[contains(text(), '{valor_busqueda}')]]"
    )

    if not filas:
        print("❌ Usuario no encontrado")
        continue

    fila_usuario = filas[0]
    boton_eliminar = fila_usuario.find_element(
    By.XPATH, ".//button[contains(text(), 'Eliminar')]"
)
    boton_eliminar.click()

    print(f"➡️ Acción disponible: {boton_eliminar}")
    
    time.sleep(2)


    

print("✅ Prueba de búsqueda terminada")
