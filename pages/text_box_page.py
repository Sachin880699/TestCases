from selenium.webdriver.common.by import By

class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"

        # locators
        self.full_name_input = (By.ID,"userName")
        self.email_input     = (By.ID,"userEmail")
        self.current_address = (By.ID,'currentAddress')
        self.permanent_address=(By.ID,'permanentAddress')
        self.submit_button   = (By.ID,'submit')

        # Output fields
        self.output_name     = (By.ID, 'name')
        self.output_email    = (By.ID, 'email')

    def load(self):
        self.driver.get(self.url)

    def fill_form(self, name, email, current_addr, perm_addr):
        self.driver.find_element(*self.full_name_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.current_address).send_keys(current_addr)
        self.driver.find_element(*self.permanent_address).send_keys(perm_addr)

    
    def submit(self):
        # self.driver.find_element(*self.submit_button)[0].click()
        buttons = self.driver.find_elements(*self.submit_button)
        if buttons:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", buttons[0])
            buttons[0].click()
        else:
            raise Exception("No submit buttons found")
        
    
    def get_output(self):
        name    = self.driver.find_element(*self.output_name).text
        email   = self.driver.find_element(*self.output_email).text
        return name, email