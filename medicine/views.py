from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from accounts.models import Peracik

from accounts.serializer import PeracikSerializer
    
from .serializer import DashboardPeracikSerializer, MedicineSerializer
from .models import Medicine
from permission import PeracikPermission
    
class ListMedicine(generics.ListCreateAPIView, generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    # permission_classes = [PeracikPermission]
    search_fields = ['name', 'ingredients__name']
    
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class DashboardPeracik(generics.GenericAPIView):
    queryset = Peracik.objects.all()
    serializer_class = DashboardPeracikSerializer
    permission_classes = [PeracikPermission]
    
    def get(self, request):
        serializer = self.get_serializer(request.user.peracik)
        accepted_medication = Medicine.objects.filter(peracik=request.user.peracik, status='ACCEPTED')
        waiting_medication = Medicine.objects.filter(peracik=request.user.peracik, status='WAITING')
        canceled_medication = Medicine.objects.filter(peracik=request.user.peracik, status='CANCELED')
        
        peracik_current = Peracik.objects.get(user=request.user)
        
        if peracik_current.status == 'WAITING':
            return Response({
                "message": "Your account is still waiting for approval"
            }, status=200)
        elif peracik_current.status == 'CANCELED':
            return Response({
                "message": "Your account has been canceled",
                "tips" : "Please contact admin for more information",
                "message_status" : serializer.data['message_status']
            }, status=200)
        else :
            return Response({
                "status" : "ACCEPTED",
                "profile": serializer.data,
                "accepted_medication": MedicineSerializer(accepted_medication, many=True).data,
                "waiting_medication": MedicineSerializer(waiting_medication, many=True).data,
                "canceled_medication": MedicineSerializer(canceled_medication, many=True).data,
                
            })
        
    