from sys import exit  
  
def gold_room():  
    print "This room is full of food. How much do you take?"  
    next = raw_input("> ")
    
    if  next < 50 :  
        print "Nice, you're not greedy, you win! you can gou another room .please enter 9"
        cc=raw_input(">>")
        if cc=="9":
            cthulhu_room()
        else :
            print "please enter 9"
               
    elif next > 50:
        print "you are so greedy,you will meet a bear , if you beat it ,you can get all gold "
              
        bear_room()
                 
    else:  
        print ("please enter a number!")  
  
def bear_room():  
    print "There is a bear here."  
    print "The bear has a bunch of honey."  
    print "The fat bear is in front of another door."  
    print "How are you going to move the bear?"  
    bear_moved = False  
  
    while True:  
        next = raw_input("> ")  
  
        if next == "take honey":  
            dead("The bear looks at you then slaps your face off.")  
        elif next == "taunt bear" and not bear_moved:  
            print "The bear has moved from the door. You can go through it now."  
            bear_moved = True  
        elif next == "taunt bear" and bear_moved:  
            dead("The bear gets pissed off and chews your leg off.")  
        elif next == "open door" and bear_moved:  
            gold_room()  
        else:  
            print "I got no idea what that means."  
  
def cthulhu_room():  
    print "Here you see the great evil Cthulhu."  
    print "He, it, whatever stares at you and you go insane."  
    print "Do you flee for your life or eat your head?"  
  
    next = raw_input("> ")  
  
    if "flee" in next:  
        start()  
    elif "head" in next:  
        dead("Well that was tasty!")  
    else:  
        cthulhu_room()  
  
def dead(why):  
    print why, "Good job!"  
    exit(0)  
  
def start():  
    print "If your eyes are covered."  
    print "There is a door to your right and left."  
    print "Which one do you take?"  
  
    next = raw_input("> ")  
  
    if next == "left":  
        gold_room()  
    elif next == "right":  
        cthulhu_room()  
    else:  
        print "You shuold input left or right." 
  
start() 