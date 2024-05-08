Feature: Facebook login functionality

  Scenario: Test login with valid credentials
     Given we have facebook API
      When we enter valid credential
      Then user will log in
      And correct profile opened

  Scenario: Test login with invalid credentials
     Given we have facebook API
      When we enter invalid credential
      Then user will log in
      And incorrect profile opened