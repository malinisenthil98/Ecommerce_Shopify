Feature: Verifying if the category exists on collections

    Scenario: check if the random category exists on collections

        Given I go to the page "Home_Page"
        Then verify if the "{category_name}" exists on collections
        Then click on the first item present in "{category_name}"

