#BlackJack Game

import random
global players_chips
global bet_chip
class deck():
    suits=['heart','diamond','club','spade']
    values=['A','2','3','4','5','6','7','8','9','10','J','K','Q']
    random.shuffle(suits)
    random.shuffle(values)
    def __str__(self):
        return "THE DECK IS READY"


class chips():
    def __init__(self,total_chip,chip):
        self.chip=chip
        self.total_chip=total_chip
    def chip_chk(self):
        if self.chip>self.total_chip:
            print( "Player's bet exceeds the available chips! Please enter the valid value" )
            return 'Q'
        else:
            print( "Players total available chips is {} and bet is {}".format(self.total_chip,self.chip))
def win_chip():
    print("Player's total available chips is {}".format(players_chips))
def lose_chip():
    print("Player's total available chips is {}".format(players_chips))

            

class player(deck):
    def choice(self):
       global s
       s=random.choice(deck.suits)
       global v
       v=random.choice(deck.values)
       choice=v + " of " + s
       return choice
    
class dealer(deck):
    def choice(self):
       global s
       s=random.choice(deck.suits)
       global v
       v=random.choice(deck.values)
       choice=v + " of " + s
       return choice    
global inp
inp='Y'
d={'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'K':10,'Q':10}

print("Welcome to the Black Jack Game\n")
players_chips=int(input("How much chips does the player have\n"))
while inp=='Y':
    d_lst=[]
    p_lst=[]
    p_sum=0
    d_sum=0
    Bust=False
    d_Bust=False
    bet_chip=int(input("How much does the player wish to bet\n"))
    c=chips(players_chips,bet_chip)
    p=c.chip_chk()
    if p=='Q':
        continue
    dck=deck()
    print(dck)
    d1=dealer()
    d_card_1=d1.choice()
    print("Dealers first card \n" + d_card_1)
    d_sum=d[v]+d_sum
    d_lst.append(v)
    d_card_1=d1.choice()
    d_sum=d[v]+d_sum
    d_lst.append(v)
    p1=player()
    p_card_1=p1.choice()
    print("players first card \n" + p_card_1)
    p_sum=p_sum+d[v]
    p_lst.append(v)
    p_card_2=p1.choice()
    print("players second card\n" + p_card_2)
    p_sum=p_sum+d[v]
    p_lst.append(v)
    print("Players total value is {}\n".format(p_sum))
    while Bust!=True:
        h_s=input("Do the player want to HIT or STAY \n")
        if h_s=='HIT':
            p_card_3=p1.choice()
            print("Players next card " + p_card_3)
            p_sum=p_sum+d[v]
            if p_sum<21:
                print("Players new value is {}\n".format(p_sum))
                p_lst.append(v)
            if p_sum>21:
                if 'A' in p_lst:
                    p_sum=p_sum-10
                    p_lst.remove('A')
                    print("Players new value is {}\n".format(p_sum))
                    if p_sum>21:
                        Bust=True
                        print("Player Busts, Dealer wins {} chips\n".format(bet_chip))
                        players_chips=players_chips-bet_chip
                        lose_chip()
                        break
                else:
                    Bust=True
                    print("Player Busts, Dealer wins {} chips\n".format(bet_chip))
                    players_chips=players_chips-bet_chip
                    lose_chip()
                    break
            elif p_sum==21:
                print("Player Wins!!! {}chips\n" .format(bet_chip))
                players_chips=players_chips+bet_chip
                win_chip()
                Bust=True
            else:
                continue
        if h_s=='STAY':
            while d_Bust!=True:
                if d_sum>21:
                    if 'A' in d_lst:
                        d_sum=d_sum-10
                        d_lst.remove('A')
                        if d_sum>21:
                            d_Bust=True
                            print("Dealer Busts, player wins {} chips\n". format(bet_chip))
                            players_chips=players_chips+bet_chip
                            win_chip()
                            Bust=True
                            break
                    else:
                        d_Bust=True
                        print("Dealer Busts, player wins {} chips\n". format(bet_chip))
                        players_chips=players_chips+bet_chip
                        win_chip()
                        Bust=True
                        break
                elif d_sum>p_sum:
                    print("Dealer Wins!!! {} chips\n".format(bet_chip))
                    players_chips=players_chips-bet_chip
                    lose_chip()
                    Bust=True
                    break
                else:
                    print("Dealer hits again")
                    d_card_3=d1.choice()
                    print(d_card_3)
                    d_sum=d_sum+d[v]
                    if d_sum<21:
                        print("Dealer's new value is {}\n".format(d_sum))
                    d_lst.append(v)

    inp=input("Do you wish to play another Game?")

        
            
        
        
        
