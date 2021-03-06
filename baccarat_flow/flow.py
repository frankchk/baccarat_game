import _thread
import time
from baccarat_rule.stack import Stack
from baccarat_rule.hand import Hand
from baccarat_rule.card import Card
from baccarat_flow.utility import *
from baccarat_rule.odds import Odds
from baccarat_strategy.count_card import CountCard






def play():
    player_win_count = 0
    banker_win_count = 0
    draw_count = 0
    match_counter = 0
    no_bet = 0
    human = CountCard()

    for i in range(100):
        # print("8 deck : {}".format(i+1))
        s1 = Stack(80)
        s1.shuffle()
        # s1.print()
        while s1.size() > 6:
            match_counter += 1
            # print("\n")
            # print("round {}".format(match_counter))

            bet = human.bet()
            banker_hand = Hand()
            player_hand = Hand()

            player_hand.add(s1.pop())
            banker_hand.add(s1.pop())
            player_hand.add(s1.pop())
            banker_hand.add(s1.pop())

            # print("player : ")
            # player_hand.print()
            # print("score : {}".format(hand_score(player_hand)))
            # print("banker : ")
            # banker_hand.print()
            # print("score : {}".format(hand_score(banker_hand)))
            if is_player_draw_3rd(player_hand,banker_hand):
                player_hand.add(s1.pop())
            if is_banker_draw_3rd(player_hand,banker_hand):
                banker_hand.add(s1.pop())
            if len(player_hand.card_list) > 2 or len(banker_hand.card_list) > 2:
                # print("\nAfter drawing 3rd cards")
                # print("player : ")
                # player_hand.print()
                # print("score : {}".format(hand_score(player_hand)))
                # print("banker : ")
                # banker_hand.print()
                # print("score : {}".format(hand_score(banker_hand)))
                pass


            if hand_score(banker_hand) > hand_score(player_hand):
                # print("banker win")
                winner = 0
                banker_win_count += 1
            elif hand_score(banker_hand) < hand_score(player_hand):
                # print("player win")
                winner = 1
                player_win_count += 1
            else:
                # print("draw")
                winner = 2
                draw_count += 1

            human.calculate_score(banker_hand)
            human.calculate_score(player_hand)
            # banker_hand.print()
            # player_hand.print()
            # print(human.score());



            if bet == winner:
                human.clearing(Odds.case(bet))
            elif bet == -1:
                no_bet += 1
            elif winner != 2:
                human.clearing(Odds.case(-1))
            print("bet : {} win : {} profit : {}".format(bet, winner, human.profit))
        human.reset_score()




    print("--------------------------------------------")
    print("total match : {}".format(match_counter))
    print("banker win : {}".format(banker_win_count))
    print("player win : {}".format(player_win_count))
    print("draw : {}".format(draw_count))
    print("no bet : {}".format(no_bet))
    print("human profit : {}".format(human.profit))
    print("human win : {}".format(human.win))
    print("human expectation : {}".format(human.profit/((match_counter-no_bet)*100)))

# try:
#     _thread.start_new_thread(play, ())
#     # _thread.start_new_thread(play, ())
#     # _thread.start_new_thread(play, ())
#     # _thread.start_new_thread(play, ())
#
# except:
#     print("error")
#
# while 1:
#     tim             

play()