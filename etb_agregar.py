
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

###################### Iniciacion del programa e inicio de sesion ############################

driver = webdriver.Chrome()
driver.get("https://suma.etb.co:6443/")

