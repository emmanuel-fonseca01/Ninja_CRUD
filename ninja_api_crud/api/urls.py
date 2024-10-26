from django.urls import path
from .views import api as crud

urlpatterns = [
    path('/api', crud.urls),
]