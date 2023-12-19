import json
import boto3
from time import time

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))
    eventBody = json.dumps(event['body'])
    
    # use boto3 to create personalize createdataset
    # import data from s3
    # name = f"ryan-dataset-{int(time())}"
    # personalize = boto3.client('personalize')
    # response = personalize.create_dataset(
    #     name = name,
    #     schemaArn = eventBody['schemaArn'],
    #     datasetGroupArn = eventBody['datasetGroupArn'],
    #     datasetType = 'dataset_type', # note: dataset_type, default is USER_RETURNS_DATASET, USER_INTERACTIONS_DATASET, or ITEM_METADATA_DATASET.
    #     dataConfig = {
    #         's3DataSource': {
    #             'path': 's3://bucket/path',
    #             'ingestionMode': 'ALL' # note: ALL or INCLUDE_ONLY, default is INCLUDE_ONLY
    #         }
    #     },
    # )
    # dataset_arn = response['datasetArn']
    dataset_arn = "DATASETARN"
    
    # print(response)
    print(dataset_arn)

    return {"datasetArn": dataset_arn}