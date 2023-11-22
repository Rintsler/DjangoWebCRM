from django.urls import path
from app import views

urlpatterns = [
    #path('', home, name='home'),
    path('', views.HomeListView.as_view() , name='home'),
    path('detail/<int:pk>', views.HomeDetailView.as_view(), name='detail_page'),
    path('edit-page', views.edit_page, name='edit_page'),
]
