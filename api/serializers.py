from magpy.request import PypiResponse
from rest_framework import serializers

from .models import PackageRelease, Project


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ['name', 'version']
        extra_kwargs = {'version': {'required': False}}

    # def get_version(self, data):
    #     if "version" in data:
    #         return data["version"]
    #     else:
    #         return None

    # def validate(self, data):
    #     version = self.get_version(data)
    #     name = data["name"]
    #     pipy_response = PypiResponse(name, version)
    #     if pipy_response.request_package_response().status_code != 200:
    #         raise serializers.ValidationError("One or more packages doesn't exist")
    #     return "xablau"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'packages']

    packages = PackageSerializer(many=True)

    def create(self, validated_data):
        packages = validated_data.pop('packages')
        project = Project.objects.create(**validated_data)
        for package in packages:
            PackageRelease.objects.create(project=project, **package)
        return project
