import os
import unittest
from tennis6 import TennisGame6

class GoldenMasterTest(unittest.TestCase):
    #windows
    DIR = "./golden-master"
    LANG = 'en'
    #LANG = 'fr'

    @staticmethod
    def play_game(p1Points, p2Points, p1Name, p2Name, lang=LANG):
        game = TennisGame6(p1Name, p2Name, lang)
        for i in range(max(p1Points, p2Points)):
            if i < p1Points:
                game.won_point(p1Name)
            if i < p2Points:
                game.won_point(p2Name)
        return game.score()

    def make_file_name(self, score_player_1, score_player_2):
        return f"{self.DIR}/{self.LANG}/{score_player_1}_{score_player_2}.txt"

    def _test_record(self):
        # Création des répertoires si nécessaire pour assurer que les repertoires existent
        os.makedirs(f"{self.DIR}/{self.LANG}/", exist_ok=True)

        # Enregistrement des résultats de chaque partie dans des fichiers
        for score_player_1 in range(16):
            for score_player_2 in range(16):
                with self.subTest(f"{score_player_1}, {score_player_2}"):
                    score = self.play_game(score_player_1, score_player_2, "player1", "player2")
                    file_path = self.make_file_name(score_player_1, score_player_2)
                    with open(file_path, "w") as file:
                        file.writelines(score)

    def test_replay(self):
        # Vérification que les résultats rejoués correspondent aux enregistrements
        for score_player_1 in range(16):
            for score_player_2 in range(16):
                with self.subTest(f"{score_player_1}, {score_player_2}"):
                    expected_file_path = self.make_file_name(score_player_1, score_player_2)
                    # utiliser 'with' pour garantir que les fichiers sont correctement fermés même en cas d'erreur.
                    with open(expected_file_path, "r",encoding="latin-1") as expected_file:
                        expected_score = expected_file.read()
                    actual_score = self.play_game(score_player_1, score_player_2, "player1", "player2")
                    self.assertEqual(expected_score, actual_score)

if __name__ == '__main__':
    unittest.main()
