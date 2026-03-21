import os
from cartas import print_mao
import time

win_states = {
    "CONTINUE": 0,
    "PLAYER_WIN": 1,
    "DEALER_WIN": 2,
    "TIE": 3
}

def render_menu():
    os.system('clear')
    print("---------------------------------------------")
    print("                 BlackJack                   ")
    print("---------------------------------------------")
##

def render_game(coins, bet, player_hand, dealer_hand):
    
    os.system('clear')
    print("--------------------------------------")
    print("dealer: ", end=" ")
    print_mao(dealer_hand)
    print("--------------------------------------")
    print("player: ", end=" ")
    print_mao(player_hand)
    print("--------------------------------------")
    print("coins:", coins, "      bet:", bet)

##

def render_aposta(coins):
    os.system('clear')
    print("--------------------------------------")
    print("             APOSTA                   ")
    print("--------------------------------------")
    print("dinheiro:", coins,"      ", end=" ")
##

def render_win(win_state):

    if(win_state == win_states["CONTINUE"]):
        return 0
    if(win_state == win_states["PLAYER_WIN"]):
        os.system('clear')
        print("jogador ganhou!")
    if(win_state == win_states["DEALER_WIN"]):
        os.system('clear')
        print("dealer ganhou")
    if(win_state == win_states["TIE"]):
        os.system('clear')
        print("empachi")

    time.sleep(1)
##

def render_regras():
    print("BLACKJACK RULES (SIMPLIFIED)\n")

    print("Goal:")
    print("Get as close to 21 as possible without going over, and beat the dealer.\n")
    print("For each round, you can choose how much you want to bet, with a 10% minimum")
    print("Each roud you win you doble the bet amout, and loss equals losing the bet amount")
    print("Card Values:")
    print("- 2–10 = face value")
    print("- J, Q, K = 10")
    print("- A = 11 or 1 (automatically adjusted if needed)\n")

    print("Game Start:")
    print("- You receive 2 cards")
    print("- The dealer receives 2 cards (one is hidden)\n")

    print("Your Turn:")
    print('- Choose "Hit" to take another card')
    print('- Choose "Stand" to stop')
    print("- You can keep hitting until you stand or go over 21\n")

    print("Bust:")
    print("- If your total goes over 21, you lose immediately\n")

    print("Dealer Turn:")
    print("- Dealer reveals hidden card")
    print("- Dealer must hit if total is less than 17")
    print("- Dealer stands on 17 or higher\n")

    print("Winning:")
    print("- If the dealer busts, you win")
    print("- If your total is higher than the dealer, you win")
    print("- If your total is lower, you lose")
    print("- If both totals are equal, it's a draw \n\n")


##