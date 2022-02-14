

Feature: Verifying the home page url goes to the right place

    Scenario: Opening the historicpictoric home page

        Given I go to the site "historicpictoric.com"
        Then I can reach the home page of "historicpictoric.com"

    Scenario: The historicpictoric home page should have correct title

        Given I go to the site "historicpictoric.com"
        Then the page title should be "Test - Historic Pictoric"

    Scenario: The historicpictoric home page should have correct url

        Given I go to the site "historicpictoric.com"
        Then current url should be "https://historicpictoric.com/collections/test/"