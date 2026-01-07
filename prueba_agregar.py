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

login_username = driver.find_element(By.NAME, "username")
login_password = driver.find_element(By.NAME, "password")


login_username.send_keys("je2006")
login_password.send_keys("Manila2026")
login_password.send_keys(Keys.ENTER)



driver.get("http://localhost:8000/agregar_usuario")

# ---------- 2. CARGAR EXCEL ----------
workbook = load_workbook("usuarios.xlsx")
sheet = workbook.active

# ---------- 3. RECORRER EXCEL ----------
for fila in range(2, sheet.max_row + 1):

    username = sheet.cell(row=fila, column=1).value
    email = sheet.cell(row=fila, column=2).value
    password = sheet.cell(row=fila, column=3).value

    if not username or not email or not password:
        continue

    print(f"🔍 Agregando: {username}")

    
    driver.get("http://localhost:8000/agregar_usuario")


    # ---------- 4. BUSCAR ----------
    

    input_username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)


    input_email = driver.find_element(By.NAME, "email")
    input_password = driver.find_element(By.NAME, "password")

    input_username.clear()
    input_username.send_keys(username)

    input_email.clear()
    input_email.send_keys(email)

    input_password.clear()
    input_password.send_keys(password)


    input_password.send_keys(Keys.ENTER)
    
    time.sleep(2) 
    

print("✅ Prueba de Agregar Usuarios terminada")
