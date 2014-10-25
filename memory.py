# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck, card_pos, exposed, zero_pos, mouse_pos 
    global state, card1, card2
    deck = range(8) + range(8)
    random.shuffle(deck)
    card_pos = [5, 75]
    exposed = []
    for i in range(len(deck)):
        exposed.append(False)
    zero_pos = [[0, 0], [50, 0], [50, 100], [0, 100]]
    mouse_pos = None
    state = 0
    card1 = 0
    card2 = 0
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    mouse_pos = list(pos)
    card_num = mouse_pos[0] / 50
    if exposed[card_num] != True:
        exposed[card_num] = True
        
    global state, card1, card2
    if state == 0:
        state = 1
        card1 = card_num
    elif state == 1:
        state = 2
        card2 = card_num
    else:
        state = 1
        if deck[card1] != deck[card2]:
            exposed[card1] = False
            exposed[card2] = False
        card1 = card_num
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(deck)):
        if exposed[i] == True:
            canvas.draw_text(str(deck[i]), (card_pos[0], card_pos[1]), 75, 'White')
            card_pos[0] += 50
            zero_pos[0][0] += 50
            zero_pos[1][0] += 50
            zero_pos[2][0] += 50
            zero_pos[3][0] += 50
        else:
            canvas.draw_polygon(zero_pos , 2, 'Red', "Green")
            card_pos[0] += 50
            zero_pos[0][0] += 50
            zero_pos[1][0] += 50
            zero_pos[2][0] += 50
            zero_pos[3][0] += 50
    # reset horizontal position to prevent the draw handler from 
    # drawing one deck after the other
    card_pos[0] = 5
    zero_pos[0][0] = 0
    zero_pos[1][0] = 50
    zero_pos[2][0] = 50
    zero_pos[3][0] = 0


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