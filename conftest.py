import logging

import pytest as pytest
from _pytest.runner import CallInfo
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)
