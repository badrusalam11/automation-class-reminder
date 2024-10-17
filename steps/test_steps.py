from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By class
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@given('I open the browser')
def step_impl(context):
    # Use Service to manage the ChromeDriver
    chrome_service = Service(ChromeDriverManager().install())
    
    # Initialize the Chrome driver
    context.driver = webdriver.Chrome(service=chrome_service)

@when('I navigate to "{url}"')
def step_impl(context, url):
    context.driver.get(url)

@then('I should see the homepage loaded successfully with the title "{expected_title}"')
def step_impl(context, expected_title):
    # Get the title of the webpage and assert it matches the expected title
    actual_title = context.driver.title
    assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

    # Close the browser after validation
    context.driver.quit()


LOGIN_URL = "http://103.175.219.114/perbanas-institute/#/"
@given('I have loaded Perbanas Institute Login Page')
def step_impl(context):
    # Initialize the Chrome driver and load the login page
    chrome_service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=chrome_service)
    context.driver.get(LOGIN_URL)

@when('I fill the username and password field with "{username}" and "{password}"')
def step_impl(context, username, password):
    # Locate the username and password input fields using the placeholder attribute
    username_field = context.driver.find_element(By.XPATH, "//input[@placeholder='Enter your username']")  # Adjust the placeholder as needed
    password_field = context.driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")  # Adjust the placeholder as needed
    
    # Enter the provided username and password
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Submit the form by clicking the login button (adjust the button selector as needed)
    login_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")
    login_button.click()

@then('I should see Perbanas Dashboard')
def step_impl(context):
    context.driver.implicitly_wait(10)
    dashboard_element = context.driver.find_element(By.XPATH, "//a[contains(text(), 'Main Dashboard')]")  # Adjust as needed
    assert dashboard_element is not None, "Dashboard not loaded or login failed"
    
    context.driver.quit()


@then("I should see error text Username atau password salah")
def step_impl(context):
    context.driver.implicitly_wait(10)
    error_element = context.driver.find_element(By.XPATH, "//div[contains(text(), 'Username atau password salah')]")  # Adjust as needed
    assert error_element is not None, "Login failed"
    context.driver.quit()
