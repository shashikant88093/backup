from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
# from django.views import View
from .serializers import (
    TableSerializer,
   )
from rest_framework import viewsets
from .models import Table
from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class TableList(ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    def get_extra_actions(self,request, *args, **kwargs):
        queryset_list = Table.objects.all()
        # .order_by('-id')[:10]
        query = request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                # Q(Run_status__icontains=query) |
                Q(Date_time__icontains=query) |
                Q(Run_status__icontains=query)
            ).distinct()
        else:
            queryset_list = queryset_list.order_by('-id')[:10]

        return queryset_list


class ReadFile(APIView):
    # authentication_classes=[Token]
    # lookup_field = 'id'
    # queryset = Table.objects.all
    permission_classes = [IsAuthenticated]
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    def post(self,request):
        paths = self.request.data['path']
        print(paths)
        f = open(paths,'r')
        readtxt = f.read()
        print(readtxt)
        return Response(readtxt)