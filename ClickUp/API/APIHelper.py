from configs.clickUp import CLICKUP_API_KEY

def withAuth(headers):
    headers['Authorization'] = CLICKUP_API_KEY
    return headers