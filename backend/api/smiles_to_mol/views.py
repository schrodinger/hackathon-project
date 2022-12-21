from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from api.smiles_to_mol.serializers import SmilesToMolSerializer

from science.science.rdkit_endpoints import smiles_to_mol


class SmilesToMol(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = SmilesToMolSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        mol = smiles_to_mol(smiles=serializer.validated_data["smiles"], title=serializer.validated_data["title"])
        response = {"mol": mol}
        return Response(response)
