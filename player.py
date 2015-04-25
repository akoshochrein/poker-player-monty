
class Player:
    VERSION = "NO FOLDS LOL"

    def betRequest(self, game_state):
        player_index = game_state['in_action']
        hole_cards = game_state['players'][player_index]['hole_cards']
        ranks = [c['rank'] for c in hole_cards]
        if 'A' in ranks or 'K' in ranks or 'Q' in ranks or 'J' in ranks:
            print '##### hole hand A'
            return 1000
        return 500

    def showdown(self, game_state):
        pass


def is_pair(hole_cards):
    return hole_cards[0]["rank"] == hole_cards[1]["rank"]

def get_call_value(game_state):
    return current_buy_in - players[in_action][bet]

def get_minimum_raise_value(game_state):
    return current_buy_in - players[in_action][bet] + minimum_raise
