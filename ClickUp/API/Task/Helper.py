import pandas


def checkIfTaskExistsInZendesk(taskId: str) -> bool:
    existingTasks = pandas.read_csv('../../logs/TicketsTask.csv')
    return taskId in existingTasks['task_id']


def handleHistoryItems(historyItems: list) -> None:
    for item in historyItems:
        print(item)
