import tkinter as tk
from PIL import ImageTk, Image
from InstructionsText import instr_pages_text
from ColoursAndFonts import *
from GameBackend import *
from Competitor import user, dealer
from Card import card_mapping


# Opens a new window to play game
def play_game(is_first_time):
    global pot
    global bank

    # Only remove beginning frame first time clicking PLAY button; all other times, ignore this
    if is_first_time:
        temp_frame.destroy()

    # Temp frame so when PLAY button pressed, all children inside frame will be forgotten too
    mainscr_frame = tk.Frame(root, bg=poker_green, highlightbackground="black", highlightthickness=1.5)
    mainscr_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # Create instructions button with text and custom image
    instructions_btn = tk.Button(mainscr_frame, text=" Instructions", image=question_mark, borderwidth=0,
                                 compound=tk.LEFT, bg=poker_green, activebackground=poker_green, fg=gold,
                                 activeforeground="white", font=instr_btn_font, cursor="hand2",
                                 command=open_instructions)
    instructions_btn.place(relx=0.01, rely=0.01)

    # Create cash out button with text and custom image
    cash_out_btn = tk.Button(mainscr_frame, text="Cash Out ", image=money_sign, borderwidth=0,
                             compound=tk.RIGHT, bg=poker_green, activebackground=poker_green, fg=gold,
                             activeforeground="white", font=instr_btn_font, cursor="hand2",
                             command=cash_out)
    cash_out_btn.place(relx=0.869, rely=0.01)

    # Create frame for chips
    chips_frame = tk.Frame(mainscr_frame, bg=classic_blue, highlightbackground=ghost_white, highlightthickness=1.5)
    chips_frame.place(relx=0.1, rely=0.55, relwidth=0.45, relheight=0.5)
    bank_frame = tk.Frame(mainscr_frame, bg=classic_blue, highlightbackground=ghost_white, highlightthickness=1.5)
    bank_frame.place(relx=0.1, rely=0.428, relwidth=0.18, relheight=0.125)
    rmv_border = tk.Label(mainscr_frame, bg=classic_blue)  # Hide border line between 2 above chip frames
    rmv_border.place(relx=0.102, rely=0.55, relwidth=0.176, relheight=0.01)

    # Labels for bank and pot
    bank_lbl = tk.Label(bank_frame, text="Bank: $" + str(bank), font=bank_font, bg=classic_blue, fg=gold)
    bank_lbl.place(relx=0.05, rely=0.05)
    pot_lbl = tk.Label(mainscr_frame, text="Pot: $" + str(pot), font=pot_font, bg=poker_green, fg=gold)
    pot_lbl.place(relx=0.38, rely=0.435)
    # Reset button to reset pot and get chips back to re-bet
    reset_pot_btn = tk.Button(mainscr_frame, text="RESET", highlightbackground='black', borderwidth=1.5, bg='white',
                              activebackground='black', fg='black', activeforeground='white', font=bank_font,
                              cursor="hand2", command=lambda: reset_bet(mainscr_frame))
    reset_pot_btn.place(relx=0.285, rely=0.491, relwidth=0.075, relheight=0.05)
    # Deal button to play round of game; only show if pot is not $0
    if pot != 0:
        deal_btn = tk.Button(mainscr_frame, text="DEAL", borderwidth=4, bg=classic_blue, activebackground=classic_blue,
                             fg=gold, activeforeground=gold, font=main_btns_font, cursor="hand2",
                             command=lambda: deal(mainscr_frame, [], True))
        deal_btn.place(relx=0.7, rely=0.42)

    # Go into other functions to create all relevant chips for user
    create_chip_buttons(mainscr_frame, chips_frame, bank_frame)


