from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books import views
from books.views import BookViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='book_viewset')


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/', include(router.urls)),

    path('books/', views.books_view, name='books'),
    path('users/<int:user_id>/books/', views.books_by_user, name="books_by_user")
]
