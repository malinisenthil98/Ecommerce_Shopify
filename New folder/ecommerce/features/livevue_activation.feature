Feature: Activating the livevue app on shopify e-commerce website

    Scenario Outline: : Login into shopify portal and activate livevue app on our store

        Given I go to the site "shopify"
        When Login with the "<username>" and "<password>"
        Then Delete "LIVEARf" if already installed
        When Explore free themes and choose "<theme>"
        Then Verify "LIVEARf" is present in  the installed apps, if not present, search and install "LIVEARf",else Delete and install




        Examples:
        |theme        |username                |password   |
        | Minimal       |snthlmln@gmail.com      |acumen#123|