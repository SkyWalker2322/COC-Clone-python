import os
import time
from input import *
from colorama import Fore, Back, Style


cannon_t_health = 1000
king_t_health = 1500
queen_t_health = 1200
Barb_t_health = 300
Arch_t_health = 1500
Balloon_t_health = 300
TH_t_health = 2000
hut_t_health = 500
wiztow_t_health = 800
wall_t_health = 800

class Troop:
    def __init__(self,name,damage,health):
        self.name = name
        self.damage = damage
        self.health = health

class King(Troop):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 1
        self.last_move = 'w'
        super().__init__("king", 200, king_t_health)

class Queen(Troop):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.last_move = 'w'
        super().__init__("queen",250, queen_t_health)

class Barbarians(Troop):
    def __init__(self,x,y):
        self.speed = 0.5
        self.x = x
        self.y = y
        super().__init__("barbarian", 40, Barb_t_health)   

    def move(self, x_dest, y_dest):
        if(self.x < x_dest-1):
            self.x +=1
        elif(self.x > x_dest+1):
            self.x-=1
        else:
            pass

        if(self.y < y_dest-1):
            self.y +=1
        elif(self.y > y_dest+1):
            self.y -=1
        else:
            pass
    
    def moveto(self, x_dest, y_dest):
        if(self.x < x_dest):
            self.x +=1
        elif(self.x > x_dest):
            self.x-=1
        else:
            pass

        if(self.y < y_dest):
            self.y +=1
        elif(self.y > y_dest):
            self.y -=1
        else:
            pass


class Archer(Troop):
    def __init__(self,x,y):
        self.speed = 1
        self.x = x
        self.y = y
        super().__init__("archer", 20, Arch_t_health)   
    
    def arch_move(self, x_dest, y_dest):
        if(abs(self.x - x_dest)<3 and abs(self.y - y_dest)<3):
            return
        else:
            if(self.x < x_dest-1):
                self.x +=1
            elif(self.x > x_dest+1):
                self.x-=1
            
            if(self.y < y_dest-1):
                self.y +=1
            elif(self.y > y_dest+1):
                self.y -=1
        
class Balloon(Troop):
    def __init__(self,x,y):
        self.speed = 1
        self.x = x
        self.y = y
        super().__init__("archer", 80, Balloon_t_health)
    
    def move(self, x_dest, y_dest):
        if(self.x < x_dest-1):
            self.x +=1
        elif(self.x > x_dest+1):
            self.x-=1
        else:
            pass

        if(self.y < y_dest-1):
            self.y +=1
        elif(self.y > y_dest+1):
            self.y -=1
        else:
            pass

    def moveto(self, x_dest, y_dest):
        if(self.x < x_dest):
            self.x +=1
        elif(self.x > x_dest):
            self.x-=1
        else:
            pass

        if(self.y < y_dest):
            self.y +=1
        elif(self.y > y_dest):
            self.y -=1
        else:
            pass

class Cannon:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.damage = 5
        self.hitpoints = cannon_t_health

class Huts:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hitpoints = hut_t_health

class Wiztower:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.damage = 5
        self.hitpoints = wiztow_t_health

class Wall:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.hitpoints = wall_t_health

class Townhall:
    def __init__(self):
        self.hitpoints = TH_t_health

# ///////////////////////////////////////////////////General print functions/////////////////////////////////////////////////////////        

def print_wall(i):
    hr = wall[i].hitpoints/wall_t_health
    if(hr>0.5 and hr<=1):
        print(Fore.GREEN + "w",end=' ')
        print(Style.RESET_ALL, end="")
    elif(hr>0.2 and hr<=0.5):
        print(Fore.YELLOW + "w",end=' ')
        print(Style.RESET_ALL, end="")
    elif(hr>0 and hr<=0.2):
        print(Fore.RED + "w",end=' ')
        print(Style.RESET_ALL, end="")
    else:
        print(" ", end=' ')    

def print_element(l,hr):
    if(hr>0.5 and hr<=1):
        print(Fore.GREEN + l,end=' ')
        print(Style.RESET_ALL, end="")
    elif(hr>0.2 and hr<=0.5):
        print(Fore.YELLOW + l,end=' ')
        print(Style.RESET_ALL, end="")
    elif(hr>0 and hr<=0.2):
        print(Fore.RED + l,end=' ')
        print(Style.RESET_ALL, end="")
    else:
        print(" ", end=' ')
    
def print_troop(l,hr):
    if(hr>0.5 and hr<=1):
        print(Back.GREEN + l,end=' ')
        print(Style.RESET_ALL, end="")
    elif(hr>0.2 and hr<=0.5):
        print(Back.YELLOW + l,end=' ')
        print(Style.RESET_ALL, end="")
    elif(hr>0 and hr<=0.2):
        print(Back.RED + l,end=' ')
        print(Style.RESET_ALL, end="")
    else:
        print(" ", end=' ')

#//////////////////////////////////////Display()////////////////////////////////////////////////////////

