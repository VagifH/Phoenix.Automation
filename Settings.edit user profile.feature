Feature: Edit user profile Functionality

  Scenario: Settings Edit User Profile
    Given the user is on the login page
    When the user enters 'Vagif22' valid username
    When the user enters 'BAkcell88--' valid password
    And clicks on the login button
    And Click user menu icon
    When user go to Settings page
    And user clicks on edit profile button
    And I enter an 'Valid' to fullname field to edit
    And I edit email_address_field 'edtemal@gmail.com'
    And I edit phone number field '+994505505115'
    And I enter a correct password 'BAkcell88--'
    And the user clicks on the "Update" button
    And Check that profile is updated


  Scenario: Edit User Profile - Invalid Full Name
    Given the user is on the login page
    When the user enters 'Vagif22' valid username
    When the user enters 'BAkcell88--' valid password
    And clicks on the login button
    And Click user menu icon
    When user go to Settings page
    And user clicks on edit profile button
    And I enter an '$$$' to fullname field to edit
    And I edit email_address_field 'edtemal@gmail.com'
    And I edit phone number field '+994505505115'
    And I enter a correct password 'BAkcell88--'
    And the user clicks on the "Update" button
    And Check that profile is not updated due to invalid Fullname


  Scenario: Edit User Profile - Invalid email address
    Given the user is on the login page
    When the user enters 'Vagif22' valid username
    When the user enters 'BAkcell88--' valid password
    And clicks on the login button
    And Click user menu icon
    When user go to Settings page
    And user clicks on edit profile button
    And I enter an 'Valid' to fullname field to edit
    And I edit email_address_field 'invalidemail'
    And I edit phone number field '+994505505115'
    And I enter a correct password 'BAkcell88--'
    And the user clicks on the "Update" button
    And Check that profile is not updated due to invalid email


  Scenario: Edit User Profile - Invalid phone number
    Given the user is on the login page
    When the user enters 'Vagif22' valid username
    When the user enters 'BAkcell88--' valid password
    And clicks on the login button
    And Click user menu icon
    When user go to Settings page
    And user clicks on edit profile button
    And I enter an 'Valid' to fullname field to edit
    And I edit email_address_field 'edtemal@gmail.com'
    And I edit phone number field '+994'
    And I enter a correct password 'BAkcell88--'
    And the user clicks on the "Update" button
    And Check that profile is not updated due to invalid phone number



  Scenario: Edit User Profile - Invalid password
    Given the user is on the login page
    When the user enters 'Vagif22' valid username
    When the user enters 'BAkcell88--' valid password
    And clicks on the login button
    And Click user menu icon
    When user go to Settings page
    And user clicks on edit profile button
    And I enter an 'Valid' to fullname field to edit
    And I edit email_address_field 'edtemal@gmail.com'
    And I edit phone number field '+994505505115'
    And I enter a correct password 'Invalid'
    And the user clicks on the "Update" button
    And Check that profile is not updated due to invalid password


  Scenario: Edit User Profile - Leave password field blank
    Given the user is on the login page
    When the user enters 'Vagif22' valid username
    When the user enters 'BAkcell88--' valid password
    And clicks on the login button
    And Click user menu icon
    When user go to Settings page
    And user clicks on edit profile button
    And I enter an 'Valid' to fullname field to edit
    And I edit email_address_field 'edtemal@gmail.com'
    And I edit phone number field '+994'
    And the user clicks on the "Update" button
    And Check that profile is not updated
