from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def inicializar_driver():
    try:
        driver = webdriver.Chrome()
        driver.get("http://0.0.0.0:8000/formulario.html")  # Reemplaza con la ruta local del archivo
        return driver
    except Exception as e:
        print(f"Error al iniciar el navegador: {e}")
        return None

def completar_formulario(driver):
    try:
        
        driver.find_element(By.ID, "nombre").send_keys("Juan Pablo Arias Betancur")
        driver.find_element(By.ID, "correo").send_keys("juan.arias.486@unisabaneta.edu.co")
        driver.find_element(By.ID, "telefono").send_keys("12332323321")
        driver.find_element(By.ID, "direccion").send_keys("sabaneta , Medellin, Antioquia")
        print("Formulario completado con éxito")
    except Exception as e:
        print(f"Error al completar el formulario: {e}")

def seleccionar_opciones(driver):
    try:
        # Seleccionar casillas de verificación
        driver.find_element(By.ID, "deporte").click()
        driver.find_element(By.ID, "tecnologia").click()

        # Seleccionar botón de opción
        driver.find_element(By.ID, "otro").click()
        print("Opciones seleccionadas correctamente")
        
    except Exception as e:
        print(f"Error al seleccionar opciones: {e}")

def interactuar_botones(driver):
    try:
        # Clic en el botón "Enviar"
        driver.find_element(By.ID, "cancelar").click()
        time.sleep(1)  # Tiempo de espera para Simular la acción del click del boton
        print("Botón 'Enviar' Pulsado correctamente")
    except Exception as e:
        print(f"Error al interactuar con los botones: {e}")

def cerrar_driver(driver):
    try:
        driver.quit()
        print("Navegador cerrado correctamente")
    except Exception as e:
        print(f"Error al cerrar el navegador: {e}")

if __name__ == "__main__":
    driver = inicializar_driver()
    if driver:
        completar_formulario(driver)
        seleccionar_opciones(driver)
        interactuar_botones(driver)
        time.sleep(10)  # Espera para Mantener el navegador abierto por un tiempo de 10 segg
        cerrar_driver(driver)
