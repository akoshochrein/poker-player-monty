from ranks_points import rank_distance, RANKS_POINTS
from ranking_api import call_ranking_api

SHITTY_CARDS = ['2', '3', '4', '5', '6']
OKAY_CARDS = ['7', '8', '9', '10']
GOOD_CARDS = ['Q', 'J']
HIGH_CARDS = ['A', 'K']


class Player:
    VERSION = "ace low"

    def betRequest(self, game_state):
        player_index = game_state['in_action']
        hole_cards = game_state['players'][player_index]['hole_cards']
        ranks = [c['rank'] for c in hole_cards]
        suits = [c['suit'] for c in hole_cards]

        total_bet = 0

        # http://www.holdemsecrets.com/startinghands.htm
        # Follow this! This is our bible!

        community_cards = game_state['community_cards']
        if community_cards:
            print "Community cards are out, going to request rank from ranking API"
            ranking = call_ranking_api(hole_cards + community_cards)
            if ranking['rank'] > 3:
                print "Rank is higher than 3, going all in"
                total_bet += 100000000

        if is_pair(hole_cards) and includes_high_card(ranks):
            print "high pair (A, K): 80-85%"
            total_bet += 100000000

        if is_pair(hole_cards) and includes_good_card(ranks):
            print "medium pair (Q, J): 77-80%"
            total_bet += 100000000

        if is_pair(hole_cards) and includes_okay_card(ranks):
            print "okay pair: 65-74%"
            total_bet += 100000000

        if is_ace_face_suited(hole_cards):
            print "ace face suited: 64-66%"
            total_bet += 100000000

        if ace_face_offsuit(ranks, hole_cards):
            print "ace face offsuit: 63-65%"
            total_bet += 100000000

        if is_ace_low_suited(hole_cards):
            print "ace low suited: 55-63%"
            total_bet += 100000000

        if is_face_face_offsuit(hole_cards):
            print 'face-face offsuit: 57-60%'
            total_bet += 100000000

        if is_pair(hole_cards):
            print "low pair: 49-62%"
            total_bet += get_call_value(game_state)

        if is_king_flush_draw(hole_cards):
            print "king flush draw: 52-62%"
            total_bet += get_call_value(game_state)

        if is_ace_low_offsuit(hole_cards):
            print "ace-low offsuit: 53-61%"
            total_bet += get_call_value(game_state)

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


def is_part_of_straight(ranks):
    return rank_distance(ranks) == 1


def is_ace_face_suited(hole_cards):
    other_pair = ['K', 'Q', 'J']
    ranks = [c['rank'] for c in hole_cards]
    includes_other = any(r in other_pair for r in ranks)
    return (includes_ace(hole_cards) and includes_other) and is_same_suit(hole_cards)


def is_face_face_offsuit(hole_cards):
    ranks = [c['rank'] for c in hole_cards]
    if 'K' in ranks and ('Q' in ranks or 'J' in ranks):
        return True
    if 'Q' in ranks and 'J' in ranks:
        return True
    return False


def includes_good_card(ranks):
    return any(r in GOOD_CARDS for r in ranks)


def includes_high_card(ranks):
    return any(r in HIGH_CARDS for r in ranks)


def includes_okay_card(ranks):
    return any(r in OKAY_CARDS for r in ranks)


def is_ace_low_suited(hole_cards):
    return is_same_suit(hole_cards) and includes_ace(hole_cards) and any([RANKS_POINTS[c['rank']] <= 10 for c in hole_cards])


def get_call_value(game_state):
    player_index = game_state['in_action']
    return game_state['current_buy_in'] - game_state['players'][player_index]['bet']


def get_minimum_raise_value(game_state):
    player_index = game_state['in_action']
    return game_state['current_buy_in'] - game_state['players'][player_index]['bet'] + game_state['minimum_raise']


def ace_face_offsuit(ranks, hole_cards):
    different_suit = not is_same_suit(hole_cards)
    return different_suit and 'A' in ranks and any(r in ['K', 'Q', 'J'] for r in ranks)


def is_king_flush_draw(hole_cards):
    ranks = [c['rank'] for c in hole_cards]
    has_king = "K" in ranks
    return is_same_suit(hole_cards) and has_king

def is_ace_low_offsuit(hole_cards):
    other_card = ['7', '8', '9', '10', 'J']
    ranks = [c['rank'] for c in hole_cards]
    has_other_card = any(r in other_card for r in ranks)
    return includes_ace(hole_cards) and is_same_suit(hole_cards) and has_other_card
