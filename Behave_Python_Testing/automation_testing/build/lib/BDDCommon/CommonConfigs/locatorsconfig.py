

LOCATORS = {
    'main navigation' : {'type': 'id', 'locator':'mainnav'},
    'top navigation' : {'type': 'id', 'locator':'top'},
    'options' : {'type': 'css selector', 'locator':'.options-bar'},
    'accept_cookie' : {'type': 'xpath','locator' : '/html/body/div[12]/div/button'}
}
REPLICARTE ={
    'category' : {'type': 'css selector', 'locator': 'div.collection-grid-item__title'},
    'product' : {'type': 'xpath','locator':'//a[@class="grid-view-item__link grid-view-item__image-container full-width-link"]'},
    'frame_thumb' : {'type' : 'css selector','locator' : 'label.form-option'},
    1 :{'type' : 'xpath','locator' : '//img[contains(@style, "border-image: url(https://lb4b-shoppers.s3.amazonaws.com/media/images/replicarte_myshopify/Frame1/image/png)")]'},
    2: {'type' : 'xpath','locator' : '//img[contains(@style, "border-image: url(https://res.cloudinary.com/dxodr7sdd/image/upload/v1621593967/Replicarte/replicarte_frames/Frame2.png)")]'},
    3 : {'type' : 'xpath','locator' : '//img[contains(@style, "border-image: url(https://res.cloudinary.com/dxodr7sdd/image/upload/v1621593967/Replicarte/replicarte_frames/Frame3.png)")]'},
    4 : {'type' : 'xpath','locator' : '//img[contains(@style,"border-image: url(https://res.cloudinary.com/dxodr7sdd/image/upload/v1621593968/Replicarte/replicarte_frames/Frame4.png)")]'},
    5: {'type' : 'xpath','locator' : '//img[contains(@style, "border-image: url(https://res.cloudinary.com/dxodr7sdd/image/upload/v1621593968/Replicarte/replicarte_frames/Frame5.png)")]'},
    6 : {'type' : 'xpath','locator' : '//img[contains(@style, "border-image: url(https://res.cloudinary.com/dxodr7sdd/image/upload/v1621593969/Replicarte/replicarte_frames/Frame6.png)")]'},
    7 : {'type' : 'xpath','locator' : '//img[contains(@style, "border-image: url(https://res.cloudinary.com/dxodr7sdd/image/upload/v1621593969/Replicarte/replicarte_frames/Frame7.png)")]'},
    8 : {'type' : 'xpath','locator' : '//img[contains(@style, "border-image: url(https://res.cloudinary.com/dxodr7sdd/image/upload/v1621593969/Replicarte/replicarte_frames/Frame8.png)")]'},
    9 : {'type' : 'xpath','locator' : '//img[contains(@style, "border-image: url(https://res.cloudinary.com/dxodr7sdd/image/upload/v1621616305/Replicarte/replicarte_frames/Frame9.png)")]'},
    'no_frame' : {'type' : 'xpath','locator' : '//img[contains(@style, "border-image: url()")]'},
    'button' : {'type': 'css selector', 'locator': 'button.btn.product-form__cart-submit'},
    'room_preview' : {'type': 'xpath', 'locator': '//img[@id = "room_previewId"]'},
    'room_picture': {'type':'css selector','locator':'img.zoom'},
    'circle':{'type':'css selector','locator':'circle.inner-circle'},
    'wall_colour_btn':{'type':'css selector','locator':'input#changeWallColor'},
    'wall':{'type':'css selector','locator':'img#mainImage'},
    'room1':{'type':'css selector','locator':'img[title="living-room"]'},
    'room2':{'type':'css selector','locator':'img[title="Bedroom"]'},
    'room3':{'type':'css selector','locator':'img[title="Office-Space"]'},
    'room4':{'type':'css selector','locator':'img[title="Study-Room"]'},
    'room5':{'type':'css selector','locator':'img[title="Dining-Room"]'}
}
FRINTS = {
    'Choose_File_btn': {'type':'css selector','locator': 'input#attribute_file_95'}
}
JEDIART = {
    'price':{'type':'xpath','locator':'(//span[@class = "price price--withTax"])[1]'},
    'framed':{'type':'xpath','locator':'//label[@data-product-attribute-value="705"]'},
    'Black':{'type':'xpath','locator':'//label[@data-product-attribute-value="707"]'},
    'light_Timber':{'type':'xpath','locator':'//label[@data-product-attribute-value="708"]'},
    'coloured':{'type':'xpath','locator':'//label[@data-product-attribute-value="708"]'},
    'classic_black_gold':{'type':'xpath','locator':'//label[@data-product-attribute-value="710"]'},
    'glass':{'type':'xpath','locator':'//label[@data-product-attribute-value="764"]'},
    'clear_float_glass' : {'type':'xpath','locator':'//label[@data-product-attribute-value="752"]'},
    'laminate':{'type':'xpath','locator':'//label[@data-product-attribute-value="765"]'},
    'gloss_laminate':{'type':'xpath','locator':'//label[@data-product-attribute-value="758"]'},
    'matt1':{'type':'xpath','locator':'//label[@data-product-attribute-value="728"]'},
    'Ash':{'type':'xpath','locator':'//label[@data-product-attribute-value="731"]'}
}
SHOPIFY = {
    'login':{'type':'xpath','locator':'(//a[@href="/login"])[2]'},
    'username':{'type':'xpath','locator':'//input[@type="email"]'},
    'next':{'type':'xpath','locator':'//button[@name="commit"]'},
    'password':{'type':'xpath','locator':'//input[@id="account_password"]'},
    'loginn':{'type':'xpath','locator':'//button[@name="commit"]'},
    'apps':{'type':'xpath','locator':'//span[contains(.,"Apps")]'},
    'IsInstalled':{'type':'xpath','locator':'(//span[@class="Polaris-TextStyle--variationStrong_rpyvj"])[3]'},
    'search': {'type':'css selector','locator': '._2jjD3'},
    'topApps': {'type':'css selector','locator': '._1hYhU'},
    'explore':{'type':'xpath','locator':'//div[@id="search-results"]/div/div[3]/a/span/span'},
    'searchApp':{'type':'xpath','locator':'//form[@id="ui-app-store-hero__home-search"]//input[@name = "q"]'},
    'appName': {'type':'css selector','locator': '.heading--4.ui-app-card__name'},
    'AddApp':{'type':'xpath','locator':'//form[@class="button_to"]/input[2]'},
    'installApp': {'type':'css selector','locator': 'button[id="proceed_cta"]'},
    'installedApp': {'type':'css selector','locator': '.vKX0A'},
    'checkbox':{'type':'xpath','locator':'//input[@type="checkbox"]/following-sibling::span'},
    'dismiss':{'type':'xpath','locator':'// span[contains(., "dismiss")]'},
    'livevue':{'type':'xpath','locator':'//ul[@class="sidebar-nav"]/li[5]/a/span'},
    'create':{'type':'xpath','locator': '//form[@name="registerForm"]/button'},
    'liveArf':{'type':'xpath','locator': '//div[@class="vKX0A"]'},
    'delete':{'type':'xpath','locator': '(//span[@class="Polaris-Button__Text_yj3uv"])[4]'},
    'delete1':{'type':'xpath','locator': '(//span[@class="Polaris-Button__Text_yj3uv"])[8]'},
    'activation':{'type':'xpath','locator': '//ul[@class="sidebar-nav"]/li[4]/a/span'},
    'setupActivation':{'type':'xpath','locator': '//a[@href="/setup/activation"]/span'},
    'close':{'type':'xpath','locator': '//button[@class="close"]/span'},
    'nextbtn':{'type':'xpath','locator': '//button[@class="mat-flat-button mat-button-base mat-primary"]'},
    'catdwnld':{'type':'xpath','locator': '//li[@class="ng-star-inserted"]/button'},
    'chkbox': {'type':'css selector','locator': '.mat-checkbox-inner-container'},
    'resync': {'type':'css selector','locator': '.btn btn-primary'},
    'cat2save':{'type':'xpath','locator': '//div[@id="cdk-step-content-1-1"]/div[1]//button'},
    'cat2next':{'type':'xpath','locator': '//div[@id="cdk-step-content-1-1"]/div[2]/button[1]'},
    'radioNo':{'type':'xpath','locator': '//div[@class="c-radio"]/label/span'},
    'radioYes':{'type':'xpath','locator': '//div[@class="c-radio"]//input[@value="Yes"]'},
    'enableHook':{'type':'xpath','locator': '//ul[@class="list-unstyled"]/li/button'},
    'cat3next':{'type':'xpath','locator': '//div[@id="cdk-step-content-1-2"]/div[2]/button[1]'},
    'syncallprod':{'type':'xpath','locator': '//div[@id ="cdk-step-content-1-3"]/div/ul/li/button'},
    'theme':{'type':'xpath','locator': '//div[@id="AppFrameNav"]/nav/div[2]/ul[2]/li[2]/div/a/div/span'},
    'theme11':{'type':'xpath','locator': '(//div[@id="PolarisSecondaryNavigation15"]/ul/li/div/a/span)[1]'},
    'freetheme':{'type':'xpath','locator':'//div[@id="FreeThemesModalActivator"]/button'},
    'frame1':{'type':'xpath','locator':'//iframe[@title="Online Store"]'},
    'app_frame':{'type':'xpath','locator':'//iframe[@name="app-iframe"]'},
    'theme_name':{'type':'xpath','locator':'//ul[@class="KhgbJ"]/li/button/div/div/span'},
    'frame2':{'type':'xpath','locator':'//iframe[@class="_2EmM3"]'},
    'Add_to_theme_library':{'type':'xpath','locator':'//div[@id="app"]/div/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/button/span/span'},
    'action1':{'type':'xpath','locator':'//ul[@class="_3LL0u"]/li/div/div/div/div[2]/div/div/div/button/span/span[1]'},
    'publish':{'type':'xpath','locator':'(//div[@id="Polarispopover3"]/div/ul/li/div/ul/li[2]/button/span/span)[1]'},
    'frame3':{'type':'css selector','locator':'iframe._1spNS'},
    'publish_theme':{'type':'xpath','locator':'//div[@class="Polaris-ButtonGroup_yy85z"]/div[2]/button/span/span'},
    'action2':{'type':'xpath','locator':'//div[@class="Polaris-ButtonGroup__Item_yiyol"]/div/button/span/span[1]'},
    'edit_code':{'type':'xpath','locator':'(//a[@class="Polaris-ActionList__Item_yiyol"]//span[@class="Polaris-ActionList__Text_yj3uv"])[2]'},
    'section':{'type':'xpath','locator':'//div[@id="asset-list"]/div[3]/h2/span'},
    'prod_temp_liq':{'type':'xpath','locator':'(//ul[@class="asset-listing-list unstyled"]/li[25]/a/span)[1]'},
    'livevue':{'type':'xpath','locator':'//a[@title="LIVEVUE"]/span'},
    'livevueAct':{'type':'xpath','locator':'//a[@title="LIVEVUE Activation"]/span'},
    'startpro':{'type':'xpath','locator':'//div[@class="row"]/div[2]/button'},
    'confYes':{'type':'xpath','locator':'//div[@class="swal2-actions"]/button[1]'},
    'tcat1':{'type':'xpath','locator':'//div[@class="success-message"]/a[1]'},
    'tcat2':{'type':'xpath','locator':'//div[@class="success-message"]/a[2]'}
}
Temp_email ={
    'email':{'type':'xpath','locator':'//input[@id="mail"]'},
    'copy':{'type':'xpath','locator':'//button[@id="click-to-copy"]'},
    'startFreeTrial':{'type':'xpath','locator':'(//input[@value="Start free trial"])[1]'},
    'username':{'type':'xpath','locator':'(//input[@name="signup[email]"])[1]'},
    'pass':{'type':'xpath','locator':'(//input[@name="signup[password]"])[1]'},
    'store':{'type':'xpath','locator':'//input[@name="signup[shop_name]"]'},
    'createStore':{'type':'xpath','locator':'(//button[@type="submit"])[1]'},
    'skip':{'type':'xpath','locator':'(//span[@class="Polaris-Button__Text_yj3uv"])[1]'},
    'firstName':{'type':'xpath','locator':'//input[@name="account_setup[firstName]"]'},
    'lastName':{'type':'xpath','locator':'//input[@name="account_setup[lastName]"]'},
    'address':{'type':'xpath','locator':'//input[@name="account_setup[address1]"]'},
    'city':{'type':'xpath','locator':'//input[@name="account_setup[city]"]'},
    'country':{'type':'xpath','locator':'//select[@name="account_setup[country]"]'},
    'state':{'type':'xpath','locator':'//select[@name="province"]'},
    'zip':{'type':'xpath','locator':'//input[@name="account_setup[zip]"]'},
    'phone':{'type':'xpath','locator':'//input[@name="account_setup[phone]"]'},
    'enter':{'type':'xpath','locator':'(//span[@class="Polaris-Button__Text_yj3uv"])[4]'}

}








