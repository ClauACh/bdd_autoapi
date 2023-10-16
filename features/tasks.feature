@tasks @acceptance

Feature: Tasks

  @task
  Scenario:  Verify GET all tasks is returning all data correctly
      As a user I want to GET the tasks from TODOIST API

    Given I set the base url and headers
    When I call to tasks endpoint using "GET" method using the "None" as parameter
    Then I receive a 200 status code in response

  @task_id @ttt
  Scenario:  Verify GET one tasks is returning all data correctly
      As a user I want to GET the tasks from TODOIST API

    Given I set the base url and headers
    When I call to tasks endpoint using "GET" method using the "task_id" as parameter
    Then I receive a 200 status code in response
    And I validate the response data


  @post
  Scenario: Verify POST task endpoint creates a task with the name provided

    Given I set the base url and headers
    When I call to tasks endpoint using "POST" method using the "content" as parameter
    """
    {
      "content": "Task created lml"
    }
    """
    Then I receive a 200 status code in response

  @task_id
  Scenario: Verify DELETE task endpoint deletes a task with the id provided

    Given I set the base url and headers
    When I call to tasks endpoint using "DELETE" method using the "project_id" as parameter
    Then I receive a 204 status code in response

  @post
  Scenario: Verify POST task endpoint updates a task with the content provided

    Given I set the base url and headers
    When I call to tasks endpoint using "POST" method using the "update task data" as parameter
    """
    {
      "content": "Task Updated",
    }
    """
    Then I receive a 200 status code in response


