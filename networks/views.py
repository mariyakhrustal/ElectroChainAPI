from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from networks.models import Contact, Network, Product
from networks.serializers import ContactSerializer, NetworkSerializer, ProductSerializer


class NetworkViewSet(ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()


class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailAPIView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()


class ContactUpdateAPIView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDestroyAPIView(DestroyAPIView):
    queryset = Contact.objects.all()
