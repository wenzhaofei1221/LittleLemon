from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer

# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class bookingView(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    

# class bookingView(APIView):
#     def get(self,request):
#         items = Booking.objects.all()
#         serializer = bookingSerializer(items, many=True)
#         return Response(serializer.data)
    
# class menuView(APIView):
#     def post(self,request):
#         serializer = menuSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success","data":serializer.data})