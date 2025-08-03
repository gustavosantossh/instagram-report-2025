from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config.LoginInstagram import LoginInstagram
from src.config.ReportMap import ReportMap
from src.config.Config import Config

class ReportProcess:
    
    def __init__(self, window):
        config = Config.get()
        wait = WebDriverWait(window, 100)
        window.get(f"http://instagram.com/accounts/login/?next=%2F{config['username_to_report']}%2F&source=desktop_nav")
        LoginInstagram.login(By, EC, wait, config)
        ReportMap.report(By, EC, wait)