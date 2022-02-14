Feature: Verifying the framework setup for the chosen picture in Room preview

  Scenario: Select the "{CategoryName}" ,check the frame options in different rooms preview

    Given I go to the page "Home_Page"
    When  I click on "{CategoryName}" and select the first pic from the collections
    Then  Click on Room preview option
    Then I change the wall colour
    Then Move the picture to the desired position on the wall
    Then  Select the frame
    Then Click on "room2" and Assert wall colour,picture position,frame design remain same
      And Click on "room3" and Assert wall colour,picture position,frame design remain same
      And Click on "room4" and Assert wall colour,picture position,frame design remain same
      And Click on "room5" and Assert wall colour,picture position,frame design remain same


