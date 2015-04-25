SHITTY_CARDS = ['2', '3', '4', '5', '6']
OKAY_CARDS = ['7', '8', '9', '10']
GOOD_CARDS = ['Q', 'J']
HIGH_CARDS = ['A', 'K']

class Player:
    VERSION = "NO FOLDS LOL"

    def betRequest(self, game_state):
        player_index = game_state['in_action']
        hole_cards = game_state['players'][player_index]['hole_cards']
        ranks = [c['rank'] for c in hole_cards]

        total_bet = 0
        if is_pair(hole_cards):
            print "pair"
            total_bet += 500

        if includes_high_card(ranks):
            print "high card"
            total_bet += 500

        if includes_good_card(ranks):
            print "good card"
            total_bet += 300

        if includes_okay_card(ranks):
            print "okay card"
            total_bet += 200
        
        return int(total_bet)

    def showdown(self, game_state):
        pass

def is_pair(hole_cards):
    return hole_cards[0]["rank"] == hole_cards[1]["rank"]


def includes_good_card(ranks):
    return any(r in GOOD_CARDS for r in ranks)


def includes_high_card(ranks):
    symbols = ['A', 'K']
    return any(r in HIGH_CARDS for r in ranks)


def includes_okay_card(ranks):
    return any(r in OKAY_CARDS for r in ranks)


def get_call_value(game_state):
    player_index = game_state['in_action']
    return game_state['current_buy_in'] - game_state['players'][player_index]['bet']


def get_minimum_raise_value(game_state):
    player_index = game_state['in_action']
    return game_state['current_buy_in'] - game_state['players'][player_index]['bet'] + game_state['minimum_raise']

