
# paso1 -  Ejecutar el script
# paso2 - abrir la aplicacion
# paso3- iniciar sesion / las credenciales deben ser correctas
# paso4 - dirigirse al panel correcto / se debe buscar la forma ya sea que se le da la URL correcta
# paso5 - ir a la hoja de excel y buscar la cedula 
# paso6 - volver al  sistema / llenar el campo de la cedula para buscar el usuario y darle click a buscar 
# el sistema debe de entender si se obtuve una respuesta  o el usuario no se encuentra
# paso7 - Se da en un boton para dar de baja
# paso8 - Se debe recargar la pagina y esperar a que obtenga de nuevo el dasbhoard para de nuevo buscar al usuario y ver si su estadi es de baja 
# paso9 - Si el estado es de baja, se dirige a agregar de nuevo ese usuario
# paso10 - Se dirige a la hoja de excel y se relacionan los campos de excel con los del formulario y se llevan los datos al formulario para llenarlo, adicional a este se debe de dejar dar instrucciones nose si es algo valido poderla entrenar con el paso paso que debe hacer y luego soltarla a que la haga por si sola
# paso11 - Si este falla sacar un reporte del error // si este se da correctamente sacar exitoso 
# paso12 - Este script deja de funcionar si el usuario  da enter o el excel llega al fin / a lo ultimo debe generar un archivo txt con el reporte sobre los usuarios - diciendo que usuario con la cedula tal fue exitoso su baja y su integracion a la nueva campaña

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

###################### Iniciacion del programa e inicio de sesion ############################

driver = webdriver.Chrome()
driver.get("http://localhost:8000/iniciarSesion/")

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("je2006")
password.send_keys("Manila2026")
password.send_keys(Keys.ENTER)




############## Buscar usuarios ###############

driver.get("http://localhost:8000/usuarios")

# Esperar a que la página de usuarios cargue completamente
busqueda = driver.find_element(By.NAME, "buscador_Users")
busqueda.clear()
busqueda.send_keys("emergia")
busqueda.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(
    EC.url_contains("buscador_Users=emergia")
) 

############## Dar de baja usuario ###############

fila = driver.find_element(
    By.XPATH,
    "//tr[td[contains(text(),'emergia')]]"
)

boton = fila.find_element(By.TAG_NAME, "button")
boton.click()


fila = driver.find_element(
    By.XPATH,
    "//tr[td[contains(text(),'emergia')]]"
)

boton = fila.find_element(By.TAG_NAME, "button")
estado = boton.text

print("Estado actual:", estado)
################### Agregar Usuario #############################
driver.get("http://localhost:8000/agregar_usuario")

username = driver.find_element(By.NAME, "username")
email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")

username.send_keys("JUU")
email.send_keys("jj@gmail.com")
password.send_keys("Manila2026")
password.send_keys(Keys.ENTER)

# Mantener el navegador abierto por 10 segundos
time.sleep(200)

# Cerrar el navegador
driver.quit()


print("Proceso Exitoso")



