from django.urls import path
from . import views

urlpatterns=[

path('', views.home, name = 'home'),
path('board/<int:board_id>/', views.board_topics_view, name = 'viewboard')

]