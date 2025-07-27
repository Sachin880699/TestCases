import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def driver_init(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    request.cls.driver = driver
    yield
    # quit driver
    driver.quit()

import logging
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
