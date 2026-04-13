from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView # Importamos las vistas de Swagger
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    # Tus rutas de la API (El router ya maneja el /products/ y tu endpoint personalizado)
    path('api/', include(router.urls)),
    
    # Ruta requerida por Swagger para descargar el esquema interno
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Ruta para acceder a la interfaz gráfica de Swagger UI en el navegador
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]