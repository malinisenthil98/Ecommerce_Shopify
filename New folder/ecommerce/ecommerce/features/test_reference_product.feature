Feature: Testing the features of reference product
  Scenario: Login into shopify portal and activate livevue app on our store and explore the reference product

    Given I go to the page "Test_Product"
    Then  Choose the different frames from the given options and Check if the Add_to_Cart Button is enabled / disabled
    Then  Click on Room preview option
    Then I change the wall colour
    Then Move the picture to the desired position on the wall
    Then  Select the frame
    Then Click on "room2" and Assert wall colour,picture position,frame design remain same
      And Click on "room3" and Assert wall colour,picture position,frame design remain same
      And Click on "room4" and Assert wall colour,picture position,frame design remain same
      And Click on "room5" and Assert wall colour,picture position,frame design remain same

