from django.urls import reverse, resolve
from django.test import TestCase
from .views import home, board_topics_view
from .models import Board

# Create your tests here.


class Hometest(TestCase):
    def test_home_view(self):
   
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)


    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


class BoardTopic(TestCase):
    def setUp(self):
        Board.objects.create(name ='Django7', description='My django test')

    def test_board_topic_view(self):

        response = self.client.get(reverse('viewboard', kwargs={'board_id':1}))

        self.assertEquals(response.status_code, 200)
    
    def test_board_topic_view_fail(self):

        response = self.client.get(reverse('viewboard', kwargs={'board_id':10}))

        self.assertEquals(response.status_code, 404)


    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/board/85/')
        self.assertEquals(view.func, board_topics_view)
