# -*- coding: utf-8 -*-

class TennisGame6:
    # Utilisation d'une liste SCORE_NAMES pour stocker les noms des scores, ce qui élimine la duplication de code.
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0

    def won_point(self, playerName):
        if (playerName == "player1"):
            self.player1Score += 1
        else:
            self.player2Score += 1

    def score(self):
        result: str

        if (self.player1Score == self.player2Score):
            # tie score
           tieScore: str
           tieScore = self._tie_score()
           return tieScore
        elif (self.player1Score >= 4 or self.player2Score >= 4):
            # end-game score
            endGameScore: str

            if (self.player1Score - self.player2Score == 1):
                endGameScore = "Advantage " + self.player1Name
            elif (self.player1Score - self.player2Score == -1):
                endGameScore = "Advantage " + self.player2Name
            elif (self.player1Score - self.player2Score >= 2):
                endGameScore = "Win for " + self.player1Name
            else:
                endGameScore = "Win for " + self.player2Name

            result = endGameScore
        else:
            # regular score
            regularScore: str

            match (self.player1Score):
                case 0:
                    score1 = "Love"
                case 1:
                    score1 = "Fifteen"
                case 2:
                    score1 = "Thirty"
                case _:
                    score1 = "Forty"

            match (self.player2Score):
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