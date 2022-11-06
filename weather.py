import boto3
import random
import datetime
from boto3.dynamodb.conditions import Key

ts = datetime.datetime.now()
Timestamp = int(ts.timestamp() * 1000)


dynamoDb = boto3.resource('dynamodb')

tables = dynamoDb.tables.all()


def GenerateTemp():
    tabled = dynamoDb.Table('Puck_Figs')
    tabled.put_item(
    Item={
        'zipcode': '20166',
        'Humidity': '56',
        'Temperature': '74',
        'Timestamp': Timestamp,        
    })

GenerateTemp()

