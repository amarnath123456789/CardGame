import random
deck =  ["As","2s","3s","4s","5s","6s","7s","8s","9s","10s","Ks","Qs","Js","Ac","2c","3c","4c","5c","6c","7c","8c","9c","10c","Kc","Qc","Jc"
         ,"Ah","2h","3h","4h","5h","6h","7h","8h","9h","10h","Kh","Qh","Jh","Ad","2d","3d","4d","5d","6d","7d","8d","9d","10d","Kd","Qd","Jd"]

card_rank_priority = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10,
    '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
    '4': 4, '3': 3, '2': 2
}

def get_card_priority(card):
    # Extract rank from card ('As' -> 'A', '10c' -> '10')
    rank = card[:-1]
    return card_rank_priority[rank]

# Create a new deck with priorities
priority_deck = {card: get_card_priority(card) for card in deck}

p1 = []
p2 = []
p3 = []
p4 = []


for i in range(0, len(deck), 4):

    x = random.choice(deck)
    p1.append(x)
    deck.remove(x)

    x = random.choice(deck)
    p2.append(x)
    deck.remove(x)

    x = random.choice(deck)
    p3.append(x)
    deck.remove(x)

    x = random.choice(deck)
    p4.append(x)
    deck.remove(x)

mideck = []
element = "As"
lists = [p1,p2,p3,p4]

for j in [p1,p2,p3,p4]:
    if element in j:
        mideck.append(element)
        j.remove(element)
        lists = lists[i:] + lists[:i]
        break

print(mideck)

p1, p2, p3, p4 = lists
'''print("p1:", p1)
print("p2:", p2)
print("p3:", p3)
print("p4:", p4)'''

current_turn = 1
turn_counter = 1
garbage_deck = []
highest_priority = 0


while True: 
   player_turn = lists[current_turn]
   print(player_turn)
   pl_input = input("Enter the card you want to Place")
   if pl_input in player_turn:
       mideck.append(pl_input)
       player_turn.remove(pl_input)
       current_turn = (current_turn + 1) % len(lists)
       turn_counter = turn_counter + 1
       print(turn_counter)
       if turn_counter == 4:
           garbage_deck.extend(mideck)
           for card in mideck:
               priority = priority_deck[card]
               if priority > highest_priority:
                highest_priority = priority
                highest_priority_card = card
           print(highest_priority_card)
           mideck.clear()
           print("Round Over")
           break


   

   print("Middle deck:", mideck)
   print("Remaining Cards",player_turn)
   print("Next player's Cards:", lists[current_turn])
   
print("Middle deck:", mideck)




   
