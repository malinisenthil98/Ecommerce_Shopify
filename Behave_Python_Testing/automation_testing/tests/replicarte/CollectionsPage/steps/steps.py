
import time
import random
from behave import given, when, then, step
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonSteps.webstepscommon import *
from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonConfigs import logconfig
from BDDCommon.CommonConfigs import locatorsconfig
import StepDef
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains







@then ('verify if the "{category_name}" exists on collections')
def is_category_exists(context,category_name):

    StepDef.pick_a_random_category(context)
    print("The category name Searched for :  ", context.category_name)
    cat = locatorsconfig.REPLICARTE.get('category')
    #context.elements = context.find_elements(context,cat['type'],cat['locator'])
    context.elements = context.driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, cat['locator'])))
    found = False

    for element in context.elements:
        ele_txt = element.text
        if (ele_txt == context.category_name):
            print(context.category_name, " exists in collections")
            found = True
            context.ele = element
            if (element.is_displayed()):
              print(context.category_name, " is displayed ")
        else:
            continue
    if (found == False):
        print (context.category_name, "does not exist in collections" )


@then ('click on the first item present in "{category_name}"')

def click_on_first_item(context,category_name):
    category_name = context.category_name
    print ("I am on click_on_item and item name is : ",category_name)
    item = context.ele
    StepDef.click_on_item(context,item)


@when('I click on "{Category}" and select the first picture from the collections')
def click_on_category_select_picture(context,Category):
    category_name = Category
    print("I am on given step and category name is  : ", category_name)
    j = StepDef.get_category_index(context,category_name)
    cate = locatorsconfig.REPLICARTE.get('category')
    webelements = context.driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,cate['locator'])))
    #webelements = webcommon.find_elements(context, cate['type'], cate['locator'])

    context.element = webelements[j]
    print ("I am on given step and the element here is :",context.element.text )
    StepDef.click_on_item(context,context.element)


@when('I click on "{CategoryName}" and select the first pic from the collections')
def click_on_category_select_pic(context,CategoryName):
    StepDef.pick_a_random_category(context)



    category_name = context.category_name
    print("I am on given step and category name is  : ", category_name)
    j = StepDef.get_category_index(context,category_name)
    cate = locatorsconfig.REPLICARTE.get('category')
    webelements = context.driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,cate['locator'])))
    #webelements = webcommon.find_elements(context, cate['type'], cate['locator'])

    context.element = webelements[j]
    print ("I am on given step and the element here is :",context.element.text )
    StepDef.click_on_item(context,context.element)










