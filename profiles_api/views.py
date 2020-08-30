from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Retruns a list of APIView features"""
        an_apiview = [
          'Uses HTTP methods as function (get, post, patch, put, delete)',
          'Is similar to a traditioanl Django View',
          'Gives you the most control over you application logic',
          'Is mapped manuallly to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})