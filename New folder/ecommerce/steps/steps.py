import time
import random
from behave import given, when, then, step
from selenium.webdriver.common.alert import Alert

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
import stepDef
from selenium.common.exceptions import NoSuchElementException


@when('Login with the "{username}" and "{password}"')
def login_shopify(context,username,password):

    log = locatorsconfig.SHOPIFY.get('login')
    login = webcommon.find_element(context, log['type'], log['locator'])
    login.click()
    print("Login button clicked")
    uname=locatorsconfig.SHOPIFY.get('username')
    #user=webcommon.find_element(context,uname['type'],uname['locator'])

    user = context.driver.wait.until(EC.visibility_of_element_located((By.XPATH,uname['locator'])))
    user.send_keys(username)
    print(username," entered in user name field")
    commit = locatorsconfig.SHOPIFY.get('next')
    #next = webcommon.find_element(context,commit['type'],commit['locator'])
    next=context.driver.wait.until(EC.element_to_be_clickable((By.XPATH,commit['locator'])))
    next.click()
    print("Next button clicked")
    pw = locatorsconfig.SHOPIFY.get('password')
    passwrd = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH,pw['locator'])))
    passwrd.send_keys(password)
    print("Password Entered")
    lgn = locatorsconfig.SHOPIFY.get('loginn')
    loginn = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH,lgn['locator'])))
    loginn.click()
    print("login button clicked")
    time.sleep(3)

@then('Delete "{app_name}" if already installed')
def delete_app_before_publish_theme(context,app_name):
    appre = locatorsconfig.SHOPIFY.get('apps')
    context.apps = context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, appre['locator'])))
    context.driver.execute_script("arguments[0].click();", context.apps)
    # context.apps.click()
    print("apps clicked")
    time.sleep(3)
    try:
        stepDef.deleteApp(context, app_name)
    except:
        print("No Apps available")


@then('Verify "{app_name}" is present in  the installed apps, if not present, search and install "{app_name}",else Delete and install')
def verify_app_presence_in_InstalledApps(context,app_name):
    context.driver.switch_to.default_content()
    appre = locatorsconfig.SHOPIFY.get('apps')
    context.apps = context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, appre['locator'])))
    context.driver.execute_script("arguments[0].click();", context.apps)
    #context.apps.click()
    print("apps clicked")
    time.sleep(3)
    stepDef.Search_App(context, app_name)
    stepDef.Install_app(context)

    stepDef.elseblock(context, app_name)
    context.driver.refresh()
    time.sleep(2)
    stepDef.app_frame1(context)
    liv = locatorsconfig.SHOPIFY.get('livevue')
        # livevue=webcommon.find_element(context,liv['type'],liv['locator'])
    livevue = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, liv['locator'])))
    #context.driver.execute_script("arguments[0].click;",livevue)
    livevue.click()
    livAct = locatorsconfig.SHOPIFY.get('livevueAct')
    liveAct = context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, livAct['locator'])))
    liveAct.click()
    time.sleep(3)
    context.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    start = locatorsconfig.SHOPIFY.get('startpro')
    startpro = webcommon.find_element(context, start['type'], start['locator'])
    # context.driver.execute_script("arguments[0].scrollIntoView();", startpro)
    context.driver.execute_script("arguments[0].click();", startpro)
    time.sleep(5)
    con = locatorsconfig.SHOPIFY.get('confYes')
    # confirm = webcommon.find_element(context,con['type'],con['locator'])
    confirm = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, con['locator'])))
    confirm.click()
    time.sleep(10)
    testc1 = locatorsconfig.SHOPIFY.get('tcat1')
    testcat1 = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, testc1['locator'])))
    # testcat1 = webcommon.find_element(context,testc1['type'],testc1['locator'])
    #context.driver.execute_script("arguments[0].click;",testcat1)
    testcat1.click()
    time.sleep(5)

@when('Explore free themes and choose "{theme}"')
def change_theme(context,theme):
    stepDef.pick_a_random_theme(context)
    print("The theme name Searched for :  ", context.theme)


    themes = locatorsconfig.SHOPIFY.get('theme')
    the = webcommon.find_element(context,themes['type'],themes['locator'])
    context.driver.execute_script("arguments[0].click();", the)
    #the.click()
    the11 = locatorsconfig.SHOPIFY.get('theme11')
    thee11 = webcommon.find_element(context,the11['type'],the11['locator'])
    thee11.click()
    time.sleep(2)
    fra = locatorsconfig.SHOPIFY.get('frame1')
    frame1 = context.driver.wait.until(EC.presence_of_element_located((By.XPATH,fra['locator'])))
    context.driver.wait.until(EC.frame_to_be_available_and_switch_to_it((frame1)))
    #context.driver.switch_to_frame(frame1)

    context.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    free= locatorsconfig.SHOPIFY.get('freetheme')
    expfreetheme = context.driver.wait.until(EC.presence_of_element_located((By.XPATH,free['locator'])))
    context.driver.execute_script("arguments[0].scrollIntoView();", expfreetheme)
    expfreetheme.click()

    context.driver.switch_to.default_content()
    time.sleep(2)
    frm2 = locatorsconfig.SHOPIFY.get('frame2')
    frme2 = context.driver.wait.until(EC.presence_of_element_located((By.XPATH,frm2['locator'])))
    #context.driver.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frm2['locator'])))
    context.driver.switch_to_frame(frme2)
    themeName = locatorsconfig.SHOPIFY.get('theme_name')
    #theName = webcommon.find_elements(context,themeName['type'],themeName['locator'])
    theName = context.driver.wait.until(EC.visibility_of_all_elements_located((By.XPATH, themeName['locator'])))

    for tname in theName:
        try:
            name = context.driver.execute_script("return arguments[0].innerHTML;", tname)
            print ("Theme name : ",name)
        except:
            print("")

        if name == theme:
            context.driver.execute_script("arguments[0].click();", tname)
            #tname.click()
    add2themelib = locatorsconfig.SHOPIFY.get('Add_to_theme_library')
    a2TheLib = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, add2themelib['locator'])))
    context.driver.execute_script("arguments[0].click();", a2TheLib)
    #a2TheLib.click()
    print("Theme added to Library")
    context.driver.switch_to.default_content()
    context.driver.switch_to_frame(frame1)
    act1 = locatorsconfig.SHOPIFY.get('action1')
    action1=context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, act1['locator'])))
    context.driver.execute_script("arguments[0].click();", action1)
    pub = locatorsconfig.SHOPIFY.get('publish')
    publish= context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, pub['locator'])))
    context.driver.execute_script("arguments[0].click();", publish)
    context.driver.switch_to.default_content()
    time.sleep(2)
    context.driver.wait.until(EC.frame_to_be_available_and_switch_to_it((frme2)))
    #context.driver.switch_to_frame(frame3)
    pub_thee =locatorsconfig.SHOPIFY.get('publish_theme')
    pub_theme = webcommon.find_element(context,pub_thee['type'],pub_thee['locator'])
    context.driver.execute_script("arguments[0].click();", pub_theme)
    print("Theme Published")






















