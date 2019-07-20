from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import itertools
import random
#import pandas as pd # HEROKU HUB INCOMPATIBLE
from .rounds_config import rounds_config


from .config import CHOICES

author = 'Your name here'

doc = """
Your app description
"""


# нужны идиомы для within/between дизайнов
# и для strategymethod
# и ???



class Constants(BaseConstants):
    name_in_url = 'myfirstapp'
    players_per_group = 4 # param = n2
    num_rounds = 10
    fictive_players = 12
    correct_answers = {
        'cq1_a': 14,
        'cq2_a': 4,
        'cq3_a': 70
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        players = self.get_players()
        groups = self.get_groups()
        round_per_treatment = 5
        round_for_treatment = (self.round_number - 1) // round_per_treatment
        round_in_treatment = int((self.round_number - 1) % round_per_treatment)
                
        if self.round_number == 1:
            experimental_groups = itertools.cycle([0, 1, 2, 3])
            for g in groups:
                experimental_group = next(experimental_groups)
                for p in g.get_players():
                    p.participant.vars['experimental_group'] = self.session.config.get('experimental_group', experimental_group)

        for group in groups:
            p1 = group.get_player_by_id(1)
            group.experimental_group = p1.participant.vars['experimental_group']
            group.treatment_type = int((group.experimental_group + round_for_treatment) % len(CHOICES))
            if group.experimental_group != 0 and round_for_treatment == (Constants.num_rounds/round_per_treatment) - 1:
                group.treatment_type = 0

            group.choice_of_row = random.choice(range(10))
            group.Bvalue = c(group.choice_of_row*10 + 5)

            group.capacityA = rounds_config[round_in_treatment]['capacityA']
            group.capacityB = rounds_config[round_in_treatment]['capacityB']

        for p in players:
            p.order_of_options = random.choice([False, True])


class Group(BaseGroup):
    choice_of_row = models.IntegerField()
    capacityA = models.IntegerField()
    capacityB = models.IntegerField()
    experimental_group = models.IntegerField()
    treatment_type = models.IntegerField()
    Bvalue = models.CurrencyField()


def make_strategy_field(amount):
    return models.StringField(
        label=r'Доход абитуриентов типа 1 после университе а B равен {}.'.format(amount),
        widget=widgets.RadioSelectHorizontal
    )


def strategy_choices(self):
    choices = CHOICES[self.group.treatment_type].copy()

    if self.order_of_options:
        choices.reverse()
    return choices

def strategy_label(amount):
    def inner(self):
        return LABEL[self.group.treatment_type].format(amount)
    return inner

class Player(BasePlayer): # сделать схему динамической
    cq1_a = models.IntegerField()
    cq2_a = models.IntegerField()
    cq3_a = models.CurrencyField()

    preferences_type = models.IntegerField(initial=1)
    allocation = models.StringField()
    order_of_options = models.BooleanField()
    ident = models.IntegerField(label='Укажите номер вашего стола.', min=1) #, max=????

    strategy9 = make_strategy_field(95)
    strategy9_choices = strategy_choices
    strategy8 = make_strategy_field(85)
    strategy8_choices = strategy_choices
    strategy7 = make_strategy_field(75)
    strategy7_choices = strategy_choices
    strategy6 = make_strategy_field(65)
    strategy6_choices = strategy_choices
    strategy5 = make_strategy_field(55)
    strategy5_choices = strategy_choices
    strategy4 = make_strategy_field(45)
    strategy4_choices = strategy_choices
    strategy3 = make_strategy_field(35)
    strategy3_choices = strategy_choices
    strategy2 = make_strategy_field(25)
    strategy2_choices = strategy_choices
    strategy1 = make_strategy_field(15)
    strategy1_choices = strategy_choices
    strategy0 = make_strategy_field(5)
    strategy0_choices = strategy_choices

