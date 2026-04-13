from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView # Importamos las vistas de Swagger
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    
    path('api/', include(router.urls)),
    
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]