Feature: Repeated login

  Scenario: same user has to login 5 times
    Given user is on login page
    When user logged in 5 times by entering valid credentials and clicking login button
    Then user has to enter welcome page
