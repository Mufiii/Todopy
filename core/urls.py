
from django.urls import path, include
from .import views

urlpatterns = [
   path("", views.home , name='home'),
   path("update/<int:todo_id>/",views.update ,name='update' ),
   path("path/<int:todo_id>/", views.delete , name='delete')
]