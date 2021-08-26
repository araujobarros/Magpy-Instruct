from rest_framework import viewsets, status
from rest_framework.response import Response

from magpy.request import PypiResponse
from .models import Project
from .serializers import  ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    """
    retrieve:
        Return a project instance.

    list:
        Return all projects, ordered by most recently joined.

    create:
        Create a new project.

    delete:
        Remove an existing project.

    partial_update:
        Update one or more fields on an existing project.

    update:
        Update a project.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "name"


    @staticmethod
    def all_packages_are_valid (serializer):
        valid_packages = []
        for package in serializer.validated_data["packages"]:
            version = package["version"] if "version" in package else None
            pypi_response = PypiResponse(package["name"], version)
            valid_packages.append(pypi_response.is_valid_package())
        return False not in valid_packages


    @staticmethod
    def response_if_valid_serializer (serializer):
        if not ProjectViewSet.all_packages_are_valid(serializer):
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
