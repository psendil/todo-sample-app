# Import ToDo Class
from ToDoSampleApp import ToDo
import boto3
import json
dynamodb = boto3.client('dynamodb')

class Dynamo:
    def __init__(self, table_name, todo_item = None):
        self.table_name = table_name
        self.todo_item = todo_item

    def checkTable(self):
        try:
            check_table = dynamodb.describe_table(
                TableName=self.table_name)
            return True
        except:
            return False

    def createTable (self):
        try:
            table = dynamodb.create_table(
                AttributeDefinitions=[
                    {
                        'AttributeName': 'Title',
                        'AttributeType': 'S'
                    }
                ],
                TableName=self.table_name,
                KeySchema=[
                    {
                        'AttributeName': 'Title',
                        'KeyType': 'HASH'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
                )
            return (table)
        except Exception as err:
            print (err)

    def putItem(self):
        print ("Adding following new item to dynamoDB table")
        print (self.todo_item.title)
        item = {
            "Title": self.todo_item.title,
            "date": self.todo_item.date,
            "time": self.todo_item.time,
            "description": self.todo_item.description
        }
        item = json.dumps(item)
        putObject = dynamodb.put_item(
            TableName=self.table_name,
            Item=json.loads(item),
            ReturnValues='UPDATED_NEW',
            ReturnConsumedCapacity= 'TOTAL',
            ReturnItemCollectionMetrics='SIZE'
            )
        print("PutItem succeeded:")
        return (putObject)

    def getItem(table_name, primay_key):
        getObject = table.get_item(
            Key={
                'Title': primay_key
            }
            )
        return getObject
        
        
        
        
