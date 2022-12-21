from rest_framework.serializers import CharField, Serializer


class SmilesToMolSerializer(Serializer):
    smiles = CharField(required=True, trim_whitespace=False)
    title = CharField(required=False, trim_whitespace=False)
