from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from functions import iniciar_webdriver
import time

# Inicializa el WebDriver de Chrome
driver=iniciar_webdriver(headless=False,pos="izquierda")
# Navega a la página de Google Maps del lugar
driver.get("https://www.google.com/search?sa=X&sca_esv=e1f926a63c79aa92&sca_upv=1&biw=1920&bih=967&tbm=lcl&sxsrf=ADLYWIKymCx8BxhZqStsEGteXbXW4Ddq6w:1727500270727&q=bar%20tabernita%20reviews&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxI2NDU0MTIztzCxMDKyNDQ0MjU128DI-IpRNCmxSKEkMSm1KC-zJFGhKLUsM7W8eBErdnEAk1wZFkoAAAA&rldimm=1514267848229112556&hl=en-ES&ved=0CAwQ5foLahcKEwior4OB8OSIAxUAAAAAHQAAAAAQBQ#lkt=LocalPoiReviews&arid=ChZDSUhNMG9nS0VJQ0FnSUREa1pHZ2ZREAE&topic=mid:/m/05853c")

# Espera que la página cargue completamente
# time.sleep(5)  # Esto se puede ajustar según la velocidad de tu conexión
input("wait")
# Busca el botón de "Reseñas" y haz clic para abrirlas
reviews_button = driver.find_element(By.XPATH, '//button[contains(text(), "reseñas")]')
reviews_button.click()

# Espera a que las reseñas carguen
time.sleep(3)

# Extrae las reseñas
reviews = driver.find_elements(By.CLASS_NAME, 'section-review-text')

# Muestra las reseñas extraídas
for review in reviews:
    print(review.text)

# Cierra el navegador
driver.quit()
