from django.contrib.gis.forms.widgets import BaseGeometryWidget


class LeafletPointWidget(BaseGeometryWidget):
    template_name = 'trips/leaflet_point_widget.html'
    geom_type = 'POINT'
    map_srid = 4326

    def serialize(self, value):
        return value.ewkt if value else ''

    def deserialize(self, value):
        from django.contrib.gis.geos import GEOSGeometry
        try:
            return GEOSGeometry(value)
        except Exception:
            return None

    class Media:
        css = {
            'all': (
                'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
            )
        }
        js = (
            'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
        )
