from selenium.webdriver.common.by import By

class CheckBoxPage:
    def __init__(self,driver):
        self.driver = driver
        self.url    = "https://demoqa.com/checkbox"


        # locators
        self.check_box  = (By.ID,"tree-node-home")

        # Output Fields
        self.result     = (By.ID,"result")
    
    def load(self):
        self.driver.get(self.url)
    
    def submit(self):
        checkbox_label = self.driver.find_element(By.CSS_SELECTOR, "label[for='tree-node-home']")
        checkbox_label.click()

    
    def get_output(self):
        result    = self.driver.find_element(*self.result).text
        return result

