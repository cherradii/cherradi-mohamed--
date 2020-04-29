from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Trav
from .serializers import TravSerializer


# class TravView(APIView):
#
#     def get(self, request):
#         serializer = TravSerializer(Trav.objects.all(), many=True)
#         response = {"travaux": serializer.data}
#         return Response(response, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         data = request.data
#         serializer = TravSerializer(data=data)
#         if serializer.is_valid():
#             trav = Trav(**data)
#             trav.save()
#             response = serializer.data
#             return Response(response, status=status.HTTP_200_OK)
#
#
# def show(request):
#     data = {}
#     p = Trav.objects.all()
#     data["travaux"] = p
#     return render(request, "travaux/public.html", data)

# def searchShow(request):
#     if 'search' in request.GET:
#         search_string = request.GET['search']
#     context = {
#             "search_string": search_string,
#     }
#     return render(request, "polls/show.html", context)

def show(request):
    # data = {}
    # p = Trav.objects.all()
    # data["travaux"] = p
    return render(request, "travaux/public.html")
