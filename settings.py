from os import environ
import random as rand

left_range = -10
right_range= 10
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [

{
    'name': 'normal_form_game_3x3',
    'display_name': "Generic Normal Form Game, 2 Players, 3x3 Strategies",
    'num_demo_participants': 2,
    'app_sequence': ['normal_form_game_3x3', 'payment_info'],
    'num_repetitions': 1,
    'timeout_for_instructions': 100,
    'timeout_for_decisions': 100,
    'timeout_for_intermediate_results': 100,
    'chat': 'yes',
#    Eingabe von "space" = kein Chat / Eingabe von "chat" = Chat wird angezeigt
    'pdf_link_text': ' ',
    'pdf_link_color': '#0067a3',
 #   'num_strategies_A': 1,
 #   'num_strategies_B': 1,
    'game_name': "This game",
    'P1_strategy_1': "Strategy P1 1",
    'P1_strategy_2': "Strategy P1 2",
    'P1_strategy_3': "Strategy P1 3",
    'P2_strategy_1': "Strategy P2 1",
    'P2_strategy_2': "Strategy P2 2",
    'P2_strategy_3': "Strategy P2 3",
    'Custom Random Payoffs': 'False',
    'Distribution': 'False',
    'Center of distribution': 0.0,
    'Width of distribution': 0.0,

    'P1_payoff_P1S1_P2S1': rand.randrange(left_range,right_range),
    'P1_payoff_P1S1_P2S2': rand.randrange(left_range,right_range),
    'P1_payoff_P1S1_P2S3': rand.randrange(left_range,right_range),
    
    'P1_payoff_P1S2_P2S1': rand.randrange(left_range,right_range),
    'P1_payoff_P1S2_P2S2': rand.randrange(left_range,right_range),
    'P1_payoff_P1S2_P2S3': rand.randrange(left_range,right_range),

    'P1_payoff_P1S3_P2S1': rand.randrange(left_range,right_range),
    'P1_payoff_P1S3_P2S2': rand.randrange(left_range,right_range),
    'P1_payoff_P1S3_P2S3': rand.randrange(left_range,right_range),

    'P2_payoff_P2S1_P1S1': rand.randrange(left_range,right_range),
    'P2_payoff_P2S1_P1S2': rand.randrange(left_range,right_range),
    'P2_payoff_P2S1_P1S3': rand.randrange(left_range,right_range),
    
    'P2_payoff_P2S2_P1S1': rand.randrange(left_range,right_range),
    'P2_payoff_P2S2_P1S2': rand.randrange(left_range,right_range),
    'P2_payoff_P2S2_P1S3': rand.randrange(left_range,right_range),

    'P2_payoff_P2S3_P1S1': rand.randrange(left_range,right_range),
    'P2_payoff_P2S3_P1S2': rand.randrange(left_range,right_range),
    'P2_payoff_P2S3_P1S3': rand.randrange(left_range,right_range),

    'text':"""
In this study, you will be randomly and anonymously paired with another participant.
Each of you simultaneously and privately chooses the strategy to follow.
Your payoffs will be determined by the choices of both as below:""",

    'doc': """
"""
},
    {
        'name': 'normal_form_game_2x2',
        'display_name': "Generic Normal Form Game, 2 Players, 2x2 Strategies",
        'num_demo_participants': 2,
        'app_sequence': ['normal_form_game_2x2', 'payment_info'],
        'num_repetitions': 1,
        'timeout_for_instructions': 100,
        'timeout_for_decisions': 100,
        'timeout_for_intermediate_results': 100,
        'chat': 'yes',
        'pdf_link_text': ' ',
        'pdf_link_color': '#0067a3',
 #       'num_strategies_A': 1,
 #       'num_strategies_B': 1,
        'game_name': "This game",
        'P1_strategy_1': "Strategy P1 1",
        'P1_strategy_2': "Strategy P1 2",
        'P2_strategy_1': "Strategy P2 1",
        'P2_strategy_2': "Strategy P2 2",
        'Custom Random Payoffs': 'False',
        'Distribution': 'False',
        'Center of distribution': 0.0,
        'Width of distribution': 0.0,

        'P1_payoff_P1S1_P2S1': rand.randrange(left_range,right_range),
        'P1_payoff_P1S1_P2S2': rand.randrange(left_range,right_range),

        'P1_payoff_P1S2_P2S1': rand.randrange(left_range,right_range),
        'P1_payoff_P1S2_P2S2': rand.randrange(left_range,right_range),

        'P2_payoff_P2S1_P1S1': rand.randrange(left_range,right_range),
        'P2_payoff_P2S1_P1S2': rand.randrange(left_range,right_range),

        'P2_payoff_P2S2_P1S1': rand.randrange(left_range,right_range),
        'P2_payoff_P2S2_P1S2': rand.randrange(left_range,right_range),

        'text': """
In this study, you will be randomly and anonymously paired with another participant.
 Each of you simultaneously and privately chooses which strategy to follow.
 Your payoffs will be determined by the choices of both as below:
 """
    },


    {
        'name': 'normal_form_game_2x3',
        'display_name': "Generic Normal Form Game, 2 Players, 2x3 Strategies",
        'num_demo_participants': 2,
        'app_sequence': ['normal_form_game_2x3', 'payment_info'],
        'num_repetitions': 1,
        'timeout_for_instructions': 100,
        'timeout_for_decisions': 100,
        'timeout_for_intermediate_results': 100,
        'chat': 'yes',
        'pdf_link_text': ' ',
        'pdf_link_color': '#0067a3',
#        'num_strategies_A': 1,
#        'num_strategies_B': 1,
	    'game_name': "This game",
        'P1_strategy_1': "Strategy P1 1",
        'P1_strategy_2': "Strategy P1 2",
#'P1_strategy_3': "Strategy P1_3",
        'P2_strategy_1': "Strategy P2 1",
        'P2_strategy_2': "Strategy P2 2",
        'P2_strategy_3': "Strategy P2 3",
        'Custom Random Payoffs' : 'False',
        'Distribution': 'False',
        'Center of distribution': 0.0,
        'Width of distribution': 0.0,

        'P1_payoff_P1S1_P2S1': rand.randrange(left_range,right_range),
        'P1_payoff_P1S1_P2S2': rand.randrange(left_range,right_range),
        'P1_payoff_P1S1_P2S3': rand.randrange(left_range,right_range),

        'P1_payoff_P1S2_P2S1': rand.randrange(left_range,right_range),
        'P1_payoff_P1S2_P2S2': rand.randrange(left_range,right_range),
        'P1_payoff_P1S2_P2S3': rand.randrange(left_range,right_range),

#    'P1_payoff_P1S3_P2S1': 0,
#    'P1_payoff_P1S3_P2S2': 2,
#    'P1_payoff_P1S3_P2S3': 2,

        'P2_payoff_P2S1_P1S1': rand.randrange(left_range,right_range),
        'P2_payoff_P2S1_P1S2': rand.randrange(left_range,right_range),
#    'P2_payoff_P2S1_P1S3': 8,

        'P2_payoff_P2S2_P1S1': rand.randrange(left_range,right_range),
        'P2_payoff_P2S2_P1S2': rand.randrange(left_range,right_range),
#    'P2_payoff_P2S2_P1S3': 2,

        'P2_payoff_P2S3_P1S1': rand.randrange(left_range,right_range),
        'P2_payoff_P2S3_P1S2': rand.randrange(left_range,right_range),
#    'P2_payoff_P2S3_P1S3': 2,


        'text1': """
In this study, you will be randomly and anonymously paired with another participant.
 Each of you simultaneously and privately chooses which strategy to follow.
 Your payoffs will be determined by the choices of both as below:
""",

        'text2': """
In this study, you will be randomly and anonymously paired with another participant.
 Each of you simultaneously and privately chooses which strategy to follow.
 Your payoffs will be determined by the choices of both as below:
""",

        'doc': """
"""
    },
    

]
# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

#the room file contains the list of allowed players
ROOMS = [
    {
        'name': 'Gamification1',
        'display_name': 'Gamification Showcase Session: Game 1',
    },
    {
        'name': 'Gamification2',
        'display_name': 'Gamification Showcase Session: Game 2',
    },
    {
        'name': 'Gamification3',
        'display_name': 'Gamification Showcase Session: Game 3',
    },

  {
        'name': 'Test',
        'display_name': 'Gamification Showcase Session: Test',
    }
 ]


DEMO_PAGE_INTRO_HTML = """
Here are various games implemented for the Gamification Project in Economics at ZHAW. 
These games were designed for any multiple-of-2 number of players on the basis of Normal Form Games, equipped with different number of strategies.
The games' parameters can be configured from the admin user in the "Configure Session" menu in the Tab Sessions or Rooms.
"""
ADMIN_USERNAME = ''
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = ''

# don't share this with anybody.
SECRET_KEY = '{{ secret_key }}'


# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

