@comments @acceptance

Feature: Comments

  @task_id
  Scenario:  Verify GET all comments from a task is returning all data correctly
      As a user I want to GET the comments from TODOIST API

    Given I set the base url and headers
    When I call to comments endpoint using "GET" method using the "task_id" as parameter
    Then I receive a 200 status code in response


  @task_id
  Scenario: Verify POST comment endpoint creates a comment with the name provided

    Given I set the base url and headers
    When I call to comments endpoint using "POST" method using the "content" as parameter
    """
    {
    "task_id": "task_id",
    "content": "Comment created"
    }
    """
    Then I receive a 200 status code in response

  @comment_id
  Scenario: Verify DELETE comment endpoint creates a comment with the name provided

    Given I set the base url and headers
    When I call to comments endpoint using "DELETE" method using the "comment_id" as parameter
    Then I receive a 204 status code in response

  @comment_id
  Scenario: Verify POST project endpoint updates a comment with the name provided

    Given I set the base url and headers
    When I call to comments endpoint using "POST" method using the "update comment data" as parameter
    """
    {
      "task_id": "task_id",
      "content": "Comment updated"
    }
    """
    Then I receive a 200 status code in response

