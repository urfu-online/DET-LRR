from rest_framework import viewsets, permissions

from . import models
from . import serializers


class SubjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Subject class"""

    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrganizationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Organization class"""

    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]


class EduProgramViewSet(viewsets.ModelViewSet):
    """ViewSet for the EduProgram class"""

    queryset = models.EduProgram.objects.all()
    serializer_class = serializers.EduProgramSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResultEduViewSet(viewsets.ModelViewSet):
    """ViewSet for the ResultEdu class"""

    queryset = models.ResultEdu.objects.all()
    serializer_class = serializers.ResultEduSerializer
    permission_classes = [permissions.IsAuthenticated]


import logging

logger = logging.getLogger(__name__)


class DigitalResourceViewSet(viewsets.ModelViewSet):
    """ViewSet for the DigitalResource class"""

    queryset = models.DigitalResource.objects.all()
    serializer_class = serializers.DigitalResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(DigitalResourceViewSet, self).get_serializer(*args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CompetenceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Competence class"""

    queryset = models.Competence.objects.all()
    serializer_class = serializers.CompetenceSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlatformViewSet(viewsets.ModelViewSet):
    """ViewSet for the Platform class"""

    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer
    permission_classes = [permissions.IsAuthenticated]


class LanguageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Language class"""

    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubjectTagViewSet(viewsets.ModelViewSet):
    """ViewSet for the SubjectTag class"""

    queryset = models.SubjectTag.objects.all()
    serializer_class = serializers.SubjectTagSerializer
    permission_classes = [permissions.IsAuthenticated]


class EduProgramTagViewSet(viewsets.ModelViewSet):
    """ViewSet for the EduProgramTag class"""

    queryset = models.EduProgramTag.objects.all()
    serializer_class = serializers.EduProgramTagSerializer
    permission_classes = [permissions.IsAuthenticated]


class SourceViewSet(viewsets.ModelViewSet):
    """ViewSet for the SubjectTag class"""

    queryset = models.Source.objects.all()
    serializer_class = serializers.SourceSerializer
    permission_classes = [permissions.IsAuthenticated]
