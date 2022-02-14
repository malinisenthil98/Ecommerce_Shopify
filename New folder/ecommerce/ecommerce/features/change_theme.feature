Feature: Change the theme of our online store and edit code
        Scenario Outline: Explore free themes and change to different themes


        Given I go to the site "shopify"
        When Login with the "<username>" and "<password>"
        Then Explore free themes and choose "<theme>"




                Examples:
        |username                       |password       |      theme    |
        |kumarmaliniacumen@gmail.com    |acumen#123     |      Debut    |