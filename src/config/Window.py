from selenium import webdriver
from src.config.WindowConfig import WindowConfig
from src.config.ReportProcess import ReportProcess

class Window:
    """
        Creates a browser instance, applies its settings, and then starts the reporting process.
    """
    def __init__(self):
        window = webdriver.Chrome()
        WindowConfig.setup(window)
        ReportProcess(window)

        