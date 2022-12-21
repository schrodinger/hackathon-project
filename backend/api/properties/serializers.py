from rest_framework.serializers import CharField, ListField, Serializer


class PropertiesSerializer(Serializer):
    #TODO manaf, update this once I know what products are and have wifi
    products = CharField(required=True, trim_whitespace=False)
    rgroup_mols = ListField(child=CharField(required=True, trim_whitespace=False), required=True)
