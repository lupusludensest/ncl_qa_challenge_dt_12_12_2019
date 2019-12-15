# Created by Vic at 12/12/2019
Feature: Guest explores Ports of Departure

  Scenario: Guest explores Ports of Departure
    Given a Guest
    And I am on Homepage
    And I navigated to "Shore Excursion" page
    And I click Find Excursions
    And Shore Excursions page is present
    When Price range is filtered to "$0-$30"
    Then Only shore excursions within range are displayed
