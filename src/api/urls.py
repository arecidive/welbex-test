from cargo.urls import urlpatterns as cargo_urls
from location.urls import urlpatterns as location_urls
from truck.urls import urlpatterns as truck_urls

urlpatterns = []
urlpatterns += cargo_urls
urlpatterns += truck_urls
urlpatterns += location_urls
