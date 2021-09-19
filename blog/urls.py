from django.urls import path
from blog import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('landscape/', views.LandscapeView.as_view(), name='landscape'),
    path('portrait/', views.PortraitView.as_view(), name='portrait'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('post/<int:pk>/', views.Post_detailView.as_view(), name='post_detail'),
    path('post/new/', views.Post_newView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.Post_editView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.Post_deleteView.as_view(), name='post_delete'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact_complete/', views.Contact_completeView.as_view(), name='contact_complete'),
    path('aboutme/', views.AboutmeView.as_view(), name='aboutme'),
]