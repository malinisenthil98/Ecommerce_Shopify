Feature: Verifying the framework setup for the chosen picture with different frames and Check the "Add to Cart" button

  Scenario Outline: Select the "<Category>" ,check the frame options and verify the Add_to_Cart button status

    Given I go to the page "Home_Page"
    When  I click on "<Category>" and select the first picture from the collections
    Then  Choose the different frames from the given options and Check if the Add_to_Cart Button is enabled / disabled

    Examples:
      |Category|
      |Abstrato|
      |Animais |
      |Arquitetura & Urbano|
      |Astronomia          |
      |Dança & Música      |
      |Esportes            |
      |Figurativa          |
      |Floral              |
      |Militar & Guerra    |
      |Paisagem            |
      |Paisagem Marítima   |
      |Religioso           |
