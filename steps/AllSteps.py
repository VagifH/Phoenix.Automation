import time
import self as self
from behave import *
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from features.page.base import BasePage


class AllSteps(BasePage):
    # login element info
    URL = 'https://rpi.local/dashboard/users'
    USERNAME_SELECTOR = (By.NAME, 'UserNameOrEmail')
    PASSWORD_SELECTOR = (By.NAME, 'Password')
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    ERROR_MESSAGE_USERNAME = (By.XPATH, "//div[@class='alert alert-danger']")
    USERNAME_PASSWORD_FIELDS_BLANK_ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")

    # Setting edit profile element info
    ACTION_BTN = (By.XPATH, "(//button[@data-testid='editUser'])[1]")
    EMAIL_SELECTOR = (By.XPATH, "(//input[@class='MuiInputBase-input MuiOutlinedInput-input css-j6vbi8'])[2]")
    UPDATE_PROFILE = (By.XPATH,
                      "(//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-disableElevation MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-disableElevation css-1prp8n9'])[1]")

    FULLNAME_SELECTOR = (By.CSS_SELECTOR,
                         'div:nth-of-type(1) > .MuiFormControl-root.MuiTextField-root.css-i44wyl  .MuiInputBase-input.MuiOutlinedInput-input.css-j6vbi8')

    PHONENUMBER_SELECTOR = (By.CSS_SELECTOR,
                            'div:nth-of-type(3) > .MuiFormControl-root.MuiTextField-root.css-i44wyl  .MuiInputBase-input.MuiOutlinedInput-input.css-j6vbi8')

    SUCCESSFULL_POPUPMESSAGE_SELECTOR = (By.CSS_SELECTOR, "#notistack-snackbar")

    INCORRECT_FULLNAME_ERROR = (By.CSS_SELECTOR, "div:nth-of-type(2) > .MuiFormHelperText-root.css-170h3rz")
    INCORRECT_EMAIL_ADDRESS = (By.CSS_SELECTOR, "div:nth-of-type(2) > .MuiFormHelperText-root.css-170h3rz")
    PHONE_NUMBER_ERROR = (By.CSS_SELECTOR, "div:nth-of-type(3) > .MuiFormHelperText-root.css-170h3rz")

    # SettingClockMode
    USERMENU_ICON = (By.CSS_SELECTOR, "div[aria-label='User Menu']")
    SETTING_BUTTON = (By.XPATH, "//li[@role='menuitem'][1]")
    CLOCKMODE_BUTTON = (By.XPATH, "(//button[@type='button'])[5]")
    CHANGE_CLOCKMODE_BUTTON = (By.CSS_SELECTOR, "span[class='MuiSwitch-root MuiSwitch-sizeMedium css-cl5tzc']")

    # Setting Timezone
    TIMEZONE_BUTTON = (By.CSS_SELECTOR,
                       "div[role='tabpanel'] .MuiTabs-fixed.MuiTabs-scroller.css-1anid1y > div[role='tablist'] > button:nth-of-type(3)")
    TIMEZONE_DROPDOWN_BUTTON = (By.CSS_SELECTOR, "div[role='tabpanel'] div[role='button']")
    AMERICA_PANAMA_DROPDOWN_LIST = (By.XPATH, "//div[@id='menu-']//ul[@role='listbox']/li[93]")

    # Change Password
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div[role='tablist'] > button:nth-of-type(3)")
    CURRENT_PASSWORD = (By.CSS_SELECTOR, "input#oldPassword")
    USERMENU_ICON = (By.CSS_SELECTOR, "div[aria-label='User Menu']")
    NEW_PASSWORD = (By.CSS_SELECTOR, "input#newPassword")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#confirmPassword")
    UPDATE_BUTTON = (By.CSS_SELECTOR, "[class='MuiBox-root css-16332ei'] [tabindex]")
    PW_SUUCESFULY_CHANGED_NOTIFICATION_SELECTOR = (By.CSS_SELECTOR,
                                                   "div#root > .MuiAppBar-colorPrimary.MuiAppBar-positionFixed.MuiAppBar-root.MuiPaper-elevation.MuiPaper-elevation4.MuiPaper-root.css-1ew0fbc.mui-fixed")
    ALERT_NOTIFICATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR,
                                           "div:nth-of-type(3) > .MuiFormControl-root.css-13sljp9 > .MuiFormHelperText-contained.MuiFormHelperText-filled.MuiFormHelperText-root.MuiFormHelperText-sizeMedium.css-1lisuo3")
    ALERT_NOTIFICATION_WEAK_PASSWORD = (By.CSS_SELECTOR,
                                        "div:nth-of-type(2) > .MuiFormControl-root.css-13sljp9 > .MuiFormHelperText-contained.MuiFormHelperText-filled.MuiFormHelperText-root.MuiFormHelperText-sizeMedium.css-1lisuo3")

    # Create new user
    CREATE_USER_BUTTON = (By.CSS_SELECTOR, "[href='\/dashboard\/users\/create'] [tabindex]")
    FULL_NAME_FIELD = (By.XPATH, "//input[@class='MuiInputBase-input MuiOutlinedInput-input css-j6vbi8'][1]")
    USERNAME_FIELD = (By.CSS_SELECTOR, "form .css-z7vtc8:nth-of-type(2) .MuiOutlinedInput-input")
    ROLE_FIELD_CLICK = (By.XPATH, "//div[@id='roleIds']")
    SELECT_ADMINISTRATOR_ROLE = (By.XPATH, "//li[@data-value='Administrator']")
    EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "form .css-z7vtc8:nth-of-type(4) .MuiOutlinedInput-input")
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, "form .css-z7vtc8:nth-of-type(5) .MuiOutlinedInput-input")
    PASSWORD_FIELD = (By.XPATH, "/html//input[@id='password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "/html//input[@id='confirmPassword']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[class='MuiBox-root css-16332ei'] [tabindex]")
    ROLE_IS_NOT_SELECTED_ERROR = (By.XPATH,
                                  "/html//div[@id='root']/div[@class='css-qvls4e']/div[@class='MuiBox-root css-ajnmy4']/div[@class='MuiBox-root css-erhn22']//form/div[3]/div[@class='MuiFormControl-root css-13sljp9']/p[.='The field is required']")

    INCORRECT_EMAIL = (By.XPATH, "/html//div[@id='root']/div[@class='css-qvls4e']/div[@class='MuiBox-root css-ajnmy4']//form/div[4]/div[@class='MuiFormControl-root MuiTextField-root css-i44wyl']//input")
    INVALID_USERNAME_ERROR = (By.XPATH,"//div[2]/div[contains(@class, 'MuiFormControl-root') and contains(@class, 'MuiTextField-root')]""/descendant::input[contains(@class, 'MuiInputBase-input') and contains(@class, 'MuiOutlinedInput-input')]")
    INVALID_FULLNAME_ERROR = (By.CSS_SELECTOR,"form .css-z7vtc8:nth-of-type(1) p")
    INVALID_PHONE_NUMBER_ERROR = (By.CSS_SELECTOR,"form .css-z7vtc8:nth-of-type(5) p")
    PASSWORD_MISMATCH = (By.CSS_SELECTOR,"form .css-z7vtc8:nth-of-type(7) [class='MuiFormHelperText-root MuiFormHelperText-sizeMedium MuiFormHelperText-contained MuiFormHelperText-filled css-1lisuo3']")

    def driver_refresh(self):
        self.driver.refresh()

    def input_clock_mode(self):
        clockmode_button = self.driver.find_element(*self.CLOCKMODE_BUTTON)
        clockmode_button.click()
        time.sleep(2)

    def user_menu_icon(self):
        user_menu_icon = self.driver.find_element(*self.USERMENU_ICON)
        user_menu_icon.click()
        time.sleep(2)

    def change_clock_mode(self):
        change_clockmode_button = self.driver.find_element(*self.CHANGE_CLOCKMODE_BUTTON)
        change_clockmode_button.click()
        time.sleep(3)

    def input_setting_mode(self):
        setting_button = self.driver.find_element(*self.SETTING_BUTTON)
        setting_button.click()
        time.sleep(3)

    def input_username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_SELECTOR)
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_SELECTOR)
        password_input.send_keys(password)

    def UpdateProfile_Click(self):
        UpdateProfile = self.driver.find_element(*self.UPDATE_PROFILE)
        UpdateProfile.click()

    def click_login(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()

    def click_action_btn(self):
        action_button = self.driver.find_element(*self.ACTION_BTN)
        action_button.click()

    def loginInSite(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    def incorrect_credentials__error_message(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.ERROR_MESSAGE_USERNAME)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    def input_email(self, email):
        email_address_input = self.driver.find_element(*self.EMAIL_SELECTOR)
        email_address_input.clear()
        time.sleep(3)
        email_address_input.send_keys(Keys.CONTROL, 'a')
        email_address_input.send_keys(Keys.BACKSPACE)
        email_address_input.send_keys(email)

    def input_fullname(self, fullname):
        fullname_input = self.driver.find_element(*self.FULLNAME_SELECTOR)
        fullname_input.clear()
        time.sleep(3)
        fullname_input.send_keys(Keys.CONTROL, 'a')
        fullname_input.send_keys(Keys.BACKSPACE)
        fullname_input.send_keys(fullname)
        time.sleep(3)

    def input_phonenumber(self, phonenumber):
        phonenumber_input = self.driver.find_element(*self.PHONENUMBER_SELECTOR)
        phonenumber_input.clear()
        time.sleep(3)
        phonenumber_input.send_keys(Keys.CONTROL, 'a')
        phonenumber_input.send_keys(Keys.BACKSPACE)
        phonenumber_input.send_keys(phonenumber)

    # Edit user profile > Successfull Pop up message

    def check_pop_up_message(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.SUCCESSFULL_POPUPMESSAGE_SELECTOR)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    # Setting > edit user profile > invalid full name
    def check_fullname_error_message(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.INCORRECT_FULLNAME_ERROR)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

        # Edit user profile > Incorrect email address

    def check_email_address_error_message(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.INCORRECT_EMAIL_ADDRESS)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    # Edit user profile > Incorrect email address
    def check_phone_number_error_message(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.PHONE_NUMBER_ERROR)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    # Login_Page_Blank_field_error_message
    def blank_field_error_message(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.USERNAME_PASSWORD_FIELDS_BLANK_ERROR_MESSAGE)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    # Settings_Timezne_Dropdown_Button
    def timezone_dropdown_button(self):
        timezone_dropdown_button = self.driver.find_element(*self.TIMEZONE_DROPDOWN_BUTTON)
        timezone_dropdown_button.click()
        time.sleep(2)

    def timezone_button(self):
        timezone_button = self.driver.find_element(*self.TIMEZONE_BUTTON)
        timezone_button.click()
        time.sleep(2)

    def select_panama_in_dropdown_list(self):
        select_panama_in_dropdown_list = self.driver.find_element(*self.AMERICA_PANAMA_DROPDOWN_LIST)
        select_panama_in_dropdown_list.click()

    # Check that America/Panama is there
    def check_american_panama(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.AMERICA_PANAMA_DROPDOWN_LIST)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

        # Change Password Button

    def change_password_button(self):
        change_password_button = self.driver.find_element(*self.CHANGE_PASSWORD_BUTTON)
        change_password_button.click()
        time.sleep(2)

    def current_password(self, current_password):
        current_password_input = self.driver.find_element(*self.CURRENT_PASSWORD)
        current_password_input.send_keys(current_password)

    def new_password(self, new_password):
        new_password_input = self.driver.find_element(*self.NEW_PASSWORD)
        new_password_input.send_keys(new_password)

    def confirm_password(self, confirm_password):
        confirm_password_input = self.driver.find_element(*self.CONFIRM_PASSWORD)
        confirm_password_input.send_keys(confirm_password)

    def update_button(self):
        update_button = self.driver.find_element(*self.UPDATE_BUTTON)
        update_button.click()
        time.sleep(3)

    # Change password successful notification
    def password_changed_notification(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.PW_SUUCESFULY_CHANGED_NOTIFICATION_SELECTOR)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    time.sleep(3)

    # Change password alert notification about confirm password is not the same
    def password_changed_alert_notification(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.ALERT_NOTIFICATION_CONFIRM_PASSWORD)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    time.sleep(3)

    # Change password alert notification about weak password
    def alert_notification_week_password(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.ALERT_NOTIFICATION_WEAK_PASSWORD)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    # Create User Button
    def create_user_button(self):
        create_user_button = self.driver.find_element(*self.CREATE_USER_BUTTON)
        create_user_button.click()
        time.sleep(1)

    # Create New User_ Fullname
    def full_name(self, full_name):
        fullname_input = self.driver.find_element(*self.FULL_NAME_FIELD)
        fullname_input.send_keys(full_name)

    # Create New Use_Username
    def username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_FIELD)
        username_input.send_keys(username)

    # Create new user_Role field click
    def click_role_field(self):
        click_role_field = self.driver.find_element(*self.ROLE_FIELD_CLICK)
        click_role_field.click()

    # Create new user page _Select Administrator Role
    def select_administrator_role(self):
        select_administrator_role = self.driver.find_element(*self.SELECT_ADMINISTRATOR_ROLE)
        select_administrator_role.click()
        select_administrator_role.send_keys(Keys.ESCAPE)

    # Create new user_Email address
    def email_address(self, email_address):
        email_address_input = self.driver.find_element(*self.EMAIL_ADDRESS_FIELD)
        email_address_input.send_keys(email_address)

    # Create new user_phone_number
    def phone_number(self, phone_number):
        phone_number_input = self.driver.find_element(*self.PHONE_NUMBER_FIELD)
        phone_number_input.send_keys(phone_number)

    # Create new user_password
    def set_password(self, set_password):
        set_password_input = self.driver.find_element(*self.PASSWORD_FIELD)
        set_password_input.send_keys(set_password)
        time.sleep(1)

    def set_confirm_password(self, set_confirm_password):
        set_confirm_password_input = self.driver.find_element(*self.CONFIRM_PASSWORD_FIELD)
        set_confirm_password_input.send_keys(set_confirm_password)
        time.sleep(1)

    def submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        submit_button.click()
        time.sleep(3)

    # Create User Role is not Selected error
    def role_is_not_selected_error(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.ROLE_IS_NOT_SELECTED_ERROR)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False
    time.sleep(5)

     # Create User incorrect_email_error
    def incorrect_email_error(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.INCORRECT_EMAIL)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False
    time.sleep(5)

    # Create User invalid_username_error
    def invalid_username_error(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.INVALID_USERNAME_ERROR)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    time.sleep(5)

    # Create User invalid_fullname_error
    def invalid_fullname_error(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.INVALID_FULLNAME_ERROR)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    time.sleep(5)

    # Create User invalid_phone_number_error  password_mismatch_error
    def invalid_phone_number_error(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.INVALID_PHONE_NUMBER_ERROR)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    time.sleep(5)

    # Create User password_mismatch_error
    def password_mismatch_error(self):
        loop_count = 0
        while loop_count < 1:
            try:
                web_element = self.driver.find_element(*self.PASSWORD_MISMATCH)
                return web_element
            except WebDriverException:
                pass
            loop_count += 1
        assert False

    time.sleep(5)






@given("the user is on the login page")
def step_impl(context):
    context.allSteps.get_page()


@when("the user enters '{username}' valid username")
def step_impl(context, username):
    context.allSteps.input_username(username)


@when("the user enters '{password}' valid password")
def step_impl(context, password):
    context.allSteps.input_password(password)


@when("the login '{username}' '{password}'")
def step_impl(context, username, password):
    context.allSteps.loginInSite(username, password)


@step("clicks on the login button")
def step_impl(context):
    context.allSteps.click_login()
    time.sleep(3)


@step("clicks on the action button")
def step_impl(context):
    context.allSteps.click_action_btn()
    time.sleep(3)


@then("the user should be redirected to the homepage")
def step_impl(context):
    time.sleep(3)
    url = 'https://rpi.local/dashboard/users'

    if context.browser.get_current_url() == url:
        booaal = True
    else:
        assert False, f"Expected URL: {url}, Actual URL: {context.browser.get_current_url}"


@step("I enter an '{email}' to email field")
def step_impl(context, email):
    context.allSteps.input_email(email)


@step('the user clicks on the "Save" button')
def step_impl(context):
    time.sleep(3)
    context.allSteps.UpdateProfile_Click()


@when("user go to Settings page")
def step_impl(context):
    context.allSteps.input_setting_mode()


@step("I click on the clock mode element")
def step_impl(context):
    context.allSteps.input_clock_mode()


@step("I refresh the page")
def step_impl(context):
    context.allSteps.driver_refresh()


@step("I click on the clock mode option")
def step_impl(context):
    context.allSteps.change_clock_mode()


@step("Click user menu icon")
def step_impl(context):
    context.allSteps.user_menu_icon()


@step("I enter an '{fullname}' to fullname")
def step_impl(context, fullname):
    context.allSteps.input_fullname(fullname)


@step("I enter an '{phonenumber}' to phone number field")
def step_impl(context, phonenumber):
    context.allSteps.input_phonenumber(phonenumber)


@step("verify that profile is updated")
def step_impl(context):
    pop_up_message = context.allSteps.check_pop_up_message()
    if pop_up_message.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@step("I enter an '{fullname}' to fullname field")
def step_impl(context, fullname):
    context.allSteps.input_fullname(fullname)


@step("verify that error message is there")
def step_impl(context):
    fullname_error_message = context.allSteps.check_fullname_error_message()
    if fullname_error_message.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@step("verify that error message is displayed")
def step_impl(context):
    email_address_error_message = context.allSteps.check_email_address_error_message()
    if email_address_error_message.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@step("I enter an '{phonenumber} to phone number")
def step_impl(context, phonenumber):
    context.allSteps.input_phonenumber(phonenumber)


@then("verify that error message is shown")
def step_impl(context):
    phone_number_error_message = context.allSteps.check_phone_number_error_message()
    if phone_number_error_message.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@then("the user should see an error message")
def step_impl(context):
    incorrect_credentials__error_message = context.allSteps.incorrect_credentials__error_message()
    if incorrect_credentials__error_message.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@step("the user should see an error message blank field")
def step_impl(context):
    blank_field_error_message = context.allSteps.blank_field_error_message()
    if blank_field_error_message.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@step("I click on the timezone option")
def step_impl(context):
    context.allSteps.timezone_button()


@step("I click on dropdown")
def step_impl(context):
    context.allSteps.timezone_dropdown_button()


@step('I select "America/Panama" from the dropdown list')
def step_impl(context):
    context.allSteps.select_panama_in_dropdown_list()


@then('the timezone should be set to "America/Panama"')
def step_impl(context):
    check_american_panama = context.allSteps.check_american_panama
    if check_american_panama.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@step("And I click on the timezone")
def step_impl(context):
    context.allSteps.timezone_button()


@step("the user clicks on the change password button")
def step_impl(context):
    context.allSteps.change_password_button()


@step("the user fills out the current password field with '{current_password}' current password")
def step_impl(context, current_password):
    context.allSteps.current_password(current_password)


@step("the user fills out the new password field with '{new_password}' new_password")
def step_impl(context, new_password):
    context.allSteps.new_password(new_password)


@step("the user fills out the confirm password field with '{confirm_password}' new_password")
def step_impl(context, confirm_password):
    context.allSteps.confirm_password(confirm_password)


@step("the user clicks on the Update button")
def step_impl(context):
    context.allSteps.update_button()


@then("the password should be successfully changed")
def step_impl(context):
    password_changed_notification = context.allSteps.password_changed_notification()
    if password_changed_notification.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@then("There should be an error message that confirm password is not the same")
def step_impl(context):
    password_changed_alert_notification = context.allSteps.password_changed_alert_notification()
    if password_changed_alert_notification.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@then("There should be an error message that password is weak")
def step_impl(context):
    alert_notification_week_password = context.allSteps.alert_notification_week_password()
    if alert_notification_week_password.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@step("I Click on Create User button")
def step_impl(context):
    context.allSteps.create_user_button()


@when("I enter a valid full name '{full_name}'")
def step_impl(context, full_name):
    context.allSteps.full_name(full_name)


@step("I enter a valid username '{username}'")
def step_impl(context, username):
    context.allSteps.username(username)


@step("I click on role field")
def step_impl(context):
    context.allSteps.click_role_field()


@step('I select a valid role "Administrator"')
def step_impl(context):
    context.allSteps.select_administrator_role()


@step("I enter a valid email '{email_address}'")
def step_impl(context, email_address):
    context.allSteps.email_address(email_address)


@step("I enter a valid phone number '{phone_number}'")
def step_impl(context, phone_number):
    context.allSteps.phone_number(phone_number)


@step("I enter a valid password '{set_password}'")
def step_impl(context,set_password):
    context.allSteps.set_password(set_password)


@step("I confirm the '{set_confirm_password}'")
def step_impl(context, set_confirm_password):
    context.allSteps.set_confirm_password(set_confirm_password)


@step("I submit the form")
def step_impl(context):
    context.allSteps.submit_button()


@then("I should see a success message")
def step_impl(context):
    context.allSteps.get_page()


@then("there should be an error message that role is not selected")
def step_impl(context):
    role_is_not_selected_error = context.allSteps.role_is_not_selected_error()
    if role_is_not_selected_error.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@then("there should be an error message that email is incorrect")
def step_impl(context):
    incorrect_email_error = context.allSteps.incorrect_email_error()
    if incorrect_email_error.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@then("there should be an error message that username is invalid")
def step_impl(context):
    invalid_username_error = context.allSteps.invalid_username_error()
    if invalid_username_error.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@then("there should be an error message that fullname is invalid")
def step_impl(context):
    invalid_fullname_error = context.allSteps.invalid_fullname_error()
    if invalid_fullname_error.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@then("there should be an error message that phone number is incorrect")
def step_impl(context):
    invalid_phone_number_error = context.allSteps.invalid_phone_number_error()
    if invalid_phone_number_error.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")


@then("there should be an error message that password is mismatch")
def step_impl(context):
    password_mismatch_error = context.allSteps.password_mismatch_error()
    if password_mismatch_error.is_displayed():
        print("SUCCESS: The error message is displayed.")
    else:
        print("FAILURE: The error message is not displayed.")