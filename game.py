import pickle
import pygame
import random
import sys
import os
from pygame.locals import *

from constants import *
from player import Player


class Game(object):
    ''' The game object.
    '''

    def __init__(self):
        ''' Inits pygame and displays welcome message.
        '''
        pygame.init()
        # Set up the screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Rock Paper Scissors Lizard Spock")
        self.font = pygame.font.SysFont(None, 28)

        # Loads images
        self.background = pygame.Surface(self.screen.get_size())
        self.background = pygame.image.load("src/layout_whitout.png").convert()
        # Buttons
        self.btnRock = pygame.image.load('src/rock.png').convert_alpha()
        self.btnPaper = pygame.image.load('src/paper.png').convert_alpha()
        self.btnScissors = pygame.image.load('src/scissors.png').convert_alpha()
        self.btnLizard = pygame.image.load('src/lizard.png').convert_alpha()
        self.btnSpock = pygame.image.load('src/spock.png').convert_alpha()
        #Set left hands
        self.HAND_rock = pygame.image.load('src/lRock.png').convert_alpha()
        self.HAND_paper = pygame.image.load('src/lPaper.png').convert_alpha()
        self.HAND_scissors = pygame.image.load('src/lScissors.png').convert_alpha()
        self.HAND_lizard = pygame.image.load('src/lLizard.png').convert_alpha()
        self.HAND_spock = pygame.image.load('src/lSpock.png').convert_alpha()

        self.player = None

        self.clock = pygame.time.Clock()

        self.draw_menus()

    def draw_alert(self, alert, color=BLACK):
        ''' Draws the alert box at the top 
        '''
        # First we black it out.
        self.alert = self.font.render(LONG_STRING, True, DIMGRAY, DIMGRAY)
        self.screen.blit(self.alert, (0, 0))
        # Then we print the alert
        self.alert = self.font.render(alert, True, color, DIMGRAY)
        self.screen.blit(self.alert, (0, 0))

    def draw_text_button(self, text, loc, color=WHITE, bg=DIMGRAY, outline=GREEN, thickness=6):
        ''' Draws a text button 
        '''
        loc = pygame.Rect(loc)
        button_text = self.font.render(text, True, color, bg)
        button_text_pos = button_text.get_rect()
        button_text_pos.center = loc.center

        self.screen.fill(outline, pygame.Rect(loc).inflate(thickness, thickness))
        self.screen.fill(bg, loc)
        self.screen.blit(button_text, button_text_pos)

    def draw_status_box(self, text, loc, color=WHITE, bg=DIMGRAY, outline=WHITE, thickness=4):
        ''' Draws a text button 
        '''
        loc = pygame.Rect(loc)
        button_text = self.font.render(text, True, color, bg)
        button_text_pos = button_text.get_rect()
        button_text_pos.center = loc.center

        self.screen.fill(outline, pygame.Rect(loc).inflate(thickness, thickness))
        self.screen.fill(bg, loc)
        self.screen.blit(button_text, button_text_pos)

    def draw_btn(self, bg, loc):
        self.screen.blit(bg, loc)

    def handle_quit(self):
        '''Handle a user invoked quit.
        '''
        if self.player:
            self.save_player_stats(self.player)
        sys.exit()

    def save_player_stats(self, player):
        try:
            f = open(self.player.name + SAVE_EXT, "w")
        except:
            return
        pickle.dump(player, f, 2)
        f.close()

    def load_player(self, name):
        f = open(name + SAVE_EXT, "r")
        player = pickle.load(f)
        f.close()
        return player

    def clear_player_status(self):
        os.remove("Guest.rps")

    def draw_hand(self, play, pos):
        self.hand = eval("self.HAND_"+play)
        if pos == RIGHT_HAND:
            self.hand = pygame.transform.flip(self.hand, True, False)
        self.screen.blit(self.hand, pos)


    def draw_computer_play(self, play):
        self.draw_hand(play, RIGHT_HAND)

    def computer_play(self):
        play = random.sample((ROCK, PAPER, SCISSORS, LIZARD, SPOCK), 1)
        self.draw_computer_play(play[0])
        return play[0]

    def display_winner(self):
        ret_val = self.determine_winner()
        if ret_val == 0:
            self.handle_tie()
        elif ret_val == 1:
            self.handle_win()
        elif ret_val == -1:
            self.handle_loss()

    def handle_tie(self):
        self.draw_status_box("It was a tie", RESULT_RECT)
        self.player.tie()

    def handle_win(self):
        self.draw_status_box("You won!", RESULT_RECT)
        self.player.win()

    def handle_loss(self):
        self.draw_status_box("You lost!", RESULT_RECT)
        self.player.lose()

    def determine_winner(self):
        if self.player_pick == self.computer_pick:
            return 0
        if GESTURES.get(self.player_pick):
            if self.computer_pick in GESTURES[self.player_pick]['win']:
                return 1
            else:
                return -1
        else:
            raise Exception('Gesture not found in dict.')


    def display_record(self):
        self.draw_status_box(
            "Record: {0}W - {1}L - {2}T".format(self.player.wins, self.player.losses, self.player.ties), RECORD_RECT)

    def display_streaks(self):
        if self.player.current_win_streak:
            self.draw_status_box("Current Streak: {0} Wins".format(self.player.current_win_streak), CURRENT_RECT)
        elif self.player.current_loss_streak:
            self.draw_status_box("Current Streak: {0} Losses".format(self.player.current_loss_streak), CURRENT_RECT)
        elif self.player.current_tie_streak:
            self.draw_status_box("Current Streak: {0} Ties".format(self.player.current_tie_streak), CURRENT_RECT)

        self.draw_status_box("Longest Streaks: {0} Wins {1} Losses {2} Ties".format(self.player.longest_win_streak,
                                                                                    self.player.longest_loss_streak,
                                                                                    self.player.longest_tie_streak),
                             STREAK_RECT)

    def play(self, choice):
        self.player_pick = choice
        self.draw_hand(choice, LEFT_HAND)
        self.computer_pick = self.computer_play()
        self.display_winner()

    def clear_screen(self):
        self.screen = pygame.display.set_mode((800, 600))

    def screen_background(self):
        self.screen.blit(self.background, [0, 0])

    def draw_menus(self):
        self.clear_screen()
        self.game_state = START_MENU
        self.screen_background()
        self.draw_alert("Welcome to Rock Paper Scissors Lizard Spock!")
        self.draw_text_button("Start Game", START_GAME_BUTTON_RECT)
        self.draw_text_button("Clear saved games",CLEAR_SAVED_BUTTON_RECT)
        self.event_loop()

    def start_menu(self):
        ''' The start menu.
        '''
        while 1:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.handle_quit()
                        # Command Q
                    if event.key == 113 and event.mod in [1024, 2048]:
                        self.handle_quit()
                        # Alt-F4 (Quit)
                    if event.key == 285 and event.mod in [4352, 4608]:
                        self.handle_quit()
                        # o key
                    if event.key == K_o:
                        self.draw_alert("Options:")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if pygame.Rect(START_GAME_BUTTON_RECT).collidepoint(event.pos):
                            self.start_game()
                        if pygame.Rect(CLEAR_SAVED_BUTTON_RECT).collidepoint(event.pos):
                            self.clear_player_status()
                            self.draw_alert("All save cleaned")
                if event.type == pygame.QUIT:
                    self.handle_quit()

            pygame.display.flip()

    def run_game(self):
        ''' The main loop of the game.
        '''

        while 1:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.handle_quit()
                        # Command Q
                    if event.key == 113 and event.mod in [1024, 2048]:
                        self.handle_quit()
                        # Alt-F4 (Quit)
                    if event.key == 285 and event.mod in [4352, 4608]:
                        self.handle_quit()
                        # o key
                    if event.key == K_r:
                        self.play(ROCK)
                    if event.key == K_p:
                        self.play(PAPER)
                    if event.key == K_s:
                        self.play(SCISSORS)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if pygame.Rect(ROCK_BUTTON_RECT).collidepoint(event.pos):
                            self.play(ROCK)
                        if pygame.Rect(PAPER_BUTTON_RECT).collidepoint(event.pos):
                            self.play(PAPER)
                        if pygame.Rect(SCISSORS_BUTTON_RECT).collidepoint(event.pos):
                            self.play(SCISSORS)
                        if pygame.Rect(LIZARD_BUTTON_RECT).collidepoint(event.pos):
                            self.play(LIZARD)
                        if pygame.Rect(SPOCK_BUTTON_RECT).collidepoint(event.pos):
                            self.play(SPOCK)

                        if pygame.Rect(MAIN_MENU_BUTTON_RECT).collidepoint(event.pos):
                            self.save_player_stats(self.player)
                            self.draw_menus()

                        if pygame.Rect(NEW_GAME_BUTTON_RECT).collidepoint(event.pos):
                            self.start_game()

                if event.type == pygame.QUIT:
                    self.handle_quit()

            self.display_record()
            self.display_streaks()
            pygame.display.flip()

    def start_game(self):
        self.clear_screen()
        self.game_state = RUN_GAME
        self.screen_background()
        self.player_pick = None
        self.computer_pick = None

        try:
            self.player = self.load_player("Guest")
        except:
            self.player = Player("Guest")

        self.draw_btn(self.btnRock, ROCK_BUTTON_RECT)
        self.draw_btn(self.btnPaper, PAPER_BUTTON_RECT)
        self.draw_btn(self.btnScissors, SCISSORS_BUTTON_RECT)
        self.draw_btn(self.btnLizard, LIZARD_BUTTON_RECT)
        self.draw_btn(self.btnSpock, SPOCK_BUTTON_RECT)

        self.draw_text_button("Main Menu", MAIN_MENU_BUTTON_RECT)
        self.draw_text_button("New Game", NEW_GAME_BUTTON_RECT)

        self.event_loop()

    def event_loop(self):
        if self.game_state == START_MENU:
            self.start_menu()
        elif self.game_state == RUN_GAME:
            self.run_game()
