from django.urls import path
from . import views
urlpatterns = [
    path('', views.entry_list, name='entry-list'),
    path('entry/<int:id>/', views.entry_detail, name='entry-detail'),
]