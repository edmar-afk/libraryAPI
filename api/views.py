from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Librarian, Visit, Booking
from .serializers import LibrarianSerializer, VisitorSerializer, BookingSerializer
from rest_framework.permissions import AllowAny
from django.http import Http404
from django.db.models import Count, Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone
from django.http import JsonResponse
from datetime import timedelta
# Create your views here.
class LibrarianViewSet(viewsets.ModelViewSet): 
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = [AllowAny]


class MainLibrarians(viewsets.ModelViewSet):
    queryset = Librarian.objects.filter(site='Main')
    serializer_class = LibrarianSerializer
    permission_classes = [AllowAny]

class DumingagLibrarians(viewsets.ModelViewSet):
    queryset = Librarian.objects.filter(site='Dumingag')
    serializer_class = LibrarianSerializer
    permission_classes = [AllowAny]
    
class PagadianLibrarians(viewsets.ModelViewSet):
    queryset = Librarian.objects.filter(site='Pagadian')
    serializer_class = LibrarianSerializer
    permission_classes = [AllowAny]
    
    
class CanutoLibrarians(viewsets.ModelViewSet):
    queryset = Librarian.objects.filter(site='Canuto')
    serializer_class = LibrarianSerializer
    permission_classes = [AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]
    

class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        # Get today's date at midnight (00:00:00) using timezone.now().date()
        today_start = timezone.now().date()

        # Filter visits for today's IP and user agent
        existing_visit = Visit.objects.filter(
            ip_address=ip_address,
            user_agent=user_agent,
            timestamp__date=today_start
        ).first()

        if existing_visit:
            return Response({'status': 'failure', 'message': 'User already visited today'})
        else:
            new_visit = Visit.objects.create(ip_address=ip_address, user_agent=user_agent, timestamp=today_start)
            new_visit.save()
            return Response({'status': 'success', 'message': 'Website visited'})


class VisitByMonthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, month=None):
        if month is None:
            return JsonResponse({'error': 'Month parameter is required'}, status=400)

        # Query the database to get visits for the specified month
        visits = Visit.objects.filter(timestamp__month=month)

        # Serialize the data
        serializer = VisitorSerializer(visits, many=True)

        return JsonResponse(serializer.data, safe=False)


class VisitByYearViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, year=None):
        if year is None:
            return JsonResponse({'error': 'Year parameter is required'}, status=400)

        # Query the database to get visits for the specified year
        visits = Visit.objects.filter(timestamp__year=year)

        # Serialize the data
        serializer = VisitorSerializer(visits, many=True)

        return JsonResponse(serializer.data, safe=False)
    


class VisitByDayViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, year=None, month=None, day=None):
        if year is None or month is None or day is None:
            return JsonResponse({'error': 'Year, month, and day parameters are required'}, status=400)

        # Construct timezone-aware datetime object for the specified year, month, and day
        date = timezone.datetime(int(year), int(month), int(day), tzinfo=timezone.get_current_timezone())

        # Construct start and end datetime objects for the specified day
        start_datetime = date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_datetime = start_datetime + timedelta(days=1) - timedelta(microseconds=1)

        # Filter visits for the specified date range (from start of the day to end of the day)
        visits = Visit.objects.filter(timestamp__range=(start_datetime, end_datetime))

        serializer = VisitorSerializer(visits, many=True)
        return JsonResponse(serializer.data, safe=False)