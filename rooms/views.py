from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Room, Student

# --- 房间视图 ---
class RoomListView(ListView):
    model = Room
    template_name = "rooms/room_list.html"
    context_object_name = "rooms"

class RoomDetailView(DetailView):
    model = Room
    template_name = "rooms/room_detail.html"
    context_object_name = "room"

class RoomCreateView(CreateView):
    model = Room
    template_name = "rooms/room_form.html"
    fields = ["number", "capacity"]
    success_url = reverse_lazy("room-list")

class RoomUpdateView(UpdateView):
    model = Room
    template_name = "rooms/room_form.html"
    fields = ["number", "capacity"]
    success_url = reverse_lazy("room-list")

class RoomDeleteView(DeleteView):
    model = Room
    template_name = "rooms/room_confirm_delete.html"
    success_url = reverse_lazy("room-list")

# --- 学生视图 ---
class StudentListView(ListView):
    model = Student
    template_name = "rooms/student_list.html"
    context_object_name = "students"

class StudentCreateView(CreateView):
    model = Student
    template_name = "rooms/student_form.html"
    fields = ["name", "room"]
    success_url = reverse_lazy("student-list")

class StudentUpdateView(UpdateView):
    model = Student
    template_name = "rooms/student_form.html"
    fields = ["name", "room"]
    success_url = reverse_lazy("student-list")

class StudentAssignView(UpdateView):
    model = Student
    template_name = "rooms/student_assign.html"
    fields = ["room"]
    success_url = reverse_lazy("student-list")