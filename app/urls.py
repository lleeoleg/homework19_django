from django.urls import path
from .views import Create, Detail


urlpatterns = [
    path('create/', Create.as_view(), name='index'),
    path('user/<int:user_id>', Detail.as_view(), name='detail')
]
