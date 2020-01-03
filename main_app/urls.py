from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('wishes/create/', views.AddWish.as_view(), name='add_wish'),
  path('wishes/<int:pk>/delete/', views.DeleteWish.as_view(), name='delete_wish'),
]