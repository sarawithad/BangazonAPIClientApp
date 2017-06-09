from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from API import views


router = routers.DefaultRouter()
#All routes for API resources
router.register(r'customer', views.CustomerViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'paymenttype', views.PaymentTypeViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'order', views.OrderProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

