from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'librarians', views.LibrarianViewSet, basename='librarians')
router.register(r'main', views.MainLibrarians, basename='main')
router.register(r'dumingag', views.DumingagLibrarians, basename='dumingag')
router.register(r'pagadian', views.PagadianLibrarians, basename='pagadian')
router.register(r'canuto', views.CanutoLibrarians, basename='canuto')
router.register(r'visits', views.VisitViewSet, basename='visits')
router.register(r'booking', views.BookingViewSet, basename='booking')
urlpatterns = [
    # Your existing paths can go here if needed
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('views/month/<int:month>/', views.VisitByMonthViewSet.as_view({'get': 'list'}), name='visit-by-month'),
    path('views/year/<int:year>/', views.VisitByYearViewSet.as_view({'get': 'list'}), name='visit-by-year'),
    path('views/daily/<int:year>/<int:month>/<int:day>/', views.VisitByDayViewSet.as_view({'get': 'list'}), name='visit-by-daily'),
]

urlpatterns += router.urls 