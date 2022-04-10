import requests
from ClickUp.API.APIHelper import withAuth


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


def createTaskComment(taskId: str, comment: str) -> dict:
    if taskId is None or comment is None:
        return {}
    try:
        r = requests.post(f'https://api.clickup.com/api/v2/task/{taskId}/comment/', headers=withAuth({}), json={'comment_text': comment})
        taskComment = r.json()
    finally:
        pass
    return taskComment


if __name__ == '__main__':
    print(createTaskComment('2ba3bp8', 'test'))
