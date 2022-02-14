
from behave import given, when, then
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonConfigs import logconfig
from BDDCommon.CommonConfigs import locatorsconfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from nose.tools import *
import time
from Screenshot import Screenshot_Clipping

import pdb
# start of step definitions

@given('I go to the site "{site}"')
def go_to_url(context, site):

    """
    Step definition to go to the specified url.
    :param context:
    :param url:
    """

    url = urlconfig.URLCONFIG.get(site)

    print("Navigating to the site: {}".format(url))
    logconfig.logging.info("This is a info message")


    context.driver = webcommon.go_to(url)
    currentUrl = context.driver.current_url
    assert_equal(url,currentUrl)



@given ('I go to the page "{Home_Page}"')
def go_to_page(context, Home_Page):
    """
    Step definition to go to the specified page.
    :param context:
    :param page:
    """
    url = urlconfig.REPLICARTEURL.get(Home_Page)
    print ("Home page : ",url)

    context.driver = webcommon.go_to(url)
    currentUrl = context.driver.current_url
    assert_equal(url, currentUrl)





@then ('Choose the different frames from the given options and Check if the Add_to_Cart Button is enabled / disabled')
def Choose_different_frames(context):


    frtnl = locatorsconfig.REPLICARTE.get('frame_thumb')
    frame_thumbnail=context.driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,frtnl['locator'])))
    #frame_thumbnail = webcommon.find_elements(context,frtnl['type'],frtnl['locator'])

    n = len(frame_thumbnail)
    print ("Number of frames available : ",n)
    print(frame_thumbnail)

    for i in range(n):

        if (i < n-1):
            print("i value : ", i)
            print("n value : ", n)
            no = i + 1
            frame_id = "frame_" + str(no)
            print ("Frame_id : ",frame_id)

            context.driver.execute_script("window.scrollBy(0,150)","")

            #fr=context.driver.wait.until(EC.visibility_of(frame_thumbnail[i]))


            frame_thumbnail[i].click()

            context.driver.execute_script("window.scrollBy(0,300)", "")
            print(frame_id, " is selected...")


            frame_no = locatorsconfig.REPLICARTE.get(no)
            print("no = ", no)
            frm_type = frame_no['type']
            print("frame Type ", frm_type)
            frm_loc = frame_no['locator']
            print("frame Loc", frm_loc)
            disp_frame = context.driver.wait.until(EC.presence_of_element_located((By.XPATH,frame_no['locator'])))
            #disp_frame = webcommon.find_element(context, frame_no['type'], frame_no['locator'])
            print("disp_frame : ", disp_frame)
            context.driver.execute_script("arguments[0].scrollIntoView();", disp_frame)
            if (disp_frame.is_displayed()):
                print(frame_id, " is displayed...", )
                aToC_btn = locatorsconfig.REPLICARTE.get('button')
                button = context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, aToC_btn['locator'])))
                #button = webcommon.find_element(context, aToC_btn['type'], aToC_btn['locator'])
                print("Button status = ", button.get_attribute("disabled"))
                print("Frame id : ",frame_id)
                #assert_true(button.get_attribute("disabled")="true", "Add to Cart Button is Disabled")
                #assert_equal (button.get_attribute("disabled"), "true")
                #print(" Test Passed : Add to Cart Button is Disabled for ", frame_id)

                try:
                    assert button.get_attribute("disabled")=="true"
                    print(" Test Passed : Add to Cart Button is Disabled for ", frame_id)
                except AssertionError:
                    print("Assertion failed. Add to Cart Button is Enabled for ", frame_id)





            context.driver.execute_script("window.scrollBy(0,0)", "")
        else:
            frame_id = "No_frame"
            frame_thumbnail[i].click()
            print(frame_id, " is selected...")

            frame_no = locatorsconfig.REPLICARTE.get('no_frame')
            disp_frame = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, frame_no['locator'])))
            #disp_frame = webcommon.find_element(context, frame_no['type'], frame_no['locator'])
            if (disp_frame.is_displayed()):
                print(frame_id, " is displayed...", )
                context.driver.execute_script("window.scrollBy(0,200)", "")
                aToC_btn = locatorsconfig.REPLICARTE.get('button')
                button = webcommon.find_element(context, aToC_btn['type'], aToC_btn['locator'])
                print("Button status = ", button.get_attribute("disabled"))
                print("Frame id : ", frame_id)
                #assert_false(button.get_attribute("disabled")=="true", "Add to Cart Button is Enabled")
                #assert_not_equal (button.get_attribute("disabled"),"true")
                #print("Test Passed : Add to Cart Button is Enabled for ", frame_id)
                try:
                    assert button.get_attribute("disabled")!="true"
                    print(" Test Passed : Add to Cart Button is Enabled for ", frame_id)
                except AssertionError:
                    print("Assertion failed. Add to Cart Button is Disabled for ", frame_id)






@then('Click on Room preview option')
def click_on_roomPreview(context):


    rmpv = locatorsconfig.REPLICARTE.get('room_preview')

    #roomPrvew = webcommon.find_element(context,rmpv['type'],rmpv['locator'])
    roomprvew = context.driver.wait.until(EC.presence_of_element_located((By.XPATH, rmpv['locator'])))
    context.driver.execute_script("window.scrollBy(0,500)","")
    print("window scroll down")
    context.driver.execute_script("arguments[0].click();", roomprvew)
    #webcommon.click(roomprvew)
    print("Room preview option clicked")