# Creates chip buttons, only generating chips that user has enough money to bet
def create_chip_buttons(mscr_frame, chp_frame, bnk_frame):
    # ALL IN button
    allin_btn = tk.Button(bnk_frame, text="ALL IN", highlightbackground='black', borderwidth=1.5, bg='white',
                          activebackground='black', fg='black', activeforeground='white', font=bank_font,
                          cursor="hand2", command=lambda: bet_chips(mscr_frame, bank))
    allin_btn.place(relx=0.25, rely=0.55, relwidth=0.5, relheight=0.4)
    # $1 CHIP button
    if bank >= 1:
        chip_1_btn = tk.Button(chp_frame, image=all_chips.get(1), borderwidth=0, bg=classic_blue,
                               activebackground=classic_blue, cursor="hand2", command=lambda: bet_chips(mscr_frame, 1))
        chip_1_btn.place(relx=0.02, rely=0.05, relwidth=0.23, relheight=0.39)
    # $5 CHIP button
    if bank >= 5:
        chip_5_btn = tk.Button(chp_frame, image=all_chips.get(5), borderwidth=0, bg=classic_blue,
                               activebackground=classic_blue, cursor="hand2", command=lambda: bet_chips(mscr_frame, 5))
        chip_5_btn.place(relx=0.26, rely=0.05, relwidth=0.23, relheight=0.39)
    # $25 CHIP button
    if bank >= 25:
        chip_25_btn = tk.Button(chp_frame, image=all_chips.get(25), borderwidth=0, bg=classic_blue,
                                activebackground=classic_blue, cursor="hand2",
                                command=lambda: bet_chips(mscr_frame, 25))
        chip_25_btn.place(relx=0.505, rely=0.05, relwidth=0.23, relheight=0.39)
    # $50 CHIP button
    if bank >= 50:
        chip_50_btn = tk.Button(chp_frame, image=all_chips.get(50), borderwidth=0, bg=classic_blue,
                                activebackground=classic_blue, cursor="hand2",
                                command=lambda: bet_chips(mscr_frame, 50))
        chip_50_btn.place(relx=0.75, rely=0.05, relwidth=0.23, relheight=0.39)
    # $100 CHIP button
    if bank >= 100:
        chip_100_btn = tk.Button(chp_frame, image=all_chips.get(100), borderwidth=0, bg=classic_blue,
                                 activebackground=classic_blue, cursor="hand2",
                                 command=lambda: bet_chips(mscr_frame, 100))
        chip_100_btn.place(relx=0.02, rely=0.47, relwidth=0.23, relheight=0.39)
    # $500 CHIP button
    if bank >= 500:
        chip_500_btn = tk.Button(chp_frame, image=all_chips.get(500), borderwidth=0, bg=classic_blue,
                                 activebackground=classic_blue, cursor="hand2",
                                 command=lambda: bet_chips(mscr_frame, 500))
        chip_500_btn.place(relx=0.26, rely=0.47, relwidth=0.23, relheight=0.39)
    # $1000 CHIP button
    if bank >= 1000:
        chip_1000_btn = tk.Button(chp_frame, image=all_chips.get(1000), borderwidth=0, bg=classic_blue,
                                  activebackground=classic_blue, cursor="hand2",
                                  command=lambda: bet_chips(mscr_frame, 1000))
        chip_1000_btn.place(relx=0.505, rely=0.47, relwidth=0.23, relheight=0.39)
    # $5000 CHIP button
    if bank >= 5000:
        chip_5000_btn = tk.Button(chp_frame, image=all_chips.get(5000), borderwidth=0, bg=classic_blue,
                                  activebackground=classic_blue, cursor="hand2",
                                  command=lambda: bet_chips(mscr_frame, 5000))
        chip_5000_btn.place(relx=0.75, rely=0.47, relwidth=0.23, relheight=0.39)


# Updates chip buttons, pot, and user's bank depending on amount user chooses to bet
def bet_chips(ms, bet_amt):
    global pot
    global bank
    pot = pot + bet_amt
    bank = bank - bet_amt
    ms.destroy()
    play_game(False)


# If user wants to reset amount they bet, all money in pot returns to user's bank
def reset_bet(ms):
    global pot
    global bank
    bank = bank + pot
    pot = 0
    ms.destroy()
    play_game(False)


# Creates popup window that prompts if user wants to cash out or not
def cash_out():
    # Initialize new Cash Out window and all its attributes
    co_window = tk.Toplevel()
    co_window.attributes("-topmost", True)
    co_window.overrideredirect(True)  # Remove toolbar of window
    co_window.configure(bg="black")
    position_right = int(co_window.winfo_screenwidth() / 2 - window_width - 10)
    position_down = int(co_window.winfo_screenheight() / 2 - window_height / 2)
    co_window.geometry("400x200+" + str(position_right) + "+" + str(position_down))
    co_window.grab_set()

    # Creating central frame for cashing out
    co_frame = tk.Frame(co_window, bg=classic_blue)
    co_frame.place(relx=0.0125, rely=0.025, relwidth=0.975, relheight=0.95)

    # Define popup window user will see for cashing out

    # Creates title of page
    co_title = tk.Label(co_frame, text="CASH OUT", font=instr_title_font, bg=classic_blue, fg=gold, justify="center")
    co_title.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.2)
    # Creates description of page
    co_body = tk.Label(co_frame, text="Take cash and leave?\nYou will leave with:\n\n$" + str(user.money),
                       font=instr_content_font, fg='white', bg=classic_blue, borderwidth=0)
    co_body.place(relx=0.25, rely=0.35, relwidth=0.5, relheight=0.4)
    # Creates YES button to cash out
    co_yes = tk.Button(co_frame, text="YES", command=lambda: take_cash(co_window), font=instr_toolbar_font,
                       bg=classic_blue, activebackground=classic_blue, fg=gold, activeforeground=gold, borderwidth=0,
                       cursor="hand2")
    co_yes.place(relx=0.09, rely=0.75)
    # Creates NO button to not cash out
    co_no = tk.Button(co_frame, text="NO", command=co_window.destroy, font=instr_toolbar_font, bg=classic_blue,
                      activebackground=classic_blue, fg=gold, activeforeground=gold, borderwidth=0, cursor="hand2")
    co_no.place(relx=0.75, rely=0.75)


# If user chooses to cash out, remove cash out screen and show stats screen
def take_cash(co_w):
    co_w.destroy()
    show_stats()


