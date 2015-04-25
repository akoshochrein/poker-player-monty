SHITTY_CARDS = ['2', '3', '4', '5', '6']
OKAY_CARDS = ['7', '8', '9', '10']
GOOD_CARDS = ['A', 'K', 'Q', 'J']

class Player:
    VERSION = "NO FOLDS LOL"

    def betRequest(self, game_state):
        player_index = game_state['in_action']
        hole_cards = game_state['players'][player_index]['hole_cards']
        ranks = [c['rank'] for c in hole_cards]

        total_bet = 0
        if includes_high_symbol(ranks) or is_pair(hole_cards):
            print '##### hole hand A'
            total_bet += 1000
        if includes_okay_cards(ranks):
            total_bet += 500
        return total_bet

    def showdown(self, game_state):
        pass

def is_pair(hole_cards):
    return hole_cards[0]["rank"] == hole_cards[1]["rank"]


def includes_symbol(ranks):
    return any(r in GOOD_CARDS for r in ranks)


def includes_high_symbol(ranks):
    symbols = ['A', 'K']
    return any(r in symbols for r in ranks)

def includes_okay_cards(ranks):
    return any(r in OKAY_CARDS for r in ranks)

def get_call_value(game_state):
    player_index = game_state['in_action']
    return game_state['current_buy_in'] - game_state['players'][player_index]['bet']


def get_minimum_raise_value(game_state):
    player_index = game_state['in_action']
    return game_state['current_buy_in'] - game_state['players'][player_index]['bet'] + game_state['minimum_raise']

