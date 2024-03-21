from django.urls import path
from .views import AuthorViewSet

urlpatterns = [
    path('all-author/', AuthorViewSet.as_view(), name="all-author"),
    path('author/<uuid:id>/', AuthorViewSet.as_view(), name="update-author")
]