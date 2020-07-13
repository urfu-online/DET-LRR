from lrr.repository import models
from lrr.repository import serializers
from rest_framework import viewsets, permissions


class DigitalResourceViewSet(viewsets.ModelViewSet):
    """ViewSet for the DigitalResource class"""

    queryset = models.DigitalResource.objects.all()
    serializer_class = serializers.DigitalResourceSerializer
    #permission_classes = [permissions.IsAuthenticated]


class DirectionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Direction class"""

    queryset = models.Direction.objects.all()
    serializer_class = serializers.DirectionSerializer
    #permission_classes = [permissions.IsAuthenticated]


class LanguageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Language class"""

    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    #permission_classes = [permissions.IsAuthenticated]


class CompetenceCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the CompetenceCategory class"""

    queryset = models.CompetenceCategory.objects.all()
    serializer_class = serializers.CompetenceCategorySerializer
    #permission_classes = [permissions.IsAuthenticated]


class CompetenceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Competence class"""

    queryset = models.Competence.objects.all()
    serializer_class = serializers.CompetenceSerializer
    #permission_classes = [permissions.IsAuthenticated]


class PlatformViewSet(viewsets.ModelViewSet):
    """ViewSet for the Platform class"""

    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer
    #permission_classes = [permissions.IsAuthenticated]


class OrganisationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Organisation class"""

    queryset = models.Organisation.objects.all()
    serializer_class = serializers.OrganisationSerializer
    #permission_classes = [permissions.IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Author class"""

    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    #permission_classes = [permissions.IsAuthenticated]


class SourceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Source class"""

    queryset = models.Source.objects.all()
    serializer_class = serializers.SourceSerializer
    #permission_classes = [permissions.IsAuthenticated]


class ResourceStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the ResourceStatus class"""

    queryset = models.ResourceStatus.objects.all()
    serializer_class = serializers.ResourceStatusSerializer
    #permission_classes = [permissions.IsAuthenticated]


class DisciplineThemeViewSet(viewsets.ModelViewSet):
    """ViewSet for the DisciplineTheme class"""

    queryset = models.DisciplineTheme.objects.all()
    serializer_class = serializers.DisciplineThemeSerializer
    #permission_classes = [permissions.IsAuthenticated]


class DisciplineViewSet(viewsets.ModelViewSet):
    """ViewSet for the Discipline class"""

    queryset = models.Discipline.objects.all()
    serializer_class = serializers.DisciplineSerializer
    #permission_classes = [permissions.IsAuthenticated]


class ThematicPlanViewSet(viewsets.ModelViewSet):
    """ViewSet for the ThematicPlan class"""

    queryset = models.ThematicPlan.objects.all()
    serializer_class = serializers.ThematicPlanSerializer
    #permission_classes = [permissions.IsAuthenticated]


class DisciplineThemeResourceViewSet(viewsets.ModelViewSet):
    """ViewSet for the DisciplineThemeResource class"""

    queryset = models.DisciplineThemeResource.objects.all()
    serializer_class = serializers.DisciplineThemeResourceSerializer
    #permission_classes = [permissions.IsAuthenticated]

