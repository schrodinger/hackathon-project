from io import BytesIO
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
        smiles = serializer.validated_data["smiles"]
        title = serializer.validated_data["title"] if "title" in serializer.validated_data else None

        mol = smiles_to_mol(smiles=smiles, title=title)
        print("getting images")
        print(mol)
        print(BytesIO(mol))
        response = {"mol": BytesIO(mol)}
        return Response(response)
