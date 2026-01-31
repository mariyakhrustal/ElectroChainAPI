from rest_framework.serializers import ModelSerializer

from networks.models import Contact, Network, Product


class NetworkSerializer(ModelSerializer):
    class Meta:
        model = Network
        fields = "__all__"
        read_only_fields = (
            "debt",
            "level",
            "created_at",
        )


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
