from django.urls import path
from . import views
from .views import MenuItemView, SingleMenuItemView,bookingView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/',MenuItemView.as_view(),name="menu-list"),
    path('menu/<int:pk>',SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    # path('booking/',bookingView.as_view()),
]
