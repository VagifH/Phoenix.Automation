Feature:Date format

Scenario: Change Date format

Given the user is on the login page
When the user enters 'Vagif101' valid username
When the user enters 'BAkcell88---' valid password
And clicks on the login button
And Click user menu icon
When user go to Settings page
And I click on the date format element
And I click on the date option
And I refresh the page
And I click on the clock mode element
#Then  verify that date mode is 24h