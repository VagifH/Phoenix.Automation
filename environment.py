from features.browser import Browser
from features.steps.AllSteps import AllSteps


def before_scenario(context, scenario):
    context.browser = Browser()
    context.allSteps = AllSteps(context.browser)
    # context.editUserProfile = EditUserProfile(context.browser)
    # context.createuser = createuser


def after_scenario(context, scenario):
    context.browser.quit()
