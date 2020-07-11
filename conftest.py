import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")
    print(f"\nstart browser for test in {user_language}")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    link = f"http://selenium1py.pythonanywhere.com/{user_language}/"
    browser.get(link)
    browser.maximize_window()
    time.sleep(3)
    yield browser
    print("\nquit browser..")
    browser.quit()
