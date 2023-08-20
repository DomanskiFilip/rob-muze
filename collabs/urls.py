from django.urls import path
from . import views

app_name = 'collabs'

urlpatterns = [
    path('', views.collabs, name='collabs'),
    path('<pk>', views.collab, name='collab'),
    path('<pk>/przeslij', views.przeslij, name='przeslij'),
    path('glosowanie/', views.votings, name='votings'),
    path('glosowanie/<pk>', views.voting, name='voting'),
]