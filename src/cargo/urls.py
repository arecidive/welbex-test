from rest_framework import routers

from .views import CargoViewSet

router = routers.SimpleRouter()
router.register('cargos', CargoViewSet, 'cargo')

urlpatterns = router.urls
