from django.urls import path
from .views import CategoryDetailView
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('register/', views.register, name="register"),
]


