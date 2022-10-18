import flask
from datetime import datetime
from flask import make_response, jsonify
from ClickUp.API.Task import Helper as CTaskHelper, API as CAPI
from Zendesk.API.Tickets import API as ZAPI
from configs.clickUp import LIST_ID
from configs.zendesk import GROUP_IDS


def handleTechSupportTaskCreatedEvent(payload: dict) -> flask.Response:

    taskId = payload['task_id']
    CAPI.setTaskFieldValue(taskId, '564c2600-9fa3-47db-9a7c-010750d265ff', payload['history_items']['date'])

    # Check if task already exist in the lookup table record
    if CTaskHelper.checkIfTaskExistsInZendesk(taskId):
        return make_response({'message': 'Task already exist in Zendesk'}, 202)

    # if task is created by zendesk
    taskComments = CAPI.getTaskComments(taskId)
    for comment in taskComments['comments']:
        if comment['user']['source'] == 'Zendesk':
            return make_response(jsonify({'message': 'This task is posted from Zendesk'}), 202)
    # else
    taskDetail = CAPI.getTask(taskId)
    newTicket = ZAPI.createTicketFromTask(taskDetail, GROUP_IDS['CUSTOMER_SUCCESS_TEAM'])
    CAPI.createTaskComment(taskId, f'Check Zendesk Ticket Here: https://kerb.zendesk.com/agent/tickets/{newTicket["ticket"]["id"]}')
    return make_response(
        jsonify({'message': f'Ticket (#{newTicket["ticket"]["id"]}) has been created in zendesk'}),
        201
    )


def handleTaskDeletedEvent(payload: dict) -> flask.Response:
    return make_response(jsonify({'message': 'Task Deletion Operation not yet implemented'}), 202)


def handleTaskUpdatedEvent(payload: dict) -> flask.Response:
    return make_response(jsonify({'message': 'Task Deletion Operation not yet implemented'}), 202)


def handleTaskStatusUpdatedEvent(payload: dict) -> flask.Response:
    return make_response(jsonify({'message': 'Task Deletion Operation not yet implemented'}), 202)


def handleTaskAssigneeUpdatedEvent(payload: dict) -> flask.Response:
    return make_response(jsonify({'message': 'Task Deletion Operation not yet implemented'}), 202)


def handleTaskPriorityUpdatedEvent(payload: dict) -> flask.Response:
    return make_response(jsonify({'message': 'Task Deletion Operation not yet implemented'}), 202)


def handleTaskDueDateUpdatedEvent(payload: dict) -> flask.Response:
    return make_response(jsonify({'message': 'Task Deletion Operation not yet implemented'}), 202)
