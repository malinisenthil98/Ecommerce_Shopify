Feature: Creating a Test store in shopify for our product testing
  Scenario: Create am Email account and Using this email id, create a test store in shopify
    Given I go to the site "Temp_email"
    When  Get temporary email id and go to "shopify",Create an account with the temp_email_id
