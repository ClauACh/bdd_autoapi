"""
(c) Copyright Jalasoft. 2023

steps_todo.py
    step definitions for feature files
"""
import json
import logging

from behave import given, when, then, step, use_step_matcher

from utils.logger import get_logger
from utils.rest_client import RestClient
from utils.validate_response import ValidateResponse

LOGGER = get_logger(__name__, logging.DEBUG)

# use_step_matcher("re")


@given('I set the base url and headers')
def step_set_base_url(context):
    LOGGER.debug("HEADERS: %s", context.headers)
    LOGGER.debug("URL: %s", context.url)


@then('I receive a {status_code:d} status code in response')
def step_verify_status_code(context, status_code):
    LOGGER.debug("Status code from response: %s", context.response["status"])
    LOGGER.debug("Status code param: %s", type(status_code))
    LOGGER.debug("Status code response: %s", type(context.response["status"]))
    context.status_code = status_code
    assert int(status_code) == context.response["status"], " Expected 200 but received " + str(context.response["status"])


# @step(u'I call to projects endpoint using "(\\w*)" method( using the "([\\w\\s]*)" as parameter)*')
@step('I call to {feature} endpoint using "{method_name}" method using the "{param}" as parameter')
def step_call_endpoint(context, feature, method_name, param):
    # url base "https://api.todoist.com/rest/v2/" + feature .ie. projects, sections, tasks, etc.
    url = context.url + context.feature_name
    data = None

    if method_name == "POST":
        if "update" in param:
            url = get_url_by_feature(context)
        if context.text:
            data = get_data_by_feature(context)
    elif method_name == "DELETE" or (method_name == "GET" and param != "None"):
        url = get_url_by_feature(context)
    # if context.table:
    #     LOGGER.debug("Table: %s", context.table)
    #     index = 0
    #     for table in context.table:
    #         LOGGER.debug("row: %s", table[index])
    #         index += 1

    # update the url with resources id created

    response = RestClient().send_request(method_name=method_name.lower(),
                                         session=context.session,
                                         url=url,
                                         headers=context.headers,
                                         data=data)

    LOGGER.debug("Response: %s", response)
    # add resources created to clean up lists
    if method_name == "POST":
        if response:
            append_to_resources_list(context, response)

    context.response = response
    context.method = method_name


@step("I validate the response data")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ValidateResponse().validate_response(actual_response=context.response,
                                         method=context.method.lower(),
                                         expected_status_code=context.status_code,
                                         feature=context.feature_name)


def get_url_by_feature(context):
    feature_id = None
    if context.feature_name == "projects":
        feature_id = context.project_id
    elif context.feature_name == "sections":
        feature_id = context.section_id
    elif context.feature_name == "tasks":
        feature_id = context.task_id

    url = f"{context.url}{context.feature_name}/{feature_id}"

    return url


def append_to_resources_list(context, response):
    """
    Method to append resources to clean up lists
    :param context:
    :param response:
    """
    if context.feature_name == "projects":
        context.project_list.append(response["body"]["id"])
    if context.feature_name == "sections":
        context.section_list.append(response["body"]["id"])


def get_data_by_feature(context):
    LOGGER.debug("JSON: %s", context.text)
    dictionary = json.loads(context.text)
    if context.feature_name == "projects":
        if "project_id" in dictionary:
            dictionary["project_id"] = context.project_id
    if context.feature_name == "sections":
        if "section_id" in dictionary:
            dictionary["section_id"] = context.section_id
        if "project_id" in dictionary:
            dictionary["project_id"] = context.project_id

    LOGGER.debug("Dictionary created: %s", dictionary)
    return dictionary

