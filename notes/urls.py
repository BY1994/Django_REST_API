from django.urls import path
from . import views

urlpatterns = [
    path('memos/', views.create_and_list),
    path('memos/<int:memo_id>/', views.delete)
]