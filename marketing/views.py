from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Mark
from .serializers import MarkSerializer

#
# class MarkView(APIView):
#
#     def get(self, request):
#         serializer = MarkSerializer(Mark.objects.all(), many=True)
#         response = {"marketing": serializer.data}
#         return Response(response, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         data = request.data
#         serializer = MarkSerializer(data=data)
#         if serializer.is_valid():
#             mark = Mark(**data)
#             mark.save()
#             response = serializer.data
#             return Response(response, status=status.HTTP_200_OK)
#
#
# def show(request):
#     data = {}
#     p = Mark.objects.all()
#     data["marketing"] = p
#     return render(request, "marketing/marketing.html", data)

# def searchShow(request):
#     if 'search' in request.GET:
#         search_string = request.GET['search']
#     context = {
#             "search_string": search_string,
#     }
#     return render(request, "polls/show.html", context)

def show(request):
    # data = {}
    # p = Mark.objects.all()
    # data["marketing"] = p
    return render(request, "marketing/marketing.html")