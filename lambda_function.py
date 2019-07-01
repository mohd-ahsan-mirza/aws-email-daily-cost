import json
import boto3
import datetime
import os
def lambda_handler(event, context):
    cost_explorer = boto3.client('ce')
    ses = boto3.client("ses")
    charset = "UTF-8"
    destination_email = os.environ['destination_email']
    source_email = destination_email
    query_date = datetime.date.today()
    #To manually test for any months. Just change the dates at the bottom
    #query_date = datetime.datetime(2019, 6, 30)
    query_date_year = str(query_date.year)
    query_date_month = query_date.strftime('%m')
    query_date_current_day = query_date.strftime('%d')
    #Setting to future date because this function errors out when the start and end dates are same
    if query_date_current_day == '01':
        query_date_current_day = '02'
    start_date = query_date_year + '-' + query_date_month + '-' + '01'
    end_date = query_date_year + '-' + query_date_month + '-' + query_date_current_day
    response = cost_explorer.get_cost_and_usage(
    TimePeriod={
        'Start': start_date,
        'End': end_date
    },
    Granularity='MONTHLY',
    Metrics=['AmortizedCost']
    )
    cost_details = response['ResultsByTime'][0]['Total']['AmortizedCost']
    #return cost_details
    cost = "$" + cost_details['Amount'] + cost_details['Unit']
    subject = "AWS Cost Usage"
    message = "Usage period: " + start_date + " - " + end_date + "<br/>" + "Cost: " + cost
    ses.send_email(
        Destination={
            'BccAddresses': [
            ],
            'ToAddresses': [
                destination_email,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': charset,
                    'Data': '<html><head></head><body>'+message+'</body></html>',
                },
                'Text': {
                    'Charset': charset,
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': charset,
                'Data': subject,
            },
        },
        Source = source_email
    )
    
    