# Shows stats of game including "CASH WON", "HANDS WON", "HIGHEST BANK"; can be reached through 2 possible ways
#   1. User manually chooses to cash out
#   2. User loses all money (has $0) and is forced to cash out/see stats screen
def show_stats():
    # Creating central frame on top of all other widgets (so background looks clean)
    frame_cover = tk.Frame(root, bg=poker_green, highlightbackground="black", highlightthickness=1.5)
    frame_cover.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)  # Auto adjusts when screen size changes

    # Initialize new Stats window
    stats_window = tk.Toplevel()
    stats_window.attributes("-topmost", True)
    stats_window.overrideredirect(True)  # Remove toolbar of window
    stats_window.configure(bg="black")
    # Positions screen based on user window screen
    position_right = int(stats_window.winfo_screenwidth() / 2 - window_width - 20)
    position_down = int(stats_window.winfo_screenheight() / 3 - window_height / 2)
    stats_window.geometry("400x400+" + str(position_right) + "+" + str(position_down))
    stats_window.grab_set()

    # Creating central frame for stats
    stats_frame = tk.Frame(stats_window, bg=classic_blue)
    stats_frame.place(relx=0.0125, rely=0.0125, relwidth=0.975, relheight=0.975)

    # String for user stats headers
    stats_headers = "\nTOTAL CASH WON: \n\nHANDS WON: \n\nHIGHEST BANK: \n\n"

    # WILL NEED TO MAKE stats_values CHANGE/VARIABLE

    # String for user's actual stats
    stats_values = "\n$" + str(user.money) + "\n\n" + str(hands_won) + "\n\n$" + str(highest_bank) + "\n\n"

    # Define popup window user will see for stats of their game

    # Creates title of stats page
    stats_title = tk.Label(stats_frame, text="GAME STATISTICS", font=instr_title_font, bg=classic_blue, fg=gold,
                           justify="center")
    stats_title.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.15, anchor=tk.N)
    # Creates stats description headers
    stats_body_lbl = tk.Label(stats_frame, text=stats_headers, font=instr_content_font, fg="white", bg=classic_blue,
                              borderwidth=0, justify="left")
    stats_body_lbl.place(relx=0.3, rely=0.35, relwidth=0.4, relheight=0.3, anchor=tk.N)
    # Creates stats values
    stats_val_lbl = tk.Label(stats_frame, text=stats_values, font=instr_content_font, fg="white", bg=classic_blue,
                             borderwidth=0, justify="right")
    stats_val_lbl.place(relx=0.8, rely=0.35, relwidth=0.4, relheight=0.3, anchor=tk.N)

    # Creates FINISH button to end game
    finish_game_btn = tk.Button(stats_frame, text="FINISH", command=root.destroy, font=main_btns_font, bg=gold,
                                activebackground='black', fg='black', activeforeground=gold, borderwidth=4,
                                cursor="hand2")
    finish_game_btn.place(relx=0.5, rely=0.85, anchor=tk.S)


# Opens a new window containing the Instructions manual
def open_instructions():
    # Initialize new Instructions window
    instr_window = tk.Toplevel()
    instr_window.attributes("-topmost", True)
    instr_window.overrideredirect(True)  # Remove toolbar of window
    instr_window.configure(bg="black")
    # Centers Instructions window on main computer screen
    position_right = int(instr_window.winfo_screenwidth() / 2 - window_width - 10)
    position_down = int(instr_window.winfo_screenheight() / 3 - window_height / 2)
    instr_window.geometry("400x400+" + str(position_right) + "+" + str(position_down))
    instr_window.grab_set()

    # Creating central frame for instructions
    instr_frame = tk.Frame(instr_window, bg=classic_blue)
    instr_frame.place(relx=0.0125, rely=0.0125, relwidth=0.975, relheight=0.975)
    # Creating temporary frame for instructions for ease of using "place_forget"
    instr_temp_frame = tk.Frame(instr_frame, bg=classic_blue)
    instr_temp_frame.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.9)

    # Define first page user will see when instructions_button is clicked

    # Creates exit button "X" to exit Instructions menu
    instr_btn_exit = tk.Button(instr_frame, text="X", command=instr_window.destroy, font=instr_exit_font,
                               bg=classic_blue,
                               activebackground=classic_blue, fg=gold, activeforeground=gold, borderwidth=0,
                               cursor="hand2")
    instr_btn_exit.place(relx=0.9, rely=0.04, relwidth=0.05, relheight=0.05)
    # Creates title of page
    page_title = tk.Label(instr_temp_frame, text=instr_pages_text[0].get("title"), font=instr_title_font,
                          bg=classic_blue, fg=gold, justify="center")
    page_title.place(height=30, width=365, x=192, y=10, anchor=tk.N)
    # Creates description of page
    page_body = tk.Label(instr_temp_frame, text=instr_pages_text[0].get("body"), font=instr_content_font, fg="white",
                         bg=classic_blue, borderwidth=0)
    page_body.place(height=225, width=350, x=192, y=55, anchor=tk.N)
    # Creates button to go back to previous page
    instr_btn_back = tk.Button(instr_temp_frame, text="<BACK",
                               command=lambda: back_next_instructions(instr_frame, instr_temp_frame, 2),
                               font=instr_toolbar_font, bg=classic_blue, activebackground=classic_blue, fg=gold,
                               activeforeground=gold, borderwidth=0, cursor="hand2")
    instr_btn_back.place(height=25, width=80, x=55, y=325, anchor=tk.S)
    instr_btn_back.place_forget()
    # Creates number of pages and current page
    page_count = tk.Label(instr_temp_frame, text="1/" + str(len(instr_pages_text)), font=instr_toolbar_font,
                          bg=classic_blue, fg=gold, borderwidth=0)
    page_count.place(height=25, width=80, x=192, y=325, anchor=tk.S)
    # Creates button to go to next page
    instr_btn_next = tk.Button(instr_temp_frame, text="NEXT>",
                               command=lambda: back_next_instructions(instr_frame, instr_temp_frame, 2),
                               font=instr_toolbar_font, bg=classic_blue, activebackground=classic_blue, fg=gold,
                               activeforeground=gold, borderwidth=0, cursor="hand2")
    instr_btn_next.place(height=25, width=80, x=326, y=325, anchor=tk.S)


