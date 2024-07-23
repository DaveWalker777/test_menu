from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page-one/', views.page_one, name='page_one'),
    path('page-two/', views.page_two, name='page_two'),
    path('page-three/', views.page_three, name='page_three'),
    path('sub_1', views.sub_1, name='sub_1'),
]
