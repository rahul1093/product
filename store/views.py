
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from store.models import *
from store.serializers import *


# Create your views here.
class ProductOp(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer