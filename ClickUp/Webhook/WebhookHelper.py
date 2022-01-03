import hmac
import json
import pandas
import hashlib
import requests
from configs.clickUp import CLICKUP_TEAM_ID


def verifiedWebhookRequest(data: bytes, signature: str) -> bool:
    try:
        webhookSecret = getWebhookSecret(json.loads(data)['webhook_id'])
        secret = bytes(webhookSecret, 'utf-8')
        hmac_hash = hmac.new(secret, data, hashlib.sha256)
        return hmac_hash.hexdigest() == signature
    except requests.exceptions.RequestException as e:
        raise e


def getWebhookSecret(webhookId: str) -> str:
    webhooks = pandas.read_csv('logs/Webhooks.csv')
    if webhookId in webhooks['webhook_id']:
        return webhooks[webhooks['webhook_id'] == webhookId]['secret']
    else:
        try:
            r = requests.get(f'https://api.clickup.com/api/v2/{CLICKUP_TEAM_ID}/webhook')
            data = r.json()
            for webhook in data['webhooks']:
                if webhook['id'] == webhookId:
                    with open('../../logs/Webhooks.csv', 'a') as file:
                        file.write(f'{webhook["webhook_id"]},{webhook["endpoint"]},{webhook["secret"]}')
                        file.write('\n')
                    return webhook['secret']
                else:
                    return ''
        except requests.exceptions.RequestException as e:
            raise e


