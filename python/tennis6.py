# -*- coding: utf-8 -*-

class TennisGame6:
    # Utilisation d'une liste SCORE_NAMES pour stocker les noms des scores, ce qui élimine la duplication de code.
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1Name = player1_name
        self.player2Name = player2_name
        self.player1Score = 0
        self.player2Score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1Score += 1
        else:
            self.player2Score += 1

    def score(self):
        result: str

        if self.player1Score == self.player2Score:
            # tie score
           tie_score: str
           tie_score = self._tie_score()
           return tie_score
        elif self.player1Score >= 4 or self.player2Score >= 4:
            # end-game score
            end_game_score: str
            end_game_score = self._end_game_score()
            return end_game_score
        else:
            # regular score
            regularScore: str

            match self.player1Score:
                case 0:
                    score1 = "Love"
                case 1:
                    score1 = "Fifteen"
                case 2:
                    score1 = "Thirty"
                case _:
                    score1 = "Forty"

            match self.player2Score:
                case 0:
                    score2 = "Love"
                case 1:
                    score2 = "Fifteen"
                case 2:
                    score2 = "Thirty"
                case _:
                    score2 = "Forty"

            regularScore = score1 + "-" + score2

            result = regularScore

        return result

    def _tie_score(self):
        if self.player1Score < 3:
            return TennisGame6.SCORE_NAMES[self.player1Score] + "-All"
        else:
            return "Deuce"

    def _end_game_score(self):
        score_diff = self.player1Score - self.player2Score
        if abs(score_diff) == 1:
            leader = self.player1Name if score_diff == 1 else self.player2Name
            return "Advantage " + leader
        else:
            winner = self.player1Name if score_diff >= 2 else self.player2Name
            return "Win for " + winner