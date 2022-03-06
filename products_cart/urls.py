from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('', views.CategoryList, basename="cart")
router.register('', views.ProductViews, basename="product"),
router.register('^(?P<name>.+)/$',views.ProductViews,basename="productsearch" ),
router.register('',views.CustomerViewSets, basename="customer")

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),

    ## for admin dashboard
    path('products/', include(router.urls)),

    ## for client side fetching
    path('all-products/', views.ProductList.as_view()),
    path('all-products/<int:pk>/', views.ProductDetail.as_view()),

    path('customers/', include(router.urls)),

]
