import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def generate_response(query, context, chat_summary):
    prompt = f'''
You are a calm, professional, and non-prescriptive virtual healthcare assistant. 
You respond clearly and concisely to symptom-related queries based on factual context provided. 
Avoid small talk or greetings like "Hi there" or "You're welcome." 
Only use information from the provided context and maintain a serious, informative tone.

Conversation Summary:
{chat_summary}

Medical Context:
{context}

User: {query}
Assistant:'''

    body = {
        "prompt": prompt.strip(),
        "temperature": 0.5,
        "top_p": 0.85,
        "max_gen_len": 350
    }

    response = bedrock.invoke_model(
        modelId="meta.llama3-8b-instruct-v1:0",
        body=json.dumps(body).encode("utf-8"),
        contentType="application/json",
        accept="application/json"
    )
    result = json.loads(response['body'].read())
    return result['generation']
