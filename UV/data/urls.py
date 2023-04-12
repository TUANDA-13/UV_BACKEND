from django.urls import path
from .views import UVListCreateAPIView

urlpatterns = [
    path('', UVListCreateAPIView.as_view(), name='uv-list-create'),
    # path('', UVViewSet.as_view(), name='get-list'),
]
