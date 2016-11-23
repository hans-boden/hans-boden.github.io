#! python3
"""
    Calculator - do some simple math
    using a simple window interface
"""

import random
import text_gui
import math

class G():
    gui = None
    calculator = None
    
def main():

    G.gui = text_gui.CmdlAppGui("Simple Calculator", text_input)
    welcome = """Hello and Welcome to this Calculator

Type 'end' or 'x' to stop this app

"""
    G.gui.put_msg(welcome)
    initiate_app()
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
        
    result, ans = G.calculator.evaluate(text)
    G.gui.put_data("{} => {}\n".format(text, ans))
    return    

def initiate_app():
    G.calculator = Calculator()
    G.gui.put_msg("""
Enter any numeric esxpression, and I will give you a result.

""")
    
    
class Calculator():
    def __init__(self):
        pass  # any initialization?
        
    def evaluate(self, expr):
        try:
            r = eval(expr)
        except:
            return False, 'too complex for me'
        return True, r
            
            
if __name__ == '__main__':
    main()
