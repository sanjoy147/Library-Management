from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BorrowRequestViewSet, StudentViewSet,BorrowedViewSet, logout_page
from .views import borrowed_book_by_student
router = DefaultRouter()
router.register('students',StudentViewSet)
router.register('books',BookViewSet)
router.register('borrowlist',BorrowedViewSet)
router.register('borrowrequest',BorrowRequestViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path("borrow/<id>/",borrowed_book_by_student.as_view()),
    # path("login/",login_page,name="Login"),
    path("logout/",logout_page,name="Logout"),

]