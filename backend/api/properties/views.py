from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from api.properties.serializers import PropertiesSerializer

from science.science.rdkit_endpoints import get_QED_props


class Properties(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = PropertiesSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        products = get_QED_props(products=serializer.validated_data["products"])
        response = {"products": products}
        return Response(response)
