Feature: Logout
    Scenario: Log out the user
        Given the user is on the dashboard
        When the user clicks the logout button
        Then the system should display a logout message 