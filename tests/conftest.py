import pytest
from playwright.sync_api import Page

@pytest.fixture
def browser(page: Page, request):
    yield page
    if request.node.session.testsfailed > 0:
        page.screenshot(path=f"{request.node.name}.png")


