#! python3
"""
    Mastermind - a guessing game
    using a simple window interface

    This is the exercise version: the actual code
    of the 'SecretNumber' class is removed.
"""

import random
import text_gui

NUMPOS = 4
NUMRANGE = 6

class G():
    gui = None
    secret = None
    numguess = 0
    
def main():

    G.gui = text_gui.CmdlAppGui("Mastermind Game", text_input)
    welcome = """Hello and Welcome to the MasterMind game

I am the game master and I will think of a number, which you have to guess.
The secret number has exactly {anz} digits in the range 1..{max}.
Your can try to find out the secret number by entering your {anz}-digit guess.
I will help you by giving you hints about the number you entered.
For every digit in you guess, which is correct AND on the right position,
you will get a plus (+). For numbers, which are correct, but in the wrong
position, you will get a minus (-).
An example: secret number is 1234, your guess is 2336, then you get +-

"""
    G.gui.put_msg(welcome.format(anz=NUMPOS, max=NUMRANGE))
    initiate_game()
    G.gui.start() # now the GUI has the control
    return

def text_input(text):
    # process text input from the gui input field
    text = text.strip()
    if text == '':
        return
    if text in ('end', 'x'):
        G.gui.finish()
        return
        
    if len(text) != NUMPOS:
        G.gui.put_msg("what? - '{0}'\n".format(text))
        return

    if text == '????':
        G.gui.put_msg(G.secret.secret)
        return

    G.numguess += 1
    result, ans = G.secret.guess(text)
    G.gui.put_data("{tries:3}. {0} > {1}\n".format(text, ans, tries=G.numguess))

    if result:  # True means: problem solved
        G.gui.put_msg("\nyou win!\n\n", 1)
        G.gui.put_data("================\n\n")
        G.gui.put_msg("you want to play again?\n")
        initiate_game()                 
    return    

def initiate_game():
    G.numguess = 0
    G.secret = SecretNumber(NUMPOS, NUMRANGE)
    
    G.gui.put_msg("""
I chose a secret number, enter your guesses.
At any time you may enter 'x' or 'end'
(or use the 'Quit'-button) to quit the game
""")
    
    
class SecretNumber():
    def __init__(self, numpos, numrange):
        pass
        
    def guess(self, test):
        resp = ''
        pass
        return False, resp
            
            
if __name__ == '__main__':
    main()
