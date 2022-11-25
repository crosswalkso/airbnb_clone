import requests
from django.conf import settings
from rest_framework.views import APIView

class GetUploadURL(APIView):
    def post(self, request):
        url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v2/direct_upload"
        one_time_url = requests.post(
            url, headers={"Authorization": f"Bearer {settings.CF_TOKEN}"}
        )
        one_time_url = one_time_url.json() 
        result = one_time_url.get("result")
        return Response({"uploadURL": result.get("uploadURL")})