#pseudocode
#this use a while loop (comment it when running the other algo)
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print ("found the key!")

#this use recursion
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)   #recursion
        elif item.is_a_key():
            print ("found the key!")

#other recursion
def countdown(i):
    print i
    if i <= 0: #base case 
        return
    else: #recursive case
        countdown(i-1)
