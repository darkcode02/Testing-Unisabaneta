from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options

# Configura el servicio y las opciones para Firefox
service = FirefoxService(executable_path='/path/to/geckodriver')  # Reemplaza con la ruta a geckodriver
options = Options()

# Inicia el WebDriver de Firefox
driver = webdriver.Firefox(service=service, options=options)

# Abre Google
driver.get("https://www.google.com")

# Verifica si "Google" está en el título
assert "Google" in driver.title

# Busca el campo de búsqueda por su nombre
search_box = driver.find_element("name", "q")

# Escribe una búsqueda en el campo
search_box.send_keys("Selenium Python")

# Envía la búsqueda presionando Enter
search_box.send_keys(Keys.RETURN)

# Opcional: Espera unos segundos para ver los resultados
driver.implicitly_wait(5)

# Cierra el navegador
driver.quit()
