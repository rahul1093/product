from rest_framework.serializers import ModelSerializer
from store.models import *


class ProductSer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
