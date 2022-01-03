import requests
from configs.clickUp import CLICKUP_API_KEY


def withAuth(headers):
    headers['Authorization'] = CLICKUP_API_KEY
    return headers


def getTask(taskId: str) -> dict:
    if taskId is None:
        return {}
    try:
        task = requests.get(f'https://api.clickup.com/api/v2/task/{taskId}', headers=withAuth({})).json()
        return task
    except requests.exceptions as e:
        raise e


def getTaskComments(taskId: str) -> dict:
    if taskId is None:
        return {}
    try:
        r = requests.get(f'https://api.clickup.com/api/v2/task/{taskId}/comment/', headers=withAuth({}))
        taskComments = r.json()
    finally:
        pass
    return taskComments


if __name__ == '__main__':
    print(getTaskComments('1tryb69'))
