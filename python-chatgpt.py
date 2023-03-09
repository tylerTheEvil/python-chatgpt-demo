import requests
import json
import argparse
import os

api_endpoint = "https://api.openai.com/v1/completions"
api_secret_key = os.getenv("OPENAI_API_KEY")

request_headers={
    "Authorization": "Bearer " + api_secret_key,
    "Content-Type": "application/json"
}

parser = argparser = argparse.ArgumentParser()
parser.add_argument("prompt", help="prompt for the chatgpt model")
parser.add_argument("file_name", help="prompt for the output file name")
args = parser.parse_args()

request_body = {
    "model": "text-davinci-003",
    "prompt": f"write python script to {args.prompt}",
    "max_tokens": 100,
    "temperature": 0.9,
}

response = requests.post(api_endpoint, headers=request_headers, json=request_body)

if response.status_code == 200:
  response_text = response.json()['choices'][0]['text']
  with open(args.file_name, 'w') as f:
    f.write(response_text)
else:
  print(f"Error: {str(response.status_code)}, {response.text}") 
