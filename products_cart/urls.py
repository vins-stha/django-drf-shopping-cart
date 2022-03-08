from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from rest_framework.authtoken import views

router_products= routers.DefaultRouter()
router_admin = routers.DefaultRouter()
router_user = routers.DefaultRouter()


# router.register('', views.CategoryList, basename="cart")
router_products.register('', views.ProductViews, basename="product"),
router_products.register('^(?P<name>.+)/$',views.ProductViews,basename="productsearch" ),
router_user.register('',views.CustomerViewSets, basename="customer")

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),

    ## for admin dashboard
    path('products/', include(router_products.urls)),

    ## for client side fetching
    path('all-products/', views.ProductList.as_view()),
    path('all-products/<int:pk>/', views.ProductDetail.as_view()),

    # admin login routes

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # customer routes
    path('customers/', include(router_user.urls)),

]