# Allows user to navigate through and go forward or back a page of the instructions
def back_next_instructions(instr_frame, i_frame, slide_num):
    # Remove everything from previous slide (Except "X" for exit)
    i_frame.destroy()

    i_frame2 = tk.Frame(instr_frame, bg=classic_blue)
    i_frame2.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.9)

    # Replace title and body of text from previous page
    page_ttl = tk.Label(i_frame2, text=instr_pages_text[slide_num - 1].get("title"), font=instr_title_font,
                        bg=classic_blue, fg=gold, justify="center")
    page_ttl.place(height=30, width=365, x=192, y=10, anchor=tk.N)
    page_bdy = tk.Label(i_frame2, text=instr_pages_text[slide_num - 1].get("body"), font=instr_content_font, fg="white",
                        bg=classic_blue, borderwidth=0)
    page_bdy.place(height=225, width=350, x=192, y=55, anchor=tk.N)

    # Replace back/next buttons with ones that point to a different page
    instr_btn_bck = tk.Button(i_frame2, text="<BACK",
                              command=lambda: back_next_instructions(instr_frame, i_frame, slide_num - 1),
                              font=instr_toolbar_font, bg=classic_blue, activebackground=classic_blue, fg=gold,
                              activeforeground=gold, borderwidth=0, cursor="hand2")
    instr_btn_bck.place(height=25, width=80, x=55, y=325, anchor=tk.S)
    instr_btn_nxt = tk.Button(i_frame2, text="NEXT>",
                              command=lambda: back_next_instructions(instr_frame, i_frame, slide_num + 1),
                              font=instr_toolbar_font, bg=classic_blue, activebackground=classic_blue, fg=gold,
                              activeforeground=gold, borderwidth=0, cursor="hand2")
    instr_btn_nxt.place(height=25, width=80, x=326, y=325, anchor=tk.S)

    # Creates current page out of total pages (e.g. 5/8)
    page_count = tk.Label(i_frame2, text=str(slide_num) + "/" + str(len(instr_pages_text)), font=instr_toolbar_font,
                          bg=classic_blue, fg=gold, borderwidth=0)
    page_count.place(height=25, width=80, x=192, y=325, anchor=tk.S)

    # If first or last slide, then remove back/next button accordingly
    if slide_num == 1:
        instr_btn_bck.place_forget()
    elif slide_num == len(instr_pages_text):
        instr_btn_nxt.place_forget()


# When user clicks DEAL, change UI such that user and dealer has cards and betting interface is gone
def deal(ms_frame, deck, first_time):
    # Clear frame and add new UI features
    ms_frame.destroy()
    # Temp frame so when PLAY button pressed, all children inside frame will be forgotten too
    ms_frame = tk.Frame(root, bg=poker_green, highlightbackground="black", highlightthickness=1.5)
    ms_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # Create instructions button with text and custom image
    instructions_btn = tk.Button(ms_frame, text=" Instructions", image=question_mark, borderwidth=0,
                                 compound=tk.LEFT, bg=poker_green, activebackground=poker_green, fg=gold,
                                 activeforeground="white", font=instr_btn_font, cursor="hand2",
                                 command=open_instructions)
    instructions_btn.place(relx=0.01, rely=0.01)

    # Create frame and label for bank (same as before, just no chips)
    bank_frame = tk.Frame(ms_frame, bg=classic_blue, highlightbackground=ghost_white, highlightthickness=1.5)
    bank_frame.place(relx=0.1, rely=0.94, relwidth=0.18, relheight=0.07)
    bank_lbl = tk.Label(bank_frame, text="Bank: $" + str(bank), font=bank_font, bg=classic_blue, fg=gold)
    bank_lbl.place(relx=0.05, rely=0.05)

    # Label for amount in pot
    pot_lbl = tk.Label(ms_frame, text="$" + str(pot), font=pot_font, bg=poker_green, fg=gold)
    pot_lbl.place(relx=0.455, rely=0.45)

    # "Dealer" label and card worth
    dealer_lbl = tk.Label(ms_frame, text="DEALER", font=names_font, bg=poker_green, fg=gold)
    dealer_lbl.place(relx=0.7, rely=0.1, relwidth=0.15, relheight=0.05)

    # "Player" label and card worth
    player_lbl = tk.Label(ms_frame, text="PLAYER", font=names_font, bg=poker_green, fg=gold)
    player_lbl.place(relx=0.7, rely=0.85, relwidth=0.15, relheight=0.05)

    if first_time:
        # Create and shuffle deck, and deal 2 cards to user and dealer
        deck = shuffle_deck()
        deal_starter_cards(deck)

    # Displays cards for both user and dealer
    show_cards(user, ms_frame, True, deck)
    show_cards(dealer, ms_frame, True, deck)

    # Hit button to get another card
    hit_btn = tk.Button(ms_frame, text=" HIT ", borderwidth=4, bg=classic_blue, activebackground=classic_blue,
                        fg=gold, activeforeground=gold, font=main_btns_font, cursor="hand2",
                        command=lambda: hit(deck, ms_frame, True))
    hit_btn.place(relx=0.13, rely=0.45)

    # Stand button to end round of game
    stand_btn = tk.Button(ms_frame, text="STAND", borderwidth=4, bg=classic_blue, activebackground=classic_blue,
                          fg=gold, activeforeground=gold, font=main_btns_font, cursor="hand2",
                          command=lambda: stand(deck, ms_frame))
    stand_btn.place(relx=0.69, rely=0.45)


