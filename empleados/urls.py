from rest_framework import routers
from .api import PerffilViewSet

router= routers.DefaultRouter()
router.register('api/empleados', PerffilViewSet, 'empleados')

urlpatterns= router.urls