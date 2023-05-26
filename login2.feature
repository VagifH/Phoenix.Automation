Feature: Login Functionality

Scenario: User successfully logs in with correct credentials
  Given the user is on the login page
  When the user enters 'Vagif101' valid username
  When the user enters 'BAkcell88---' valid password
  And clicks on the login button
  Then the user should be redirected to the homepage

  Scenario: User unsuccessfully logs in with incorrect credentials
    Given the user is on the login page
    When the user enters 'Elmdar' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    Then the user should see an error message



  Scenario: User cannot log in without entering credentials
  Given the user is on the login page
  And clicks on the login button
  And the user should see an error message blank field

