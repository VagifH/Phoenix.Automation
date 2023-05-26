
Feature: User Registration
    Scenario: Valid Registration
    Given the user is on the login page
    When the user enters 'Vagif101' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    And I Click on Create User button
    When I enter a valid full name 'Charles'
    And I enter a valid username ' johndoe'
    And I click on role field
    And I select a valid role "Administrator"
    And I enter a valid email 'johndoe@gmail.com'
    And I enter a valid phone number '1234567890'
    And I enter a valid password 'BAkcell88--'
    And I confirm the 'BAkcell88--'
    And I submit the form
    Then I should see a success message

    Scenario: Invalid Full Name
    Given the user is on the login page
    When the user enters 'Vagif101' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    And I Click on Create User button
    When I enter a valid full name '$$$10'
    And I enter a valid username ' johnQQdoe'
    And I click on role field
    And I select a valid role "Administrator"
    And I enter a valid email 'johndQoe@gmail.com'
    And I enter a valid phone number '+994555902753'
    And I enter a valid password 'BAkcell88--'
    And I confirm the 'BAkcell88--'
    And I submit the form
    Then there should be an error message that fullname is invalid

    Scenario: Invalid Username
     Given the user is on the login page
    When the user enters 'Vagif101' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    And I Click on Create User button
    When I enter a valid full name 'Charrrles'
    And I enter a valid username ' johndhhoe'
    And I click on role field
    And I select a valid role "Administrator"
    And I enter a valid email 'johndoaae@gmail.com'
    And I enter a valid phone number '+994555902753'
    And I enter a valid password 'BAkcell88--'
    And I confirm the 'BAkcell88--'
    And I submit the form
    Then there should be an error message that username is invalid



    Scenario: Role is not selected
    Given the user is on the login page
    When the user enters 'Vagif101' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    And I Click on Create User button
    When I enter a valid full name 'Charrles'
    And I enter a valid username ' johnrdoe'
    And I enter a valid email 'johnd0oe@gmail.com'
    And I enter a valid phone number '1234567890'
    And I enter a valid password 'BAkcell88--'
    And I confirm the 'BAkcell88--'
    And I submit the form
    Then there should be an error message that role is not selected

    Scenario: Invalid Email
     Given the user is on the login page
    When the user enters 'Vagif101' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    And I Click on Create User button
    When I enter a valid full name 'Charleees'
    And I enter a valid username ' johndgddoe'
    And I click on role field
    And I select a valid role "Administrator"
    And I enter a valid email 'invalidmail'
    And I enter a valid phone number '+994505505115'
    And I enter a valid password 'BAkcell88--'
    And I confirm the 'BAkcell88--'
    And I submit the form
    Then there should be an error message that email is incorrect


    Scenario: Invalid Phone Number
     Given the user is on the login page
    When the user enters 'Vagif101' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    And I Click on Create User button
    When I enter a valid full name 'Charleqs'
    And I enter a valid username ' johndoqe'
    And I click on role field
    And I select a valid role "Administrator"
    And I enter a valid email 'johndo-e@gmail.com'
    And I enter a valid phone number '12340'
    And I enter a valid password 'BAkcell88--'
    And I confirm the 'BAkcell88--'
    And I submit the form
    Then there should be an error message that phone number is incorrect


    Scenario: Password Mismatch
   Given the user is on the login page
    When the user enters 'Vagif101' valid username
    When the user enters 'BAkcell88---' valid password
    And clicks on the login button
    And I Click on Create User button
    When I enter a valid full name 'Charlels'
    And I enter a valid username ' cocacola'
    And I click on role field
    And I select a valid role "Administrator"
    And I enter a valid email 'johdndoe@gmail.com'
    And I enter a valid phone number '+94555902753'
    And I enter a valid password 'BAkcell88--'
    And I confirm the 'BAkcell88---'
    And I submit the form
    Then there should be an error message that password is mismatch