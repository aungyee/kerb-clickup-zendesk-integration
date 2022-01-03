import json
import flask
from ClickUp.Webhook import Webhook as CTaskWebhook
from ClickUp.Webhook import TechSupport as TechSupportWebhook
from ClickUp.Webhook.WebhookHelper import verifiedWebhookRequest
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handleHome():
    with open('logs/Logs.txt', 'a') as file:
        file.write(request.data.decode())
        file.write('\n')
    return make_response(jsonify({'message': 'success'}), 200)


@app.route('/clickup-comment', methods=['POST'])
def handleClickUpComment():
    payload = json.loads(request.data.decode())

    if payload['event'] == 'taskCommentPosted':
        pass
    if payload['event'] == 'taskCommentPosted':
        pass


@app.route('/clickup-task', methods=['POST'])
def handleClickUpTaskEvents() -> flask.Response:

    # ----- Check if request payload is valid ----- #
    if request.data:
        if verifiedWebhookRequest(request.data, request.headers.get('X-Signature')):
            payload = json.loads(request.data.decode())
        else:
            return make_response(jsonify({'message': 'Payload cannot be verified'}), 400)
    else:
        return make_response(jsonify({'message': 'No payload provided'}), 400)

    # ----- Check event types and handle them accordingly ----- #
    if payload['event'] == 'taskCreated':
        return CTaskWebhook.handleTaskCreatedEvent(payload)
    if payload['event'] == 'taskDeleted':
        return CTaskWebhook.handleTaskDeletedEvent(payload)
    if payload['event'] == 'taskUpdated':
        return CTaskWebhook.handleTaskUpdatedEvent(payload)
    if payload['event'] == 'taskStatusUpdated':
        return CTaskWebhook.handleTaskStatusUpdatedEvent(payload)
    if payload['event'] == 'taskAssigneeUpdated':
        return CTaskWebhook.handleTaskAssigneeUpdatedEvent(payload)
    if payload['event'] == 'taskPriorityUpdated':
        return CTaskWebhook.handleTaskPriorityUpdatedEvent(payload)
    if payload['event'] == 'taskDueDateUpdated':
        return CTaskWebhook.handleTaskDueDateUpdatedEvent(payload)

    return make_response({'message': f'event type: {payload["event"]} not yet implemented'}, 202)


@app.route('/tech-support-task', methods = ['POST'])
def handleTechSupportTask():
    # ----- Check if request payload is valid ----- #
    if request.data:
        if verifiedWebhookRequest(request.data, request.headers.get('X-Signature')):
            payload = json.loads(request.data.decode())
        else:
            return make_response(jsonify({'message': 'Payload cannot be verified'}), 400)
    else:
        return make_response(jsonify({'message': 'No payload provided'}), 400)

    # ----- Check event types and handle them accordingly ----- #
    if payload['event'] == 'taskCreated':
        return TechSupportWebhook.handleTechSupportTaskCreatedEvent(payload)
    if payload['event'] == 'taskDeleted':
        return TechSupportWebhook.handleTaskDeletedEvent(payload)
    if payload['event'] == 'taskUpdated':
        return TechSupportWebhook.handleTaskUpdatedEvent(payload)
    if payload['event'] == 'taskStatusUpdated':
        return TechSupportWebhook.handleTaskStatusUpdatedEvent(payload)
    if payload['event'] == 'taskAssigneeUpdated':
        return TechSupportWebhook.handleTaskAssigneeUpdatedEvent(payload)
    if payload['event'] == 'taskPriorityUpdated':
        return TechSupportWebhook.handleTaskPriorityUpdatedEvent(payload)
    if payload['event'] == 'taskDueDateUpdated':
        return TechSupportWebhook.handleTaskDueDateUpdatedEvent(payload)

    return make_response({'message': f'event type: {payload["event"]} not yet implemented'}, 202)


@app.route('/zendesk-ticket', methods = ['POST'])
def handleZendeskTicket():
    return True


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