# Goes through each of person's cards, and places them on screen and updates card_worth (cw) Label
def show_cards(person, ms_frame, is_first_time, deck):
    # Create frame and label for bank (same as before, just no chips)
    bank_frame = tk.Frame(ms_frame, bg=classic_blue, highlightbackground=ghost_white, highlightthickness=1.5)
    bank_frame.place(relx=0.1, rely=0.94, relwidth=0.18, relheight=0.07)
    bank_lbl = tk.Label(bank_frame, text="Bank: $" + str(bank), font=bank_font, bg=classic_blue, fg=gold)
    bank_lbl.place(relx=0.05, rely=0.05)

    # Label for amount in pot
    pot_lbl = tk.Label(ms_frame, text="$" + str(pot), font=pot_font, bg=poker_green, fg=gold)
    pot_lbl.place(relx=0.455, rely=0.45)

    if is_first_time and bank >= pot:
        # X2 button to double bet
        double_bet_btn = tk.Button(ms_frame, image=double_bet_img, borderwidth=0,
                                   compound=tk.LEFT, bg=poker_green, activebackground=poker_green, font=instr_btn_font,
                                   cursor="hand2", command=lambda: double_bet(deck, ms_frame))
        double_bet_btn.place(relx=0.35, rely=0.41, relwidth=0.1, relheight=0.18)

    if person == user:
        yval = 0.62
        # Frame for all of users cards
    else:
        yval = 0.05
        # Frame for all of dealers cards
    cards_frame = tk.Frame(ms_frame, bg=poker_green)
    cards_frame.place(relx=0.18, rely=yval, relwidth=0.52, relheight=0.32)
    i = 0  # Index tracking if card should be to left or right of middle card for odd number of cards

    # To show dealer's cards when round just starts
    # If round just started, make sure one of dealer's cards is hidden
    if len(person.cards) == 2 and person == dealer and is_first_time:
        # Show face of one card, show back of 2nd card
        tk.Label(cards_frame, image=card_images.get("back_of_card"), borderwidth=0).place(relx=0.345, rely=0.22)
        tk.Label(cards_frame, image=card_images.get(dealer.cards[0].name), borderwidth=0).place(relx=0.515, rely=0.22)
        # Display dealer's hand worth
        dealer_cw_lbl = tk.Label(ms_frame, image=card_worth_img, text=str(dealer.cards[0].worth), font=card_worth_font,
                                 borderwidth=0, bg=poker_green, fg='white', compound="center")
        dealer_cw_lbl.place(relx=0.742, rely=0.155, relwidth=0.06, relheight=0.1)
        return

    left_dx = 0  # Location of card displaced slightly to left of card before
    right_dx = 0  # Location of card displaced slightly to right of card before

    # Determine if person has even or odd number of cards
    if len(person.cards) % 2 == 0 or len(person.cards) > 6:
        for card in person.cards:
            if i < 6:
                if i % 2 == 0:
                    tk.Label(cards_frame, image=card_images.get(card.name), borderwidth=0).place(relx=0.515 + right_dx,
                                                                                                 rely=0.22)
                    right_dx += 0.17
                else:
                    tk.Label(cards_frame, image=card_images.get(card.name), borderwidth=0).place(relx=0.345 - left_dx,
                                                                                                 rely=0.22)
                    left_dx += 0.17
            else:  # Else person has more than 6 cards
                if i == 6:  # Reset the slight change so new cards can be placed on top of old ones
                    left_dx = 0
                    right_dx = 0

                if i % 2 == 0:
                    tk.Label(cards_frame, image=card_images.get(card.name), borderwidth=0).place(relx=0.43 + right_dx,
                                                                                                 rely=0.22 - 0.2)
                    right_dx += 0.17
                else:
                    left_dx += 0.17
                    tk.Label(cards_frame, image=card_images.get(card.name), borderwidth=0).place(relx=0.43 - left_dx,
                                                                                                 rely=0.22 - 0.2)
            i += 1  # Increment "i" to next index
    else:  # Else odd number of cards
        for card in person.cards:
            if i == 0:  # Print card directly in middle
                tk.Label(cards_frame, image=card_images.get(card.name), borderwidth=0).place(relx=0.43, rely=0.22)
                left_dx += 0.17
                right_dx += 0.17
            elif i % 2 == 0:
                tk.Label(cards_frame, image=card_images.get(card.name), borderwidth=0).place(relx=0.43 + right_dx,
                                                                                             rely=0.22)
                right_dx += 0.17
            else:
                tk.Label(cards_frame, image=card_images.get(card.name), borderwidth=0).place(relx=0.43 - left_dx,
                                                                                             rely=0.22)
                left_dx += 0.17
            i += 1  # Increment "i" to next index

    # Calculates person's hand worth, and displays it as a Label
    hw = calc_hand_worth(person)
    if person == user:
        user_cw_lbl = tk.Label(ms_frame, image=card_worth_img, text=str(hw), font=card_worth_font, borderwidth=0,
                               bg=poker_green, fg='white', compound="center")
        user_cw_lbl.place(relx=0.742, rely=0.742, relwidth=0.06, relheight=0.1)
    elif person == dealer:
        dealer_cw_lbl = tk.Label(ms_frame, image=card_worth_img, text=str(hw), font=card_worth_font, borderwidth=0,
                                 bg=poker_green, fg='white', compound="center")
        dealer_cw_lbl.place(relx=0.742, rely=0.155, relwidth=0.06, relheight=0.1)


