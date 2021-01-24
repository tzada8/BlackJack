# This module has all the paragraphs of text for the Instructions manual

page1_title_text = "BLACKJACK"
page1_text = """
The goal of BlackJack is to win as much 
money as possible from the dealer. 
You must achieve this by betting money 
at the beginning of each round and having 
a higher hand worth than the dealer.
Enjoy the game!
"""

page2_title_text = "BETTING AND CHIPS"
page2_text = """
You start off the entire game with $1000, 
and from there, you can either gain money 
or lose it all and end with $0. To play a 
round, you must place a bet before the 
round begins; no bet, no play. A bet can 
range anywhere from $1 all the way to ALL 
IN. Bets can be placed by clicking on your 
chips (you can click on the RESET button 
to reset a bet). However, once cards are 
dealt, bets cannot be taken back. So bet 
wisely!
"""

page3_title_text = "DEAL"
page3_text = """
Once happy with you bet, click DEAL, and 
the dealer will deal you two cards which 
will form your hand, and two cards to 
themselves. You can immediately see both 
your cards, and only one of the dealers 
cards. To win, you need to ensure your 
combined value of cards is greater than the 
dealers combined value, while also not going 
over a total value of 21.
"""

page4_title_text = "DOUBLE BET (X2)"
page4_text = """
After placing your bets and receiving your 
cards, there is an option to double your bet 
(X2). You can only double your bet on the 
first turn, which will cause you to 
pickup exactly one card and then 
automatically STAND. For example, if you 
initially bet $100, clicking X2 would increase 
your bet to $200 causing you to either lose 
more money or gain more money.
"""

page5_title_text = "HIT AND STAND"
page5_text = """
You can add more cards to your hand by 
choosing HIT, but be careful; If you exceed 
21, you automatically lose the round. Once 
you're ready to play the hand, click STAND. 
The dealer will then reveal their hidden 
card and then try to beat the value you 
stopped at. 
"""

page6_title_text = "CARD VALUES"
page6_text = """
Aces are worth either 1 or 11, automatically 
chosen to provide the best possible hand for 
you. All Face Cards (J, Q, K) are worth 10, 
and Number cards are worth the value 
indicated on the card.
"""

page7_title_text = "WINNING"
page7_text = """
Typically, whoever gets 21 will win. If both 
you and the dealer have the same worth, then 
the round ends in a tie and your bet is 
refunded. If you finish with a higher value 
than the dealer (granted that it's below 21), 
then you win. Winning with BlackJack awards 
you 1.5x the amount you initially bet.
"""

page8_title_text = "CASH OUT"
page8_text = """
At the end of each round you will be given 
the option to CASH OUT with your winnings. 
This will immediately end the game. Should 
you run out of money and the game ends, feel 
free to try again; there's no limit on 
attempts! It's a risky game, but fortune 
favours the bold. Best of luck!
"""

# All titles and descriptions combined in a list for ease of calling
instr_pages_text = [
    {"title": page1_title_text, "body": page1_text},
    {"title": page2_title_text, "body": page2_text},
    {"title": page3_title_text, "body": page3_text},
    {"title": page4_title_text, "body": page4_text},
    {"title": page5_title_text, "body": page5_text},
    {"title": page6_title_text, "body": page6_text},
    {"title": page7_title_text, "body": page7_text},
    {"title": page8_title_text, "body": page8_text}
]
