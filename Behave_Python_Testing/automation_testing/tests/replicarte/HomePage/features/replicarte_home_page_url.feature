

Feature: Verifying the home page url goes to the right place

    Scenario: Opening the replicarte home page

        Given I go to the site "replicarte.com"
        Then I can reach the home page of "replicarte.com"

    Scenario: The replicarte home page should have correct title

        Given I go to the site "replicarte.com"
        Then the page title should be "ReplicArte: Reproduções Pintadas à Mão com Qualidade Museu – Replicarte"

    Scenario: The replicarte home page should have correct url

        Given I go to the site "replicarte.com"
        Then current url should be "https://replicarte.com.br/"