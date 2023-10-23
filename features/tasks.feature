@tasks @acceptance

Feature: Tasks

  @task
  Scenario:  Verify GET all tasks is returning all data correctly
      As a user I want to GET the tasks from TODOIST API

    Given I set the base url and headers
    When I call to tasks endpoint using "GET" method using the "None" as parameter
    Then I receive a 200 status code in response
    And I validate the response data from file using all

  @task_id
  Scenario:  Verify GET one tasks is returning all data correctly
      As a user I want to GET the tasks from TODOIST API

    Given I set the base url and headers
    When I call to tasks endpoint using "GET" method using the "task_id" as parameter
    Then I receive a 200 status code in response
    And I validate the response data from file using ""


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
    And I validate the response data from file using ""


  @project_id @task_id
  Scenario:  Verify POST section creates the task using a project provided correctly
      As a user I want to create a task with project id provided from TODOIST API

    Given I set the base url and headers
    When I call to tasks endpoint using "POST" method using the "task data" as parameter
    """
    {
      "content": "Task created from feature",
      "project_id": "project_id",
      "due_string": "tomorrow at 11:00",
      "due_lang": "es",
      "priority": 3
    }
    """
    Then I receive a 200 status code in response
    And I validate the response data from file using ""


  @task_id
  Scenario: Verify DELETE task endpoint deletes a task with the id provided

    Given I set the base url and headers
    When I call to tasks endpoint using "DELETE" method using the "project_id" as parameter
    Then I receive a 204 status code in response
    And I validate the response data from file using ""

  @post @task_id
  Scenario: Verify POST task endpoint updates a task with the content provided

    Given I set the base url and headers
    When I call to tasks endpoint using "POST" method using the "update task data" as parameter
    """
    {
      "content": "Task Updated"
    }
    """
    Then I receive a 200 status code in response
    And I validate the response data from file using ""


    @task_id
    Scenario:  Verify that a task can be reopened
      As a user I want to reopen a task from TODOIST API
    Given I set the base url and headers
    When I want close the task
    Then I want to reopen the task
    And I receive a 204 status code in response
    And I validate the response data from file using ""



