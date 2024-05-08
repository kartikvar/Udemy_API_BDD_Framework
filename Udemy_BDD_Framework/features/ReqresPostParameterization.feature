Feature: Test the creation of user

 @smoke
  Scenario: Verify that user is created
    Given Valid user data is given
    When Create user API is triggered
    Then User is created

 @regression
  Scenario Outline: Verify that multiple users are created
    Given Valid <name> and <job> are given
    When Create user API is triggered
    Then Users are created
    Examples:
      | name | job |
      | "Swapnil" | "Dhandhebaz" |
      | "Sammi" | "Golibaaz" |
      | "Arun" | "Raat Kaali" |