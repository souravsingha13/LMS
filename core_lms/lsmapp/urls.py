from django.urls import path
from .views.book_views import BookViewSet
from .views.book_loan_view import BookLoanViewSet
from.views.views import AuthorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')
router.register(r'loan',BookLoanViewSet, basename='loan')

urlpatterns = [
    path('all-author/', AuthorViewSet.as_view(), name="all-author"),
    path('author/<uuid:id>/', AuthorViewSet.as_view(), name="update-author")
]
urlpatterns += router.urls