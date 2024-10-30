import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import player


class UnitTests(unittest.TestCase):
    #print()
    #print("####Quincy#####")

    #Quincy
    def test_quincy_vs_quincy(self):
        print("Testing game quincy against quincy...")
        actual = play(quincy, quincy, 1000) >= 60

    def test_quincy_vs_abbey(self):
        print("Testing game quincy against abbey...")
        actual = play(quincy, abbey, 1000) >= 60

    def test_quincy_vs_kris(self):
        print("Testing game quincy against kris...")
        actual = play(quincy, kris, 1000) >= 60

    def test_quincy_vs_mrugesh(self):
        print("Testing game quincy against mrugesh...")
        actual = play(quincy, mrugesh, 1000) >= 60

    #print()
    #print("####Abbey#####")

    #Abbey
    def test_abbey_vs_abbey(self):
        print("Testing game abbey against abbey...")
        actual = play(abbey, abbey, 1000) >= 60

    def test_abbey_vs_quincy(self):
        print("Testing game abbey against quincy...")
        actual = play(abbey, quincy, 1000) >= 60

    def test_abbey_vs_kris(self):
        print("Testing game abbey against kris...")
        actual = play(abbey, kris, 1000) >= 60

    def test_abbey_vs_mrugesh(self):
        print("Testing game abbey against mrugesh...")
        actual = play(abbey, mrugesh, 1000) >= 60

    #print()
    #print("####Kris#####")

    #Kris
    def test_kris_vs_kris(self):
        print("Testing game kris against kris...")
        actual = play(kris, kris, 1000) >= 60

    def test_kris_vs_quincy(self):
        print("Testing game kris against quincy...")
        actual = play(kris, quincy, 1000) >= 60

    def test_kris_vs_abbey(self):
        print("Testing game kris against abbey...")
        actual = play(abbey, kris, 1000) >= 60

    def test_kris_vs_mrugesh(self):
        print("Testing game kris against mrugesh...")
        actual = play(kris, mrugesh, 1000) >= 60

    #mrugesh
    def test_mrugesh_vs_mrugesh(self):
        print("Testing game mrugesh against mrugesh...")
        actual = play(mrugesh, mrugesh, 1000) >= 60

    def test_mrugesh_vs_quincy(self):
        print("Testing game mrugesh against quincy...")
        actual = play(mrugesh, quincy, 1000) >= 60

    def test_mrugesh_abbey(self):
        print("Testing game mrugesh against abbey...")
        actual = play(mrugesh, abbey, 1000) >= 60

    def test_mrugesh_vs_kris(self):
        print("Testing game mrugesh against kris...")
        actual = play(mrugesh, kris, 1000) >= 60

if __name__ == "__main__":
    unittest.main()
