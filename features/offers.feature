Feature:Book my show offers

  Scenario Outline: : Common steps
    Given launch the browser
    When open BookMyshow homepage
    And choose city
    Then Click on offers button
    Then enter  "<search>" in search bar
    Then   apply credit card filter
    And  apply debit card filter
    And  apply wallet filter
    Examples:
    |search|
    |SBI   |










