#credit Burak Emre TOPRAK
import random

def wait_for_player():
    
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
   
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') 
    return deck

def shuffle_deck(deck):
    
    random.shuffle(deck)

def deal_cards(deck):
     
     
     dealer=[]
     other=[]
     while len(deck)>1:
          other.append(deck.pop())
          dealer.append(deck.pop())
     other.append(deck.pop()) 
     return (dealer, other)


def del_cards_v2(deck):
    dealer=deck[1::2]
    other=deck[0::2]
    return (dealer, other)



def remove_pairs(l):
    

    no_pairs=[]

    l.sort()
    i=0
    while i<len(l)-1:
        card1=l[i]
        card2=l[i+1]
        if card1[:-1] == card2[:-1]: 
            i=i+1           
        else:
            no_pairs.append(l[i])
        i=i+1
    if i==len(l)-1: 
        no_pairs.append(l[i])

    random.shuffle(no_pairs)
    return no_pairs

def remove_pairs_v2(l):
    tmp=[]
    no_pairs=[]

    
    for item in l:
        tmp.append(item[:-1]) 

    
    for i in range(len(tmp)):
        if tmp.count(tmp[i]) % 2==1 and i==tmp.index(tmp[i]):
            no_pairs.append(l[i]) 

 
    random.shuffle(no_pairs)
    return no_pairs



def remove_pairs_v3(l):
    no_pairs=[]

    no_pairs=l[:] 
    i=0
    while i<len(no_pairs)-1:
        card1=no_pairs[i]
        print(card1)
        found_pair=False
        j=0
        while j<len(no_pairs) and found_pair==False:
            card2=no_pairs[j]
            if card1[:-1]==card2[:-1] and i!=j: 
                print(no_pairs.count(card1))
                no_pairs.remove(card1)
                no_pairs.remove(card2)
                found_pair=True
            j=j+1
        i=i+1
        if found_pair:
            i=0 

    random.shuffle(no_pairs)
    return no_pairs
                     
                
                

        


def print_deck(deck):
   
    print()
    for item in deck:
        print(item, end=' ')
    print("\n")

def get_valid_input(n):
     
     print("I have", n, "cards. If 1 stands for my first card and")
     print(n, "for my last card, which of my cards would you like?")
     position=int(input("Give me an integer between 1 and "+str(n)+": ").strip())
     
     while not(position>=1 and position <=n):
          position=int(input("Invalid number. Please enter integer between 1 and "+str(n)+": ").strip())
     return position

def play_game():
     
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)
     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     round_parity=0 
     while len(dealer)>0 and len(human)>0:
          if round_parity==0: 
               print("***********************************************************")
               print("Your turn.")
               print("\nYour current deck of cards is:")
               print_deck(human)
               
               card_position=get_valid_input(len(dealer))
               item=dealer[card_position-1]
               dealer.remove(item) 

              
               english_ordinals_end=["st", "nd", "rd", "th"]
               if card_position>3:
                   ord_index=3
               else:
                   ord_index=card_position-1
                   
               print("You asked for my "+str(card_position)+english_ordinals_end[ord_index]+" card.")

               print("Here it is. It is", item)

               human.append(item)
               print("\nWith", item, "added, your current deck of cards is:")
               print_deck(human)

               print("And after discarding pairs and shuffling, your deck is:")
               human=remove_pairs(human)
               print_deck(human)

               wait_for_player()
               round_parity=1
          
          else:
               print("***********************************************************")
               print("My turn.\n")
               card_index=random.randint(0,len(human)-1)
               item=human[card_index]
               human.remove(item)
               dealer.append(item)
               dealer=remove_pairs(dealer)

               
               english_ordinals_end=["st", "nd", "rd", "th"]
               if card_index>2:
                   ord_index=3
               else:
                   ord_index=card_index

               print("I took your "+str(card_index+1)+english_ordinals_end[ord_index]+" card.")

               wait_for_player()
               round_parity=0
               
          
     if len(dealer)==0:
          print("Ups. I do not have any more cards")
          print("You lost! I, Robot, win")
     else:
          print("***********************************************************")
          print("Ups. You do not have any more cards")
          print("Congratulations! You, Human, win")
	
	 

# main
play_game()