def display():

    # 21 * 32 grids 
    # Town Halls coordinates (4X3)
    # (10,14) --> (12,17)

    for i in range(0,21):
        for j in range(0,65):
            print("-",end=" ") 
        print("")

        for j in range(0,64):

            flagbarb=0
            for k in range(len(barbarian)):
                if (barbarian[k].x-1) == i and ((2*(barbarian[k].y))-1) == j and barbarian[k].health >=0 :
                    hr = barbarian[k].health/Barb_t_health
                    print_troop("B",hr)
                    flagbarb=1
            if(flagbarb==1):
                continue

            flagarch=0
            for k in range(len(archer)):
                if (archer[k].x-1) == i and ((2*(archer[k].y))-1) == j and archer[k].health >=0 :
                    hr = archer[k].health/Arch_t_health
                    print_troop("A",hr)
                    flagarch=1
            if(flagarch==1):
                continue

            flagballoon=0
            for k in range(len(balloon)):
                if (balloon[k].x-1) == i and ((2*(balloon[k].y))-1) == j and balloon[k].health >=0 :
                    hr = balloon[k].health/Balloon_t_health
                    print_troop("O",hr)
                    flagballoon=1
            if(flagballoon==1):
                continue
                    
            if((i>=9 and i<=11) and (j==27 or j==29 or j==31 or j==33)):
                hr = townhall.hitpoints/TH_t_health
                print_element("T",hr)
            
            elif(i==king.x-1 and j==(king.y*2-1)):
                hr = king.health/king_t_health
                print_troop("K",hr)
            
            elif(i==queen.x-1 and j==(queen.y*2-1)):
                hr = queen.health/queen_t_health
                print_troop("Q",hr) 
            
            elif(i==hut1.x-1 and j==2*(hut1.y)-1):
                hr = hut1.hitpoints/hut_t_health
                print_element("H",hr)
            elif(i==hut2.x-1 and j==2*(hut2.y)-1):
                hr = hut2.hitpoints/hut_t_health
                print_element("H",hr)
            elif(i==hut3.x-1 and j==2*(hut3.y)-1):
                hr = hut3.hitpoints/hut_t_health
                print_element("H",hr)
            elif(i==hut4.x-1 and j==2*(hut4.y)-1):
                hr = hut4.hitpoints/hut_t_health
                print_element("H",hr)
            elif(i==hut5.x-1 and j==2*(hut5.y)-1):
                hr = hut5.hitpoints/hut_t_health
                print_element("H",hr)
                
            
            elif(wall[0].x-1 == i and (2*wall[0].y-1)==j):
                print_wall(0)
            elif(wall[1].x-1 == i and (2*wall[1].y-1)==j):
                print_wall(1)
            elif(wall[2].x-1 == i and (2*wall[2].y-1)==j):
                print_wall(2)
            elif(wall[3].x-1 == i and (2*wall[3].y-1)==j):
                print_wall(3)
            elif(wall[4].x-1 == i and (2*wall[4].y-1)==j):
                print_wall(4)
            elif(wall[5].x-1 == i and (2*wall[5].y-1)==j):
                print_wall(5)
            elif(wall[6].x-1 == i and (2*wall[6].y-1)==j):
                print_wall(6)
            elif(wall[7].x-1 == i and (2*wall[7].y-1)==j):
                print_wall(7)
            elif(wall[8].x-1 == i and (2*wall[8].y-1)==j):
                print_wall(8)
            elif(wall[9].x-1 == i and (2*wall[9].y-1)==j):
                print_wall(9)
            elif(wall[10].x-1 == i and (2*wall[10].y-1)==j):
                print_wall(10)
            elif(wall[11].x-1 == i and (2*wall[11].y-1)==j):
                print_wall(11)
            elif(wall[12].x-1 == i and (2*wall[12].y-1)==j):
                print_wall(12)
            elif(wall[13].x-1 == i and (2*wall[13].y-1)==j):
                print_wall(13)
            elif(wall[14].x-1 == i and (2*wall[14].y-1)==j):
                print_wall(14)
            elif(wall[15].x-1 == i and (2*wall[15].y-1)==j):
                print_wall(15)
            elif(wall[16].x-1 == i and (2*wall[16].y-1)==j):
                print_wall(16)
            elif(wall[17].x-1 == i and (2*wall[17].y-1)==j):
                print_wall(17)
            
            elif(i==cannon1.x-1 and j==2*(cannon1.y)-1):
                hr = cannon1.hitpoints/cannon_t_health
                print_element("C",hr)
            elif(i==cannon2.x-1 and j==2*(cannon2.y)-1):
                hr = cannon2.hitpoints/cannon_t_health
                print_element("C",hr)
            elif(i==cannon3.x-1 and j==2*(cannon3.y)-1):
                hr = cannon3.hitpoints/cannon_t_health
                print_element("C",hr)
            elif(i==cannon4.x-1 and j==2*(cannon4.y)-1):
                hr = cannon4.hitpoints/cannon_t_health
                print_element("C",hr)
            

            elif(i==wiztower1.x-1 and j==2*(wiztower1.y)-1):
                hr = wiztower1.hitpoints/wiztow_t_health
                print_element("E",hr)
            elif(i==wiztower2.x-1 and j==2*(wiztower2.y)-1):
                hr = wiztower2.hitpoints/wiztow_t_health
                print_element("E",hr)
            elif(i==wiztower3.x-1 and j==2*(wiztower3.y)-1):
                hr = wiztower3.hitpoints/wiztow_t_health
                print_element("E",hr)
            elif(i==wiztower4.x-1 and j==2*(wiztower4.y)-1):
                hr = wiztower4.hitpoints/wiztow_t_health
                print_element("E",hr)

            elif(i==2 and j==7):
                print(Fore.CYAN + "S",end=' ')
                print(Style.RESET_ALL, end="")
            elif(i==18 and j==7):
                print(Fore.CYAN + "S",end=' ')
                print(Style.RESET_ALL, end="")
            elif(i==2 and j==55):
                print(Fore.CYAN + "S",end=' ')
                print(Style.RESET_ALL, end="")

            elif(j%2==0):
                print("|",end=" ")
            else:
                print(" ",end=" ")
        print("|")
    for j in range(0,65):
        print("-",end=' ')
    print('')
    print("")
    if(queenflag==0):    
        print("King's Health |",end='')
        for i in range(0,50):
            if(i<=(king.health/king_t_health)*50):
                print(Back.CYAN + " ",end='')
                print(Style.RESET_ALL,end="")
            else:
                print(" ",end="")
        print('',end='')
        print("|")
        print("Last Step of the Hero: " + king.last_move)
    if(queenflag==1):
        print("Queen's Health |",end='')
        for i in range(0,50):
            if(i<=(queen.health/queen_t_health)*50):
                print(Back.CYAN + " ",end='')
                print(Style.RESET_ALL,end="")
            else:
                print(" ",end="")
        print('',end='')
        print("|")
        print("Last Step of the Hero: " + queen.last_move)



