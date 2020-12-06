from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from lrr.complexes import api as complexes_api
from lrr.repository import api as repository_api
from lrr.users.api.views import StudentViewSet, PersonViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# USERS

router.register("Person", PersonViewSet)
router.register("Student", StudentViewSet)

# REPOSITORY

router.register("DRStatus", repository_api.DRStatusViewSet)
router.register("ExpertiseStatus", repository_api.ExpertiseStatusViewSet)
router.register("Subject", repository_api.SubjectViewSet)
router.register("Organization", repository_api.OrganizationViewSet)
router.register("EduProgram", repository_api.EduProgramViewSet)
router.register("ProvidingDiscipline", repository_api.ProvidingDisciplineViewSet)
router.register("ResultEdu", repository_api.ResultEduViewSet)
router.register("DigitalResource", repository_api.DigitalResourceViewSet)
router.register("Competence", repository_api.CompetenceViewSet)
router.register("Platform", repository_api.PlatformViewSet)
router.register("Language", repository_api.LanguageViewSet)
router.register("SubjectTag", repository_api.SubjectTagViewSet)
# router.register("Student", repository_api.StudentViewSet)
router.register("ConformityTheme", repository_api.ConformityThemeViewSet)
router.register("EduProgramTag", repository_api.EduProgramTagViewSet)
router.register("SubjectTheme", repository_api.SubjectThemeViewSet)
router.register("ThematicPlan", repository_api.ThematicPlanViewSet)
router.register("Source", repository_api.SourceViewSet)
# router.register("Person", repository_api.PersonViewSet)

# COMPLEXES

router.register("digitalComplex", complexes_api.DigitalComplexViewSet)
router.register("cell", complexes_api.CellViewSet)
router.register("complexSpaceCell", complexes_api.ComplexSpaceCellViewSet)
router.register("workPlanAcademicGroup", complexes_api.WorkPlanAcademicGroupViewSet)

app_name = "api"
urlpatterns = router.urls
