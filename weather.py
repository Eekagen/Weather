import boto3
import random
import datetime
from boto3.dynamodb.conditions import Key

class Weather:
    zip = 1
    humidity = 1
    temperature = 1

    def __init__(self, zip, humidity, temperature):
        self.zip = zip
        self.humidity = humidity
        self.temperature = temperature

dynamoDb = boto3.resource('dynamodb')

tables = dynamoDb.tables.all()

def GenerateTemp(weather):
    ts = datetime.datetime.now()
    timestamp = int(ts.timestamp() * 1000)
    tabled = dynamoDb.Table('Puck_Figs')
    tabled.put_item(
    Item={
        'zipcode': str(weather.zip),
        'Humidity': weather.humidity,
        'Temperature': weather.temperature,
        'Timestamp': timestamp,        
    })

def Florida():
    genhumid = random.randint(44, 99)
    gentemp = random.randint(30, 94)
    return Weather(33765, genhumid, gentemp)

def Virginia():
    genhumid = random.randint(44, 99)
    gentemp = random.randint(30, 94)
    return Weather(20166, genhumid, gentemp)

GenerateTemp(Virginia())
GenerateTemp(Florida())