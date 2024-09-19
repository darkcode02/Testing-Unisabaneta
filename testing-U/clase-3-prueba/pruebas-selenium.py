import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    #primero ejecutar: python3 -m http.server
    driver.get("http://localhost:8000/formulario.html")  # Cambiado a localhost
    yield driver
    driver.quit()

def test_formulario(driver):
    form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "formulario-prueba"))
    )
    
    # Llenar el formulario
    driver.find_element(By.ID, "nombre").send_keys("Juan Pablo")
    driver.find_element(By.ID, "apellido").send_keys("Arias")
    driver.find_element(By.ID, "email").send_keys("juan.pablo@gmail.com")
    driver.find_element(By.ID, "direccion").send_keys("Sabaneta")
    time.sleep(5)  # Mantiene el navegador abierto por 5 segundos
    
    # Enviar el formulario
    form.submit()
    
    driver.close()
