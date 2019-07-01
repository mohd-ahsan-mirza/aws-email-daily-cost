import json
import boto3
import datetime
def lambda_handler(event, context):
    client = boto3.client('ce')
    #To manually test for any months. Just change the dates at the bottom
    #query_date = datetime.datetime(2019, 6, 30)
    query_date = datetime.date.today()
    query_date_year = str(query_date.year)
    query_date_month = query_date.strftime('%m')
    query_date_current_day = query_date.strftime('%d')
    #Setting to future date because this function errors out when the start and end dates are same
    if query_date_current_day == '01':
        query_date_current_day = '02'
    response = client.get_cost_and_usage(
    TimePeriod={
        'Start': query_date_year + '-' + query_date_month + '-' + '01',
        'End': query_date_year + '-' + query_date_month + '-' + query_date_current_day
    },
    Granularity='MONTHLY',
    Metrics=['AmortizedCost']
    )
    cost_details = response['ResultsByTime'][0]['Total']['AmortizedCost']
    cost = cost_details['Amount'] + cost_details['Unit']
    return cost_details
