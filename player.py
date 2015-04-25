
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        return 1000

    def showdown(self, game_state):
        pass


def is_pair(hole_cards):
    return hole_cards[0]["rank"] == hole_cards[1]["rank"]
