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

@then('Verify "{app_name}" is present in  the installed apps, if not present, search and install "{app_name}"')
def verify_app_presence_in_InstalledApps(context,app_name):
    insApp = stepDef.check_installed_app(context,app_name)
    if len(insApp) == 0:
        stepDef.elseblock(context,app_name)
    else:
        context.livearf = insApp[0]
        found = False
        for app in insApp:
            name = context.driver.execute_script("return arguments[0].innerHTML;", app)
        #name = app.get_attribute('innerHTML')
            if name == app_name:
                found = True
                context.livearf = app
                break;
        if (found == True):
            print(app_name," is already Installed")
        else :
            print("App is not Installed yet")

@when('Select the app "{app_name}" and activate Livevue')
def activate_livevue(context,app_name):
    context.driver.refresh()
    insApp = stepDef.check_installed_app(context, app_name)
    if len(insApp) != 0:
        for app in insApp:
            name = context.driver.execute_script("return arguments[0].innerHTML;", app)
            if name == app_name:
                app.click()
            break;
    #context.driver.refersh();
    context.driver.switch_to_frame("app-iframe")
    act = locatorsconfig.SHOPIFY.get('activation')
    activation = webcommon.find_element(context,act['type'],act['locator'])
    activation.click()
    print("activation clicked")
    setact = locatorsconfig.SHOPIFY.get('setupActivation')
    setup = webcommon.find_element(context,setact['type'],setact['locator'])
    setup.click()

    clo = locatorsconfig.SHOPIFY.get('close')
    close = webcommon.find_element(context,clo['type'],clo['locator'])
    try:
        close.click()
    except:
        print ("Move on to activation steps")
    cat = locatorsconfig.SHOPIFY.get('catdwnld')
    catdown = webcommon.find_element(context,cat['type'],cat['locator'])
    #rec = locatorsconfig.SHOPIFY.get('resync')
    #resync = webcommon.find_element(context,rec['type'],rec['locator'])
    try:
        catdown.click()
    except :
        print("Move on step 2")

    button = locatorsconfig.SHOPIFY.get('nextbtn')
    nxt = webcommon.find_element(context,button['type'],button['locator'])
    nxt.click()
    print("Next button clicked")
    chbox = locatorsconfig.SHOPIFY.get('chkbox')
    ckbox = webcommon.find_elements(context,chbox['type'],chbox['locator'])

    n = 0
    for cx in ckbox:
        if (n==0 or n==3 or n==6 or n==7 or n==8 or n==11 or n==12 or n==13 or n==16):
            context.driver.execute_script("window.scrollBy(0,10)", "")
            context.driver.execute_script("arguments[0].click();", cx)

        n=n+1
    cat2 = locatorsconfig.SHOPIFY.get('cat2save')
    cat2save = webcommon.find_element(context,cat2['type'],cat2['locator'])
    context.driver.execute_script("arguments[0].click();", cat2save)
    print("Business category saved")
    cat2n = locatorsconfig.SHOPIFY.get('cat2next')
    cat2next = webcommon.find_element(context,cat2n['type'],cat2n['locator'])
    context.driver.execute_script("arguments[0].click();",cat2next)
    print("Moving to step 3")
    context.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    #radno= locatorsconfig.SHOPIFY.get('radioNo')
    #radioNo = webcommon.find_element(context,radno['type'],radno['locator'])
    radyes = locatorsconfig.SHOPIFY.get('radioYes')
    radioYes = webcommon.find_element(context,radyes['type'],radyes['locator'])
    context.driver.execute_script("arguments[0].click();",radioYes)
    enbhk = locatorsconfig.SHOPIFY.get('enableHook')
    enableHook = webcommon.find_element(context,enbhk['type'],enbhk['locator'])
    context.driver.execute_script("arguments[0].click();",enableHook)
    cat3n = locatorsconfig.SHOPIFY.get('cat3next')
    cat3next = webcommon.find_element(context,cat3n['type'],cat3n['locator'])
    context.driver.execute_script("arguments[0].click();",cat3next)
    print("Moving to step4")
    try:
        syn = locatorsconfig.SHOPIFY.get('syncallprod')
        syncAll = webcommon.find_element(context, syn['type'], syn['locator'])
        context.driver.execute_script("arguments[0].click();", syncAll)
    except :
        print("Move to step 5")



@then('Explore free themes and choose "{theme}"')
def change_theme(context,theme):
    themes = locatorsconfig.SHOPIFY.get('theme')
    the = webcommon.find_element(context,themes['type'],themes['locator'])
    the.click()
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

        name = context.driver.execute_script("return arguments[0].innerHTML;", tname)
        print ("Theme name : ",name)
        if name == theme:
            tname.click()
    add2themelib = locatorsconfig.SHOPIFY.get('Add_to_theme_library')
    a2TheLib = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, add2themelib['locator'])))
    a2TheLib.click()
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
    context.driver.switch_to.default_content()
    time.sleep(2)
    context.driver.wait.until(EC.frame_to_be_available_and_switch_to_it((frame1)))
    act2=locatorsconfig.SHOPIFY.get('action2')
    action2 = webcommon.find_element(context,act2['type'],act2['locator'])
    context.driver.execute_script("arguments[0].click();", action2)
    edcode = locatorsconfig.SHOPIFY.get('edit_code')
    edit_code = webcommon.find_element(context,edcode['type'],edcode['locator'])
    context.driver.execute_script("arguments[0].click();", edit_code)
    context.driver.switch_to.default_content()
    sec = locatorsconfig.SHOPIFY.get('section')
    section = webcommon.find_element(context,sec['type'],sec['locator'])
    context.driver.execute_script("arguments[0].click();",section)
    prod=locatorsconfig.SHOPIFY.get('prod_temp_liq')
    prod_temp=webcommon.find_element(context,prod['type'],prod['locator'])
    context.driver.execute_script("arguments[0].click();",prod_temp)
    time.sleep(5)






















