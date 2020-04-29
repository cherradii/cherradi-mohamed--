from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Vehicule
from .serializers import VehiculeSerializer


# class VehiculeView(APIView):
#
#     def get(self, request):
#         serializer = VehiculeSerializer(Vehicule.objects.all(), many=True)
#         response = {"vehicules": serializer.data}
#         return Response(response, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         data = request.data
#         serializer = VehiculeSerializer(data=data)
#         if serializer.is_valid():
#             smart = Vehicule(**data)
#             smart.save()
#             response = serializer.data
#             return Response(response, status=status.HTTP_200_OK)


# def show(request):
#     data = {}
#     p = Vehicule.objects.all()
#     data["vehicules"] = p
#     return render(request, "vehicules/vehicule.html", data)

# def searchShow(request):
#     if 'search' in request.GET:
#         search_string = request.GET['search']
#     context = {
#             "search_string": search_string,
#     }
#     return render(request, "polls/show.html", context)

def show(request):
    # data = {}
    # p = Vehicule.objects.all()
    # data["vehicules"] = p
    return render(request, "vehicules/vehicule.html")