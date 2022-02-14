Feature: Verifying the home page url goes to the right place

    Scenario: Opening the frints home page

        Given I go to the site "frints.com"
        Then I can reach the home page of "frints.com"

    Scenario: The frints home page should have correct title

        Given I go to the site "frints.com"
        Then the page title should be "Framed Fine Art print - Frints"

    Scenario: The frints home page should have correct url

        Given I go to the site "frints.com"
        Then current url should be "https://frints.com/framed-fine-art-print/"