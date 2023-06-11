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
        'message': {
            'toRecipients': [{
                'emailAddress': {
                    'address': 'vladyslav.onishchuk.kmn.2020@lpnu.ua'
                }
            }]
        },
        'subject': 'Test Email From API',
        'importance': 'normal',
        'body': {
            'contentType': 'HTML',
            'content': 'This is a test email sent from <b>Python</b> API',
        },
        'attachments': [
            draft_attachment('/requirements.txt'),
        ]
    }
    endpoint = GRAPH_ENDPOINT + '/me/sendMail'
    response = requests.post(url=endpoint, json=request_body, headers={'Authorization': access_token})
    print('Response reason', response.reason)
    return response
