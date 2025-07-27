class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url    = "https://demoqa.com"

    
    def go_to_homepage(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
    