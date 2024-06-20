from django.shortcuts import render

from rest_framework import generics
from .models import Event, Location, Planning
from .serializers import EventSerializer, LocationSerializer, PlanningSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class PlanningListCreateView(generics.ListCreateAPIView):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializer

class PlanningDetailView(generics.RetrieveAPIView):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializer

@api_view(['POST'])
def create_planning(request):
    event_id = request.data.get('event')
    location_id = request.data.get('location')
    date = request.data.get('date')

    try:
        event = Event.objects.get(id=event_id)
        location = Location.objects.get(id=location_id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
    except Location.DoesNotExist:
        return Response({"error": "Location not found."}, status=status.HTTP_404_NOT_FOUND)

    planning = Planning(event=event, location=location, date=date)
    planning.save()

    serializer = PlanningSerializer(planning)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def delete_planning(request, pk):
    try:
        planning = Planning.objects.get(pk=pk)
    except Planning.DoesNotExist:
        return Response({"error": "Planning not found."}, status=status.HTTP_404_NOT_FOUND)

    planning.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def planning_form_view(request):
    events = Event.objects.all()
    locations = Location.objects.all()
    return render(request, 'planning_form.html', {'events': events, 'locations': locations})