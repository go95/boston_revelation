from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Questionaire(Page):
    form_model = 'player'

    def get_form_fields(self):
        return ['choice']
        # player.payoff = player.choice * 10


page_sequence = [
    Questionaire
]
