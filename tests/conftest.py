import pytest
from playwright.async_api import Page

@pytest.fixture
def browser(page: Page):
    yield page


