from rest_framework import routers

from .views import TruckViewSet

router = routers.SimpleRouter()
router.register('trucks', TruckViewSet, 'truck')

urlpatterns = router.urls
