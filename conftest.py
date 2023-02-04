import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as optionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language from the list: "
                          "ar, ca, cs, da, de, en-gb, el, es, fi, fr,it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans"
                     )


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    print("\nChecking language..")
    if browser_language in ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt",
                            "pt-br", "ro", "ru", "sk", "uk", "zh-hans"]:
        print("\nstart chrome browser for test..")
    else:
        raise pytest.UsageError("Select a proper --language")

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options_chrome = Options()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = optionsFirefox()
        options_firefox.set_preference("intl.accept_languages", browser_language)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
