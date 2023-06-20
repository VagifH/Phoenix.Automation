Feature:Roles Page

Scenario: Roles Page
Given the user is on the login page
When the user enters 'Vagif101' valid username
When the user enters 'BAkcell88---' valid password
And clicks on the login button
And Click on Roles page
When Click on first user in the list
And Click on Auth Profile Read to turn on/off
And I click on Auth Profile manager to turn on/off
And Click and edit '60' App Render Engine read
And Click and edit '100' App Render Engine write
And Click on Update button
Then Verify that successfull pop message is displayed




