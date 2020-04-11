from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('leave_comment', views.leave_comment, name = 'leave_comment'),
    path('leave_comment1', views.leave_comment1, name = 'leave_comment1'),
    path('comment/', views.AddComment.as_view(), name='add_comment')
]