from django.urls import path
from pic_app import views

app_name = 'pic_app'
urlpatterns = [
    path('', views.imageList.as_view(), name='imageList'),
    path("new", views.imageAdd.as_view(), name="imageAdd"),
    path('show/<int:id>', views.imageDetail.as_view(), name="imageDetail"),
    path('delete/<int:id>', views.imageDelete.as_view(), name="imageDelete"),
    path('<int:id>/edit', views.imageEdit.as_view(), name="imageEdit"),
    

]