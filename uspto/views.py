from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from uspto.models import Poll
from .serializers import PollSerializer


# class PollView(APIView):
#
#     def get(self, request):
#         serializer = PollSerializer(Poll.objects.all(), many=True)
#         response = {"polls": serializer.data}
#         return Response(response, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         data = request.data
#         serializer = PollSerializer(data=data)
#         if serializer.is_valid():
#             poll = Poll(**data)
#             poll.save()
#             response = serializer.data
#             return Response(response, status=status.HTTP_200_OK)
#
#
# def index(request):
#     data = {}
#     return render(request,"uspto/index.html",data)
#
# def show(request):
#     data = {}
#     p = Poll.objects.all()
#     data["polls"] = p
#     return render(request, "uspto/show.html", data)
#
#
#
# def searchShow(request):
#     if 'search' in request.GET:
#         search_string = request.GET['search']
#     context = {
#             "search_string": search_string,
#     }
#     return render(request, "uspto/show.html", context)

def index(request):
    data = {}
    return render(request,"uspto/index.html",data)

def show(request):
    # data = {}
    # p = Poll.objects.all()
    # data["polls"] = p
    return render(request, "uspto/show.html")