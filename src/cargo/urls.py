from rest_framework import routers

from .views import CargoViewSet

router = routers.SimpleRouter()
router.register('cargo', CargoViewSet)

urlpatterns = router.urls
