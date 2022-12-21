from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from api.image.serializers import ImageGenerationSerializer
from science.science.rdkit_endpoints import generate_image


class GenerateImage(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ImageGenerationSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        encoded_image = generate_image(mol=serializer.validated_data["mol"], width=serializer.validated_data["width"], height=serializer.validated_data["height"])
        response = {"image": encoded_image}
        return Response(response)
