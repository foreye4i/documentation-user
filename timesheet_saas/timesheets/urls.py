from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TimesheetViewSet, TimesheetEntryViewSet

router = DefaultRouter()
router.register(r'timesheets', TimesheetViewSet, basename='timesheet')
router.register(r'entries', TimesheetEntryViewSet, basename='timesheet-entry')

urlpatterns = [
	path('', include(router.urls)),
]