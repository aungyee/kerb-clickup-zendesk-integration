from datetime import datetime
from configs.clickUp import LIST_ID, TECH_SUPPORT_CUSTOM_FIELDS


def createPayloadFromTask(taskDetail, group):

    if int(taskDetail['list']['id']) == LIST_ID['CUSTOMER_SUPPORT_TECHNICAL']:

        requestor = None
        requestorName = None
        urgency = None
        category = None
        subcategory = None
        bookingDate = None
        bookingType = None

        for field in taskDetail['custom_fields']:
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['BOOKING_TYPES']['id'] and 'value' in field:
                bookingType = TECH_SUPPORT_CUSTOM_FIELDS['BOOKING_TYPES']['values'][field['value']]
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['DATE_BOOKED']['id'] and 'value' in field:
                bookingDate = datetime.utcfromtimestamp(int(field['value'])/1000).strftime('%d %B, %Y')
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['USER_EMAIL']['id'] and 'value' in field:
                requestor = field['value']
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['SUPPORT_CATEGORY']['id'] and 'value' in field:
                category = TECH_SUPPORT_CUSTOM_FIELDS['SUPPORT_CATEGORY']['values'][field['value']]
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['SUPPORT_SUB_CATEGORY']['id'] and 'value' in field:
                subcategory = TECH_SUPPORT_CUSTOM_FIELDS['SUPPORT_SUB_CATEGORY']['values'][field['value']]
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['URGENCY']['id'] and 'value' in field:
                urgency = TECH_SUPPORT_CUSTOM_FIELDS['URGENCY']['values'][field['value']]
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['USER_NAME']['id'] and 'value' in field:
                requestorName = field['value']

        payload = {
            'ticket': {
                'comment': {
                    'body': f"""
                        {taskDetail['creator']['username']} has requested a technical support task for {requestorName} in in ClickUp.
                        Check it out at: {taskDetail['url']}

                        Description:
                        {taskDetail['description']}
                        
                        Details:
                        Urgency     : {urgency if urgency is not None else 'Nil'}
                        Name        : {requestorName if requestorName is not None else 'Nil'}
                        Requester   : {requestor if requestor is not None else 'Nil'}
                        Booking Date: {bookingDate if bookingDate is not None else 'Nil'}
                        Booking Type: {bookingType if bookingType is not None else 'Nil'}
                        Category    : {category if category is not None else 'Nil'}
                        Subcategory : {subcategory if subcategory is not None else 'Nil'}
                        
                        """,
                    'public': False
                },
                'group_id': group,
                'subject': taskDetail['name'],
                'description': taskDetail['description'],
                'priority': taskDetail['priority']['priority'] if taskDetail['priority'] is not None else None,
                "requester": {'email': requestor if requestor is not None else taskDetail['creator']['email'],
                              'name': requestorName if requestorName is not None else f"New Zendesk Customer<{taskDetail['creator']['email']}>"}
            }
        }

        return payload

    return None
