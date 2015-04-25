import unittest
from player import *

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.game_state = """{
                              "players":[
                                {
                                  "name":"Player 1",
                                  "stack":1000,
                                  "status":"active",
                                  "bet":0,
                                  "hole_cards":[],
                                  "version":"Version name 1",
                                  "id":0
                                },
                                {
                                  "name":"Player 2",
                                  "stack":1000,
                                  "status":"active",
                                  "bet":0,
                                  "hole_cards":[],
                                  "version":"Version name 2",
                                  "id":1
                                }
                              ],
                              "tournament_id":"550d1d68cd7bd10003000003",
                              "game_id":"550da1cb2d909006e90004b1",
                              "round":0,
                              "bet_index":0,
                              "small_blind":10,
                              "orbits":0,
                              "dealer":0,
                              "community_cards":[],
                              "current_buy_in":0,
                              "pot":0
                            }"""

        self.player = Player()

    def test_betRequest_type_returned_integer(self):
        self.assertEqual(type(self.player.betRequest(self.game_state)), int)

    def test_is_pair(self):
        hole_cards_with_pair = [dict(rank="6", suit="hearts"), dict(rank="6", suit="spades")]

        self.assertTrue(is_pair(hole_cards_with_pair))

        hole_cards_without_pair = [dict(rank="6", suit="hearts"), dict(rank="K", suit="spades")]
        self.assertFalse(is_pair(hole_cards_without_pair))

if __name__ == "__main__":
    unittest.main()
