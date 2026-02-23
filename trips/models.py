from django.contrib.gis.db import models


class Trip(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    description = models.TextField(blank=True, verbose_name='Description')
    start_date = models.DateField(null=True, blank=True, verbose_name='Start date')
    end_date = models.DateField(null=True, blank=True, verbose_name='End date')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'
        ordering = ['-start_date', '-created_at']

    def __str__(self):
        return self.name


class Location(models.Model):
    trip = models.ForeignKey(
        Trip, related_name='locations', on_delete=models.CASCADE, verbose_name='Trip'
    )
    name = models.CharField(max_length=200, verbose_name='Location name')
    description = models.TextField(blank=True, verbose_name='Description')
    point = models.PointField(srid=4326, verbose_name='Coordinates')
    order = models.PositiveIntegerField(default=0, verbose_name='Order')
    visited_at = models.DateField(null=True, blank=True, verbose_name='Visited at')

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ['trip', 'order', 'visited_at']

    def __str__(self):
        return f'{self.trip.name} — {self.name}'


class Photo(models.Model):
    location = models.ForeignKey(
        Location, related_name='photos', on_delete=models.CASCADE, verbose_name='Location'
    )
    image = models.ImageField(upload_to='photos/%Y/%m/', verbose_name='Image')
    caption = models.CharField(max_length=500, blank=True, verbose_name='Caption')
    taken_at = models.DateTimeField(null=True, blank=True, verbose_name='Taken at')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        ordering = ['taken_at']

    def __str__(self):
        return f'{self.location.name} — {self.caption or "Photo"}'
