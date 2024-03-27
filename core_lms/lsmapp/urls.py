from django.urls import path
from .views.book_views import BookViewSet
from.views.views import AuthorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')

urlpatterns = [
    path('all-author/', AuthorViewSet.as_view(), name="all-author"),
    path('author/<uuid:id>/', AuthorViewSet.as_view(), name="update-author")
]
urlpatterns += router.urls