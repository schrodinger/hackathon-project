from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from api.image.serializers import ImageGenerationSerializer
from science.science.rdkit_endpoints import generate_image, json_to_mol


class GenerateImage(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ImageGenerationSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        json_mol = serializer.validated_data["mol"]
        print("json mol")
        print(json_mol)
        mol = json_to_mol(json_mol)
        print("printing mol")
        print(mol)
        width = serializer.validated_data["width"] if "width" in serializer.validated_data else 400
        height = serializer.validated_data["height"] if "height" in serializer.validated_data else 400
        encoded_image = generate_image(mol=mol, height= height, width=width )
        response = {"image": encoded_image}
        return Response(response)
