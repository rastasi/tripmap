from django.contrib.gis.db import models


class Trip(models.Model):
    name = models.CharField(max_length=200, verbose_name='Név')
    description = models.TextField(blank=True, verbose_name='Leírás')
    start_date = models.DateField(null=True, blank=True, verbose_name='Kezdő dátum')
    end_date = models.DateField(null=True, blank=True, verbose_name='Befejező dátum')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Utazás'
        verbose_name_plural = 'Utazások'
        ordering = ['-start_date', '-created_at']

    def __str__(self):
        return self.name


class Location(models.Model):
    trip = models.ForeignKey(
        Trip, related_name='locations', on_delete=models.CASCADE, verbose_name='Utazás'
    )
    name = models.CharField(max_length=200, verbose_name='Helyszín neve')
    description = models.TextField(blank=True, verbose_name='Leírás')
    point = models.PointField(srid=4326, verbose_name='Koordináták')
    order = models.PositiveIntegerField(default=0, verbose_name='Sorrend')
    visited_at = models.DateField(null=True, blank=True, verbose_name='Látogatás dátuma')

    class Meta:
        verbose_name = 'Helyszín'
        verbose_name_plural = 'Helyszínek'
        ordering = ['trip', 'order', 'visited_at']

    def __str__(self):
        return f'{self.trip.name} — {self.name}'


class Photo(models.Model):
    location = models.ForeignKey(
        Location, related_name='photos', on_delete=models.CASCADE, verbose_name='Helyszín'
    )
    image = models.ImageField(upload_to='photos/%Y/%m/', verbose_name='Kép')
    caption = models.CharField(max_length=500, blank=True, verbose_name='Felirat')
    taken_at = models.DateTimeField(null=True, blank=True, verbose_name='Készítés időpontja')

    class Meta:
        verbose_name = 'Fotó'
        verbose_name_plural = 'Fotók'
        ordering = ['taken_at']

    def __str__(self):
        return f'{self.location.name} — {self.caption or "Fotó"}'
