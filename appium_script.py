from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

from time import sleep

# #########RENAME

desired_capabilities = {
    "platformName": "Android",
    "automationName": 'uiautomator2',
    "platformVersion": "15",
    "deviceName": "Android Emulator",
    "appActivity": "org.wikipedia.main.MainActivity",
    "appPackage": "org.wikipedia",
    # Put your path below:
    "app": "C:/Users/Owner/Desktop/internship-project/mobile_app/mobile_app/wikipedia.apk"
    # "app": ".../mobile_app/wikipedia.apk"
}

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)  # automationName

driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(5)



########## START TEST CASE CODING###################


# Click Skip btn #CSS SELECTORS DO NOT WORK ON MOBILE
driver.find_element(AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()
# driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia:id/fragment_onboarding_skip_button']").click()
# *//android.widget.Button[@resource-id='org.wikipedia:id/fragment_onboarding_skip_button'].click()
# //android.widget.Button[@text='SKIP']
# //android.widget.Button[contains(@resource-id, 'skip_button')]
# //*[contains(@resource-id, 'skip_button')]
#
# Click Search icon
driver.find_element(AppiumBy.XPATH, "//*[@content-desc='Search Wikipedia']").click()

# Populate search field:
driver.find_element(AppiumBy.ID, 'org.wikipedia:id/search_src_text').send_keys('Python (programming language)')

# Verification
expected_result = 'Python (programming language)'
actual_result = driver.find_element(AppiumBy.ID, 'org.wikipedia:id/page_list_item_title').text

assert actual_result == expected_result, f'Expected {expected_result} did not match actual {actual_result}'
print('Test case PASSED!')
driver.quit()
