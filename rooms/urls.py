from django.urls import path
from . import views

urlpatterns = [
    path("", views.RoomListView.as_view(), name="room-list"),
    path("create/", views.RoomCreateView.as_view(), name="room-create"),

    path("students/", views.StudentListView.as_view(), name="student-list"),
    path("students/create/", views.StudentCreateView.as_view(), name="student-create"),
    path("students/<int:pk>/update/", views.StudentUpdateView.as_view(), name="student-update"),
    path("students/<int:pk>/assign/", views.StudentAssignView.as_view(), name="student-assign"),

    path("<int:pk>/", views.RoomDetailView.as_view(), name="room-detail"),
    path("<int:pk>/update/", views.RoomUpdateView.as_view(), name="room-update"),
    path("<int:pk>/delete/", views.RoomDeleteView.as_view(), name="room-delete"),
]