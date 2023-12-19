import json
import boto3
from time import time

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))
    
    # use boto3 to create personalize datasetgroup
    name = f"ryan-datasetGroup-{int(time())}"
    personalize = boto3.client('personalize')
    response = personalize.create_dataset_group(name=name)
    dataset_group_arn = response['datasetGroupArn']
    
    print(response)
    print(dataset_group_arn)
    
    return {"datasetGroupArn": dataset_group_arn}