from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    def get_timeout_seconds(self):
        return self.session.config['timeout_for_instructions']

    def is_displayed(self):
        return self.round_number == 1
        
    def vars_for_template(self):
        game_name = self.session.config['game_name']
        pdf_link_color = self.session.config['pdf_link_color']
        pdf_link_text = self.session.config['pdf_link_text']
        return dict(
            game_name=game_name,
            image_path='img_for_players/3x3/1_introduction/{}.jpg'.format(self.round_number),
            pdf_path='pdf_for_players/3x3/1_introduction/{}.pdf'.format(self.round_number),
            pdf_link_color=pdf_link_color,
            pdf_link_text=pdf_link_text
        )

class Decision(Page):
    def get_timeout_seconds(self):
        return self.session.config['timeout_for_decisions']

    def is_displayed(self):
        return self.round_number <= self.session.config['num_repetitions']
    form_model = 'player'
    form_fields = ['decision']

    def vars_for_template(self):
        chat1 = self.session.config['chat']
        return dict(
            image_path='img_for_players/3x3/2_decision/{}.jpg'.format(self.round_number),
            chat1 = chat1
        )

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def get_timeout_seconds(self):
        return self.session.config['timeout_for_intermediate_results']

    def is_displayed(self):
        return self.round_number <= self.session.config['num_repetitions']

    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return {
            'my_decision': me.decision,
            'opponent_decision': opponent.decision,
            'same_choice': me.decision == opponent.decision,
            'image_path':'img_for_players/3x3/3_interm_results/{}.jpg'.format(self.round_number)
        }


class ResultsSummary(Page):

    def is_displayed(self):
        return self.round_number == self.session.config['num_repetitions']

    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()

        player_in_all_rounds = me.in_all_rounds()
        opponent_in_all_rounds = opponent.in_all_rounds()
        player_opponent_in_all_rounds = zip(player_in_all_rounds, opponent_in_all_rounds)


        return {


            'player_in_all_rounds': player_in_all_rounds,
            'player_opponent_in_all_rounds' : player_opponent_in_all_rounds
        }



page_sequence = [
    Introduction,
    Decision,
    ResultsWaitPage,
    Results,
    ResultsSummary
]
