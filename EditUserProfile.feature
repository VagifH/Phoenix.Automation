Feature: Edit user profile Functionality

Scenario: Edit User Profile click action button
  Given the user is on the login page
  When the user enters 'Vagif101' valid username
  When the user enters 'BAkcell88---' valid password
  And clicks on the login button
  And clicks on the action button
  And I enter an 'editprofileuser' to fullname
  And I enter an 'editprofileuser@gmail.com' to email field
  And I enter an '+994505505115' to phone number field
  And the user clicks on the "Save" button
  And verify that profile is updated


    Scenario: Edit User Profile - Invalid Full Name
    Given the user is on the login page
    Given the user is on the login page
    When the user enters 'Vagif101' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    And clicks on the action button
    And I enter an '$$$$' to fullname field
    And the user clicks on the "Save" button
    And verify that error message is there


    Scenario: Edit User Profile - Invalid email address
    Given the user is on the login page
    Given the user is on the login page
    When the user enters 'Vagif101' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    And clicks on the action button
    And I enter an 'hhhhh' to email field
    And the user clicks on the "Save" button
    And verify that error message is displayed


    Scenario: Edit User Profile - Invalid phone number
    Given the user is on the login page
    Given the user is on the login page
    When the user enters 'Vagif101' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    And clicks on the action button
    And I enter an '+99' to phone number
    And the user clicks on the "Save" button
    Then verify that error message is shown

