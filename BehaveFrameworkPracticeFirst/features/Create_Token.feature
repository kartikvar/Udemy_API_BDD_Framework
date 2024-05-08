Feature: Test Create Token API

  Scenario: Test token is created with valid data
    Given Valid username and password is entered
    When Create Token API is triggered with valid data
    Then Token is created

  Scenario Outline: Test token is not created with invalid data
    Given Invalid <username> and <password> is entered
    When Create Token API is triggered with invalid data
    Then Token is not created
    Examples:
      | username | password |
      |  user    | pass     |
      |  user1   | password |
      | username | pass1    |
