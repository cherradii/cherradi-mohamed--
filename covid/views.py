from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CovidSerializer


# class SmartView(APIView):
#
#     def get(self, request):
#         serializer = SmartSerializer(Smart.objects.all(), many=True)
#         response = {"smarts": serializer.data}
#         return Response(response, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         data = request.data
#         serializer = SmartSerializer(data=data)
#         if serializer.is_valid():
#             smart = Smart(**data)
#             smart.save()
#             response = serializer.data
#             return Response(response, status=status.HTTP_200_OK)
#
#
# def show(request):
#     data = {}
#     p = Smart.objects.all()
#     data["smarts"] = p
#     return render(request, "smarts/smartCities.html", data)

# def searchShow(request):
#     if 'search' in request.GET:
#         search_string = request.GET['search']
#     context = {
#             "search_string": search_string,
#     }
#     return render(request, "polls/show.html", context)

def show(request):
    # data = {}
    # p = Smart.objects.all()
    # data["smarts"] = p
    return render(request, "covid19/covidViews.html")
