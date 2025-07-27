import pytest
from pages.check_box_page import CheckBoxPage
import logging

logger = logging.getLogger(__name__)

import logging

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("driver_init")
class TestCheckBox:
    def test_check_box(self):
        logger.info("Starting checkbox test")

        page = CheckBoxPage(self.driver)
        page.load()
        logger.info("Page loaded")

        page.submit()
        logger.info("Checkbox clicked")

        output = page.get_output()
        logger.info(f"Output received: {output}")

        assert "You have selected" in output
        logger.info("Test passed")
