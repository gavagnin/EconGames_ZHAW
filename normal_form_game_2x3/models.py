from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from numpy import random,round

doc = """
This is a normal games with 2x3 strategies. Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'normal_form_game_2x3'
    players_per_group = 2
    num_rounds = 30

    instructions_template = 'normal_form_game_2x3/Instructions.html'
    instructions_template2 = 'normal_form_game_2x3/Instructions2.html'


class Subsession(BaseSubsession):
    P1_strategy_3 = models.CharField(initial='Strategy P1_3')
    #P1_payoff_P1S3_P2S1 = 0
    P1_payoff_P1S3_P2S1 = models.IntegerField(initial=0)
    #P1_payoff_P1S3_P2S2 = 2
    P1_payoff_P1S3_P2S2 = models.IntegerField(initial=2)
    #P1_payoff_P1S3_P2S3 = 2
    P1_payoff_P1S3_P2S3 = models.IntegerField(initial=2)
    #P2_payoff_P2S1_P1S3 = 8
    P2_payoff_P2S1_P1S3 = models.IntegerField(initial=8)
    #P2_payoff_P2S2_P1S3 = 2
    P2_payoff_P2S2_P1S3 = models.IntegerField(initial=2)
    #P2_payoff_P2S3_P1S3 = 2
    P2_payoff_P2S3_P1S3 = models.IntegerField(initial=2)

    def creating_session(self):
#        num_strategies_A = self.session.config['num_strategies_A']
#        num_strategies_B = self.session.config['num_strategies_B']
        strategies_P1 = [self.session.config['P1_strategy_1'], self.session.config['P1_strategy_2'], self.P1_strategy_3]
        strategies_P2 = [self.session.config['P2_strategy_1'], self.session.config['P2_strategy_2'], self.session.config['P2_strategy_3']]
        strategies = [strategies_P1, strategies_P2]
        set_custom_random = self.session.config['Custom Random Payoffs']
        user_distribution = self.session.config['Distribution']
        user_center = self.session.config['Center of distribution']
        user_width= self.session.config['Width of distribution']


        def create_random_payoffs(distribution, center, width):
            if distribution == "Normal":
                random_payoffs = random.normal(center, width,
                                       size=[2, 3, 3])  # 8 is the number of payoffs for 2 players game ,2x2 startgies
            if distribution == "Uniform":
                random_payoffs = random.uniform(center - width, center + width, size=[2, 3, 3])
            return (round(random_payoffs, 0))  # rounding otherwise otree just cut the decimal part #to be improved


        if (set_custom_random == 'True') * (user_distribution != 'False') * (user_width > 0):
            payoffs = create_random_payoffs(user_distribution, user_center, user_width)

        if (set_custom_random == 'False') * (user_distribution == 'False') * (user_width == 0) * (user_center == 0):

            payoffs_P1 = [[self.session.config['P1_payoff_P1S1_P2S1'], self.session.config['P1_payoff_P1S1_P2S2'], self.session.config['P1_payoff_P1S1_P2S3']],
                      [self.session.config['P1_payoff_P1S2_P2S1'], self.session.config['P1_payoff_P1S2_P2S2'], self.session.config['P1_payoff_P1S2_P2S3']],
                      [self.P1_payoff_P1S3_P2S1, self.P1_payoff_P1S3_P2S2, self.P1_payoff_P1S3_P2S3]]
            payoffs_P2 = [[self.session.config['P2_payoff_P2S1_P1S1'], self.session.config['P2_payoff_P2S1_P1S2'], self.P2_payoff_P2S1_P1S3],
                      [self.session.config['P2_payoff_P2S2_P1S1'], self.session.config['P2_payoff_P2S2_P1S2'], self.P2_payoff_P2S2_P1S3],
                      [self.session.config['P2_payoff_P2S3_P1S1'], self.session.config['P2_payoff_P2S3_P1S2'], self.P2_payoff_P2S3_P1S3]]
            payoffs = [payoffs_P1, payoffs_P2]

        players = self.get_players()
        i = 0
        for p in players:
            j = i % 2
            # first player gets first strategy, second player gets second strategy
            p.strategy_1 = strategies[j][0]
            p.strategy_2 = strategies[j][1]
            p.strategy_3 = strategies[j][2]
            p.payoff_selfS1_otherS1 = payoffs[j][0][0]
            p.payoff_selfS1_otherS2 = payoffs[j][0][1]
            p.payoff_selfS1_otherS3 = payoffs[j][0][2]
            p.payoff_selfS2_otherS1 = payoffs[j][1][0]
            p.payoff_selfS2_otherS2 = payoffs[j][1][1]
            p.payoff_selfS2_otherS3 = payoffs[j][1][2]
            p.payoff_selfS3_otherS1 = payoffs[j][2][0]
            p.payoff_selfS3_otherS2 = payoffs[j][2][1]
            p.payoff_selfS3_otherS3 = payoffs[j][2][2]
            i = i + 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    strategy_1 = models.StringField()
    strategy_2 = models.StringField()
    strategy_3 = models.StringField()
    payoff_selfS1_otherS1 = models.IntegerField()
    payoff_selfS1_otherS2 = models.IntegerField()
    payoff_selfS1_otherS3 = models.IntegerField()
    payoff_selfS2_otherS1 = models.IntegerField()
    payoff_selfS2_otherS2 = models.IntegerField()
    payoff_selfS2_otherS3 = models.IntegerField()
    payoff_selfS3_otherS1 = models.IntegerField()
    payoff_selfS3_otherS2 = models.IntegerField()
    payoff_selfS3_otherS3 = models.IntegerField()

    decision = models.StringField(
    #     #choices=['Strategy A', 'Defect'], ##not necessary, defined in decision_choices
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )
    def decision_choices(self):
        choices = [self.strategy_1, self.strategy_2, self.strategy_3]
        return choices

    def other_player(self):
        return self.get_others_in_group()[0]

##continue here: add payoffs to matrix
    def set_payoff(self):
        payoff_matrix = {
            self.strategy_1:
                {
                    self.other_player().strategy_1: self.payoff_selfS1_otherS1,
                    self.other_player().strategy_2: self.payoff_selfS1_otherS2,
                    self.other_player().strategy_3: self.payoff_selfS1_otherS3

                },
            self.strategy_2:
                {
                    self.other_player().strategy_1: self.payoff_selfS2_otherS1,
                    self.other_player().strategy_2: self.payoff_selfS2_otherS2,
                    self.other_player().strategy_3: self.payoff_selfS2_otherS3

                },
            self.strategy_3:
                {
                    self.other_player().strategy_1: self.payoff_selfS3_otherS1,
                    self.other_player().strategy_2: self.payoff_selfS3_otherS2,
                    self.other_player().strategy_3: self.payoff_selfS3_otherS3

                }
        }
        self.payoff = payoff_matrix[self.decision][self.other_player().decision]