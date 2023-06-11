import os
import base64
import requests

from core.settings import PROJECT_PATH

GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0'


def draft_attachment(file_path):
    abs_path = PROJECT_PATH + file_path
    if not os.path.exists(abs_path):
        raise Exception("File path not found")

    with open(abs_path, 'rb') as upload:
        media_content = base64.b64encode(upload.read())

    data_body = {
        '@odata.type': '#microsoft.graph.fileAttachment',
        'contentBytes': media_content.decode('utf-8'),
        'name': os.path.basename(file_path)
    }
    return data_body


def send_email(access_token, data):
    request_body = {
        "message": {
            "subject": "From django 2",
            "body": {
                "contentType": "Text",
                "content": "The new cafeteria is open."
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": "kngf4427@gmail.com"
                    }
                }
            ]
        }
    }
    endpoint = GRAPH_ENDPOINT + '/me/sendMail'
    response = requests.post(url=endpoint, json=request_body, headers={'Authorization': access_token})
    return response


def get_me(access_token):
    endpoint = GRAPH_ENDPOINT + '/me'
    response = requests.get(url=endpoint, headers={'Authorization': access_token})
    return response
