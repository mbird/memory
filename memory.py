# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck, card_pos 
    deck = range(8) + range(8)
    random.shuffle(deck)
    card_pos = [20, 50]

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card in deck:
        canvas.draw_text(str(card), (card_pos[0], card_pos[1]), 50, 'Red')
        card_pos[0] += 50
    # reset horizontal position to prevent the draw handler from 
    # drawing one deck after the other
    card_pos[0] = 25


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric