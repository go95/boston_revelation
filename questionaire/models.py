from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questionaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        players = self.get_players()
        for p in players:
            p.truth = random.randint(1, 6)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    truth = models.IntegerField()
    choice = models.IntegerField(
        label='Сообщите, какое число выпало на кубике. В дополнение к вашему основному выигрышу мы вам заплатим столько HSE',
        choices=[1,2,3,4,5,6],
        widget=widgets.RadioSelectHorizontal
        )

