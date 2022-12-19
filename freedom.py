from rest_framework.response import Response
from rest_framework.views import APIView


class SuccessUrl(APIView):
    def get(self, request):
        print(request)
        return Response('success')
