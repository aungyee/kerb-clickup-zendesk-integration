import json
import requests
from pathlib import Path
from configs.zendesk import username, password, baseURL
from Zendesk.Helper import createPayloadFromTask


def createTicketFromTask(taskDetail: dict, group: int) -> dict:
    header = {'content-type': 'application/json'}
    payload = createPayloadFromTask(taskDetail, group)
    print(payload)
    try:
        r = requests.post(baseURL + '/api/v2/tickets', auth=(username, password), headers=header,
                          data=json.dumps(payload))
        newTicket = r.json()
        print(newTicket)
        fn = Path(__file__).parents[3] / 'logs' / 'TasksTickets.csv'
        with open(fn, 'a') as file:
            file.write(f"{taskDetail['id']},{taskDetail['parent']},{newTicket['ticket']['id']}")
            file.write('\n')
        return newTicket
    except Exception as e:
        raise e


def getTicket():
    pass


if __name__ == '__main__':
    task = {'id': '1u08tjd', 'custom_id': None, 'name': 'testing 21', 'text_content': 'testing 21 description',
            'description': 'testing 21 description',
            'status': {'id': 'sc152445941_qB6p889i', 'status': 'Open', 'color': '#f9d900', 'orderindex': 0,
                       'type': 'open'}, 'orderindex': '4012918.00000000000000000000000000000000',
            'date_created': '1641730509246', 'date_updated': '1641730509506', 'date_closed': None, 'archived': False,
            'creator': {'id': 48625512, 'username': 'Aung Yee', 'color': '#d60800', 'email': 'aung.yee@kerb.works',
                        'profilePicture': None}, 'assignees': [], 'watchers': [
            {'id': 48625512, 'username': 'Aung Yee', 'color': '#d60800', 'initials': 'AY',
             'email': 'aung.yee@kerb.works', 'profilePicture': None}], 'checklists': [], 'tags': [], 'parent': None,
            'priority': None, 'due_date': None, 'start_date': None, 'points': None, 'time_estimate': None,
            'time_spent': 0, 'custom_fields': [
            {'id': '22aa4fd1-e9e5-49ba-9f51-56890c06ba86', 'name': 'Booking Type', 'type': 'drop_down',
             'type_config': {'default': 0, 'placeholder': None, 'options': [
                 {'id': '186280f5-93b8-429a-a07a-06723cdbc6d6', 'name': 'Hourly', 'color': None, 'orderindex': 0},
                 {'id': '4f6f1a24-2744-43f2-a093-d5aa6a610229', 'name': 'Daily', 'color': None, 'orderindex': 1},
                 {'id': '06ecf377-2577-44f5-a65b-b9c9b65f16c7', 'name': 'Subscription', 'color': None, 'orderindex': 2},
                 {'id': 'b249454a-f496-44c1-9636-b7898e130c56', 'name': 'N/A', 'color': None, 'orderindex': 3}]},
             'date_created': '1641209755075', 'hide_from_guests': False, 'value': 1, 'required': False},
            {'id': '4cf435c7-590f-4233-ae4c-cc5c5c609fd5', 'name': 'Date Booked', 'type': 'date', 'type_config': {},
             'date_created': '1641209718929', 'hide_from_guests': False, 'value': '1641787200000', 'required': False},
            {'id': 'ea2bf17a-8e06-49ef-a9c7-bef77ca53218', 'name': 'Space ID', 'type': 'short_text', 'type_config': {},
             'date_created': '1641209709476', 'hide_from_guests': False, 'value': '2203', 'required': False},
            {'id': 'cba037c0-056c-4483-8013-c2a1607a54eb', 'name': 'Support Category', 'type': 'drop_down',
             'type_config': {'default': 0, 'placeholder': None, 'options': [
                 {'id': '38c3d076-5003-4e57-9d2c-72f4c655e196', 'name': 'Space Owner', 'color': None, 'orderindex': 0},
                 {'id': '1e3dd2dc-d96e-4f01-9e82-904cd2c510d1', 'name': 'Driver', 'color': None, 'orderindex': 1},
                 {'id': '65d77c4e-6034-4200-8358-a4cc2b15e811', 'name': 'Guest User', 'color': None, 'orderindex': 2}]},
             'date_created': '1641209506169', 'hide_from_guests': False, 'value': 1, 'required': False},
            {'id': 'b53528e6-798c-4ae1-be6a-d8d53fb8dff4', 'name': 'Support Sub Category', 'type': 'drop_down',
             'type_config': {'default': 0, 'placeholder': None, 'options': [
                 {'id': '12bd3d3b-57eb-437e-a550-01ea0b76c96d', 'name': 'App Problem', 'color': None, 'orderindex': 0},
                 {'id': 'd35712de-037e-475c-bcfb-1f6d54589e79', 'name': 'Website Problem', 'color': None,
                  'orderindex': 1},
                 {'id': '6d0ec288-bce4-490e-aebc-b48afe33c820', 'name': 'Gate Problem', 'color': None, 'orderindex': 2},
                 {'id': '64237356-f557-4072-9ff6-40fbbb9fe986', 'name': 'Payment Problem', 'color': None,
                  'orderindex': 3},
                 {'id': '070fb498-4ea5-4a1a-a1c9-439e95be03ab', 'name': 'OTP', 'color': None, 'orderindex': 4},
                 {'id': '6f43fab0-6671-4e27-a3ea-ad7c28ebf264', 'name': 'Refund', 'color': None, 'orderindex': 5},
                 {'id': '55b85e36-e6aa-45c8-bc0a-d9f8486eeb25', 'name': 'Email Address Change', 'color': None,
                  'orderindex': 6},
                 {'id': 'd1581570-26f4-4044-a0a4-75d97e1262ae', 'name': 'Duplicate Charges', 'color': None,
                  'orderindex': 7},
                 {'id': '940a81f2-d33b-4f95-98f3-7aec5ab1f742', 'name': 'Discount', 'color': None, 'orderindex': 8},
                 {'id': 'd67190f6-e769-4710-8784-1333493813e7', 'name': 'Invoice', 'color': None, 'orderindex': 9},
                 {'id': '87ededf8-2e70-49bb-9b7c-1af647452e1c', 'name': 'Parking Invitation', 'color': None,
                  'orderindex': 10},
                 {'id': '025ac5a8-9e7b-4083-ba7b-80d3eaacbe11', 'name': 'Something Else', 'color': None,
                  'orderindex': 11}]}, 'date_created': '1641209603470', 'hide_from_guests': False, 'value': 0,
             'required': False}, {'id': 'f0cfd09d-c589-4c88-9f39-ab2883659823', 'name': 'Urgency', 'type': 'drop_down',
                                  'type_config': {'default': 0, 'placeholder': None, 'new_drop_down': True, 'options': [
                                      {'id': '86279321-368e-4589-a6c3-48ba8b93eb9a', 'name': 'Right Now',
                                       'color': '#e50000', 'orderindex': 0},
                                      {'id': 'a33e8e35-9dec-438a-a2ea-89d74202edda', 'name': 'Today',
                                       'color': '#f9d900', 'orderindex': 1},
                                      {'id': '6a86c683-a505-4c44-9d30-edecdad469fc', 'name': 'Not Urgent',
                                       'color': '#04A9F4', 'orderindex': 2}]}, 'date_created': '1641209463805',
                                  'hide_from_guests': False, 'value': 0, 'required': False},
            {'id': 'ddc58de0-4652-47f5-ab4a-7e0d3800d2b7', 'name': 'User Email', 'type': 'email', 'type_config': {},
             'date_created': '1641209639283', 'hide_from_guests': False, 'value': 'aung.yee@kerb.works',
             'required': False}], 'dependencies': [], 'linked_tasks': [], 'team_id': '20439320',
            'url': 'https://app.clickup.com/t/1u08tjd', 'permission_level': 'create',
            'list': {'id': '152445941', 'name': 'Customer Support - Technical', 'access': True},
            'project': {'id': '86436533', 'name': 'Customer Support', 'hidden': False, 'access': True},
            'folder': {'id': '86436533', 'name': 'Customer Support', 'hidden': False, 'access': True},
            'space': {'id': '32593455'}, 'attachments': []}
    print(createTicketFromTask(task, 360009684396))
