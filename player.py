SHITTY_CARDS = ['2', '3', '4', '5', '6']
OKAY_CARDS = ['7', '8', '9', '10']
GOOD_CARDS = ['Q', 'J']
HIGH_CARDS = ['A', 'K']

class Player:
    VERSION = "fuck ok"

    def betRequest(self, game_state):
        player_index = game_state['in_action']
        hole_cards = game_state['players'][player_index]['hole_cards']
        ranks = [c['rank'] for c in hole_cards]
        suits = [c['suit'] for c in hole_cards]

        total_bet = 0

        # http://www.holdemsecrets.com/startinghands.htm
        # Follow this! This is our bible!

        if is_pair(hole_cards) and includes_high_card(ranks):
            print "high pair -- ALL IN"
            total_bet += 100000000

        if is_pair(hole_cards) and includes_good_card(ranks):
            print "good pair -- ALL IN"
            total_bet += 100000000

        if is_ace_face_suited(hole_cards):
            print "ace face suited"
            total_bet += 100000000

        if is_pair(hole_cards):
            print "pair"
            total_bet += 500

        if includes_high_card(ranks):
            print "high card"
            total_bet += 500

        if includes_good_card(ranks):
            print "good card"
            total_bet += 300

        if is_same_suit(hole_cards):
            print "same suit"
            total_bet += 100
        
        print total_bet, hole_cards
        return int(total_bet)

    def showdown(self, game_state):
        pass

def is_pair(hole_cards):
    return hole_cards[0]["rank"] == hole_cards[1]["rank"]


def is_same_suit(hole_cards):
    return hole_cards[0]["suit"] == hole_cards[1]["suit"]


def includes_ace(hole_cards):
    if hole_cards[0]['rank'] == 'A':
        return True
    if hole_cards[1]['rank'] == 'A':
        return True
    return False


def is_ace_face_suited(hole_cards):
    other_pair = ['K', 'Q', 'J']
    ranks = [c['rank'] for c in hole_cards]
    includes_other = any(r in other_pair for r in ranks)
    return (includes_ace(hole_cards) and includes_other) and is_same_suit(hole_cards)


def includes_good_card(ranks):
    return any(r in GOOD_CARDS for r in ranks)


def includes_high_card(ranks):
    return any(r in HIGH_CARDS for r in ranks)


def includes_okay_card(ranks):
    return any(r in OKAY_CARDS for r in ranks)


def get_call_value(game_state):
    player_index = game_state['in_action']
    return game_state['current_buy_in'] - game_state['players'][player_index]['bet']


def get_minimum_raise_value(game_state):
    player_index = game_state['in_action']
    return game_state['current_buy_in'] - game_state['players'][player_index]['bet'] + game_state['minimum_raise']


def ace_face_offsuit(ranks, hole_cards):
    different_suit = not is_same_suit(hole_cards)
    return different_suit and 'A' in ranks and any(r in ['K', 'Q', 'J'] for r in ranks)
