from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Game

class GameTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_thing = Game.objects.create(player=testuser1, title='Elden Ring', description='git gud scrub')
        test_thing.save()

    def test_things_model(self):
        game = Game.objects.get(id=1)
        actual_player = str(game.player)
        actual_title = str(game.title)
        actual_description = str(game.description)
        self.assertEqual(actual_player,'testuser')
        self.assertEqual(actual_title, 'Elden Ring')
        self.assertEqual(actual_description,'git gud scrub')