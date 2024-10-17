Feature: Perbanas Institute Website Navigation
As a user,
I want to visit the Perbanas Institute website
So that I can check if the homepage loads correctly

Scenario: Visit the Perbanas Institute homepage
  Given I open the browser
  When I navigate to "http://103.175.219.114/perbanas-institute/#/"
  Then I should see the homepage loaded successfully with the title "Perbanas Institute"

Scenario: Login with valid credential
    Given I have loaded Perbanas Institute Login Page
    When I fill the username and password field with "usertes" and "password"
    Then I should see Perbanas Dashboard

Scenario: Login with invalid password
    Given I have loaded Perbanas Institute Login Page
    When I fill the username and password field with "usertes" and "blabla"
    Then I should see error text Username atau password salah