Feature:ChangePassword

Scenario: Change Password
Given the user is on the login page
When the user enters 'Vagif2' valid username
When the user enters 'BAkcell88--' valid password
And clicks on the login button
And Click user menu icon
When user go to Settings page
And the user clicks on the change password button
And the user fills out the current password field with 'BAkcell88--' current password
And the user fills out the new password field with 'BAkcell88---' new_password
And the user fills out the confirm password field with 'BAkcell88---' new_password
And the user clicks on the Update button
Then the password should be successfully changed


Scenario: Change Password - Incorrect Confirmation
Given the user is on the login page
When the user enters 'Vagif2' valid username
When the user enters 'BAkcell88--' valid password
And clicks on the login button
And Click user menu icon
When user go to Settings page
And the user clicks on the change password button
And the user fills out the current password field with 'BAkcell88--' current password
And the user fills out the new password field with 'BAkcell88---' new_password
And the user fills out the confirm password field with 'BAkcell88--' new_password
And the user clicks on the Update button
Then There should be an error message that confirm password is not the same


Scenario: Change Password - Weak New and Conform password fields
Given the user is on the login page
When the user enters 'Vagif2' valid username
When the user enters 'BAkcell88--' valid password
And clicks on the login button
And Click user menu icon
When user go to Settings page
And the user clicks on the change password button
And the user fills out the current password field with 'BAkcell88--' current password
And the user fills out the new password field with 'BAkcell' new_password
And the user fills out the confirm password field with 'BAkcell' new_password
And the user clicks on the Update button
Then There should be an error message that password is weak
