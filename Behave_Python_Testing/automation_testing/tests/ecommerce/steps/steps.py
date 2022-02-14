import time
import random
from behave import given, when, then, step
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

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
import tkinter as tk
import re



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
            stepDef.elseblock(context, app_name)

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

@when('Get temporary email id and go to "{site}",Create an account with the temp_email_id')
def get_temp_email(context,site):
    copy=locatorsconfig.Temp_email.get('copy')
    click_copy = webcommon.find_element(context,copy['type'],copy['locator'])
    time.sleep(2)
    click_copy.click()
    root = tk.Tk()
    context.temp_email=root.clipboard_get()



    url = urlconfig.URLCONFIG.get('shopify')
    context.driver.get(url)
    print("shopify title : ", context.driver.title)

    username = context.temp_email
    res = [re.findall(r'(\w+?)(\d+)', username)[0]]
    store1 = res
    store = store1[0]
    context.storeName = store[0] + "Acumen"+str(stepDef.generate_random_number(context, 1000))
    context.password = "acumen#123"
    freeTrial = locatorsconfig.Temp_email.get('startFreeTrial')
    startTrial = webcommon.find_element(context, freeTrial['type'], freeTrial['locator'])
    startTrial.click()
    uname = locatorsconfig.Temp_email.get('username')
    usename = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, uname['locator'])))
    usename.send_keys(context.temp_email)
    print("Username entered")
    pw = locatorsconfig.Temp_email.get('pass')
    pword = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, pw['locator'])))
    pword.send_keys(context.password)
    print("Password entered")
    sn = locatorsconfig.Temp_email.get('store')
    sname = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, sn['locator'])))
    sname.send_keys(context.storeName)
    print("Store name entered")
    cs = locatorsconfig.Temp_email.get('createStore')
    crestor = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, cs['locator'])))
    crestor.click()
    print("Create store button clicked")
    skp= locatorsconfig.Temp_email.get('skip')
    skip = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, skp['locator'])))
    #skip=webcommon.find_element(context,skp['type'],skp['locator'])
    context.driver.execute_script("window.scrollBy(0,500)", "")
    #context.driver.execute_script("arguments[0].scrollIntoView();", skip)

    context.driver.execute_script("arguments[0].click();", skip)
    fn = locatorsconfig.Temp_email.get('firstName')
    #fname = context.driver.execute_script("arguments[0].scrollIntoView();", fn)
    fname = context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, fn['locator'])))
    fname.clear()
    fname.send_keys(store)
    ln = locatorsconfig.Temp_email.get('lastName')
    lname = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, ln['locator'])))
    lname.clear()
    lname.send_keys("Acumen")
    address = "678 East Santa Clara Street"
    ad = locatorsconfig.Temp_email.get('address')
    add = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, ad['locator'])))
    add.send_keys(address)
    city = "Fresno"
    ct = locatorsconfig.Temp_email.get('city')
    cty = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, ct['locator'])))
    cty.send_keys(city)
    cn = locatorsconfig.Temp_email.get('country')
    #cntry = context.driver.execute_script("arguments[0].scrollIntoView();", cn)
    context.driver.execute_script("window.scrollBy(0,500)", "")
    #cntry = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, cn['locator'])))
    #sel = Select(cntry)
    #sel.sel.select_by_visible_text("United States")
    st = locatorsconfig.Temp_email.get('state')
    #state = context.driver.execute_script("arguments[0].scrollIntoView();", st)
    statee = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, st['locator'])))
    sel = Select(statee)
    sel.select_by_value("CA")
    zip = "70563"
    zp = locatorsconfig.Temp_email.get('zip')
    #zep = context.driver.execute_script("arguments[0].scrollIntoView();", zp)
    zep = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, zp['locator'])))
    zep.send_keys(zip)
    mobile = "9250091234"
    ph = locatorsconfig.Temp_email.get('phone')
    phone = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, ph['locator'])))
    phone.send_keys(mobile)
    er = locatorsconfig.Temp_email.get('enter')
    #entr = context.driver.execute_script("arguments[0].scrollIntoView();", er)
    entr = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, er['locator'])))
    context.driver.execute_script("arguments[0].click();", entr)
    time.sleep(5)
    context.driver.back()
    print(context.driver.title)






























