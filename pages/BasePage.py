from selenium import webdriver

class BasePage:

    def __init__(self, driver):
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver

    def is_url(self, url):
        return self.driver.current_url == url
    
    def close(self):
        self.driver.quit()