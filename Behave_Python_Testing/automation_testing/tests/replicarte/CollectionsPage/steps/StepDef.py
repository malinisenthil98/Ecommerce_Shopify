from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonConfigs import logconfig
from BDDCommon.CommonConfigs import locatorsconfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random

def category_list(context):
    category_list = ['Abstrato', 'Animais', 'Arquitetura & Urbano', 'Astronomia', 'Dança & Música', 'Esportes',
                'Figurativa','Floral', 'Militar & Guerra', 'Paisagem', 'Paisagem Marítima', 'Religioso']
    return category_list
def get_category_index(context,Category):
    category_name = Category
    category_list(context)
    n1 = 0
    found = False
    print ("I am in get category index")
    for cat in category_list(context):

        if (cat == category_name):
            found = True
            break
        else:
         n1=n1+1

    if found == False:
        print ("Category does not exist")
    print("Value of n = ", n1)
    return n1


def click_on_item(context, cat_element):

    it = cat_element
    print("Item name is ::", it.text)
    webcommon.scroll_window_till_element_found(context, it)
    print("Window scroll down")

    item = context.driver.wait.until(EC.visibility_of(it))
    webcommon.scroll_window_till_element_found(context,item)
    context.driver.execute_script("arguments[0].click();", item)
    #item.click()
    print("item clicked")

    prod = locatorsconfig.REPLICARTE['product']

    context.products = context.driver.wait.until(EC.presence_of_all_elements_located((By.XPATH,prod['locator'])))
    #products = webcommon.find_elements(context, prod['type'], prod['locator'])
    product = context.products[0]

    webcommon.scroll_window_till_element_found(context,product)

    product.click()
    print ("picture selected")

def product_locator(context):
    return context.products

def pick_a_random_category(context):
    ele_list = category_list(context)
    ele_count = len(ele_list)
    n = random.randrange(ele_count)
    context.category_name = ele_list[n]
    return context.category_name




