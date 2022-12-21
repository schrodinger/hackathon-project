from rest_framework.serializers import CharField, IntegerField, Serializer


class ImageGenerationSerializer(Serializer):
    mol = CharField(required=True, trim_whitespace=False)
    width = IntegerField(required=False)
    width = IntegerField(required=False)
