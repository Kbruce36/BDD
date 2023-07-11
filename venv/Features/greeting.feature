Feature: Greeting
    Scenario: Greet the user
        Given the user is on the homepage
        When the user enters their name
        Then the system should display a greeting message with the user's name
