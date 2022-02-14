import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import locatorsconfig

Product = {
    'Blue Green and Brown':{'base_price':70.4,'width':73,'height':108},
    'purple-robe-and-anemones-1937':{'base_price':44,'width':28,'height':36}
}



Picture_size = {
    '73.6X56.6': {'width':73.6,'height':56.6},
    '91.6X76.4': {'width': 91.6,'height': 76.4},
    '67X50': {'width' : 67,'height':50},
    '28X36':{'width': 28,'height':36}
}

Frame_Style = {
    'None':0,
    'Calais Black Gold' : 0.6,
    'Bevelled Black' : 0.65,
    'Chantilly Ornate Blac' : 0.7,
    'Calais Black Gold - _M':0.6,
    'Bevelled Black - _M':0.65,
    'Chantilly Ornate Black - _M':0.7,
    'Bevelled Natural':0.7,
    'Rustic Light Brown':0.75,
    'Moda Natural':0.8,
    'Bevelled Natural - _M':0.7,
    'Rustic Light Brown - _M':0.75,
    'Moda Natural - _M':0.8,
    'Thin flat gree':0.6,
    'Thin flat light blue':0.65,
    'Thin flat red':0.7,
    'Thin flat green - _M':0.6,
    'Thin flat light blue - _M':0.65,
    'Thin flat red - _M':0.7,
}
Matt_Styles = {
    'None':0,
    'Ash':0.16,
    'Black':0.15,
    'Charcoal':0.17,
    'Dresden':0.14,
    'Bluestone':0.13,
    'Sardinia blue':0.12,
    'Caramel':0.11,
    'Drift Wood':0.1,
    'Mustard Yellow':0.18

}
Second_Matt_Styles={
    'None':0,
    'Ash':0.016,
    'Black':0.015,
    'Charcoal':0.017,
    'Dresden':0.014,
    'Bluestone':0.013,
    'Sardinia blue':0.012,
    'Caramel':0.011,
    'Drift Wood':0.01,
    'Mustard Yellow':0.018,
}
Glass = {
    'None':0,
    'Clear Float Glass':0.12,
    'Non-reflective Glass':0.14,
    'PlexiGlass':0.15,
    'Clear Float Glass - _M':0.12,
    'Non-reflective Glass - _M':0.14,
    'PlexiGlass - _M':0.15
}
Laminate = {
    'None':0,
    'Gloss Laminate':0.1,
    'Matt Laminate':0.11,
    'Gloss Laminate - _M':0.1,
    'Matt Laminate - _M':0.11
}
Others ={
    'None':0,
    'addl_charge_block_mounting':50,
    'block_mounting_per_cm':0.02,
    'addl_charge_back_boarding':20,
    'back_boarding_per_cm':0.006,
    'addl_charge_glass':10,
    'addl_charge_matt1':20
}
def Calculate_price(context,picture,frame_style,matt_style,sec_matt_style,glass,laminate):
    pic = Product[picture]
    basePrice =pic['base_price']
    addl_charge_block_mounting = 50
    block_mounting_per_cm = 0.02
    addl_charge_back_boarding = 20
    back_boarding_per_cm = 0.006
    addl_charge_glass = 10
    addl_charge_matt1 = 20

    width = pic['width']
    height = pic['height']
    perimeter = 2*(width+height)
    mibl = max((width*1.5),(height*1.5))
    print ("MIBL = ",mibl)
    if (mibl <4 ):
        mibl = 4
    elif (mibl >9):
        mibl = 9

    wm1 = width+(2*mibl)
    hm1 = height+(2*mibl)

    if frame_style == "None":
        back_boarding_per_cm =0
        addl_charge_back_boarding = 0
    else:
        frm_styl = Frame_Style[frame_style]
    if matt_style == "None":
        addl_charge_matt1 = 0
        mat_styl= Matt_Styles[matt_style]
    else:
        mat_styl = Matt_Styles[matt_style]
    if sec_matt_style == "None":
        sec_mat_styl = 0;
    else:
        sec_mat_styl = Second_Matt_Styles[sec_matt_style]
    if glass == "None":
        addl_charge_glass = 0
        glassPrice = Glass[glass]
    else:
        glassPrice = Glass[glass]

    lamin = Laminate[laminate]


    calc_price = basePrice + (float(perimeter)*frm_styl)+(float(perimeter)*back_boarding_per_cm)+addl_charge_back_boarding+(float(perimeter)*glassPrice)+addl_charge_glass+(float(wm1*hm1)*mat_styl)+addl_charge_matt1+(float(perimeter)*sec_mat_styl)+(float(perimeter)*lamin)

    calculated_price = str(round(calc_price,2))
    print ("Calculated Price : ",calculated_price)
    return calculated_price

def get_price(context):

    prod_price = locatorsconfig.JEDIART.get('price')
    product_price = webcommon.find_element(context, prod_price['type'], prod_price['locator'])


    price = product_price.get_attribute("innerHTML")

    print("Product price : ", price)
    price = price.lstrip('$')

    return price
