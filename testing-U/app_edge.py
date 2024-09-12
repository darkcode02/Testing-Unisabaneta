from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options

# Configura el servicio y las opciones para Edge
service = EdgeService(executable_path='/usr/local/bin/msedgedriver')  # Reemplaza con la ruta a msedgedriver
options = Options()

# Inicia el WebDriver de Edge
driver = webdriver.Edge(service=service, options=options)

# Abre Google
driver.get("https://www.google.com")

# Verifica si "Google" está en el títulowebdriver edge 128.0.2739.79 
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
