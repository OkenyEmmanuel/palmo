from django.urls import path
from .views import CategoryDetailView
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('register/', views.register, name="register"),
    path('login/',views.handlelogin,name='handlelogin'),
    path('signup/', views.signup,name='signup'),
    path('logout/',views.handlelogout,name='handlelogout'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),
    name='activate'),
]


