from django.http import HttpResponse
from django.views.generic import View
from chatterbot import ChatBot 

class MyView(View):
  def get(self, request, *args, **kwargs):
    return HttpResponse('This is GET request ' + ChatBot.get_response(request.GET['msg']))