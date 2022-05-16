from django import views
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets, generics, status, permissions, mixins
from .models import Category, Buses, Customers, Routes, Seats, Ticketbooking, User
from .serializers import BusSerializer, CategorySerializer, RouteSerializer, SeatSerializer, TicketbookingSerializer, UserSerializer

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'current_user':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_path="current-user", detail=False)
    def current_user(self, request):
        return Response(self.serializer_class(request.user, context={'request': request}).data,
                        status=status.HTTP_200_OK)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset =  Category.objects.filter(active = True)
    serializer_class = CategorySerializer

class BusViewSet(viewsets.ModelViewSet):
    queryset =  Buses.objects.filter(active = True)
    serializer_class = BusSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset =  Seats.objects.filter(active = True)
    serializer_class = SeatSerializer
    
class RouteViewSet(viewsets.ModelViewSet):
    queryset =  Routes.objects.filter(active = True)
    serializer_class = RouteSerializer

class TicketbookingViewSet(viewsets.ModelViewSet):
    queryset =  Ticketbooking.objects.filter(active = True)
    serializer_class = TicketbookingSerializer
    


# Create your views here.
