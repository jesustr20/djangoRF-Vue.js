from rest_framework import routers
from .viewsets import LibrosViewSet

router = routers.SimpleRouter()

router.register('libros', LibrosViewSet)

urlpatterns = router.urls