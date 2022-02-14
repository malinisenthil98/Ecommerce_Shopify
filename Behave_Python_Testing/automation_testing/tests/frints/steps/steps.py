import os
import time
import random
from behave import given, when, then, step
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonConfigs import logconfig
from BDDCommon.CommonConfigs import locatorsconfig
from BDDCommon.CommonSteps.webstepscommon import *
import StepDef
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import autoit
import pyautogui

@when ('Upload the picture for printing')
def upload_picture(context):
    pat = os.getcwd()
    pat1 = pat.replace('\\features','')
    path = pat1+"\Sample.jpg"
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    btn_locator = locatorsconfig.FRINTS.get('Choose_File_btn')
    choose = webcommon.find_element(context,btn_locator['type'],btn_locator['locator'])
    path1 = StepDef.refine_path(context,path)
    print ("New Path : ",path1)
    choose.send_keys(path1)
    print("File path entered ")
    time.sleep(10)