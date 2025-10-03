from rest_framework.routers import DefaultRouter
from .views import ProductCategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'products_category', ProductCategoryViewSet, basename='products_category')

urlpatterns = router.urls
