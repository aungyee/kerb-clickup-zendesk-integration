from datetime import datetime
from configs.clickUp import LIST_ID, TECH_SUPPORT_CUSTOM_FIELDS


def createPayloadFromTask(taskDetail, group):

    if int(taskDetail['list']['id']) == LIST_ID['CUSTOMER_SUPPORT_TECHNICAL']:

        requestor = None
        urgency = None
        category = None
        subcategory = None
        bookingDate = None
        bookingType = None

        for field in taskDetail['custom_fields']:
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['BOOKING_TYPES']['id'] and field['value']:
                bookingType = TECH_SUPPORT_CUSTOM_FIELDS['BOOKING_TYPES']['values'][field['value']]
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['DATE_BOOKED']['id'] and field['value']:
                bookingDate = datetime.utcfromtimestamp(int(field['value'])/1000).strftime('%d %B, %Y')
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['USER_EMAIL']['id'] and field['value']:
                requestor = field['value']
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['SUPPORT_CATEGORY']['id'] and field['value']:
                category = TECH_SUPPORT_CUSTOM_FIELDS['SUPPORT_CATEGORY']['values'][field['value']]
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['SUPPORT_SUB_CATEGORY']['id'] and field['value']:
                subcategory = TECH_SUPPORT_CUSTOM_FIELDS['SUPPORT_SUB_CATEGORY']['values'][field['value']]
            if field['id'] == TECH_SUPPORT_CUSTOM_FIELDS['URGENCY']['id'] and field['value']:
                urgency = TECH_SUPPORT_CUSTOM_FIELDS['URGENCY']['values'][field['value']]

        payload = {
            'ticket': {
                'comment': {
                    'body': f"""
                        {taskDetail['creator']['username']} has requested a technical support task in in ClickUp.
                        Check it out at: {taskDetail['url']}

                        Description:
                        {taskDetail['description']}
                        
                        Details:
                        Urgency     : {urgency if urgency is not None else 'Nil'}
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
                "requester": {'email': requestor if requestor is not None else taskDetail['creator']['email']}
            }
        }

        return payload

    return None
