from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.core import get_settings
from src.util.driver import WebDriver


class WebDriver(Chrome):
    def __init__(self, option = get_settings().LEVEL):
        path = get_settings().DRIVER_PATH
        chrome_options = Options()
        
        if option == "DEVELOP":
            pass
        
        else:
            pass
        
        Chrome.__init__(self, executable_path=path, options=chrome_options)
        
        
class DriverUtils(object):
    def __init__(self):
        self.timeout = 3
        self.driver = WebDriver()

        self.driver.get(url=get_settings().CRAWLING_URL)
        
        
    def wait_element(self, option: str, selector: str, value: str) -> bool:
        if option == "locate":
            return self.wait_until_located(selector=selector, value=value)
            
        elif option == "click":
            return self.wait_until_clickable(selector=selector, value=value)
        
        else:
            return False
    
    
    def wait_until_located(self, selector: str, value: str) -> bool:
        try:
            WebDriverWait(self.driver, timeout=self.timeout).until(
                EC.presence_of_element_located((selector, value))
            )
            return True
        
        except Exception as error:
            print(error)
            return False
            
     
    def wait_until_clickable(self, selector: str, value: str) -> bool:
        try:
            WebDriverWait(self.driver, timeout=self.timeout).until(
                EC.element_to_be_clickable((selector, value))
            )
            return True
        
        except Exception as error:
            print(error)
            return False
        
        
    def get_element_by_xpath(
        self,
        option: str,
        value: str,
        selector: str = By.XPATH
    ):
        flag = self.wait_element(
            option=option, selector=selector, value=value
        )
        
        if flag:
            element = self.driver.find_element(by=selector, value=value)
            return element
        
        else:
            return
    
    
    def get_element_by_name(
        self,
        option: str,
        value: str,
        selector: str = By.NAME
    ):  
        flag = self.wait_element(
            option=option, selector=selector, value=value
        )
        
        if flag:
            element = self.driver.find_element(by=selector, value=value)
            return element
        
        else:
            return
           
           
    def get_element_by_css_selector(
        self,
        option: str,
        value: str,
        selector: str = By.CSS_SELECTOR
    ):
        flag = self.wait_element(
            option=option, selector=selector, value=value
        )
        
        if flag:
            element = self.driver.find_element(by=selector, value=value)
            return element
        
        else:
            return
    
    
    def get_elements_by_xpath(
        self,
        option: str,
        value: str,
        selector: str = By.XPATH
    ):
        flag = self.wait_element(
            option=option, selector=selector, value=value
        )
        
        if flag:
            elements = self.driver.find_elements(by=selector, value=value)
            return elements

        else:
            return
     
     
    def get_elements_by_name(
        self,
        option:str,
        value: str,
        selector: str = By.NAME
    ):
        flag = self.wait_element(
            option=option, selector=selector, value=value
        )
        
        if flag:
            elements = self.driver.find_elements(by=selector, value=value)
            return elements
        
        else:
            return
    
    
    def get_elements_by_css_selector(
        self,
        option: str,
        value: str,
        selector: str = By.CSS_SELECTOR
    ):
        flag = self.wait_element(
            option=option, selector=selector, value=value
        )
        
        if flag:
            elements = self.driver.find_elements(by=selector, value=value)
            return elements
        
        else:
            return