import unittest
import json as simplejson
from player import *
from ranks_points import rank_distance

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.game_state = simplejson.loads("""{
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
                                  "hole_cards":[
                                  {
                                      "rank": "A",
                                      "suit": "hearts"
                                  },
                                  {
                                      "rank": "K",
                                      "suit": "spades"
                                  }],
                                  "version":"Version name 2",
                                  "id":1
                                }
                              ],
                              "in_action": 1,
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
                            }""")
        self.hole_cards = self.game_state['players'][1]['hole_cards']
        self.hole_cards2 = [
                            {
                                "rank": "A",
                                "suit": "hearts"
                            },
                            {
                                "rank": "K",
                                "suit": "hearts"
                            }]
        self.hole_cards3 = [
                            {
                                "rank": "Q",
                                "suit": "hearts"
                            },
                            {
                                "rank": "K",
                                "suit": "hearts"
                            }]
        self.player = Player()

    def test_betRequest_type_returned_integer(self):
      self.assertEqual(type(self.player.betRequest(self.game_state)), int)

    def test_is_pair(self):
      hole_cards_with_pair = [dict(rank="6", suit="hearts"), dict(rank="6", suit="spades")]
      self.assertTrue(is_pair(hole_cards_with_pair))

      hole_cards_without_pair = [dict(rank="6", suit="hearts"), dict(rank="K", suit="spades")]
      self.assertFalse(is_pair(hole_cards_without_pair))

    def test_get_call_value(self):
      self.assertEqual(get_call_value(self.game_state), 0)

    def test_includes_high_card(self):
      self.assertTrue(includes_high_card(['A']))
      self.assertTrue(includes_high_card(['K']))

    def test_includes_good_card(self):
      self.assertTrue(includes_good_card(['Q']))
      self.assertTrue(includes_good_card(['J']))
      self.assertFalse(includes_good_card(['10']))

    def test_is_same_suit(self):
      self.assertFalse(is_same_suit(self.hole_cards))

    def test_includes_ace(self):
      self.assertTrue(includes_ace(self.hole_cards))

    def test_is_ace_face_suited(self):
      self.assertFalse(is_ace_face_suited(self.hole_cards))
      self.assertTrue(is_ace_face_suited(self.hole_cards2))

    def test_ace_face_offsuit(self):
        self.assertTrue(ace_face_offsuit(['A', 'K'], [dict(rank="A", suit="hearts"), dict(rank="K", suit="spades")]))
        self.assertFalse(ace_face_offsuit(['A', '10'], [dict(rank="A", suit="hearts"), dict(rank="K", suit="spades")]))
        self.assertFalse(ace_face_offsuit(['A', 'A'], [dict(rank="A", suit="hearts"), dict(rank="A", suit="spades")]))
        self.assertFalse(ace_face_offsuit(['K', 'K'], [dict(rank="K", suit="hearts"), dict(rank="K", suit="spades")]))

    def test_ace_low_suited(self):
        self.assertTrue(is_ace_low_suited([dict(rank="A", suit="hearts"), dict(rank="2", suit="hearts")]))
        self.assertFalse(is_ace_low_suited([dict(rank="A", suit="hearts"), dict(rank="2", suit="spades")]))
        self.assertFalse(is_ace_low_suited([dict(rank="A", suit="hearts"), dict(rank="K", suit="hearts")]))

    def test_ranks_distance(self):
        self.assertEqual(rank_distance(['2', '3']), 1)
        self.assertEqual(rank_distance(['3', '2']), 1)
        self.assertEqual(rank_distance(['K', 'Q']), 1)
        self.assertEqual(rank_distance(['A', 'Q']), 2)

    def test_is_face_face_offsuit(self):
        self.assertFalse(is_face_face_offsuit(self.hole_cards))
        self.assertTrue(is_face_face_offsuit(self.hole_cards3))
        self.assertTrue(is_face_face_offsuit([dict(rank="J", suit="hearts"), dict(rank="K", suit="diamonds")]))

    def test_is_king_flush_draw(self):
        self.assertFalse(is_king_flush_draw(self.hole_cards))
        self.assertTrue(is_king_flush_draw([dict(rank="J", suit="hearts"), dict(rank="K", suit="hearts")]))

if __name__ == "__main__":
    unittest.main()
