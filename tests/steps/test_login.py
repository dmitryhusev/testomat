from pytest_bdd import given, when, then, scenario

@scenario('../features/login.feature', 'Valid log in')
def test_login():
    pass

@given('Navigate to login page')
def navigate_to(browser):
    browser.goto('https://alib.com.ua')
    assert browser.title == 2

@when('User on page')
def on_page(browser):
    browser.goto('https://alib.com.ua')
    assert 1

@then('Page title is')
def title_is(browser):
    title = browser.title
    assert 1


# def test_1(browser):
#     browser.goto('https://alib.com.ua')
#     assert browser.title == '1'