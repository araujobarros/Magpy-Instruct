import sys
from magpy.request import PypiResponse
# from requests.models import Response
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Project
from .serializers import PackageSerializer, ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "name"

    @staticmethod
    def response_if_valid_serializer (serializer):
        valid_packages = []
        for package in serializer.validated_data["packages"]:
            version = package["version"] if "version" in package else None
            pypi_response = PypiResponse(package["name"], version)
            valid_packages.append(pypi_response.is_valid_package())
        if False in valid_packages:
            message = {"error": "One or more packages doesn't exist"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def appropriate_response (serializer):
        if serializer.is_valid() :
            return ProjectViewSet.response_if_valid_serializer(serializer)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    def create(self, request):
        serializer = ProjectSerializer(data=request.data)
        return ProjectViewSet.appropriate_response(serializer)
