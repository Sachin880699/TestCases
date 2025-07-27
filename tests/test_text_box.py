import pytest
from pages.text_box_page import TextBoxPage

@pytest.mark.usefixtures("driver_init")
class TestTextBox:
    @pytest.mark.parametrize(
        'name,email,current_addr,perm_addr',
        [
            ("Sachin Pawar","sachin@test.com","123 Pune","456 Pune"),
            ("Tushar Pawar","tushar@test.com","123 Nagar","123 Nager")
        ]
    )
    def test_text_box_form(self, name, email, current_addr, perm_addr):
        page = TextBoxPage(self.driver)
        page.load()
        page.fill_form(name, email, current_addr, perm_addr)
        page.submit()
        output_name, output_email = page.get_output()

        assert name in output_name
        assert email in output_email