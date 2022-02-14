


Feature: Verifying the page is successfully open on the browser if we hit with the url

    Scenario Outline: Opening the "<client>" home page

        Given I go to the site "<client>"
        Then I can reach the home page of "<client>"



        Examples:
        |client|
        |artisticpictureframing.com|
        |frints.com                |
        |historicpictoric.com      |
        |replicarte.com            |
