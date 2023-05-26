Feature:Clock Mode

Scenario: Change clock mode

Given the user is on the login page
When the user enters 'Vagif101' valid username
When the user enters 'BAkcell88---' valid password
And clicks on the login button
And Click user menu icon
When user go to Settings page
And I click on the clock mode element
And I click on the clock mode option
And I refresh the page
And I click on the clock mode element
#Then  verify that clock mode is 24h