"""
(c) Copyright Jalasoft. 2023

environment.py
    file with all fixture methods for feature and step files
"""
import logging

import requests

from config.config import BASE_URL, HEADERS
from utils.logger import get_logger
from utils.rest_client import RestClient

LOGGER = get_logger(__name__, logging.DEBUG)


def before_all(context):
    """
    method to define variables that will be used in steps definitions
    :param context:   object     Context object to store and get variables
    """
    context.session = requests.Session()
    context.headers = HEADERS
    context.project_list = []
    context.section_list = []
    context.task_list = []
    context.resource_list = {
        "projects": [],
        "sections": [],
        "tasks": []
    }

    context.url = BASE_URL
    LOGGER.debug("Headers before feature: %s", context.headers)
    projects = get_all_projects(context)
    LOGGER.debug(projects)
    context.project_id_from_all = projects["body"][1]["id"]


def before_feature(context, feature):
    """
    Method to be executed before each feature
    :param context:     object      Contains context information
    :param feature:     object      Contains feature information
    """
    LOGGER.debug("Before feature")
    context.feature_name = feature.name.lower()
    # context.url = BASE_URL + feature.name.lower()


def before_scenario(context, scenario):
    LOGGER.debug("Scenario tags: %s", scenario.tags)
    LOGGER.debug("Scenario Name: %s", scenario.name)

    if "project_id" in scenario.tags:

        response = create_project(context=context, name_project="project x")
        context.project_id = response["body"]["id"]
        LOGGER.debug("Project id created: %s", context.project_id)
        context.resource_list["projects"].append(context.project_id)

    if "section_id" in scenario.tags:

        response = create_section(context=context, project_id=context.project_id_from_all,
                                  section_name="section x")
        context.section_id = response["body"]["id"]
        LOGGER.debug("Section id created: %s", context.section_id)
        context.resource_list["sections"].append(context.section_id)

    if "task_id" in scenario.tags:

        response = create_task(context=context)
        context.task_id = response["body"]["id"]
        LOGGER.debug("Task id created: %s", context.task_id)
        context.resource_list["tasks"].append(context.task_id)


def after_scenario(context, scenario):
    print("after scenario")


def after_feature(context, feature):
    print("After feature")


def after_all(context):
    LOGGER.debug("After all")
    LOGGER.debug("Resources: %s", context.resource_list)
    for resource in context.resource_list:
        LOGGER.debug("Resource: %s", resource)
        for r in context.resource_list[resource]:
            # i.e https://api.todoist.com/rest/v2/ projects / project_id
            url = f"{context.url}{resource}/{r}"
            RestClient().send_request(method_name="delete", session=context.session,
                                      url=url, headers=context.headers)
            LOGGER.info("Deleting %s: %s", resource, r)


def create_project(context, name_project):

    body_project = {
        "name": name_project
    }
    response = RestClient().send_request(method_name="post", session=context.session,
                                         url=context.url+"projects", headers=context.headers,
                                         data=body_project)
    return response


def create_section(context, project_id, section_name):

    body_section = {
        "project_id": project_id,
        "name": section_name
    }
    response = RestClient().send_request(method_name="post", session=context.session,
                                         url=context.url+"sections", headers=context.headers,
                                         data=body_section)
    return response


def get_all_projects(context):
    """
    Method to get all projects
    :param context:   object    Store contextual information about test
    :return:
    """
    response = RestClient().send_request(method_name="get", session=context.session,
                                         url=context.url + "projects", headers=context.headers)

    return response


def create_task(context, project_id=None, section_id=None):
    data = {
        "content": "Task created in feature",
        "due_string": "tomorrow at 11:00",
        "due_lang": "en",
        "priority": 4
    }
    if project_id:
        data["project_id"] = project_id
    if section_id:
        data["section_id"] = section_id

    response = RestClient().send_request(method_name="post", session=context.session, headers=context.headers,
                                         url=context.url + "tasks", data=data)

    return response


def create_comment(context, task_id=None, section_id=None):
    data = {
        "content": "Comment created in task",

    }
    if task_id:
        data["project_id"] = task_id

    response = RestClient().send_request(method_name="post", session=context.session, headers=context.headers,
                                         url=context.url + "tasks", data=data)

    return response
