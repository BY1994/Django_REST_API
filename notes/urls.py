from django.urls import path
from . import views

urlpatterns = [
    path('memos/', views.create_and_list),
]