from django.urls import path
from .views import WeddingListView

urlpatterns = [
    path('wedding-list/', WeddingListView.as_view(), name='wedding-list'),
]