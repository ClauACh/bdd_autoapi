@labels @acceptance

Feature: Labels

  @label_id
  Scenario:  Verify GET one label is returning all data correctly
      As a user I want to GET a label from TODOIST API

    Given I set the base url and headers
    When I call to labels endpoint using "GET" method using the "label_id" as parameter
    Then I receive a 200 status code in response
  #  And I validate the response data from file


  Scenario:  Verify GET all personal labels is returning all data correctly
      As a user I want to GET all personal labels from TODOIST API

    Given I set the base url and headers
    When I call to labels endpoint using "GET" method using the "None" as parameter
    Then I receive a 200 status code in response
   # And I validate the response data from file


  Scenario:  Verify POST label creates the label correctly
      As a user I want to create a label from TODOIST API

    Given I set the base url and headers
    When I call to labels endpoint using "POST" method using the "label data" as parameter
    """
    {
      "name": "Label F"
    }
    """
    Then I receive a 200 status code in response
  #  And I validate the response data from file


  @label_id
  Scenario:  Verify DELETE label delete the label correctly
      As a user I want to delete a label from TODOIST API

    Given I set the base url and headers
    When I call to labels endpoint using "DELETE" method using the "label_id" as parameter
    Then I receive a 204 status code in response
  #  And I validate the response data from file