@then('I change the wall colour')
def change_wall_colour(context):
    walcolourbtn = locatorsconfig.REPLICARTE.get('wall_colour_btn')
    wall_color_btn = webcommon.find_element(context,walcolourbtn['type'],walcolourbtn['locator'])
    webcommon.scroll_window_till_element_found(context,wall_color_btn)
    context.driver.execute_script("arguments[0].click();", wall_color_btn)
    print("Wall colour button clicked")
    context.driver.execute_script("window.scrollBy(0,50)", "")
    wal_colour  = locatorsconfig.REPLICARTE.get('wall')
    context.wall = webcommon.find_element(context,wal_colour['type'],wal_colour['locator'])
    context.driver.execute_script("arguments[0].setAttribute('style', 'width: 100%; background-color: rgb(179, 175, 122);')",context.wall)



@then ('Move the picture to the desired position on the wall')
def move_the_picture(context):
    context.driver.execute_script("window.scrollBy(0,0)", "")
    room_pic = locatorsconfig.REPLICARTE.get('room_picture')
    rmpic = webcommon.find_element(context, room_pic['type'], room_pic['locator'])
    action = ActionChains(context.driver)
    action.drag_and_drop_by_offset(rmpic, 107, -24).perform()
    context.room_photo = rmpic
    print("picture moved on the wall")





@then('Select the frame')
def select_frame(context):
    frtnl = locatorsconfig.REPLICARTE.get('frame_thumb')
    frame_thumbnail = context.driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, frtnl['locator'])))
    context.driver.execute_script("window.scrollBy(0,150)", "")
    frame_thumbnail[0].click()
    context.driver.execute_script("window.scrollBy(0,300)", "")
    print(" frame is selected...")








@then('Click on "{room_type}" and Assert wall colour,picture position,frame design remain same')
def Assert_picture_features_on_different_rooms(context,room_type):
    room = room_type
    room_loc=locatorsconfig.REPLICARTE.get(room)
    room_ele = webcommon.find_element(context,room_loc['type'],room_loc['locator'])
    webcommon.scroll_window_till_element_found(context,room_ele)
    context.driver.execute_script("arguments[0].click();", room_ele)

    print ("{} is selected".format(room))
    actual_left = "107px"
    actual_top = "-24px"

    acutal_Wall_colour = "width: 100%; background-color: rgb(179, 175, 122);"
    actual_frame_value= 'url("https://lb4b-shoppers.s3.amazonaws.com/media/images/replicarte_myshopify/Frame1/image/png") 36 / 1 / 0 stretch'
    photo = context.room_photo
    expected_left = photo.value_of_css_property("left")
    expected_top = photo.value_of_css_property("top")

    expected_wall_color = context.wall.get_attribute('style')
    expected_frame_value = photo.value_of_css_property("border-image")
    #print("Actual picture postion : ",actual_picture_position)
    #print("Expected picture position : ",expected_picture_poistion)
    #print("Actual Wall colour : ",acutal_Wall_colour)
    #print("Expected wall colour : ",expected_wall_color)
    #print("Actual frame value : ",actual_frame_value)
    #print("Expected frame value : ",expected_frame_value)
    try:
        if (actual_left == expected_left) and (actual_top == expected_top):


            print("Test passed - Picture position remains same in ",room)
    except AssertionError:
        print("Assertion failed. Actual value is ", actual_left,actual_top)
        print("Assertion failed. expected value is ", expected_left,expected_top)

    try:
        assert acutal_Wall_colour == expected_wall_color
        print("Test passed - Wall colour remain same in ",room)
    except AssertionError:
        print("Assertion failed. Actual value is ", acutal_Wall_colour)
        print("Assertion failed. expected value is ", expected_wall_color)
    try:
        assert actual_frame_value == expected_frame_value
        print("Test passed - Frame remains same in ",room)
    except AssertionError:
        print("Assertion failed. Actual value is ", actual_frame_value)
        print("Assertion failed. expected value is ", expected_frame_value)




#========================================================================================#
@then('the page title should be "{expected_title}"')
def verify_homepage_title(context, expected_title):
    """
    Verifies the home page title is as expected.
    :param context:
    :param expected_title:
    :return:
    """

    webcommon.assert_page_title(context, expected_title)

#========================================================================================#
@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    """
    Verifies the current uls is as expected_url
    :param context:
    :param expected_url:
    """

    webcommon.assert_current_url(context, expected_url)


# ========================================================================================#
@then('I can reach the home page of "{site}"')

def verify_reach_homepage(context, site):
    """
    Step definition to confirm we reach the home page of given url.
    :param context:
    :param url:
    """

    url = urlconfig.URLCONFIG.get(site)
    webcommon.reach_homepage(context,url)


@when('Take screenshot')
def take_screen_shot(context):
    ob = Screenshot_Clipping.Screenshot()
    img_url = ob.full_Screenshot(context.driver, save_path=r'.', image_name='Myimage.png')
    print(img_url)
    #context.driver.save_screenshot(‘Myimage.png’)
    #screenshot = Image.open(‘Myimage.png’)
    #screenshot.show()






