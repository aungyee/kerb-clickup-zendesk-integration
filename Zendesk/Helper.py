def createPayloadFromTask(taskDetail, group):
    payload = {
        'ticket': {
            'comment': {
                'body': f"""
                    {taskDetail['creator']['username']} has created a new task in Customer Success Space in ClickUp.
                    Check it out at: {taskDetail['url']}

                    Description:
                    {taskDetail['description']}
                    """,
                'public': False
            },
            'group_id': group,
            'subject': taskDetail['name'],
            'description': taskDetail['description'],
            'priority': 'high',
            "requester": {"name": taskDetail['creator']['username'], "email": taskDetail['creator']['email']}
        }
    }
    return payload
