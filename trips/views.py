import json
from django.shortcuts import render
from .models import Trip


def map_view(request):
    trips = Trip.objects.prefetch_related('locations__photos').order_by('-start_date', '-created_at')

    locations_data = []
    for trip in trips:
        for location in trip.locations.all():
            photos_urls = [
                request.build_absolute_uri(photo.image.url)
                for photo in location.photos.all()
                if photo.image
            ]
            locations_data.append({
                'id': location.id,
                'trip_id': trip.id,
                'trip_name': trip.name,
                'name': location.name,
                'description': location.description,
                'lat': location.point.y,
                'lng': location.point.x,
                'photos': photos_urls,
            })

    return render(request, 'trips/map.html', {
        'trips': trips,
        'locations_json': json.dumps(locations_data, ensure_ascii=False),
    })
