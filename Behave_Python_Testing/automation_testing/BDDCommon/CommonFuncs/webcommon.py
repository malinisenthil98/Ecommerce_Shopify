"""
Module containing common function used in several tests.
Functions that are not test or feature specific.
"""
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Screenshot import Screenshot_Clipping
from PIL import Image



options =Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--window-size=1280,800");
options.add_argument("--allow-insecure-localhost")
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])







def go_to(url, browser_type=None):
    """
    Function to start instance of the specified browser and navigate to the specified url.

    :param url: the url to navigate to
    :param browser_type: the type of browser to start (Default is Chrome)

    :return: driver: browser instance
    """
    if not browser_type:
        # create instance of Chrome driver the browser type is not specified
        driver = webdriver.Chrome("C:\\Malini\\Selenium\\chromedriver.exe")
        #driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        #driver.implicitly_wait(20)

    elif browser_type.lower() == 'firefox':
        # create instance of the Firefox driver

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise Exception("The browser type '{}' is not supported".format(browser_type))

    # clean the url and go to the url
    url = url.strip()
    driver.get(url)
    driver.maximize_window()
    driver.wait = WebDriverWait(driver,20)
    return driver





def reach_homepage(context, url):
    """
    Function to print the confirmation
    :param context:
    :param url:
    """
    print("We reach the Home page of {} successfully!".format(url))

def assert_page_title(context, expected_title):
    """
    Function to assert title of current page.
    :param expected_title:
    :param context:
    """

    actual_title = context.driver.title
    print ("Actual title : ",actual_title)

    print("The actual title is: {}".format(actual_title))
    print("The expected title is: {}".format(expected_title))

    assert expected_title == actual_title, "The title is not as expected." \
                                           " Expected: {}, Actual: {}".format(expected_title, actual_title)
    print("The page title is as expected.")


def assert_current_url(context, expected_url):
    """
    Function to get the current url and assert it is same as the expected url.
    :param context:
    :param expected_url:
    """

    # get the current url
    current_url = context.driver.current_url


    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = 'https://' + expected_url + '/'

    assert current_url == expected_url, "The current url is not as expected." \
                                        " Actual: {}, Expected: {}".format(current_url, expected_url)

    print("The page url is as expected.")

# ======================================================================================#
def find_element(context, locator_attribute, locator_text):
        """
        Finds an element and returns the element object.
        :param context:
        :param locator_attribute: what to use to locate (example, id, class, xpath,....)
        :param locator_text: the locator text (ex. the id, the class, the name,...)
        """

        possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name",
                             "css selector"]

        if locator_attribute not in possible_locators:
            raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                                The approved attributes are : %s ' % possible_locators)
        try:
            element = context.driver.find_element(locator_attribute, locator_text)
            return element
        except Exception as e:
            raise Exception(e)

# ======================================================================================#
def find_elements(context, locator_attribute, locator_text):
            """
            Finds an element and returns the element object.
            :param context:
            :param locator_attribute: what to use to locate (example, id, class, xpath,....)
            :param locator_text: the locator text (ex. the id, the class, the name,...)
            """

            possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name",
                                 "css selector"]

            if locator_attribute not in possible_locators:
                raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                                    The approved attributes are : %s ' % possible_locators)
            try:
                element = context.driver.find_elements(locator_attribute, locator_text)
                return element
            except Exception as e:
                raise Exception(e)

# ======================================================================================#
def is_element_visible(element):
        '''
        Checks if element is visible and returns True or False
        '''

        if element.is_displayed():
            return True
        else:
            return False

# ======================================================================================#
def assert_element_visible(element):
        '''
        Function to check if the passed in element is visible.
        Raises and exception if it is not exception.
        '''

        if not element.is_displayed():
            raise AssertionError('The element is not displayed')
def type_into_element(context_or_element, input_value, locator_att, locator_text):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        input_filed = context_or_element
    else:
        input_filed = context_or_element.driver.find_element(locator_att, locator_text)

    input_filed.send_keys(input_value)
# ======================================================================================#
def click(context_or_element, locator_att=None, locator_text=None):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    element.click()
# ======================================================================================#
def scroll_window_till_element_found(context,element):
    context.driver.execute_script("arguments[0].scrollIntoView();", element)


def element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    element_text = element.text
    if not case_sensitive:
        if expected_text.lower() in element_text.lower():
            return True
        else:
            return False
    else:
        return True if expected_text in element_text else False


def assert_element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False):

    max_try = 5
    sleep_bn_try = 2
    for i in range(max_try):
        try:
            contains = element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive)
            assert contains, "Element does not contain text"
            break
        except AssertionError:
            print(f"Checking if element contains text. Retry number: {i}")

    else:
        raise Exception(f"Element with locator type '{locator_att}', and locator text '{locator_text}', "
                        f"does not contains the text '{expected_text}'. Retried {max_try * sleep_bn_try} seconds")

def assert_radio_is_selected(context_or_element, locator_att=None, locator_text=None):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    is_checked = element.get_attribute('checked')
    assert is_checked, f"The radio is not selected {element.get_attribute('name')}"
    # import pdb; pdb.set_trace()

def get_element_text(context_or_element, locator_att=None, locator_text=None):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element_text = context_or_element.text
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)
        element_text = element.text

    return element_text
