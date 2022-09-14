from django.urls import path

from librayapp import views

urlpatterns = [
    path('', views.handle_login, name='handle_login'),
    path('handle_signup', views.handle_signup, name='handle_signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('handle_logout', views.handle_logout, name='handle_logout'),
    path('add_book', views.add_book, name='add_book'),
    path('delete_book/<str:pk>', views.delete_book, name='delete_book'),
    path('upadte_book/<str:pk>', views.update_book, name='update_book'),
    path('view_book/<str:pk>', views.view_book, name='view_book'),
]
