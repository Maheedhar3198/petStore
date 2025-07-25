Feature: User sign in

  Scenario: Successful login with valid credentials
    Given user is on the login page
    And user enters a valid username and password
    When user clicks on the login button
    Then user should be redirected to the home page with welcome message