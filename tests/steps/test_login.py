from pytest_bdd import given, when, then, scenario, parsers
from playwright.sync_api import expect


@given('Navigate to login page')
def navigate_to(browser):
    browser.goto('https://playwright.dev/python/')

@when('User on page')
def on_page(browser):
    pass

@then('Page title is')
def title_is(browser):
    assert "Playwright" in browser.title()

@then('Heading is')
def heading_is(browser):
    title = browser.title
    expect(browser.locator('//div/h1').first).to_contain_text('Playwright')


@scenario('../features/login.feature', 'Check title')
def test_title():
    pass
    

@scenario('../features/login.feature', 'Check heading')
def test_heading():
    pass
