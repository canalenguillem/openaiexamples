from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome import service
from bs4 import BeautifulSoup

import undetected_chromedriver as uc

def iniciar_chrome():
    options = webdriver.ChromeOptions()
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    user_agent="Mozilla/5.0 (compatible; MSIE 7.0; Windows 95; Trident/3.1)"
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--window-size=1000,1000")
    # options.add_argument("--start-maximized")
    options.add_argument("--diable-web-security")
    options.add_argument("--disble-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sanbox")
    options.add_argument("--log-level=3")
    options.add_argument("--allow-runnig-insecure-content")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-blink-features=AutomationControlled")

    #parametros a omitir al inicio de chrome_driver
    exp_opt=[
        'enable-automation',
        'ignore-certificate-errors',
        'enable-loggin'
    ]
    options.add_experimental_option("excludeSwitches",exp_opt)

    #parámetros que definen las preferencias en chromedriver
    prefs={
        "profile.default_content_setting_values.notifications":2, #notificaciones 0=preguntar, 1=permitir, 2=no permitir
        "intl.accept_languages":["es-ES","es"],
        "credentials_enable_service":False
    }

    options.add_experimental_option("prefs",prefs)



    driver = webdriver.Chrome(service=service, options=options)
    
    return driver

def iniciar_webdriver(headless=False,pos="maximizada"):
    #maximizda, iquierda, derecha
    # Define a custom user agent
    my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    # Set up Chrome options
    options = uc.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument(f"user-agent={my_user_agent}")
    options.add_argument("--disable-search-engine-choice-screen")

    # options.add_argument("--headless")
    # options.add_experimental_option(
    #     "prefs",
    #     {
    #         "credentials_enable_service":False,
    #         "profile.password_manager_enabled":False
    #     },
    #     )
    # driver=uc.Chrome(
    #     options=options,
    #     log_level=3,
    # )

    # Initialize Chrome WebDriver with the specified options
    driver = uc.Chrome(options=options)

    if not headless:
        driver.maximize_window()
        if pos!="maximizada":
            ancho,alto=driver.get_window_size().values()
            if pos=="izquierda":
                driver.set_window_rect(x=0,y=0,width=ancho//2,height=alto)
            elif pos=="derecha":
                driver.set_window_rect(x=ancho//2,y=0,width=ancho//2,height=alto)
        return driver





if __name__=="__main__":
    # import undetected_chromedriver as uc
 
    # # Define a custom user agent
    # my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    
    # # Set up Chrome options
    # options = uc.ChromeOptions()
    # # options.add_argument("--headless")  # Corregido para incluir dos guiones
    # options.add_argument(f"user-agent={my_user_agent}")

    # Initialize Chrome WebDriver with the specified options
    driver = iniciar_webdriver(pos="derecha")

    # Make a request to your target website.
    driver.get("https://www.nowsecure.nl/")

    # Close the driver
    input()
    driver.quit()

