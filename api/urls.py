from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import VisitorCount

router = DefaultRouter()
router.register(r'librarians', views.LibrarianViewSet, basename='librarians')
router.register(r'main', views.MainLibrarians, basename='main')
router.register(r'dumingag', views.DumingagLibrarians, basename='dumingag')
router.register(r'pagadian', views.PagadianLibrarians, basename='pagadian')
router.register(r'canuto', views.CanutoLibrarians, basename='canuto')

urlpatterns = [
    path('visitor/', VisitorCount.as_view(), name='visitor_count'),
]

urlpatterns += router.urls