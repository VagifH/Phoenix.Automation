Feature: Units of measure

Scenario: Units of measure / Temperature (first element in the list)

Given the user is on the login page
When the user enters 'Vagif101' valid username
When the user enters 'BAkcell88---' valid password
And clicks on the login button
And Click user menu icon
When user go to Settings page
And I click on units of measure option
And I click on dropdown list
And I select DEGC
And I refresh the page
And Verify that DEGC element is successfully selected



Scenario: Units of measure /  Pressure (second element in the list)
Given the user is on the login page
When the user enters 'Vagif101' valid username
When the user enters 'BAkcell88---' valid password
And clicks on the login button
And Click user menu icon
When user go to Settings page
And I click on units of measure option
And I click on Pressure units of measure drop down list
And I select BAR
And I refresh the page
And Verify that BAR element is successfully selected


Scenario: Units of measure /  Rates (Last element in the list)
Given the user is on the login page
When the user enters 'Vagif101' valid username
When the user enters 'BAkcell88---' valid password
And clicks on the login button
And Click user menu icon
When user go to Settings page
And I click on units of measure option
And I click on Rates units of measure drop down list
And I select CPS
And I refresh the page
And Verify that CPS element is successfully selected



