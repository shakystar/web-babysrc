from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
import time
import sys

url = 'http://localhost:8000'

def visit(payload):
    path = chromedriver_autoinstaller.install()
    try:
        options = webdriver.ChromeOptions()
        for _ in ["headless", "window-size=1920x1080", "disable-gpu", "no-sandbox", "disable-dev-shm-usage"]:
            options.add_argument(_)

        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(5)

        driver.get(url+f'/xss?payload={payload}')
        time.sleep(3)
    except:
        driver.quit()
        print("fail")
        return
        
    driver.quit()
    print("success")

visit(sys.argv[1])