# Deals user another card, updates user card worth, and removes X2 options
def hit(deck, ms_frame, from_deal):
    user.cards.append(card_mapping.get(deck.pop()))
    show_cards(user, ms_frame, False, deck)

    # If previous function was "deal" and user now has more than 21, then show "bust" screen
    if from_deal and calc_hand_worth(user) > 21:
        show_winner_screen("bust")


# Dealer receives cards, and cards are shown, then "winner" message pops up and returned back to betting screen
def stand(deck, ms_frame):
    global bank
    global pot

    # Initial hand worth for user and dealer
    user_hand = calc_hand_worth(user)
    dealer_hand = calc_hand_worth(dealer)

    # Give cards to dealer until they are >= worth of user
    while dealer_hand < user_hand <= 21:
        dealer.cards.append(card_mapping.get(deck.pop()))
        dealer_hand = calc_hand_worth(dealer)

    # Show all of dealer's cards
    show_cards(dealer, ms_frame, False, deck)
    # Determine who won and show appropriate screen
    show_winner_screen(determine_winner(user_hand, dealer_hand))


# Double of user's money is taken and added to pot, then user given exactly 1 card, then user "stands"
def double_bet(deck, ms_frame):
    global pot
    global bank
    # Adjust pot to be 2x original bet
    bank = bank - pot
    pot = 2 * pot

    # Give user exactly one more card and immediately stand
    hit(deck, ms_frame, False)
    stand(deck, ms_frame)


# User went over 21, so show bust screen
def show_winner_screen(winner):
    global pot
    global bank
    global hands_won
    global highest_bank

    # Calculate who winner was and adjust user's money
    if winner.lower() == "user":
        if has_blackjack(user):  # If user won with blackjack, give 1.5x winnings
            bank = bank + int(((pot * 1.5) + pot))
        else:  # Else just give normal amount back
            bank = bank + (pot * 2)
        hands_won += 1  # Increase number of hands that user won
        text = "YOU WIN!"
    elif winner.lower() == "dealer":
        if bank == 0:
            text = "YOU LOSE!\nOUT OF MONEY!"
        else:
            text = "DEALER WINS!"
    elif winner.lower() == "bust":
        text = "YOU BUSTED!\nDEALER WINS!"
    else:
        bank = bank + pot  # Get money back
        text = "YOU TIED!"

    # Determine what highest amount of money user had during play through
    if highest_bank < bank:
        highest_bank = bank

    # Reset pot value, and transfer money from bank to user's money
    pot = 0
    user.money = bank

    # Initialize new bust screen all its attributes
    winner_window = tk.Toplevel()
    winner_window.attributes("-topmost", True)
    winner_window.overrideredirect(True)  # Remove toolbar of window
    winner_window.configure(bg="black")
    position_right = int(winner_window.winfo_screenwidth() / 2 - window_width - 20)
    position_down = int(winner_window.winfo_screenheight() / 2 - window_height / 4 + 10)
    winner_window.geometry("400x100+" + str(position_right) + "+" + str(position_down))
    winner_window.grab_set()

    # Creating central frame for cashing out
    winner_frame = tk.Frame(winner_window, bg=classic_blue)
    winner_frame.place(relx=0.0125, rely=0.025, relwidth=0.975, relheight=0.95)

    # Creates label with text being whatever the situation was (e.g. if user won / dealer won, etc.)
    busted_lbl = tk.Label(winner_frame, text=text, font=instr_title_font, bg=classic_blue, fg='white', justify="center")
    busted_lbl.place(rely=0.08, relwidth=1, relheight=0.5)

    # Creates CONFIRM button to go back to betting screen
    if user.money == 0:  # User out of money, so confirm button to show stats
        confirm_btn = tk.Button(winner_frame, text="CONFIRM", font=instr_toolbar_font, bg=classic_blue,
                                activebackground=classic_blue, fg=gold, activeforeground='black', borderwidth=0,
                                cursor="hand2", command=show_stats)
        confirm_btn.place(relx=0.33, rely=0.65)
    else:  # Else user still has money, so command is to keep playing game
        confirm_btn = tk.Button(winner_frame, text="CONFIRM", font=instr_toolbar_font, bg=classic_blue,
                                activebackground=classic_blue, fg=gold, activeforeground='black', borderwidth=0,
                                cursor="hand2", command=combine_funcs(winner_window.destroy, lambda: play_game(False)))
        confirm_btn.place(relx=0.33, rely=0.65)


