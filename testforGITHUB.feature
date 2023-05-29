Feature:Timezone

Scenario: Change Timezone to America/Panama

Given the user is on the login page
When the user enters 'Vagif101' valid username
When the user enters 'BAkcell88---' valid password
And clicks on the login button
And Click user menu icon
When user go to Settings page
And I click on the timezone option
And I click on dropdown
And I select "America/Panama" from the dropdown list
And I refresh the page
And And I click on the timezone
Then the timezone should be set to "America/Panama"