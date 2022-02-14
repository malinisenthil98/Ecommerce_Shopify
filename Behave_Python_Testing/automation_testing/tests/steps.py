import time
import random
from behave import given, when, then, step
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonSteps import webstepscommon
from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonConfigs import logconfig
from BDDCommon.CommonConfigs import locatorsconfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import stepDef



@then('Check the price of the picture')
def check_price(context):
    prod_price = locatorsconfig.JEDIART.get('price')
    product_price = webcommon.find_element(context, prod_price['type'], prod_price['locator'])
    price = product_price.get_attribute("innerHTML")
    print("Product price : ", price)


@when('Select Design Type, click on Framed')
def select_desiginType(context):
    des_type = locatorsconfig.JEDIART.get('framed')
    framed = webcommon.find_element(context,des_type['type'],des_type['locator'])
    context.driver.execute_script("arguments[0].scrollIntoView();", framed)
    framed.click()
    print("Design Type : 'framed' selected")

@when('Select Frames, click on Black')
def select_frames(context):
    frame_clr = locatorsconfig.JEDIART.get('Black')
    black = webcommon.find_element(context,frame_clr['type'],frame_clr['locator'])
    black.click()
    print("Frame : 'Black' is selected")

@when('Select Frame Style, click on Calais Black Gold')
def select_frame_style(context):
    frame_styl = locatorsconfig.JEDIART.get('classic_black_gold')
    black_gold = webcommon.find_element(context,frame_styl['type'],frame_styl['locator'])
    black_gold.click()
    print("Frame Style : 'Classic_Black_Gold' is selected")


@then('Check the price "{option}" and Assert listed price with the Calculated price')
def assert_listedPrice_with_calculated_price(context,option):
    opt = option
    if opt == "with frame":
        calculated_price = stepDef.Calculate_price(context,'28X36','Calais Black Gold','None','None','None','None')
    elif opt == "with frame and glass":
        calculated_price = stepDef.Calculate_price(context,'28X36', 'Calais Black Gold', 'None', 'None', 'Clear Float Glass','None')

    elif opt == "with frame and laminate":
        calculated_price = stepDef.Calculate_price(context,'28X36', 'Calais Black Gold', 'None', 'None', 'None','Gloss Laminate')
    elif opt == "with frame and matt":
        calculated_price = stepDef.Calculate_price(context, '28X36', 'Calais Black Gold', 'Ash', 'None', 'None','None')
    calated_price ="$"+calculated_price
    print ("Calculated Price ",calated_price)
    prod_price = locatorsconfig.JEDIART.get('price')
    product_price = webcommon.find_element(context, prod_price['type'], prod_price['locator'])

    context.driver.wait.until(lambda driver: product_price.get_attribute("innerHTML")== calated_price)
    price = product_price.get_attribute("innerHTML")
    print("Product price : ", price)
    assert price == calated_price
    print ("Calculated price is same as listed price")

@when('Select Glass, click on clear float glass')
def select_glass(context):
    gls = locatorsconfig.JEDIART.get('glass')
    glass = webcommon.find_element(context,gls['type'],gls['locator'])
    glass.click()
    print("Glass option clicked")
    clr_fl_gls = locatorsconfig.JEDIART.get('clear_float_glass')
    clear_float_glass = webcommon.find_element(context,clr_fl_gls['type'],clr_fl_gls['locator'])
    clear_float_glass.click()
    print("clear float glass clicked")

@when('Select Laminate, click on Gloss Laminate')
def select_laminate(context):
    lam = locatorsconfig.JEDIART.get('laminate')
    lamina = webcommon.find_element(context,lam['type'],lam['locator'])
    lamina.click()
    print("Laminate option clicked")
    gls_lam = locatorsconfig.JEDIART.get('gloss_laminate')
    glos_lamin = webcommon.find_element(context,gls_lam['type'],gls_lam['locator'])
    glos_lamin.click()
    print("Gloss Laminate clicked")
@when('Select Matt, click on Black & Grey')
def select_matt(context):
    mat=locatorsconfig.JEDIART.get('matt1')
    matt=webcommon.find_element(context,mat['type'],mat['locator'])
    matt.click()
    print("Matt : Black & Grey selected")

@when('Select Matt Styles, click on Ash')
def select_matt_style(context):
    mat_stl = locatorsconfig.JEDIART.get('Ash')
    mat_styl = webcommon.find_element(context,mat_stl['type'],mat_stl['locator'])
    mat_styl.click()
    print("Matt Styles : Ash selected")
