import hmac
import json
import hashlib
import requests

from ClickUp.API.Webhook import getWebhookSecret


def verifiedWebhookRequest(data: bytes, signature: str) -> bool:
    try:
        webhookSecret = getWebhookSecret(json.loads(data)['webhook_id'])
        secret = bytes(webhookSecret, 'utf-8')
        hmac_hash = hmac.new(secret, data, hashlib.sha256)
        return hmac_hash.hexdigest() == signature
    except requests.exceptions.RequestException as e:
        raise e