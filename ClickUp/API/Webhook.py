import pandas
import requests
from pathlib import Path
from configs.clickUp import CLICKUP_TEAM_ID
from ClickUp.API.APIHelper import withAuth


def getWebhookSecret(webhookId: str) -> str:
    fn = Path(__file__).parents[2]/'logs'/'Webhooks.csv'
    webhooks = pandas.read_csv(fn)
    if webhookId in webhooks['webhook_id'].values:
        return webhooks[webhooks['webhook_id'] == webhookId]['secret'].values[0]

    try:
        r = requests.get(f'https://api.clickup.com/api/v2/team/{CLICKUP_TEAM_ID}/webhook',headers=withAuth({}))
        data = r.json()
        for webhook in data['webhooks']:
            if webhook['id'] == webhookId:
                with open(fn, 'a') as file:
                    file.write(f'{webhook["id"]},{webhook["endpoint"]},{webhook["secret"]}')
                    file.write('\n')
                return webhook['secret']

        return ''
    except requests.exceptions.RequestException as e:
        raise e


if __name__ == '__main__':
    print(getWebhookSecret("c34a1ae9-6c9b-4f77-9ce2-b0746a0fc1ee"))