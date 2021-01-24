from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Board
from django.http import Http404

# Create your views here.

def home(request):
    boards = Board.objects.all()
    #boards_list = [data.name for data in boards]
    #response_html = '<br>'.join(boards_list)
    
    
    return render(request, 'index.html', {'boards': boards})

def board_topics_view(request, board_id):
    
    #try:
     #   boards = Board.objects.get(pk=board_id)
    #except:
    #    raise Http404()
    boards = get_object_or_404(Board, pk=board_id)
    #boards_list = [data.name for data in boards]
    #response_html = '<br>'.join(boards_list)
    
    
    return render(request, 'topics.html', {'board': boards})
