import string
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonConfigs import logconfig
from BDDCommon.CommonConfigs import locatorsconfig
from BDDCommon.CommonSteps.webstepscommon import *

def go_to_page(context, Framed_Fine_Art_Print_Page):
    """
    Step definition to go to the specified page.
    :param context:
    :param page:
    """
    url = urlconfig.FRINTS.get('Framed_Fine_Art_Print_Page')
    print ("Framed_FineP_Art_Print_Page : ",url)

    context.driver = webcommon.go_to(url)
    context.driver.wait = WebDriverWait(context.driver, 10)

def refine_path(context,path):
    path1 = path.replace("\\","\\\\")
    return path1



