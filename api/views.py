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


    # @action(detail=False, methods=['post'], url_name='projects')
    def create(self, request):
        valid_packages = True
        print("teste")
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid() :
            for package in serializer.validated_data["packages"]:
                version = package["version"] if "version" in package else None
                pypi_response = PypiResponse(package["name"], 
                version)
                if pypi_response.is_valid_package() == False:
                    valid_packages = False
            if valid_packages == False:
                message = {"error": "One or more packages doesn't exist"}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
