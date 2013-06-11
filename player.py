from constants import *

class Player(object):
    def __init__(self, name):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.name = name
        self.longest_win_streak = 0
        self.longest_loss_streak = 0
        self.longest_tie_streak = 0
        self.current_win_streak = 0
        self.current_loss_streak = 0
        self.current_tie_streak = 0
        
    def win(self):
        self.wins += 1
        self.current_win_streak += 1
        self.current_loss_streak = 0
        self.current_tie_streak = 0
        if self.current_win_streak > self.longest_win_streak:
            self.longest_win_streak = self.current_win_streak
    def lose(self):
        self.losses += 1
        self.current_win_streak = 0
        self.current_loss_streak += 1
        self.current_tie_streak = 0
        if self.current_loss_streak > self.longest_loss_streak:
            self.longest_loss_streak = self.current_loss_streak
    def tie(self):
        self.ties += 1
        self.current_win_streak = 0
        self.current_loss_streak = 0
        self.current_tie_streak += 1
        if self.current_tie_streak > self.longest_tie_streak:
            self.longest_tie_streak = self.current_tie_streak