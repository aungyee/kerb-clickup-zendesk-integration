import json
import requests
from configs.zendesk import username, password, baseURL
from Zendesk.Helper import createPayloadFromTask


def createTicketFromTask(taskDetail: dict, group: int) -> dict:

    header = {'content-type': 'application/json'}
    payload = createPayloadFromTask(taskDetail, group)
    try:
        r = requests.post(baseURL + '/api/v2/tickets', auth=(username, password), headers=header,
                          data=json.dumps(payload))
        newTicket = r.json()
        with open('../../../logs/TasksTickets.csv', 'a') as file:
            file.write(f"{taskDetail['id']},{newTicket['ticket']['id']}")
            file.write('\n')
        return newTicket
    except requests.exceptions as e:
        raise e


def getTicket():
    pass


if __name__ == '__main__':
    task = {
        "id": "9hx",
        "custom_id": None,
        "name": "Updated Task Name",
        "text_content": "New Task Description",
        "description": "New Task Description",
        "status": {
            "status": "in progress",
            "color": "#d3d3d3",
            "orderindex": 1,
            "type": "custom"
        },
        "orderindex": "1.00000000000000000000000000000000",
        "date_created": "1567780450202",
        "date_updated": "1567780450202",
        "date_closed": None,
        "creator": {
            "id": 183,
            "username": "Aung yee",
            "email": "aung.yee@kerb.works",
            "color": "#827718",
            "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
        },
        "assignees": [],
        "checklists": [],
        "tags": [],
        "parent": None,
        "priority": None,
        "due_date": None,
        "start_date": None,
        "time_estimate": None,
        "time_spent": None,
        "custom_fields": [
            {
                "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
                "name": "My Number field",
                "type": "checkbox",
                "type_config": {},
                "date_created": "1622176979540",
                "hide_from_guests": False,
                "value": "23",
                "required": True
            },
            {
                "id": "03efda77-c7a0-42d3-8afd-fd546353c2f5",
                "name": "My Text field",
                "type": "short_text",
                "type_config": {},
                "date_created": "1622176979540",
                "hide_from_guests": False,
                "value": "Text field input",
                "required": False
            },
            {
                "id": "f4d2a20d-6759-4420-b853-222dbe2589d5",
                "name": "My People",
                "type": "users",
                "type_config": {
                    "include_guests": False,
                    "include_team_members": False
                },
                "date_created": "1618440378816",
                "hide_from_guests": False,
                "required": False
            }
        ],
        "list": {
            "id": "123"
        },
        "folder": {
            "id": "456"
        },
        "space": {
            "id": "789"
        },
        "url": "https://app.clickup.com/t/9hx"
    }
    print(createTicketFromTask(task, 360009684396))
