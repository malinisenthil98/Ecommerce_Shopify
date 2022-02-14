

Feature: Verifying the home page url goes to the right place

    Scenario: Opening the artisticpictureframing home page

        Given I go to the site "artisticpictureframing.com"
        Then I can reach the home page of "artisticpictureframing.com"

    Scenario: The artisticpictureframing home page should have correct title

        Given I go to the site "artisticpictureframing.com"
        Then the page title should be "Print and Frame"

    Scenario: The artisticpictureframing home page should have correct url

        Given I go to the site "artisticpictureframing.com"
        Then current url should be "https://artisticpictureframing.com/test/print-and-frame/"