import time
import random
from behave import given, when, then, step
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonSteps.webstepscommon import *
from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonConfigs import logconfig
from BDDCommon.CommonConfigs import locatorsconfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def Search_App(context,app_name):
    srch = locatorsconfig.SHOPIFY.get('search')
    search = webcommon.find_element(context,srch['type'],srch['locator'])
    #search=context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,srch['locator'])))
    search.click()
    print("Search clicked")
    top = locatorsconfig.SHOPIFY.get('topApps')
    topapps = webcommon.find_element(context,top['type'],top['locator'])
    topapps.click()
    exp = locatorsconfig.SHOPIFY.get('explore')
    explore = webcommon.find_element(context,exp['type'],exp['locator'])
    explore.click()
    print("Explore apps clicked")
    handles = context.driver.window_handles
    parentWindow = handles[0]
    childWindow = handles[1]
    context.driver.switch_to.window(childWindow)
    srchapp= locatorsconfig.SHOPIFY.get('searchApp')
    searchapp = webcommon.find_element(context,srchapp['type'],srchapp['locator'])
    searchapp.send_keys(app_name)
    searchapp.send_keys(Keys.ENTER)
    print(app_name," entered in search box")
    apnam = locatorsconfig.SHOPIFY.get('appName')
    #appName = webcommon.find_elements(context,apnam['type'],apnam['locator'])
    appName = context.driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, apnam['locator'])))
    for app in appName:
        name = context.driver.execute_script("return arguments[0].innerHTML;", app)
        #name = app.get_attribute('innerHTML')
        print("App Name: ",name)
        if name != app_name:
            continue
        elif name == app_name:
            app.click()
            print(app_name," selected")
            break
def Install_app(context):
    adAPP = locatorsconfig.SHOPIFY.get('AddApp')
    AddAPP = webcommon.find_element(context,adAPP['type'],adAPP['locator'])
    AddAPP.click()
    insApp = locatorsconfig.SHOPIFY.get('installApp')
    installApp = webcommon.find_element(context,insApp['type'],insApp['locator'])
    context.driver.execute_script("arguments[0].scrollIntoView();", installApp)
    installApp.click()

def elseblock(context,app_name):
    print(app_name, " is not Installed yet.  Let's Search and Installed from the app store")
    Search_App(context, app_name)
    Install_app(context)
    print(app_name, " is successfully installed")
    context.driver.switch_to_frame("app-iframe")
    print("Switch to frame")
    context.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    chkbox = locatorsconfig.SHOPIFY.get('checkbox')
    checkbox = webcommon.find_elements(context, chkbox['type'], chkbox['locator'])
    for cbox in checkbox:
        context.driver.execute_script("arguments[0].click();", cbox)
    print("Check boxes selected")
    cr = locatorsconfig.SHOPIFY.get('create')
    create = webcommon.find_element(context, cr['type'], cr['locator'])
    create.click()
    print("Account is created on LIVEARf")
    #context.driver.switch_to.default_content()
def check_installed_app(context,app_name):
    appre = locatorsconfig.SHOPIFY.get('apps')
    context.apps = webcommon.find_element(context, appre['type'], appre['locator'])
    context.apps.click()
    insap = locatorsconfig.SHOPIFY.get('installedApp')
    insApp = webcommon.find_elements(context, insap['type'], insap['locator'])
    return insApp