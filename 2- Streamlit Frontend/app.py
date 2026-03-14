import streamlit as st
import json
import requests
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import Credentials
import asyncio 
import os

def call_api(prompt):
    api_url = "api gateway link"
    region = "us-east-1"
    service = "execute-api"

    # Retrieve AWS credentials from environment variables
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    if not aws_access_key_id or not aws_secret_access_key:
        return "Error: AWS credentials not found. Please check"

    headers = {
        "Content-Type": "application/json"
    }
    
    data = json.dumps({"user_prompt": prompt})

    credentials = Credentials(aws_access_key_id, aws_secret_access_key)
    request = AWSRequest(method="POST", url=api_url, data=data, headers=headers)
    SigV4Auth(credentials, service, region).add_auth(request)
    prepared_headers = dict(request.headers.items())

    try:
        response = requests.post(api_url, headers=prepared_headers, data=data)
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get('body', 'No body found')
        else:
            return f"Error: Received status code {response.status_code} with message: {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

def format_response(response):
    response = response.replace("\\n", "\n").replace('"', '')
    return response

async def send_message_async(message):
    greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
    if any(greet in message.lower() for greet in greetings):
        return "Hello!. How can I assist you today?"

    response = call_api(message)
    
    if isinstance(response, str) and response.startswith("Error:"):
        st.error(response)
        return "I'm sorry, I'm having trouble generating a response."
    
    formatted_response = format_response(response)
    return formatted_response

st.markdown("""
    <h1 style='text-align: center;'>
        ⚡ Al SalesGrid ⚡
    </h1>
    <p style='text-align: center;'>
        Your AI Assistant for Sales Team 🤖
    </p>
    """, unsafe_allow_html=True)

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is your question?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.spinner("Thinking..."):
        response = asyncio.run(send_message_async(prompt))
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()