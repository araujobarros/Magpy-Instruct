from rest_framework import serializers

from .request import PypiResponse
from .models import PackageRelease, Project


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PackageRelease
        fields = ['name', 'version']
        extra_kwargs = {'version': {'required': False}}


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['name', 'packages']

    packages = PackageSerializer(many=True)

    @staticmethod
    def get_package_with_version(package):
        version = package["version"] if "version" in package else None
        pypi_response = PypiResponse(package["name"], version)
        return {
            "name": package["name"],
            "version": pypi_response.get_version()}

    @classmethod
    def create_packages(cls, packages, project):
        for package in packages:
            new_package = cls.get_package_with_version(package)
            PackageRelease.objects.create(project=project, **new_package)

    def create(self, validated_data):
        packages = validated_data.pop('packages')
        project = Project.objects.create(**validated_data)
        ProjectSerializer.create_packages(packages, project)
        return project
