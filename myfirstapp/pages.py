from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

from collections import defaultdict
from .config import REVELATION_MAPPING
import random
from django.core import validators


# getattr вынести в нормальные переменные


class BostonMechanism(object): # + visualization
    def __init__(self, capacities):
        self.capacities = capacities

    def apply(self, actions): # allocation тоже лучше как объект
        actions = actions.copy()
        capacities = self.capacities.copy() # наверное где-то есть нормальный объект allocation
        allocation = defaultdict(list) 

        iteration = 0
        while sum(capacities.values()) != 0 or actions == {}:

            applications = defaultdict(list)
            for p, a in actions.items():
                applications[a[iteration]] += [p]

            for school, app in applications.items():
                applied = random.sample(app, min(capacities[school], len(app)))
                capacities[school] -= len(applied)
                allocation[school] += applied
                for p in applied:
                    del actions[p]

            iteration += 1

        allocation['UNALLOCATED'] = actions.keys()

        return allocation


class CompMixin:
    def get_form(self, *args, **kwargs):
        f = super().get_form(*args, **kwargs)
        for i, j in f.fields.items():
            regex = rf'^{str(Constants.correct_answers.get(i))}$'
            j.validators.append(validators.RegexValidator(message='Проверьте правильность ответа', regex=regex,
                                                          code='invalid_input'))
        return f



class Instructions_common1(Page):
    form_model= 'player'
    form_fields = ['ident']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        rate = int(self.session.config['real_world_currency_per_point'])
        if (int(str(rate)[-1]) == 1 and rate != 11):
            e = 'рубль'
        elif rate in [2, 3, 4]:
            e = 'рубля'
        else:
            e = 'рублей'
        return {'ending': e}



class Instructions_common2(Page):
    def is_displayed(self):
        return self.round_number == 1


class Instructions_common_CQ(CompMixin, Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == 1

    def get_form_fields(self):
        fields = [f.name for f in Player._meta.get_fields() if f.name.startswith('cq')]
        return fields


class Instructions_BM(CompMixin, Page):
    def is_displayed(self):
        return self.round_number in [1,6] #and self.player.group.treatment_type == 0


class Instructions_BM1(CompMixin, Page):
    def is_displayed(self):
        return self.round_number in [1,6] and self.player.group.treatment_type == 3


class Instructions_BM2(CompMixin, Page):
    def is_displayed(self):
        return self.round_number in [1,6] and self.player.group.treatment_type == 2

class Instructions_BM3(CompMixin, Page):
    def is_displayed(self):
        return self.round_number in [1,6] and self.player.group.treatment_type == 1

class Choose(Page):
    form_model= 'player'
    form_fields = [
        'strategy9',
        'strategy8',
        'strategy7',
        'strategy6',
        'strategy5',
        'strategy4',
        'strategy3',
        'strategy2',
        'strategy1',
        'strategy0'
    ]


def compute_payoffs(group):
    players = group.get_players()
    strategy_name = 'strategy' + str(group.choice_of_row)


    mechanism = BostonMechanism(
        {
            'A': group.capacityA,
            'B': group.capacityB
        }
    )

    actions = {p: REVELATION_MAPPING[getattr(p, strategy_name)] for p in players}
    
    for i in range(Constants.fictive_players):
        actions[i] = ('A', 'B')

    allocation = mechanism.apply(actions)

    for school, players in allocation.items():
        for player in players:
            if isinstance(player, Player):
                player.allocation = school
                if school == 'A':
                    player.payoff = c(100)
                elif school == 'B':
                    player.payoff = group.Bvalue
                else:
                    player.payoff = c(0)



class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number in [5,10]

    def after_all_players_arrive(self):
        all_rounds = self.group.in_rounds(self.round_number - 4, self.round_number)

        for r in all_rounds:
            compute_payoffs(r)



class Results(Page):
    def is_displayed(self):
        return self.round_number in [5,10]

    def vars_for_template(self):
        all_rounds = self.player.in_rounds(self.round_number - 4, self.round_number)
        #form = self.get_form()
        #data = zip(others, form)

        strategy_names = []

        for p in all_rounds:
            strategy_names.append(getattr(p, 'strategy' + str(p.group.choice_of_row)))
        return {'all_rounds': zip(range(self.round_number - 4, self.round_number + 1), all_rounds, strategy_names)}
        # all 5 games results
        # choice of the row, списки поступления, выигрыш

        # sum


page_sequence = [
    Instructions_common1,
    Instructions_common2,
    Instructions_BM,
    # Instructions_BM1,
    # Instructions_BM2,
    # Instructions_BM3,
#    Instructions_common_CQ,
    Choose,
    ResultsWaitPage,
    Results
]
