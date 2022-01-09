import pandas
from pathlib import Path


def checkIfTaskExistsInZendesk(taskId: str) -> bool:
    fn = Path(__file__).parents[3]/'logs'/'TasksTickets.csv'
    existingTasks = pandas.read_csv(fn)
    return taskId in existingTasks['task_id'].values


def handleHistoryItems(historyItems: list) -> None:
    for item in historyItems:
        print(item)


if __name__ == '__main__':
    print(checkIfTaskExistsInZendesk('9hx'))
