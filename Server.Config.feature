Feature:Server Config

Scenario: Server Config
Given The user is on the login page
When The user enters 'Vagif101' valid username
When The user enters 'BAkcell88---' valid password
And Clicks on the login button
And Click on server config
And Click on ethernet/serial toggle
And Click to Update
And Verify changes
And I refresh the page
Then Click on  Log Cs Communication Messages toggle
And Click to Update
And Verify changes
And I refresh the page
And I Enter '221.221.221.22' IP Address
And Click to Update
And Verify changes
And I refresh the page
And Enter '12345' Port
And Click to Update
And Verify changes
And I enter '59863214' serial port
And Click to Update
And Verify changes




Scenario: Server Config (Negative scenarios) IP Address
Given The user is on the login page
When The user enters 'Vagif101' valid username
When The user enters 'BAkcell88---' valid password
And Clicks on the login button
And Click on server config
And I Enter '221.221.221.225555' IP Address
And Click to Update
Then Verify that error message is here
And I refresh the page
And I leave ' ' ip address filed blank
And Click to Update
And Verify blank filed error message
And I refresh the page




Scenario: Server Config (Port) (Negative scenarios)
Given The user is on the login page
When The user enters 'Vagif101' valid username
When The user enters 'BAkcell88---' valid password
And Clicks on the login button
And Click on server config
And Enter '6968471' Port
And Click to Update
And Check error message
And I refresh the page
And I leave port ' ' filed blank
And Click to Update
And Verify blank error message
And I refresh the page


Scenario: Server Config (Serial Port) (Negative scenarios)
Given The user is on the login page
When The user enters 'Vagif101' valid username
When The user enters 'BAkcell88---' valid password
And Clicks on the login button
And Click on server config
And I enter '59863214569874521' serial port
And Click to Update
And Check seral port error message
And I refresh the page
And I leave serial port ' ' filed blank
And Click to Update
And Verify seral port blank error message
And I refresh the page