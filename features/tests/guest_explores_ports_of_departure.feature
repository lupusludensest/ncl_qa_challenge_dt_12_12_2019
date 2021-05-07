# Created by Vic at 12/12/2019
Feature: Guest filters shore excursions results using price range

  Scenario: Guest filters shore excursions results using price range
    Given a Guest
    And I am on Homepage
    And I navigated to "Shore Excursion" page
    And I click Find Excursions
    And Shore Excursions page is present
    When Price range is filtered to $0-$3000
    Then Only shore excursions within range $0-$3000 are displayed


