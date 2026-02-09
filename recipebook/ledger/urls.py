from django.urls import path
from .views import recipes_list

urlpatterns = [
    path('recipes/list', recipes_list, name='recipes_list'),
]

app_name = 'ledger'