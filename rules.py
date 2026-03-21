from menu import menu
from ui import render_regras
import os

def rules():
    
    render_regras()
    input_rules = input("(1): voltar para menu")
    try:
        input_rules = int(input_rules)
    except ValueError:
        input_rules = 0
    
    if(input_rules == 1):
        return "menu"
    else: 
        print("valor invalido")
        os.system('clear')
        return "rules"