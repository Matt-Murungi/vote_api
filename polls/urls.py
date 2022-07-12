
from django.urls import path
from .views import PollList, PostDetail

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PostDetail.as_view(), name="polls_detail")
]


