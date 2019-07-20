

class Economy(object):
    def __init__(self, type_space, distribution_function, utilities):
        self.type_space=type_space
        self.distribution_function = distribution_function #(can be correlated)
        self.utilities=utilities

    # + social_value_function (and some basic -- ex-post/ex-ante)
    

class BaseMechanism(object):  #or metaclass -- because smth like concrete settings will be needed to be implemented
    def __init__(self, action_space, outcome_func, economy):
        self.action_space
        self.utility_func = utility_func


class AnonimousMechanism(BaseMechanism):
    def __init__(self, n_players, one_action_space, outcome_func, economy):
        self.n_players = n_players
        self.one_action_space = one_action_space
        self.utility_func = utility_func #validate?
        super().__init__([one_action_space]*n_players, [one_utility_func]*n_players, economy)


    def get_induced_game(self):
    	pass #returns game + bayes nash can draw types + strategy method can be applied + iterative games can be made + ?





#revelation_function
#move to IC mechanisms from beginning + implementablilty questiins
# + social_choice_function ????


# заботай algorithmic game theory here

# = numerical libraries here

# comparative statics

# mb take a functional manner? -- by what about that cool ML?