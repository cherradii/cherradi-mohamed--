from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Big
from .serializers import BigSerializer


# class BigView(APIView):
#
#     def get(self, request):
#         serializer = BigSerializer(Big.objects.all(), many=True)
#         response = {"bigs": serializer.data}
#         return Response(response, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         data = request.data
#         serializer = BigSerializer(data=data)
#         if serializer.is_valid():
#             smart = Big(**data)
#             smart.save()
#             response = serializer.data
#             return Response(response, status=status.HTTP_200_OK)
#
#
# def show(request):
#     data = {}
#     p = Big.objects.all()
#     data["bigs"] = p
#     return render(request, "bigs/bigData.html", data)

# def searchShow(request):
#     if 'search' in request.GET:
#         search_string = request.GET['search']
#     context = {
#             "search_string": search_string,
#     }
#     return render(request, "polls/show.html", context)

def show(request):
    # data = {}
    # p = Big.objects.all()
    # data["bigs"] = p
    return render(request, "bigs/bigData.html")