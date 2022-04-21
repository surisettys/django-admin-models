from django.urls import path
from loginapp import views

app_name = 'loginapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('modelview/',views.modelview,name='model'),
    path('createbook/',views.CreateBook.as_view(),name='createbook'),
    path('detailbook/<int:pk>/',views.BookDetail.as_view(),name='book_detail')
]