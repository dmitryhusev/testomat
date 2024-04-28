from pytest_bdd import given, when, then, scenario, parsers
from playwright.sync_api import expect


@given('Navigate to login page')
def navigate_to(browser):
    browser.goto('https://playwright.dev/python/')

@given('Navigate to sign up page')
def signup_page(browser):
    browser.goto('https://app.testomat.io/users/sign_in')
    pass

@when('User on page')
def on_page(browser):
    pass

@then('Page title is')
def title_is(browser):
    assert "Playwright" in browser.title()

@then('Heading is')
def heading_is(browser):
    expect(browser.locator('//div/h1').first).to_contain_text('Playwright')

@then('Email field is displayed')
def title_is(browser):
    expect(browser.get_by_placeholder('name1@email.com').first).to_have_id('user_email')

    
#####

@scenario('../features/login.feature', 'Check home page title')
def test_home_page_title():
    pass

@scenario('../features/login.feature', 'Check home page heading text')
def test_home_page_heading():
    pass

@scenario('../features/signup.feature', 'Check sign up')
def test_signup_page():
    pass
