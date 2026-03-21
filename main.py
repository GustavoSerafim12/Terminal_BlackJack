from game import *
from rules import rules
from menu import menu
from game import game

def main():
    state = "menu"

    while(state != "quit"):
        if state == "menu":
            state = menu()
        elif state == "rules":
            state = rules()
        elif state == "game":
            state = game()
        elif state == "leaderboard":
            print("leaderboard")
            state = "menu"
##

main()
