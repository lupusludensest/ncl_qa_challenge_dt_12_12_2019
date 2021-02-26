# Created by Vic at 1/5/2020
Feature: Guest explores shore excursions destinations

  Scenario: Guest explores shore excursions destinations
    Given a Guest
    And I am on Homepage
    And I navigated to "Shore Excursion" page
    When I search for destination "Alaska Cruises"
    Then Shore Excursions page is present
    And Results are filtered by "Alaska Cruises"
    And Filter By Ports are only belong to "California, Japan, Washington, Russia, Alaska, British Columbia"
