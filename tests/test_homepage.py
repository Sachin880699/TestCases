import pytest
from pages.home_page import HomePage


@pytest.mark.usefixtures("driver_init")
class TestHomePage:
    def test_title(self):
        home = HomePage(self.driver)
        home.go_to_homepage()
        assert "DEMOQA" in home.get_title()
