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
        # fn = Path(__file__).parents[3] / 'logs' / 'TasksTickets.csv'
        # with open(fn, 'a') as file:
        #     file.write(f"{taskDetail['id']},{taskDetail['parent']},{newTicket['ticket']['id']}")
        #     file.write('\n')
        return newTicket
    except Exception as e:
        raise e


def createTicketComment(comment, ticket_id):
    pass


if __name__ == '__main__':
    pass
