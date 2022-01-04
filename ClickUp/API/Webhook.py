import pandas
import requests
from configs.clickUp import CLICKUP_TEAM_ID
from APIHelper import withAuth


def getWebhookSecret(webhookId: str) -> str:
    webhooks = pandas.read_csv('../../logs/Webhooks.csv')
    if webhookId in webhooks['webhook_id']:
        return webhooks[webhooks['webhook_id'] == webhookId]['secret']
    else:
        try:

            r = requests.get(f'https://api.clickup.com/api/v2/team/{CLICKUP_TEAM_ID}/webhook',headers=withAuth({}))
            data = r.json()
            print(data)
            for webhook in data['webhooks']:
                if webhook['id'] == webhookId:
                    with open('../../logs/Webhooks.csv', 'a') as file:
                        file.write(f'{webhook["id"]},{webhook["endpoint"]},{webhook["secret"]}')
                        file.write('\n')
                    return webhook['secret']
                else:
                    return ''
        except requests.exceptions.RequestException as e:
            raise e


if __name__ == '__main__':
    print(getWebhookSecret("c34a1ae9-6c9b-4f77-9ce2-b0746a0fc1ee"))