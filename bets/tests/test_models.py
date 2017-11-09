from django.test import TestCase

from bets.models import Bet
from django.contrib.auth.models import User


class BetModelTest(TestCase):

    @classmethod
    def setUp(cls):
        test_user1 = User.objects.create_user(username='test1', password='12345')
        test_user1.save()

        test_user2 = User.objects.create_user(username='test2', password='12345')
        test_user2.save()

        Bet.objects.create(
            title='Test Bet',
            description='A random bet.',
            amount=1,
            bettor=test_user1,
            taker=test_user2,
        )

    def test_title_label(self):
        bet = Bet.objects.get(id=1)
        field_label = bet._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        bet = Bet.objects.get(id=1)
        field_label = bet._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_amount_label(self):
        bet = Bet.objects.get(id=1)
        field_label = bet._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

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
