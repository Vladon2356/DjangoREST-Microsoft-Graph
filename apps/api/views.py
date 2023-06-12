from decouple import config
from msal import ConfidentialClientApplication
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api import serializers
from apps.api.services import send_email, msgraph_request

app_id = config("MICROSOFT_AUTH_CLIENT_ID")
client_secret = config("MICROSOFT_AUTH_CLIENT_SECRET")
tenant = config("MICROSOFT_TENANT_ID")
GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0'
SCOPES = [
    'User.Read',
    'Mail.Send',
    'Mail.ReadWrite',
    'User.Read.All',
    'User.ReadWrite',
    'User.ReadWrite.All',
    'Application.Read.All',
    'Application.ReadWrite.All',
    'APIConnectors.Read.All',
    'APIConnectors.ReadWrite.All',
    'Tasks.Read',
    'Tasks.ReadWrite',
]
client = ConfidentialClientApplication(client_id=app_id, client_credential=client_secret)


class GetAuthURL(APIView):

    def get(self, request):
        auth_url = client.get_authorization_request_url(SCOPES)
        return Response({'auth_url': auth_url})

class GetAccessTockenAPIView(APIView):

    def get(self, request):
        code = self.request.query_params.get('code')
        print(code)
        access_token = client.acquire_token_by_authorization_code(code, SCOPES)
        return Response({'access_token': access_token})

class SendEmaiAPIView(APIView):

    def post(self, request):
        access_token = request.headers.get('Authorization')
        response = send_email(access_token, request.data)
        return Response(response.status_code)

class GetMeEndpoint(APIView):

    def get(self, request):
        access_token = request.headers.get('Authorization')
        endpoint = GRAPH_ENDPOINT + '/me'
        response = msgraph_request(endpoint, {'Authorization': access_token})
        return Response(response)

class GetGraphEndpointAPIView(APIView):
    endpoint = None
    def get(self, request):
        access_token = request.headers.get('Authorization')
        print(self.endpoint)
        response = msgraph_request(GRAPH_ENDPOINT + self.endpoint, {'Authorization': access_token})
        return Response(response)

# def get_graph_endpoint(request, endpoint: str):
#     access_token = request.headers.get('Authorization')
#     response = msgraph_request(endpoint, {'Authorization': access_token})
#     return Response(response)
