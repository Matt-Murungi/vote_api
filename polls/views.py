from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView
from django.shortcuts import get_object_or_404, render

from polls.serializers import ChoiceSerializer, PollSerializer, VoteSerializer

from .models import Poll, Choice, Vote


class PollList(ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PostDetail(RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceList(CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CreateVote(CreateAPIView):
    serializer_class = VoteSerializer
