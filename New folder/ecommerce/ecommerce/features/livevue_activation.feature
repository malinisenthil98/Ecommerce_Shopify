Feature: Activating the livevue app on shopify e-commerce website

    Scenario Outline: : Login into shopify portal and activate livevue app on our store

        Given I go to the site "shopify"
        When Login with the "<username>" and "<password>"
        Then Verify "LIVEARf" is present in  the installed apps, if not present, search and install "LIVEARf"
        When Select the app "LIVEARf" and activate Livevue



        Examples:
        |username                |password   |
        |kumarmaliniacumen@gmail.com |acumen#123 |