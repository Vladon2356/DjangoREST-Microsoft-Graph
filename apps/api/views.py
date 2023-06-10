from decouple import config
from msal import ConfidentialClientApplication
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api import serializers

app_id = config("MICROSOFT_AUTH_CLIENT_ID")
client_secret = config("MICROSOFT_AUTH_CLIENT_SECRET")
tenant = config("MICROSOFT_TENANT_ID")
SCOPES = ['User.Read']
client = ConfidentialClientApplication(client_id=app_id, client_credential=client_secret)


class GetAuthURL(APIView):
    serializer_class = serializers.GetAuthURLSerializer

    def get(self, request):
        auth_url = client.get_authorization_request_url(SCOPES)
        return Response({'auth_url': auth_url})

class GetAccessTockenAPIView(APIView):
    serializer_class = serializers.GetAccessTockenSerializer

    def post(self, request):
        code = request.data.get('code')
        access_token = client.acquire_token_by_authorization_code(code, SCOPES)
        return Response({'access_token': access_token})