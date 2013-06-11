BLACK = (0,0,0)
DIMGRAY = (105, 105, 105)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

LONG_STRING = "X"*80

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
LIZARD = "lizard"
SPOCK = "spock"

MAIN_MENU_BUTTON_RECT = (10, 90, 180, 50)
NEW_GAME_BUTTON_RECT = (610, 90, 180, 50)

ROCK_BUTTON_RECT = (50, 500, 92, 92)
PAPER_BUTTON_RECT = (200, 500, 92, 92)
SCISSORS_BUTTON_RECT = (350, 500, 92, 92)
LIZARD_BUTTON_RECT = (500, 500, 92, 92)
SPOCK_BUTTON_RECT = (650, 500, 92, 92)

START_GAME_BUTTON_RECT = (300, 200, 200, 80)
CLEAR_SAVED_BUTTON_RECT = (300, 300, 200, 80)

OPPONENT_RECT = (0, 100, 500, 50)
RESULT_RECT = (350, 20, 100, 50)
RECORD_RECT = (10, 10, 300, 50)
CURRENT_RECT = (490, 10, 300, 50)
STREAK_RECT = (0, 450, 800, 50)

LEFT_HAND = (5, 150)
RIGHT_HAND = (445, 150)

GESTURES = {'rock': {'win': ['lizard', 'scissors']},
            'paper': {'win': ['rock', 'spock']},
            'scissors': {'win': ['lizard', 'paper']},
            'lizard': {'win': ['paper', 'spock']},
            'spock': {'win': ['rock', 'scissors']}}


SAVE_EXT = ".rps"

START_MENU = 0
RUN_GAME = 1