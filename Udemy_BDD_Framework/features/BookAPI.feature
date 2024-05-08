Feature: Verify if books are added and deleted

  @environment
  Scenario: Verify AddBook API functionality
    Given Valid data is given
    When Add Book API is triggered
    Then Book is added