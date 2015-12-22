from pokerpack.deucesmaster.deuces.card import Card
from pokerpack.deucesmaster.deuces.evaluator import Evaluator
from pokerpack.deucesmaster.deuces.evaluator import Deck
from random import choice

'''
This is a MonteCarlo-Simulation for Texas Holdem Poker!
Download packages from: https://github.com/worldveil/deuces

For testing you should update his packages to Python 3.

# How to use the class:

mc = MonteCarlo(times=10000)                                    # 'times' says how many times it should play
equity = mc.preflop(card1='Ad', card2='Ah', total_villains=4)   # Calculates the equity off ace of diamond and ace of hearts when you play against 4 opponents.

print('Equity:', round(equity*100, 3), '%')                     # Prints out the quity in formatted form!

# This Monte Carlo is really slow however I did it for fun :) !
# If you know a better way or want to teach me something go ahead :) :D !!!!

'''


class MonteCarlo(object):
    ''' Monte Carlo Simulation '''

    def __init__(self, times):
        self.times = times
        self.deck = Deck.GetFullDeck()
        self.evaluator = Evaluator()

    def _draw_random_board(self, deck, stage='preflop'):
        ''' Draws a random board! '''
        if stage == 'preflop':
            # FLOP ----------------------------------------
            f_card1 = deck.pop(deck.index(choice(deck)))
            f_card2 = deck.pop(deck.index(choice(deck)))
            f_card3 = deck.pop(deck.index(choice(deck)))

            # TURN ----------------------------------------
            t_card1 = deck.pop(deck.index(choice(deck)))

            # RIVER ---------------------------------------
            r_card1 = deck.pop(deck.index(choice(deck)))

            return [f_card1, f_card2, f_card3, t_card1, r_card1]

        elif stage == 'flop':
            # TURN -----------------------------------------
            t_card1 = deck.pop(deck.index(choice(deck)))

            # RIVER ----------------------------------------
            r_card1 = deck.pop(deck.index(choice(deck)))

            return [t_card1, r_card1]

        elif stage == 'turn':
            # RIVER ----------------------------------------
            r_card1 = deck.pop(deck.index(choice(deck)))

            return [r_card1]

    def _draw_villain_hand(self, deck):
        ''' Draws a random hand for the villain!'''

        v_card1 = deck.pop(deck.index(choice(deck)))
        v_card2 = deck.pop(deck.index(choice(deck)))

        return [v_card1, v_card2]

    def _draw_my_hand(self, deck, card1, card2):
        ''' Draw my hand! '''

        me_card1 = deck.pop(deck.index(Card.new(card1)))
        me_card2 = deck.pop(deck.index(Card.new(card2)))

        return [me_card1, me_card2]

    def preflop(self, card1, card2, total_villains=1):
        ''' Evaluates the preflop situation and returns the equity'''

        eval_cards = self.evaluator.evaluate
        draw_villain = self._draw_villain_hand
        draw_myhand = self._draw_my_hand
        draw_board = self._draw_random_board
        

        v1_score,\
        v2_score,\
        v3_score,\
        v4_score,\
        v5_score,\
        v6_score,\
        v7_score,\
        v8_score,\
        v9_score = 7463, 7463, 7463, 7463, 7463, 7463, 7463, 7463, 7463

        losecount = 0
        for games in range(self.times):
            full_deck = self.deck[:]

            # ME------------------------------------------
            me_hand = draw_myhand(deck=full_deck, card1=card1, card2=card2)

            # Board --------------------------------------
            board = draw_board(deck=full_deck, stage='preflop')

            me_score = eval_cards(all_cards=me_hand+board)

            # VILLAIN 1 -----------------------------------
            if total_villains >= 1:
                villain1_hand = draw_villain(deck=full_deck)
                v1_score = eval_cards(all_cards=villain1_hand+board)

            # VILLAIN 2 -----------------------------------
            if total_villains >= 2:
                villain2_hand = draw_villain(deck=full_deck)
                v2_score = eval_cards(all_cards=villain2_hand+board)

            # VILLAIN 3 -----------------------------------
            if total_villains >= 3:
                villain3_hand = draw_villain(deck=full_deck)
                v3_score = eval_cards(all_cards=villain3_hand+board)

            # VILLAIN 4 -----------------------------------
            if total_villains >= 4:
                villain4_hand = draw_villain(deck=full_deck)
                v4_score = eval_cards(all_cards=villain4_hand+board)

            # VILLAIN 5 -----------------------------------
            if total_villains >= 5:
                villain5_hand = draw_villain(deck=full_deck)
                v5_score = eval_cards(all_cards=villain5_hand+board)

            # VILLAIN 6 -----------------------------------
            if total_villains >= 6:
                villain6_hand = draw_villain(deck=full_deck)
                v6_score = eval_cards(all_cards=villain6_hand+board)

            # VILLAIN 7 -----------------------------------
            if total_villains >= 7:
                villain7_hand = draw_villain(deck=full_deck)
                v7_score = eval_cards(all_cards=villain7_hand+board)

            # VILLAIN 8 -----------------------------------
            if total_villains >= 8:
                villain8_hand = draw_villain(deck=full_deck)
                v8_score = eval_cards(all_cards=villain8_hand+board)

            # VILLAIN 9 -----------------------------------
            if total_villains >= 9:
                villain9_hand = draw_villain(deck=full_deck)
                v9_score = eval_cards(all_cards=villain9_hand+board)

            if me_score > v1_score or\
                            me_score > v2_score or\
                            me_score > v3_score or\
                            me_score > v4_score or\
                            me_score > v5_score or\
                            me_score > v6_score or\
                            me_score > v7_score or\
                            me_score > v8_score or\
                            me_score > v9_score:
                losecount += 1

        return 1 - losecount/self.times

    def flop(self, card1, card2, fcard1, fcard2, fcard3, total_villains=1):
        ''' Evaluates the flop situation and returns the equity'''

        eval_cards = self.evaluator.evaluate
        draw_villain = self._draw_villain_hand
        # Define the score 7463 because of the comparision at the bottom
        v1_score,\
        v2_score,\
        v3_score,\
        v4_score,\
        v5_score,\
        v6_score,\
        v7_score,\
        v8_score,\
        v9_score = 7463, 7463, 7463, 7463, 7463, 7463, 7463, 7463, 7463

        losecount = 0
        for games in range(self.times):
            full_deck = self.deck[:]
            # ME------------------------------------------
            me_hand = draw_myhand(full_deck, card1, card2)

            # BOARD --------------------------------------
            f1 = full_deck.pop(full_deck.index(Card.new(fcard1)))
            f2 = full_deck.pop(full_deck.index(Card.new(fcard2)))
            f3 = full_deck.pop(full_deck.index(Card.new(fcard3)))

            board = [f1, f2, f3]
            board.extend(draw_board(full_deck, stage='flop'))

            me_score = eval_cards(me_hand+board)

             # VILLAIN 1 -----------------------------------
            if total_villains >= 1:
                villain1_hand = draw_villain(full_deck)
                v1_score = eval_cards(villain1_hand+board)

            # VILLAIN 2 -----------------------------------
            if total_villains >= 2:
                villain2_hand = draw_villain(full_deck)
                v2_score = eval_cards(villain2_hand+board)

            # VILLAIN 3 -----------------------------------
            if total_villains >= 3:
                villain3_hand = draw_villain(full_deck)
                v3_score = eval_cards(villain3_hand+board)

            # VILLAIN 4 -----------------------------------
            if total_villains >= 4:
                villain4_hand = draw_villain(full_deck)
                v4_score = eval_cards(villain4_hand+board)

            # VILLAIN 5 -----------------------------------
            if total_villains >= 5:
                villain5_hand = draw_villain(full_deck)
                v5_score = eval_cards(villain5_hand+board)

            # VILLAIN 6 -----------------------------------
            if total_villains >= 6:
                villain6_hand = draw_villain(full_deck)
                v6_score = eval_cards(villain6_hand+board)

            # VILLAIN 7 -----------------------------------
            if total_villains >= 7:
                villain7_hand = draw_villain(full_deck)
                v7_score = eval_cards(villain7_hand+board)

            # VILLAIN 8 -----------------------------------
            if total_villains >= 8:
                villain8_hand = draw_villain(full_deck)
                v8_score = eval_cards(villain8_hand+board)

            # VILLAIN 9 -----------------------------------
            if total_villains >= 9:
                villain9_hand = draw_villain(full_deck)
                v9_score = eval_cards(villain9_hand+board)

            if me_score > v1_score or\
                            me_score > v2_score or\
                            me_score > v3_score or\
                            me_score > v4_score or\
                            me_score > v5_score or\
                            me_score > v6_score or\
                            me_score > v7_score or\
                            me_score > v8_score or\
                            me_score > v9_score:
                losecount += 1

        return 1 - losecount/self.times

    def turn(self, card1, card2, fcard1, fcard2, fcard3, tcard, total_villains=1):
        ''' Evaluates the turn situation and returns the equity'''

        eval_cards = self.evaluator.evaluate
        draw_villain = self._draw_villain_hand
        v1_score,\
        v2_score,\
        v3_score,\
        v4_score,\
        v5_score,\
        v6_score,\
        v7_score,\
        v8_score,\
        v9_score = 7463, 7463, 7463, 7463, 7463, 7463, 7463, 7463, 7463

        games = 0
        losecount = 0
        for games in range(self.times):
            full_deck = self.deck[:]
            # ME------------------------------------------
            me_hand = draw_myhand(full_deck, card1, card2)

            # BOARD --------------------------------------
            f1 = full_deck.pop(full_deck.index(Card.new(fcard1)))
            f2 = full_deck.pop(full_deck.index(Card.new(fcard2)))
            f3 = full_deck.pop(full_deck.index(Card.new(fcard3)))
            t = full_deck.pop(full_deck.index(Card.new(tcard)))

            board = [f1, f2, f3, t]

            board.extend(draw_board(full_deck, stage='turn'))

            me_score = eval_cards(me_hand+board)

             # VILLAIN 1 -----------------------------------
            if total_villains >= 1:
                villain1_hand = draw_villain(full_deck)
                v1_score = eval_cards(villain1_hand+board)

            # VILLAIN 2 -----------------------------------
            if total_villains >= 2:
                villain2_hand = draw_villain(full_deck)
                v2_score = eval_cards(villain2_hand+board)

            # VILLAIN 3 -----------------------------------
            if total_villains >= 3:
                villain3_hand = draw_villain(full_deck)
                v3_score = eval_cards(villain3_hand+board)

            # VILLAIN 4 -----------------------------------
            if total_villains >= 4:
                villain4_hand = draw_villain(full_deck)
                v4_score = eval_cards(villain4_hand+board)

            # VILLAIN 5 -----------------------------------
            if total_villains >= 5:
                villain5_hand = draw_villain(full_deck)
                v5_score = eval_cards(villain5_hand+board)

            # VILLAIN 6 -----------------------------------
            if total_villains >= 6:
                villain6_hand = draw_villain(full_deck)
                v6_score = eval_cards(villain6_hand+board)

            # VILLAIN 7 -----------------------------------
            if total_villains >= 7:
                villain7_hand = draw_villain(full_deck)
                v7_score = eval_cards(villain7_hand+board)

            # VILLAIN 8 -----------------------------------
            if total_villains >= 8:
                villain8_hand = draw_villain(full_deck)
                v8_score = eval_cards(villain8_hand+board)

            # VILLAIN 9 -----------------------------------
            if total_villains >= 9:
                villain9_hand = draw_villain(full_deck)
                v9_score = eval_cards(villain9_hand+board)

            if me_score > v1_score or\
                            me_score > v2_score or\
                            me_score > v3_score or\
                            me_score > v4_score or\
                            me_score > v5_score or\
                            me_score > v6_score or\
                            me_score > v7_score or\
                            me_score > v8_score or\
                            me_score > v9_score:
                losecount += 1

        return 1 - losecount/self.times

    def river(self, card1, card2, fcard1, fcard2, fcard3, tcard, rcard, total_villains=1):
        ''' Evaluates the river situation and returns the equity'''
        eval_cards = self.evaluator.evaluate
        draw_villain = self._draw_villain_hand
        v1_score,\
        v2_score,\
        v3_score,\
        v4_score,\
        v5_score,\
        v6_score,\
        v7_score,\
        v8_score,\
        v9_score = 7463, 7463, 7463, 7463, 7463, 7463, 7463, 7463, 7463

        games = 0
        losecount = 0
        for games in range(self.times):
            full_deck = self.deck[:]
            # ME------------------------------------------
            me_hand = draw_myhand(full_deck, card1, card2)

            # BOARD --------------------------------------
            f1 = full_deck.pop(full_deck.index(Card.new(fcard1)))
            f2 = full_deck.pop(full_deck.index(Card.new(fcard2)))
            f3 = full_deck.pop(full_deck.index(Card.new(fcard3)))
            t = full_deck.pop(full_deck.index(Card.new(tcard)))
            r = full_deck.pop(full_deck.index(Card.new(rcard)))

            board = [f1, f2, f3, t, r]

            me_score = eval_cards(me_hand+board)

             # VILLAIN 1 -----------------------------------
            if total_villains >= 1:
                villain1_hand = draw_villain(full_deck)
                v1_score = eval_cards(villain1_hand+board)

            # VILLAIN 2 -----------------------------------
            if total_villains >= 2:
                villain2_hand = draw_villain(full_deck)
                v2_score = eval_cards(villain2_hand+board)

            # VILLAIN 3 -----------------------------------
            if total_villains >= 3:
                villain3_hand = draw_villain(full_deck)
                v3_score = eval_cards(villain3_hand+board)

            # VILLAIN 4 -----------------------------------
            if total_villains >= 4:
                villain4_hand = draw_villain(full_deck)
                v4_score = eval_cards(villain4_hand+board)

            # VILLAIN 5 -----------------------------------
            if total_villains >= 5:
                villain5_hand = draw_villain(full_deck)
                v5_score = eval_cards(villain5_hand+board)

            # VILLAIN 6 -----------------------------------
            if total_villains >= 6:
                villain6_hand = draw_villain(full_deck)
                v6_score = eval_cards(villain6_hand+board)

            # VILLAIN 7 -----------------------------------
            if total_villains >= 7:
                villain7_hand = draw_villain(full_deck)
                v7_score = eval_cards(villain7_hand+board)

            # VILLAIN 8 -----------------------------------
            if total_villains >= 8:
                villain8_hand = draw_villain(full_deck)
                v8_score = eval_cards(villain8_hand+board)

            # VILLAIN 9 -----------------------------------
            if total_villains >= 9:
                villain9_hand = draw_villain(full_deck)
                v9_score = eval_cards(villain9_hand+board)

            if me_score > v1_score or\
                            me_score > v2_score or\
                            me_score > v3_score or\
                            me_score > v4_score or\
                            me_score > v5_score or\
                            me_score > v6_score or\
                            me_score > v7_score or\
                            me_score > v8_score or\
                            me_score > v9_score:
                losecount += 1

        return 1 - losecount/self.times


