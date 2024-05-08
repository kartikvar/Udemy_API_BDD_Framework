Feature: Test GitHub API

  Scenario: Session management check
    Given Valid GitHub credentials
    When Get Repo API is triggered
    Then Status code is 200