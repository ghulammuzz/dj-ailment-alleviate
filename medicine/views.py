from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, mixins
from rest_framework.response import Response
    
from .serializer import MedicineSerializer, PeracikDashboardSerializer
from .models import Medicine
from permission import PeracikPermission
    
class ListMedicine(generics.ListCreateAPIView, generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [PeracikPermission]
    search_files = ['name']
    
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class DashboardPeracik(generics.GenericAPIView):
    queryset = Medicine.objects.all()
    serializer_class = PeracikDashboardSerializer
    permission_classes = [PeracikPermission]
    
    def get(self, request):
        return Response(PeracikDashboardSerializer(request.user.peracik).data)
    
    