import boto3
import json
import numpy as np

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def get_titan_embedding(text):
    body = {
        "inputText": text
    }
    response = bedrock.invoke_model(
        modelId="amazon.titan-embed-text-v1",
        body=json.dumps(body).encode("utf-8"),
        contentType="application/json",
        accept="application/json"
    )
    result = json.loads(response['body'].read())
    return np.array(result['embedding'])
