from django.test import TestCase

from bets.models import Bet, Taker, Bettor
from django.contrib.auth.models import User


class BetModelTest(TestCase):

    @classmethod
    def setUp(cls):
        test_user1 = User.objects.create_user(username='test1', password='12345')
        test_user1.save()

        test_user2 = User.objects.create_user(username='test2', password='12345')
        test_user2.save()

        bettor = Bettor.objects.create(user=test_user1)
        taker = Taker.objects.create(user=test_user2)

        Bet.objects.create(
            title='Test Bet',
            description='A random bet.',
            wager='asdf',
            bettor=bettor,
            taker=taker,
        )


    def test_title_label(self):
        bet = Bet.objects.get(id=1)
        field_label = bet._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        bet = Bet.objects.get(id=1)
        field_label = bet._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_wager_label(self):
        bet = Bet.objects.get(id=1)
        field_label = bet._meta.get_field('wager').verbose_name
        self.assertEqual(field_label, 'wager')

    def test_bettor_label(self):
        bet = Bet.objects.get(id=1)
        field_label = bet._meta.get_field('bettor').verbose_name
        self.assertEqual(field_label, 'bettor')

    def test_taker_label(self):
        bet = Bet.objects.get(id=1)
        field_label = bet._meta.get_field('taker').verbose_name
        self.assertEqual(field_label, 'taker')

    def test_winner_label(self):
        bet = Bet.objects.get(id=1)
        field_label = bet._meta.get_field('winner').verbose_name
        self.assertEqual(field_label, 'winner')

    def test_title_max_length(self):
        bet = Bet.objects.get(id=1)
        max_length = bet._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_wager_max_length(self):
        bet = Bet.objects.get(id=1)
        max_length = bet._meta.get_field('wager').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_title(self):
        bet = Bet.objects.get(id=1)
        expected_object_name = bet.title
        self.assertEqual(expected_object_name, str(bet))

    def test_get_absolute_url(self):
        bet = Bet.objects.get(id=1)
        self.assertEqual(bet.get_absolute_url(), '/bets/bet/1')


class BettorModelTest(TestCase):
    
    @classmethod
    def setUp(cls):
        test_user = User.objects.create_user(username='test1', password='12345')
        test_user.save()

        Bettor.objects.create(user=test_user)

    def test_user_label(self):
        bettor = Bettor.objects.get(id=1)
        field_label = bettor._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_object_name_is_username(self):
        bettor = Bettor.objects.get(id=1)
        expected_object_name = bettor.user.username
        self.assertEqual(expected_object_name, str(bettor))

        
class TakerModelTest(TestCase):
    
    @classmethod
    def setUp(cls):
        test_user = User.objects.create_user(username='test1', password='12345')
        test_user.save()

        Taker.objects.create(user=test_user)

    def test_user_label(self):
        taker = Taker.objects.get(id=1)
        field_label = Taker._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_object_name_is_username(self):
        taker = Taker.objects.get(id=1)
        expected_object_name = taker.user.username
        self.assertEqual(expected_object_name, str(taker))

