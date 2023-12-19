import json
import boto3
from time import time

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))

    # use boto3 to create personalize schema
    name = f"ryan-schema-{int(time())}"
    personalize = boto3.client('personalize')
    response = personalize.create_schema(
        name = name,
        schema = json.dumps(event)['dataSchema']
    )
    schema_arn = response['schemaArn']
    
    print(response)
    print(schema_arn)
    
    return {"schemaArn": schema_arn}