# --- MAIN ---

if __name__ == "__main__":
    # Initializing GUI
    root = tk.Tk()
    root.title("BlackJack")
    root.state("zoomed")
    root.resizable(False, False)  # Window doesn't need to resize
    root.iconbitmap('c:/Users/zadat/PycharmProjects/BlackJack/images/spades.ico')
    root.configure(background="#F8F8FF")

    # Screen height and width
    window_height = root.winfo_reqheight()
    window_width = root.winfo_reqwidth()

    # Creating central frame where game is played
    frame = tk.Frame(root, bg=poker_green, highlightbackground="black", highlightthickness=1.5)
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)  # Auto adjusts when screen size changes

    # Temp frame so when PLAY button pressed, all children inside frame will be forgotten too
    temp_frame = tk.Frame(root, bg=poker_green, highlightbackground="black", highlightthickness=1.5)
    temp_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)  # Auto adjusts when screen size changes

    # Title of Game for PLAY screen
    blackjack_lbl_PLAY = tk.Label(temp_frame, text="BLACK\nJACK", font=BLACKJACK_font, bg=poker_green, fg=gold)
    blackjack_lbl_PLAY.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.3)

    # Image 1 for PLAY screen
    blackjack_hand_PLAY = ImageTk.PhotoImage(
        Image.open('images/blackjack_hand.png').resize((200, 200), Image.ANTIALIAS))
    blackjack_hand_lbl_PLAY = tk.Label(temp_frame, image=blackjack_hand_PLAY, bg=poker_green)
    blackjack_hand_lbl_PLAY.place(relx=0.075, rely=0.15, relwidth=0.2, relheight=0.4)

    # Image 2 for PLAY screen
    chips_PLAY = ImageTk.PhotoImage(
        Image.open('images/poker_chips_play.png').resize((200, 200), Image.ANTIALIAS))
    chips_lbl_PLAY = tk.Label(temp_frame, image=chips_PLAY, bg=poker_green)
    chips_lbl_PLAY.place(relx=0.725, rely=0.15, relwidth=0.2, relheight=0.4)

    # PLAY button for PLAY screen
    load_PLAY_image = ImageTk.PhotoImage(file='images/game_PLAY.png')
    play_btn = tk.Button(temp_frame, image=load_PLAY_image, command=lambda: play_game(True), bg=poker_green,
                         activebackground=poker_green, borderwidth=0, cursor="hand2")
    play_btn.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.3)

    # --- IMAGES ---
    # Image of custom Question Mark "?"
    question_mark = ImageTk.PhotoImage(
        Image.open('images/question_mark.png').resize((23, 23), Image.ANTIALIAS))
    # Image of custom dollar sign "$"
    money_sign = ImageTk.PhotoImage(
        Image.open('images/money_sign.png').resize((23, 23), Image.ANTIALIAS))
    # Images for betting chips buttons
    chip_1_img = ImageTk.PhotoImage(Image.open('images/chips/chip_1.png'))
    chip_5_img = ImageTk.PhotoImage(Image.open('images/chips/chip_5.png'))
    chip_25_img = ImageTk.PhotoImage(Image.open('images/chips/chip_25.png'))
    chip_50_img = ImageTk.PhotoImage(Image.open('images/chips/chip_50.png'))
    chip_100_img = ImageTk.PhotoImage(Image.open('images/chips/chip_100.png'))
    chip_500_img = ImageTk.PhotoImage(Image.open('images/chips/chip_500.png'))
    chip_1000_img = ImageTk.PhotoImage(Image.open('images/chips/chip_1000.png'))
    chip_5000_img = ImageTk.PhotoImage(Image.open('images/chips/chip_5000.png'))
    # Dictionary of chip images to easily call whenever button needs to be recreated
    all_chips = {
        1: chip_1_img,
        5: chip_5_img,
        25: chip_25_img,
        50: chip_50_img,
        100: chip_100_img,
        500: chip_500_img,
        1000: chip_1000_img,
        5000: chip_5000_img
    }
    # Image of X2 chip for doubling bet
    double_bet_img = ImageTk.PhotoImage(
        Image.open('images/chips/double_x2.png').resize((125, 125), Image.ANTIALIAS))
    # Image for card worth (a white circle)
    card_worth_img = ImageTk.PhotoImage(Image.open('images/card_worth_frame.png').resize((50, 50), Image.ANTIALIAS))

    # -- ALL CARD IMAGES PRE-CREATED ---
    card_images = {
        # Back of cards
        "back_of_card": ImageTk.PhotoImage(Image.open('images/cards/0_back_of_card.png').resize((75, 125))),
        # All spades
        "ace_of_spades": ImageTk.PhotoImage(Image.open('images/cards/ace_of_spades.png').resize((75, 125))),
        "2_of_spades": ImageTk.PhotoImage(Image.open('images/cards/2_of_spades.png').resize((75, 125))),
        "3_of_spades": ImageTk.PhotoImage(Image.open('images/cards/3_of_spades.png').resize((75, 125))),
        "4_of_spades": ImageTk.PhotoImage(Image.open('images/cards/4_of_spades.png').resize((75, 125))),
        "5_of_spades": ImageTk.PhotoImage(Image.open('images/cards/5_of_spades.png').resize((75, 125))),
        "6_of_spades": ImageTk.PhotoImage(Image.open('images/cards/6_of_spades.png').resize((75, 125))),
        "7_of_spades": ImageTk.PhotoImage(Image.open('images/cards/7_of_spades.png').resize((75, 125))),
        "8_of_spades": ImageTk.PhotoImage(Image.open('images/cards/8_of_spades.png').resize((75, 125))),
        "9_of_spades": ImageTk.PhotoImage(Image.open('images/cards/9_of_spades.png').resize((75, 125))),
        "10_of_spades": ImageTk.PhotoImage(Image.open('images/cards/10_of_spades.png').resize((75, 125))),
        "jack_of_spades": ImageTk.PhotoImage(Image.open('images/cards/jack_of_spades.png').resize((75, 125))),
        "queen_of_spades": ImageTk.PhotoImage(Image.open('images/cards/queen_of_spades.png').resize((75, 125))),
        "king_of_spades": ImageTk.PhotoImage(Image.open('images/cards/king_of_spades.png').resize((75, 125))),
        # All diamonds
        "ace_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/ace_of_diamonds.png').resize((75, 125))),
        "2_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/2_of_diamonds.png').resize((75, 125))),
        "3_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/3_of_diamonds.png').resize((75, 125))),
        "4_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/4_of_diamonds.png').resize((75, 125))),
        "5_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/5_of_diamonds.png').resize((75, 125))),
        "6_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/6_of_diamonds.png').resize((75, 125))),
        "7_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/7_of_diamonds.png').resize((75, 125))),
        "8_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/8_of_diamonds.png').resize((75, 125))),
        "9_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/9_of_diamonds.png').resize((75, 125))),
        "10_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/10_of_diamonds.png').resize((75, 125))),
        "jack_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/jack_of_diamonds.png').resize((75, 125))),
        "queen_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/queen_of_diamonds.png').resize((75, 125))),
        "king_of_diamonds": ImageTk.PhotoImage(Image.open('images/cards/king_of_diamonds.png').resize((75, 125))),
        # All hearts
        "ace_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/ace_of_hearts.png').resize((75, 125))),
        "2_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/2_of_hearts.png').resize((75, 125))),
        "3_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/3_of_hearts.png').resize((75, 125))),
        "4_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/4_of_hearts.png').resize((75, 125))),
        "5_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/5_of_hearts.png').resize((75, 125))),
        "6_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/6_of_hearts.png').resize((75, 125))),
        "7_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/7_of_hearts.png').resize((75, 125))),
        "8_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/8_of_hearts.png').resize((75, 125))),
        "9_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/9_of_hearts.png').resize((75, 125))),
        "10_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/10_of_hearts.png').resize((75, 125))),
        "jack_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/jack_of_hearts.png').resize((75, 125))),
        "queen_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/queen_of_hearts.png').resize((75, 125))),
        "king_of_hearts": ImageTk.PhotoImage(Image.open('images/cards/king_of_hearts.png').resize((75, 125))),
        # All clubs
        "ace_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/ace_of_clubs.png').resize((75, 125))),
        "2_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/2_of_clubs.png').resize((75, 125))),
        "3_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/3_of_clubs.png').resize((75, 125))),
        "4_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/4_of_clubs.png').resize((75, 125))),
        "5_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/5_of_clubs.png').resize((75, 125))),
        "6_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/6_of_clubs.png').resize((75, 125))),
        "7_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/7_of_clubs.png').resize((75, 125))),
        "8_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/8_of_clubs.png').resize((75, 125))),
        "9_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/9_of_clubs.png').resize((75, 125))),
        "10_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/10_of_clubs.png').resize((75, 125))),
        "jack_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/jack_of_clubs.png').resize((75, 125))),
        "queen_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/queen_of_clubs.png').resize((75, 125))),
        "king_of_clubs": ImageTk.PhotoImage(Image.open('images/cards/king_of_clubs.png').resize((75, 125)))
    }

    pot = 0
    # Make bank variable be user money so user doesn't lose money if they haven't committed bet yet
    bank = user.money

    root.mainloop()