#//////////////////////////////////////////////Declarations////////////////////////////////////////////////////////////
barbarian=[]
archer = []
balloon = []
wiz_troops = []
wall=[]
cannon =[]
wiztower = []
hut=[]
building=[]

king = King(17,27)
queen = Queen(17,28)

cannon1 = Cannon(7,21)
cannon2 = Cannon(7,10)
cannon3 = Cannon(15,10)
cannon4 = Cannon(15,21)

wiztower1 = Wiztower(6,15)
wiztower2 = Wiztower(11,22)
wiztower3 = Wiztower(12,10)
wiztower4 = Wiztower(18,16)

hut1 = Huts(9,30)
hut2 = Huts(17,14)
hut3 = Huts(5,16)
hut4 = Huts(12,23)
hut5 = Huts(11,7)

townhall = Townhall()

os.system("clear")
queenflag = int(input("Whom do you want to control?, King -> 0; Queen -> 1 \nInput:"))
print("")

f = open("replay/replay.txt","w")
start_time = time.time()
heals_used = 0
rage_used = 0
no_of_barbs = 0
no_of_archers = 0
no_of_balloons = 0

# game_cont = ''
# /////////////////////////////////////////// MAIN loop /////////////////////////////////////////////////
for indez in range(0,3):
    if(indez==0):
        heals_used = 0
        rage_used = 0
        no_of_barbs = 0
        no_of_archers = 0
        no_of_balloons = 0 

        cannon1.hitpoints = -1
        cannon2.hitpoints = -1
        cannon3.hitpoints = cannon_t_health
        cannon4.hitpoints = cannon_t_health

        wiztower1.hitpoints = wiztow_t_health
        wiztower2.hitpoints = wiztow_t_health
        wiztower3.hitpoints = -1
        wiztower4.hitpoints = -1 
        
        hut1.hitpoints = hut_t_health
        hut2.hitpoints = hut_t_health
        hut3.hitpoints = hut_t_health
        hut4.hitpoints = hut_t_health
        hut5.hitpoints = hut_t_health

        townhall.hitpoints = TH_t_health

        barbarian.clear()
        archer.clear()
        balloon.clear()
        wiz_troops.clear()
        wall.clear()
        cannon.clear()
        wiztower.clear()
        hut.clear()
        building.clear()

        cannon.append(cannon1)
        cannon.append(cannon2)
        cannon.append(cannon3)
        cannon.append(cannon4)

        wiztower.append(wiztower1)  
        wiztower.append(wiztower2)  
        wiztower.append(wiztower3)  
        wiztower.append(wiztower4)  

        hut.append(hut1)
        hut.append(hut2)
        hut.append(hut3)
        hut.append(hut4)
        hut.append(hut5)

        for i in cannon:
            building.append(i)
        for i in hut:
            building.append(i)
        for i in wiztower:
            building.append(i)

        defences = []
        for i in cannon:
            defences.append(i)
        for i in wiztower:
            defences.append(i)

        wall.append( Wall(9,13))
        wall.append( Wall(9,14))
        wall.append( Wall(9,15))
        wall.append( Wall(9,16))
        wall.append( Wall(9,17))
        wall.append( Wall(9,18))
        wall.append( Wall(10,13))
        wall.append( Wall(10,18))
        wall.append( Wall(11,13))
        wall.append( Wall(11,18))
        wall.append( Wall(12,13))
        wall.append( Wall(12,18))
        wall.append( Wall(13,13))
        wall.append( Wall(13,14))
        wall.append( Wall(13,15))
        wall.append( Wall(13,16))
        wall.append( Wall(13,17))
        wall.append( Wall(13,18))
        
    if(indez==1):
        heals_used = 0
        rage_used = 0
        no_of_barbs = 0
        no_of_archers = 0
        no_of_balloons = 0 

        cannon1.hitpoints = cannon_t_health
        cannon2.hitpoints = -1
        cannon3.hitpoints = cannon_t_health
        cannon4.hitpoints = cannon_t_health

        wiztower1.hitpoints = wiztow_t_health
        wiztower2.hitpoints = wiztow_t_health
        wiztower3.hitpoints = -1
        wiztower4.hitpoints = wiztow_t_health
        
        hut1.hitpoints = hut_t_health
        hut2.hitpoints = hut_t_health
        hut3.hitpoints = hut_t_health
        hut4.hitpoints = hut_t_health
        hut5.hitpoints = hut_t_health

        townhall.hitpoints = TH_t_health

        barbarian.clear()
        archer.clear()
        balloon.clear()
        wiz_troops.clear()
        wall.clear()
        cannon.clear()
        wiztower.clear()
        hut.clear()
        building.clear()

        cannon.append(cannon1)
        cannon.append(cannon2)
        cannon.append(cannon3)
        cannon.append(cannon4)

        wiztower.append(wiztower1)  
        wiztower.append(wiztower2)  
        wiztower.append(wiztower3)  
        wiztower.append(wiztower4)  

        hut.append(hut1)
        hut.append(hut2)
        hut.append(hut3)
        hut.append(hut4)
        hut.append(hut5)

        for i in cannon:
            building.append(i)
        for i in hut:
            building.append(i)
        for i in wiztower:
            building.append(i)

        defences = []
        for i in cannon:
            defences.append(i)
        for i in wiztower:
            defences.append(i)

        wall.append( Wall(9,13))
        wall.append( Wall(9,14))
        wall.append( Wall(9,15))
        wall.append( Wall(9,16))
        wall.append( Wall(9,17))
        wall.append( Wall(9,18))
        wall.append( Wall(10,13))
        wall.append( Wall(10,18))
        wall.append( Wall(11,13))
        wall.append( Wall(11,18))
        wall.append( Wall(12,13))
        wall.append( Wall(12,18))
        wall.append( Wall(13,13))
        wall.append( Wall(13,14))
        wall.append( Wall(13,15))
        wall.append( Wall(13,16))
        wall.append( Wall(13,17))
        wall.append( Wall(13,18))

    if(indez==2):
        heals_used = 0
        rage_used = 0
        no_of_barbs = 0
        no_of_archers = 0
        no_of_balloons = 0 

        cannon1.hitpoints = cannon_t_health
        cannon2.hitpoints = cannon_t_health
        cannon3.hitpoints = cannon_t_health
        cannon4.hitpoints = cannon_t_health

        wiztower1.hitpoints = wiztow_t_health
        wiztower2.hitpoints = wiztow_t_health
        wiztower3.hitpoints = wiztow_t_health
        wiztower4.hitpoints = wiztow_t_health
        
        hut1.hitpoints = hut_t_health
        hut2.hitpoints = hut_t_health
        hut3.hitpoints = hut_t_health
        hut4.hitpoints = hut_t_health
        hut5.hitpoints = hut_t_health

        townhall.hitpoints = TH_t_health

        barbarian.clear()
        archer.clear()
        balloon.clear()
        wiz_troops.clear()
        wall.clear()
        cannon.clear()
        wiztower.clear()
        hut.clear()
        building.clear()

        cannon.append(cannon1)
        cannon.append(cannon2)
        cannon.append(cannon3)
        cannon.append(cannon4)

        wiztower.append(wiztower1)  
        wiztower.append(wiztower2)  
        wiztower.append(wiztower3)  
        wiztower.append(wiztower4)  

        hut.append(hut1)
        hut.append(hut2)
        hut.append(hut3)
        hut.append(hut4)
        hut.append(hut5)

        for i in cannon:
            building.append(i)
        for i in hut:
            building.append(i)
        for i in wiztower:
            building.append(i)

        defences = []
        for i in cannon:
            defences.append(i)
        for i in wiztower:
            defences.append(i)

        wall.append( Wall(9,13))
        wall.append( Wall(9,14))
        wall.append( Wall(9,15))
        wall.append( Wall(9,16))
        wall.append( Wall(9,17))
        wall.append( Wall(9,18))
        wall.append( Wall(10,13))
        wall.append( Wall(10,18))
        wall.append( Wall(11,13))
        wall.append( Wall(11,18))
        wall.append( Wall(12,13))
        wall.append( Wall(12,18))
        wall.append( Wall(13,13))
        wall.append( Wall(13,14))
        wall.append( Wall(13,15))
        wall.append( Wall(13,16))
        wall.append( Wall(13,17))
        wall.append( Wall(13,18))

    while(1):
        print(chr(27) + "[2J")
        w_counter = 0
        a_counter = 0
        s_counter = 0
        d_counter = 0
        current_time = time.time()-start_time
        os.system("clear")
        display()

        if(townhall.hitpoints <=0 and len(building)==0):
            print(Fore.BLUE+"VICTORY!! \nGAME ENDED\nATTACKER WON",end=" ")
            print(Style.RESET_ALL+"")
            break

        if(no_of_barbs+no_of_archers+no_of_balloons==12): 
            if((king.health <=0 and len(barbarian)==0) and (townhall.hitpoints >=0 or len(building)>=0)):
                print(Fore.BLUE+"DEFEAT -_-\nGAME ENDED\nDEFENDERS WON",end=" ")
                print(Style.RESET_ALL+"")
                break
        
        for barb in barbarian:
            if(barb.health <= 0):
                barbarian.remove(barb)

        for arch in archer:
            if(arch.health <= 0):
                archer.remove(arch)
        
        for bal in balloon:
            if(bal.health <=0):
                balloon.remove(bal)
            
        for troop in wiz_troops:
            if(troop.health <=0 ):
                wiz_troops.remove(troop)
        
        for build in building:
            if(build.hitpoints <= 0):
                building.remove(build)

        for defen in defences:
            if(defen.hitpoints <= 0):
                defences.remove(defen)

        # Replay//////
        input = input_to()
        print(input)
        if(input !=None):
            f.write("{} {}\n".format(input,current_time))

    # /////////////////////////////////////HEROS MOVEMENT AND ATTACK /////////////////////////////
        if(input == 'w'):
            if(queenflag==0):    
                king.last_move = 'w'
                if((king.x-1==13 and (king.y>=13 and king.y<=18) and townhall.hitpoints>0) or king.x == 1):
                    continue
                for build in building:
                    if(king.x-1==build.x and king.y==build.y and build.hitpoints):
                        w_counter=1
                        break
                if(w_counter==1):
                    continue
                else:
                    king.x = king.x - 1
                os.system("clear")
                display()
                print(input)
                time.sleep(0.5)
            if(queenflag==1):    
                queen.last_move='w'
                if((queen.x-1==13 and (queen.y>=13 and queen.y<=18) and townhall.hitpoints>0) or queen.x == 1):
                    continue
                for build in building:
                    if(queen.x-1==build.x and queen.y==build.y and build.hitpoints):
                        w_counter=1
                        break
                if(w_counter==1):
                    continue
                else:
                    queen.x = queen.x - 1
                os.system("clear")
                display()
                print(input)
                time.sleep(0.5)
        if(input == 's'):
            if(queenflag==0):   
                king.last_move='s' 
                if((king.x+1==9 and (king.y>=13 and king.y<=18) and townhall.hitpoints>0) or king.x == 21):
                    continue
                for build in building:
                    if(king.x+1==build.x and king.y==build.y and build.hitpoints):
                        s_counter=1
                        break
                if(s_counter==1):
                    continue
                else:
                    king.x = king.x + 1 
                os.system("clear")
                display()
                print(input)
                time.sleep(0.5)
            if(queenflag==1): 
                queen.last_move='s'   
                if((queen.x+1==9 and (queen.y>=13 and queen.y<=18) and townhall.hitpoints>0) or queen.x == 21):
                    continue
                for build in building:
                    if(queen.x+1==build.x and queen.y==build.y and build.hitpoints):
                        s_counter=1
                        break
                if(s_counter==1):
                    continue
                else:
                    queen.x = queen.x + 1 
                os.system("clear")
                display()
                print(input)
                time.sleep(0.5)
        if(input == 'a'):
            if(queenflag==0):  
                king.last_move='a'  
                if((king.y==19 and (king.x>=9 and king.x<=13) and townhall.hitpoints>0) or king.y == 1):
                    continue
                for build in building:
                    if(king.x==build.x and king.y-1==build.y and build.hitpoints):
                        a_counter=1
                        break
                if(a_counter==1):
                    continue
                else:
                    king.y-=1
                os.system("clear")
                display()
                print(input)
                time.sleep(0.5)
            if(queenflag==1):  
                queen.last_move='a'  
                if((queen.y==19 and (queen.x>=9 and queen.x<=13) and townhall.hitpoints>0) or queen.y == 1):
                    continue
                for build in building:
                    if(queen.x==build.x and queen.y-1==build.y and build.hitpoints):
                        a_counter=1
                        break
                if(a_counter==1):
                    continue
                else:
                    queen.y-=1
                os.system("clear")
                display()
                print(input)
                time.sleep(0.5)
        if(input == 'd'):
            if(queenflag==0):  
                king.last_move='d'  
                if((king.y==12 and (king.x>=9 and king.x<=13) and townhall.hitpoints>0) or king.y == 32):
                    continue
                for build in building:
                    if(king.x==build.x and king.y+1==build.y and build.hitpoints):
                        d_counter=1
                        break
                if(d_counter==1):
                    continue
                else:
                    king.y+=1
                os.system("clear")
                display()
                print(input)
                time.sleep(0.5)
            if(queenflag==1):
                queen.last_move='d'
                if((queen.y==12 and (queen.x>=9 and queen.x<=13) and townhall.hitpoints>0) or queen.y == 32):
                    continue
                for build in building:
                    if(queen.x==build.x and queen.y+1==build.y and build.hitpoints):
                        d_counter=1
                        break
                if(d_counter==1):
                    continue
                else:
                    queen.y+=1
                os.system("clear")
                display()
                print(input)
                time.sleep(0.5)
        if(input == ' '):
            if(queenflag==0):
                if((king.x>=2 and king.x <=12) and (king.y>=16 and king.y <=26) and king.health >0):
                    cannon1.hitpoints -= king.damage
                if((king.x>=2 and king.x <=12) and (king.y >=5 and king.y<=15) and king.health >0):
                    cannon2.hitpoints -= king.damage
                if((king.x>=10 and king.x <= 20) and (king.y >= 5 and king.y <=15) and king.health >0):
                    cannon3.hitpoints -= king.damage
                if((king.x>=10 and king.x <= 20) and (king.y>=16 and king.y <=26) and king.health >0):
                    cannon4.hitpoints-=king.damage

                if((king.x>=4 and king.x <= 14) and (king.y>=25 and king.y <=32) and king.health >0):
                    hut1.hitpoints-=king.damage
                if((king.x>=12 and king.x <= 22) and (king.y>=9 and king.y <=19) and king.health >0):
                    hut2.hitpoints-=king.damage
                if((king.x>=0 and king.x <= 10) and (king.y>=11 and king.y <=21) and king.health >0):
                    hut3.hitpoints-=king.damage
                if((king.x>=7 and king.x <= 17) and (king.y>=18 and king.y <=28) and king.health >0):
                    hut4.hitpoints-=king.damage
                if((king.x>=6 and king.x <= 16) and (king.y>=2 and king.y <=12) and king.health >0):
                    hut5.hitpoints-=king.damage

                for wiz in wiztower:
                    if(abs(king.x-wiz.x)<=5 and abs(king.y-wiz.y)<=5 and king.health):
                        wiz.hitpoints -= king.damage

                if((king.x>=5 and king.x <= 17) and (king.y>=9 and king.y <=22) and king.health >0):
                    townhall.hitpoints-=king.damage

                for w in wall:
                    if(abs(king.x-w.x)<5 and abs(king.y-w.y)<5):
                        w.hitpoints-=king.damage

            if(queenflag==1):
                if(queen.last_move=='w'):
                    for build in building:
                        if(abs(queen.x-8-build.x)<3 and abs(queen.y-build.y)<3 and build.hitpoints >0 ):
                            build.hitpoints -= queen.damage
                    for w in wall:
                        if(abs(queen.x-8-w.x)<3 and abs(queen.y-w.y)<3 and w.hitpoints >0 ):
                            w.hitpoints -= queen.damage
                    if(queen.y >11 and queen.y < 20 and queen.x-8 > 7 and queen.x-8 < 15):
                        townhall.hitpoints -= queen.damage

                if(queen.last_move=='a'):
                    for build in building:
                        if(abs(queen.x - build.x)<3 and abs(queen.y-8 - build.y)<3 and build.hitpoints >0 ):
                            build.hitpoints -= queen.damage
                    for w in wall:
                        if(abs(queen.x - w.x)<3 and abs(queen.y-8 - w.y)<3 and w.hitpoints >0 ):
                            w.hitpoints -= queen.damage
                    if(queen.y-8 >11 and queen.y-8 < 20 and queen.x > 7 and queen.x < 15):
                        townhall.hitpoints -= queen.damage

                if(queen.last_move=='s'):
                    for build in building:
                        if(abs(queen.x+8 - build.x)<3 and abs(queen.y - build.y)<3 and build.hitpoints >0 ):
                            build.hitpoints -= queen.damage
                    for w in wall:
                        if(abs(queen.x+8 - w.x)<3 and abs(queen.y - w.y)<3 and w.hitpoints >0 ):
                            w.hitpoints -= queen.damage
                    if(queen.y >11 and queen.y < 20 and queen.x+8 > 7 and queen.x+8 < 15):
                        townhall.hitpoints -= queen.damage

                if(queen.last_move=='d'):
                    for build in building:
                        if(abs(queen.x - build.x)<3 and abs(queen.y+8 - build.y)<3 and build.hitpoints >0 ):
                            build.hitpoints -= queen.damage
                    for w in wall:
                        if(abs(queen.x - w.x)<3 and abs(queen.y+8 - w.y)<3 and w.hitpoints >0 ):
                            w.hitpoints -= queen.damage
                    if(queen.y+8 >11 and queen.y+8 < 20 and queen.x > 7 and queen.x < 15):
                        townhall.hitpoints -= queen.damage
            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
    # /////////////////////////// TROOPS DEPLOYMENT ////////////////////////
        if(input == '1'):
            if(no_of_barbs < 4):
                barbarian.append( Barbarians(3,4))
                wiz_troops.append( Barbarians(3,4))
                no_of_barbs+=1
            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
        if(input == '2'):
            if(no_of_barbs < 4):
                barbarian.append( Barbarians(19,4))
                wiz_troops.append( Barbarians(19,4))
                no_of_barbs +=1
            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
        if(input == '3'):
            if(no_of_barbs < 4):
                barbarian.append( Barbarians(3,28))
                wiz_troops.append( Barbarians(3,28))
                no_of_barbs +=1
            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
        if(input == '4'):
            if(no_of_archers < 4):
                archer.append(Archer(3,4))
                wiz_troops.append( Archer(3,4))
                no_of_archers+=1
            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
        if(input == '5'):
            if(no_of_archers < 4):
                archer.append(Archer(19,4))
                wiz_troops.append( Archer(19,4))
                no_of_archers+=1
            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
        if(input == '6'):
            if(no_of_archers < 4):
                archer.append(Archer(3,28))
                wiz_troops.append( Archer(3,28))
                no_of_archers+=1
            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
        if(input == '7'):
            if(no_of_balloons < 3):
                balloon.append( Balloon(3,4))
                wiz_troops.append( Balloon(3,4))
                no_of_balloons+=1
            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
        if(input == '8'):
            if(no_of_balloons < 3):
                balloon.append( Balloon(19,4))
                wiz_troops.append( Balloon(19,4))
                no_of_balloons+=1
            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
        if(input == '9'):
            if(no_of_balloons < 3):
                balloon.append( Balloon(3,28))
                wiz_troops.append( Balloon(3,28))
                no_of_balloons+=1
            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
        if(input == 'o'):           # Rage = 'o'
            if(rage_used < 2):
                rage_used += 1
                if(king.health >0):
                    king.damage *=2
                    king.speed *=2
                if(queen.health >0):
                    queen.damage *=2
                    queen.speed *=2
                for barb in barbarian:
                    if(barb.health > 0):
                        barb.damage *= 2
                        barb.speed *= 2
                for arch in archer:
                    if(arch.health >0):
                        arch.damage *=2
                        arch.speed *=2
                for bal in balloon:
                    if(bal.health >0):
                        bal.damage *=2
                        bal.speed *=2
                os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
        if(input == 'p'):           # Heal = 'p'
            if(heals_used < 2):
                heals_used +=1
                if(king.health >0 and king.health*1.5 < king_t_health):
                    king.health *=1.5
                elif(king.health >0 and king.health*1.5 >= king_t_health):
                    king.health = king_t_health

                if(queen.health >0 and queen.health*1.5 < queen_t_health):
                    queen.health *=1.5
                elif(queen.health >0 and queen.health*1.5 >= queen_t_health):
                    queen.health = queen_t_health

                for barb in barbarian:
                    if(barb.health > 0 and barb.health*1.5 < Barb_t_health):
                        barb.health *=1.5
                    elif(barb.health > 0 and barb.health*1.5 >= Barb_t_health):
                        barb.health = Barb_t_health
                
                for arch in archer:
                    if(arch.health > 0 and barb.health*1.5 < Arch_t_health):
                        arch.health *=1.5
                    elif(arch.health > 0 and arch.health*1.5 >= Arch_t_health):
                        arch.health = Arch_t_health

                for bal in balloon:
                    if(bal.health > 0 and bal.health*1.5 < Balloon_t_health):
                        bal.health *=1.5
                    elif(bal.health > 0 and bal.health*1.5 >= Balloon_t_health):
                        bal.health = Balloon_t_health

            os.system("clear")
            display()
            print(input)
            time.sleep(0.5)
    # //////////////////// DEFENCES DAMAGE ////////////////////
        for can in cannon:
            if(abs(king.x-can.x)<4 and abs(king.y-can.y)<4 and can.hitpoints>0 and king.health>=0):
                king.health-=cannon1.damage
        
        for can in cannon:
            if(abs(queen.x-can.x)<4 and abs(queen.y-can.y)<4 and can.hitpoints>0 and queen.health>=0):
                queen.health-=cannon1.damage

        for can in cannon:
            for barb in barbarian:
                if(abs(barb.x-can.x)<4 and abs(barb.y - can.y)<4 and can.hitpoints>0 ):
                    barb.health -=cannon1.damage
                    break
            
        for can in cannon:
            for arch in archer:
                if(abs(arch.x - can.x)<4 and abs(arch.y - can.y)<4 and can.hitpoints >0):
                    arch.health -= cannon1.damage
                    break

        for wiz in wiztower:
            if(abs(king.x-wiz.x)<5 and abs(king.y-wiz.y)<5 and wiz.hitpoints>0 and king.health>=0):
                king.health-=wiztower1.damage
                
        for wiz in wiztower:
            if(abs(queen.x-wiz.x)<5 and abs(queen.y-wiz.y)<5 and wiz.hitpoints>0 and queen.health>=0):
                queen.health-=wiztower1.damage

        for wiz in wiztower:
            for troop in wiz_troops:
                if(abs(wiz.x - troop.x)<5 and abs(wiz.y - troop.y)<5 and troop.health>0 ):
                    for barb in barbarian:
                        if(abs(barb.x-troop.x)<2 and abs(barb.y - troop.y)<2 and barb.health >0):
                            barb.health -= wiztower1.damage
                    for bal in balloon:
                        if(abs(bal.x-troop.x)<2 and abs(bal.y - troop.y)<2 and bal.health >0):
                            bal.health -= wiztower1.damage
                    for arch in archer:
                        if(abs(arch.x-troop.x)<2 and abs(arch.y - troop.y)<2 and arch.health >0):
                            arch.health -= wiztower1.damage
                    break

    # //////////////////////// BARBARIAN MOTION ///////////////////

        if(len(barbarian)):
            for barb in barbarian:
                shortest_barb_dist = 53
                dest_barb_x = barb.x
                dest_barb_y = barb.y
                destroyed_wall = False 

                for build in building:
                    if(shortest_barb_dist > abs(barb.x - build.x) + abs(barb.y - build.y) and build.hitpoints>0 ):
                        shortest_barb_dist = abs(barb.x - build.x) + abs(barb.y - build.y)
                        dest_barb_x = build.x
                        dest_barb_y = build.y
                        dest_type = 'build'
                
                if(shortest_barb_dist > abs(barb.x - 11) + abs(barb.y - 15) and townhall.hitpoints>0):
                    shortest_barb_dist = abs(barb.x - 11) + abs(barb.y - 15)
                    dest_type='th'

                if(dest_type=='build'):
                    barb.move(dest_barb_x, dest_barb_y)

                elif(dest_type=='th'):
                    for w in wall:
                        if(w.hitpoints<=0):
                            destroyed_wall = True
                            barb.moveto(w.x,w.y)
                            if(barb.x==w.x and barb.y==w.y):
                                townhall.hitpoints -= barb.damage
                    if(destroyed_wall==False):
                        for w in wall:
                            if(shortest_barb_dist > abs(barb.x-w.x) + abs(barb.y-w.y) and w.hitpoints>0):
                                dest_barb_x = w.x
                                dest_barb_y = w.y
                        barb.move(dest_barb_x, dest_barb_y)
                        if(len(barbarian)):
                            for barb in barbarian:
                                for w in wall:
                                    if(((abs(barb.x-w.x)==1 and abs(barb.y-w.y)==0) or (abs(barb.y-w.y)==1 and abs(barb.x-w.x)==0)) and barb.health >0):
                                        w.hitpoints -= barb.damage

    # //////////////////// ARCHER MOTION //////////////////////

        if(len(archer)):
            for arch in archer:
                shortest_arch_dist = 53
                dest_arch_x = arch.x
                dest_arch_y = arch.y

                for build in building:
                    if(shortest_arch_dist > abs(arch.x - build.x) + abs(arch.y - build.y) and build.hitpoints>0 ):
                        shortest_arch_dist = abs(arch.x - build.x) + abs(arch.y - build.y)
                        dest_arch_x = build.x
                        dest_arch_y = build.y
                
                if(shortest_arch_dist > abs(arch.x - 10) + abs(arch.y - 14) and townhall.hitpoints>0):
                    shortest_arch_dist = abs(arch.x - 10) + abs(arch.y - 14)
                    dest_arch_x = 10
                    dest_arch_y = 14
                
                if(shortest_arch_dist > abs(arch.x - 10) + abs(arch.y - 17) and townhall.hitpoints>0):
                    shortest_arch_dist = abs(arch.x - 10) + abs(arch.y - 17)
                    dest_arch_x = 10
                    dest_arch_y = 17

                if(shortest_arch_dist > abs(arch.x - 12) + abs(arch.y - 14) and townhall.hitpoints>0):
                    shortest_arch_dist = abs(arch.x - 12) + abs(arch.y - 14)
                    dest_arch_x = 12
                    dest_arch_y = 14

                if(shortest_arch_dist > abs(arch.x - 12) + abs(arch.y - 17) and townhall.hitpoints>0):
                    shortest_arch_dist = abs(arch.x - 12) + abs(arch.y - 17)
                    dest_arch_x = 12
                    dest_arch_y = 17

                arch.arch_move(dest_arch_x, dest_arch_y)
                arch.arch_move(dest_arch_x, dest_arch_y)


    # ////////////////////BALLOON MOTION //////////////////////

        if(len(balloon)):
            if(len(defences)):
                for bal in balloon:
                    shortest_bal_dist = 53
                    dest_bal_x = bal.x
                    dest_bal_y = bal.y 

                    for defen in defences:
                        if(shortest_bal_dist > abs(bal.x - defen.x) + abs(bal.y - defen.y) and defen.hitpoints ):
                            shortest_bal_dist = abs(bal.x - defen.x) + abs(bal.y - defen.y)
                            dest_bal_x = defen.x
                            dest_bal_y = defen.y

                    bal.moveto(dest_bal_x, dest_bal_y)
                    bal.moveto(dest_bal_x, dest_bal_y)
            
            elif(len(building)):
                for bal in balloon:
                    shortest_bal_dist = 53
                    dest_bal_x = bal.x
                    dest_bal_y = bal.y
                    destroyed_wall = False 

                    for build in building:
                        if(shortest_bal_dist > abs(bal.x - build.x) + abs(bal.y - build.y) and build.hitpoints ):
                            shortest_bal_dist = abs(bal.x - build.x) + abs(bal.y - build.y)
                            dest_bal_x = build.x
                            dest_bal_y = build.y
                    
                    if(shortest_bal_dist > abs(bal.x - 11) + abs(bal.y - 15) and townhall.hitpoints>0):
                        shortest_bal_dist = abs(bal.x - 11) + abs(bal.y - 15)
                        dest_bal_x = 11
                        dest_bal_y = 15

                    bal.moveto(dest_bal_x, dest_bal_y)
                    bal.moveto(dest_bal_x, dest_bal_y)
                    

    # ///////////////////Troops attacks////////////////////////
        if(len(balloon)):
            for bal in balloon:
                for build in building:
                    if((abs(bal.x-build.x)==0) and (abs(bal.y-build.y)==0) and bal.health >0):
                        build.hitpoints -= bal.damage
                        break
                if((bal.x >=10 and bal.x <=12)  and (bal.y >= 14 and bal.y <= 17) and bal.health):
                    townhall.hitpoints -= bal.damage
                        
        if(len(barbarian)):
            for barb in barbarian:
                for build in building:
                    if((abs(barb.x-build.x)==1 or abs(barb.x-build.x)==0) and (abs(barb.y-build.y)==1 or abs(barb.y-build.y)==0) and barb.health >0):
                        build.hitpoints -= barb.damage
                        break

        if(len(archer)):
            for arch in archer:
                for build in building:
                    if(abs(arch.x-build.x)<3 and abs(arch.y-build.y)<3 and arch.health):
                        build.hitpoints -= arch.damage
                        break
                if( ((abs(arch.x-10)<3 and abs(arch.y-14)<3) or (abs(arch.x-10)<3 and abs(arch.y-17)<3) or (abs(arch.x-12)<3 and abs(arch.y-14)<3) or (abs(arch.x-12)<3 and abs(arch.y-17)<3))  and arch.health ):
                    townhall.hitpoints -= arch.damage
                    
        time.sleep(0.0001) 

    # if(indez==0 or indez==1):
    #     print("Level Ended!! Do you want to continue to next level? 1-> yes and 0-> no")
    #     game_cont = input()
    # else:
    #     print("GAME ENDED !!!")
    
    # if(game_cont==1):
    #     continue
    # elif(game_cont==0):
    #     break

print("GAME ENDED")