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

def theme_list(context):
    theme_list = ['Debut','Dawn','Minimal','Brooklyn','Narrative','Supply','Venture','Boundless','Simple','Express']
    return theme_list


def Search_App(context,app_name):
    srch = locatorsconfig.SHOPIFY.get('search')
    #search = webcommon.find_element(context,srch['type'],srch['locator'])
    search=context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,srch['locator'])))
    search.click()
    print("Search clicked")
    top = locatorsconfig.SHOPIFY.get('topApps')
    topapps = webcommon.find_element(context,top['type'],top['locator'])
    topapps.click()
    exp = locatorsconfig.SHOPIFY.get('explore')
    explore = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, exp['locator'])))
        #webcommon.find_element(context,exp['type'],exp['locator'])
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
        if name == app_name:
            app.click()
            print(app_name," selected")
            break





def Install_app(context):

    adAPP = locatorsconfig.SHOPIFY.get('AddApp')
    AddAPP = webcommon.find_element(context,adAPP['type'],adAPP['locator'])
    AddAPP.click()
    insApp = locatorsconfig.SHOPIFY.get('installApp')
    installApp = context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, insApp['locator'])))
        #webcommon.find_element(context,insApp['type'],insApp['locator'])
    context.driver.execute_script("arguments[0].scrollIntoView();", installApp)
    context.driver.execute_script("arguments[0].click();", installApp)
    #installApp.click()

def elseblock(context,app_name):



    frame_app = locatorsconfig.SHOPIFY.get('app_frame')

    context.driver.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame_app['locator'])))
    time.sleep(5)
    print("Switch to frame")
    context.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    chkbox = locatorsconfig.SHOPIFY.get('checkbox')
    checkbox = webcommon.find_elements(context, chkbox['type'], chkbox['locator'])
    #for cbox in checkbox:
        #print ("Web Element : ",cbox)
    context.driver.execute_script("arguments[0].click();", checkbox[0])
    context.driver.execute_script("arguments[0].click();", checkbox[1])
    context.driver.execute_script("arguments[0].click();", checkbox[2])

    print("Check boxes selected")
    cr = locatorsconfig.SHOPIFY.get('create')
    create = context.driver.wait.until(EC.visibility_of_element_located((By.XPATH,cr['locator'])))
    context.driver.execute_script("arguments[0].click();",create)
    time.sleep(3)

    #create.click()
    print("Account is created on LIVEARf")
    #context.driver.switch_to.default_content()
def check_installed_app(context,app_name):

    insap = locatorsconfig.SHOPIFY.get('installedApp')
    insApp = context.driver.wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,insap['locator'])))
    #insApp = webcommon.find_elements(context, insap['type'], insap['locator'])
    return insApp




def app_frame(context):
    frame_app = locatorsconfig.SHOPIFY.get('app_frame')
    app_frame= context.driver.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,frame_app['locator'])))
    #context.driver.switch_to(app_frame)

def code_after_theme_published(context):
    fra = locatorsconfig.SHOPIFY.get('frame1')
    frame1 = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, fra['locator'])))
    context.driver.switch_to.default_content()
    time.sleep(2)
    context.driver.wait.until(EC.frame_to_be_available_and_switch_to_it((frame1)))
    act2 = locatorsconfig.SHOPIFY.get('action2')
    action2 = webcommon.find_element(context, act2['type'], act2['locator'])
    context.driver.execute_script("arguments[0].click();", action2)
    edcode = locatorsconfig.SHOPIFY.get('edit_code')
    edit_code = webcommon.find_element(context, edcode['type'], edcode['locator'])
    context.driver.execute_script("arguments[0].click();", edit_code)
    context.driver.switch_to.default_content()
    sec = locatorsconfig.SHOPIFY.get('section')
    section = webcommon.find_element(context, sec['type'], sec['locator'])
    context.driver.execute_script("arguments[0].click();", section)
    prod = locatorsconfig.SHOPIFY.get('prod_temp_liq')
    prod_temp = webcommon.find_element(context, prod['type'], prod['locator'])
    context.driver.execute_script("arguments[0].click();", prod_temp)
    time.sleep(5)

def activate_livevue(context,app_name):
    context.driver.refresh()
    insApp = check_installed_app(context, app_name)
    if len(insApp) != 0:
        for app in insApp:
            name = context.driver.execute_script("return arguments[0].innerHTML;", app)
            if name == app_name:
                app.click()
            break;
    context.driver.switch_to.default_content()
    time.sleep(10)
    app_frame1(context)
    act = locatorsconfig.SHOPIFY.get('activation')
    activation = webcommon.find_element(context,act['type'],act['locator'])
    activation.click()
    print("activation clicked")
    setact = locatorsconfig.SHOPIFY.get('setupActivation')
    setup = webcommon.find_element(context,setact['type'],setact['locator'])
    setup.click()

    context.driver.switch_to.default_content()
    time.sleep(3)
    frame_app = locatorsconfig.SHOPIFY.get('app_frame')
    app_frame = context.driver.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame_app['locator'])))


    try:

        clo = locatorsconfig.SHOPIFY.get('close')
        close = webcommon.find_element(context, clo['type'], clo['locator'])
        close.click()
    except:
        print ("Move on to activation steps")

    #rec = locatorsconfig.SHOPIFY.get('resync')
    #resync = webcommon.find_element(context,rec['type'],rec['locator'])
    try:
        cat = locatorsconfig.SHOPIFY.get('catdwnld')
        catdown = webcommon.find_element(context, cat['type'], cat['locator'])
        context.driver.execute_script("arguments[0].scrollIntoView();", catdown)
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

def deleteApp(context,app_name):
    insap = locatorsconfig.SHOPIFY.get('installedApp')
    # insApp = context.driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,insap['locator'])))
    insApp = webcommon.find_elements(context, insap['type'], insap['locator'])
    for app in insApp:
        print("Web element : ", app)
    context.livearf = insApp[0]
    found = False
    for app in insApp:
        name = context.driver.execute_script("return arguments[0].innerHTML;", app)
        # name = app.get_attribute('innerHTML')
        if name == app_name:
            found = True
            context.livearf = app
            break;
    if (found == True):
        print(app_name, " is already Installed")
        dele = locatorsconfig.SHOPIFY.get('delete')
        delete = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, dele['locator'])))
        delete.click()
        time.sleep(3)
        # context.driver.refresh()
        dele1 = locatorsconfig.SHOPIFY.get('delete1')
        delete1 = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, dele1['locator'])))
        context.driver.execute_script("arguments[0].click();", delete1)

        print("App deleted successfully")

    else:
        print("App is not Installed yet")

def app_frame1(context):
    frame_app = locatorsconfig.SHOPIFY.get('app_frame')
    app_frame = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, frame_app['locator'])))
    context.driver.switch_to_frame(app_frame)

def pick_a_random_theme(context):
    the_list = theme_list(context)
    theme_count = len(the_list)
    n = random.randrange(theme_count)
    context.theme = the_list[n]
    return context.theme

