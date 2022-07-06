
import os
import time
from input import *
from colorama import Fore, Back, Style
cannon_t_health = 1000
king_t_health = 1500
Barb_t_health = 300
TH_t_health = 2000
hut_t_health = 500
wall_t_health = 800
rows, cols = (21, 32)
matrix = [[0]*cols]*rows

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
        super().__init__("king", 200, king_t_health)

class Barbarians(Troop):
    def __init__(self,x,y):
        self.speed = 0.5
        self.x = x
        self.y = y
        super().__init__("barbarian", 44, Barb_t_health)   

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

    # def thmove(self):
    #     if(self.x<13):
    #         self.x+=1
    #     elif(self.x > 18):
    #         self.x-=1
        
    #     if(self.y<13):
    #         self.y+=1
    #     elif(self.y>18):
    #         self.y-=1
        

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

class Wall:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.hitpoints = wall_t_health

class Townhall:
    def __init__(self):
        self.hitpoints = TH_t_health

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

def display():

    # 21 * 32 grids 
    # Town Halls coordinates (4X3)
    # (10,14) --> (12,17)

    for i in range(0,21):
        for j in range(0,65):
            print("-",end=" ") 
        print("")

        for j in range(0,64):

            flag=0
            for k in range(len(barbarian)):
                if (barbarian[k].x-1) == i and ((2*(barbarian[k].y))-1) == j and barbarian[k].health >=0 :
                    hr = barbarian[k].health/Barb_t_health
                    if(hr>0.5 and hr<=1):
                        print(Back.GREEN + "B",end=' ')
                        print(Style.RESET_ALL, end="")
                    elif(hr>0.2 and hr<=0.5):
                        print(Back.YELLOW + "B",end=' ')
                        print(Style.RESET_ALL, end="")
                    elif(hr>0 and hr<=0.2):
                        print(Back.RED + "B",end=' ')
                        print(Style.RESET_ALL, end="")
                    else:
                        print("  ", end='')
                    flag=1
            if(flag==1):
                continue
                    
            if((i>=9 and i<=11) and (j==27 or j==29 or j==31 or j==33)):
                hr = townhall.hitpoints/TH_t_health
                if(hr>0.5 and hr<=1):
                    print(Fore.GREEN + "T",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Fore.YELLOW + "T",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Fore.RED + "T",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')
            
            elif(i==king.x-1 and j==(king.y*2-1)):
                hr = king.health/king_t_health
                if(hr>0.5 and hr<=1):
                    print(Back.GREEN + "K",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Back.YELLOW + "K",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Back.RED + "K",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')
            
            

            elif(i==8 and j==59):
                hr = hut1.hitpoints/hut_t_health
                if(hr>0.5 and hr<=1):
                    print(Fore.GREEN + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Fore.YELLOW + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Fore.RED + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')
            elif(i==16 and j==27):
                hr = hut2.hitpoints/hut_t_health
                if(hr>0.5 and hr<=1):
                    print(Fore.GREEN + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Fore.YELLOW + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Fore.RED + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')
            elif(i==4 and j==31):
                hr = hut3.hitpoints/hut_t_health
                if(hr>0.5 and hr<=1):
                    print(Fore.GREEN + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Fore.YELLOW + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Fore.RED + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')
            elif(i==11 and j==45):
                hr = hut4.hitpoints/hut_t_health
                if(hr>0.5 and hr<=1):
                    print(Fore.GREEN + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Fore.YELLOW + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Fore.RED + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')
            elif(i==10 and j==13):
                hr = hut5.hitpoints/hut_t_health
                if(hr>0.5 and hr<=1):
                    print(Fore.GREEN + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Fore.YELLOW + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Fore.RED + "H",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')


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
            
            elif(i==6 and j==41):
                hr = cannon1.hitpoints/cannon_t_health
                if(hr>0.5 and hr<=1):
                    print(Fore.GREEN + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Fore.YELLOW + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Fore.RED + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')
            elif(i==6 and j==19):
                hr = cannon2.hitpoints/cannon_t_health
                if(hr>0.5 and hr<=1):
                    print(Fore.GREEN + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Fore.YELLOW + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Fore.RED + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')
            elif(i==14 and j==19):
                hr = cannon3.hitpoints/cannon_t_health
                if(hr>0.5 and hr<=1):
                    print(Fore.GREEN + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Fore.YELLOW + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Fore.RED + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')
            elif(i==14 and j==41):
                hr = cannon4.hitpoints/cannon_t_health
                if(hr>0.5 and hr<=1):
                    print(Fore.GREEN + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0.2 and hr<=0.5):
                    print(Fore.YELLOW + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                elif(hr>0 and hr<=0.2):
                    print(Fore.RED + "C",end=' ')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end=' ')

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
    print("King's Health |",end='')
    for i in range(0,50):
        if(i<=(king.health/king_t_health)*50):
            print(Back.CYAN + " ",end='')
            print(Style.RESET_ALL,end="")
        else:
            print(" ",end="")
    print('',end='')
    print("|")


king = King(17,26)
cannon1 = Cannon(7,21)
cannon2 = Cannon(7,10)
cannon3 = Cannon(15,10)
cannon4 = Cannon(15,21)
cannon =[]
cannon.append(cannon1)
cannon.append(cannon2)
cannon.append(cannon3)
cannon.append(cannon4)

hut=[]
hut1 = Huts(9,30)
hut2 = Huts(17,14)
hut3 = Huts(5,16)
hut4 = Huts(12,23)
hut5 = Huts(11,7)

hut.append(hut1)
hut.append(hut2)
hut.append(hut3)
hut.append(hut4)
hut.append(hut5)

building=[]
for i in cannon:
    building.append(i)

for i in hut:
    building.append(i)

wall=[]
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

townhall = Townhall()

barbarian=[]


f = open("replay/replay.txt","r")

current_input = 0
replay_input = []  
replay_time = []
lines = f.readlines()
for line in lines:
    words=line.split(" ")
    if(len(words)==3):
        replay_input.append(" ")
        x=words[2].rstrip("\n")
        replay_time.append(float(x))
    else:
        x=words[1].rstrip("\n")
        replay_input.append(words[0])
        replay_time.append(float(x))        
start_time = time.time()
curr_move=0

heals_used = 0
rage_used = 0
no_of_barbs = 0
while(1):
    # print(chr(27) + "[2J")
    current_time = time.time()-start_time
    os.system("clear")
    display()

    if(townhall.hitpoints <=0 and len(building)==0):
        print(Fore.BLUE+"VICTORY!! \nGAME ENDED\n ATTACKER WON",end=" ")
        print(Style.RESET_ALL+"")
        break

    if(no_of_barbs==4):
        if((king.health <=0 and len(barbarian)==0) and (townhall.hitpoints >=0 and len(building)>=0)):
            print(Fore.BLUE+"DEFEAT -_-\nGAME ENDED\n DEFENDERS WON",end=" ")
            print(Style.RESET_ALL+"")
            break
    
    for barb in barbarian:
        if(barb.health <= 0):
            barbarian.remove(barb)
    
    for build in building:
        if(build.hitpoints <= 0):
            building.remove(build)


    time.sleep(0.1)
    input="h"

    if(curr_move >= len(replay_input) or time.time()-start_time<replay_time[curr_move]):
        input="h"
    elif(curr_move<len(replay_input)):
        input=replay_input[curr_move]    
        curr_move+=1

    if(input == 'w'):
        if((king.x-1==7 and king.y==21 and cannon1.hitpoints>0)or(king.x-1==7 and king.y==10 and cannon2.hitpoints>0)or(king.x-1==15 and king.y==21 and cannon4.hitpoints>0)or(king.x-1==15 and king.y==10 and cannon3.hitpoints>0) or (king.x-1==9 and king.y==30 and hut1.hitpoints>0)or(king.x-1==17 and king.y==14 and hut2.hitpoints>0)or(king.x-1==5 and king.y==16 and hut3.hitpoints>0)or(king.x-1==12 and king.y==23 and hut4.hitpoints>0)or(king.x-1==11 and king.y==7 and hut5.hitpoints>0)or(king.x-1==13 and (king.y>=13 and king.y<=18) and townhall.hitpoints>0) or king.x == 1):
            continue
        else:
            king.x = king.x - 1
        os.system("clear")
        display()
        print(input)
        time.sleep(0.5)
    if(input == 's'):
        if((king.x+1==7 and king.y==21 and cannon1.hitpoints>0)or(king.x+1==7 and king.y==10 and cannon2.hitpoints>0)or(king.x+1==15 and king.y==21 and cannon4.hitpoints>0)or(king.x+1==15 and king.y==10 and cannon3.hitpoints>0) or (king.x+1==9 and king.y==30 and hut1.hitpoints>0)or(king.x+1==17 and king.y==14 and hut2.hitpoints>0)or(king.x+1==5 and king.y==16 and hut3.hitpoints>0)or(king.x+1==12 and king.y==23 and hut4.hitpoints>0)or(king.x+1==11 and king.y==7 and hut5.hitpoints>0)or(king.x+1==9 and (king.y>=13 and king.y<=18) and townhall.hitpoints>0) or king.x == 21):
            continue
        else:
            king.x = king.x +1
        os.system("clear")
        display()
        print(input)
        time.sleep(0.5)
    if(input == 'a'):
        if((king.x==7 and king.y-1==21 and cannon1.hitpoints>0)or(king.x==7 and king.y-1==10 and cannon2.hitpoints>0)or(king.x==15 and king.y-1==21 and cannon4.hitpoints>0)or(king.x==15 and king.y-1==10 and cannon3.hitpoints>0) or (king.x==9 and king.y-1==30 and hut1.hitpoints>0)or(king.x==17 and king.y-1==14 and hut2.hitpoints>0)or(king.x==5 and king.y-1==16 and hut3.hitpoints>0)or(king.x==12 and king.y-1==23 and hut4.hitpoints>0)or(king.x==11 and king.y-1==7 and hut5.hitpoints>0)or(king.y==19 and (king.x>=9 and king.y<=13) and townhall.hitpoints>0) or king.y == 1):
            continue
        else:
            king.y-=1
        os.system("clear")
        display()
        print(input)
        time.sleep(0.5)
    if(input == 'd'):
        if((king.x==7 and king.y+1==21 and cannon1.hitpoints>0)or(king.x==7 and king.y+1==10 and cannon2.hitpoints>0)or(king.x==15 and king.y+1==21 and cannon4.hitpoints>0)or(king.x==15 and king.y+1==10 and cannon3.hitpoints>0) or (king.x==9 and king.y+1==30 and hut1.hitpoints>0)or(king.x==17 and king.y+1==14 and hut2.hitpoints>0)or(king.x==5 and king.y+1==16 and hut3.hitpoints>0)or(king.x==12 and king.y+1==23 and hut4.hitpoints>0)or(king.x==11 and king.y+1==7 and hut5.hitpoints>0)or(king.y==12 and (king.x>=9 and king.y<=13) and townhall.hitpoints>0) or king.y == 32):
            continue
        else:
            king.y+=1
        os.system("clear")
        display()
        print(input)
        time.sleep(0.5)
    if(input == ' '):
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

        if((king.x>=5 and king.x <= 17) and (king.y>=9 and king.y <=22) and king.health >0):
            townhall.hitpoints-=king.damage

        for w in wall:
            if(abs(king.x-w.x)<5 and abs(king.y-w.y)<5):
                w.hitpoints-=king.damage
        os.system("clear")
        display()
        print(input)
        time.sleep(0.5)
    if(input == '1'):
        if(no_of_barbs < 4):
            barbarian.append( Barbarians(3,4))
            no_of_barbs+=1
        os.system("clear")
        display()
        print(input)
        time.sleep(0.5)
    if(input == '2'):
        if(no_of_barbs < 4):
            barbarian.append( Barbarians(19,4))
            no_of_barbs+=1
        os.system("clear")
        display()
        print(input)
        time.sleep(0.5)
    if(input == '3'):
        if(no_of_barbs < 4):
            barbarian.append( Barbarians(3,28))
            no_of_barbs+=1
        os.system("clear")
        display()
        print(input)
        time.sleep(0.5)
    if(input == 'o'):
        if(rage_used < 2):
            rage_used +=1                    # Rage = 'o'
            if(king.health >0):
                king.damage *=2
                king.speed *=2
            for barb in barbarian:
                if(barb.health > 0):
                    barb.damage *= 2
                    barb.speed *= 2
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
            for barb in barbarian:
                if(barb.health > 0 and barb.health*1.5 < Barb_t_health):
                    barb.health *=1.5
                elif(barb.health > 0 and barb.health*1.5 >= Barb_t_health):
                    barb.health = Barb_t_health
        os.system("clear")
        display()
        print(input)
        time.sleep(0.5)
    
    if(((king.x>=2 and king.x <=12) and (king.y>=16 and king.y <=26) and cannon1.hitpoints > 0) or ((king.x>=2 and king.x <=12) and (king.y >=5 and king.y<=15) and cannon2.hitpoints>0) or ((king.x>=10 and king.x <= 20) and (king.y >= 5 and king.y <=15) and cannon3.hitpoints > 0) or ((king.x>=10 and king.x <= 20) and (king.y>=16 and king.y <=26) and cannon4.hitpoints >0)):
        king.health -= cannon1.damage

    for can in cannon:
        for barb in barbarian:
            if(abs(barb.x-can.x)<5 and abs(barb.y - can.y)<5 and can.hitpoints >0):
                barb.health -=cannon1.damage

    if(len(barbarian)!=0):
        for barb in barbarian:
            shortest_dist = 53
            dest_x = barb.x
            dest_y = barb.y
            dest_type = 'build'
            destroyed_wall = False 

            if(shortest_dist > abs(barb.x - cannon1.x) + abs(barb.y - cannon1.y) and cannon1.hitpoints>0):
                shortest_dist = abs(barb.x - cannon1.x) + abs(barb.y - cannon1.y)
                dest_x = cannon1.x
                dest_y = cannon1.y
            if(shortest_dist > abs(barb.x - cannon2.x) + abs(barb.y - cannon2.y) and cannon2.hitpoints>0):
                shortest_dist = abs(barb.x - cannon2.x) + abs(barb.y - cannon2.y)
                dest_x = cannon2.x
                dest_y = cannon2.y
            if(shortest_dist > abs(barb.x - cannon3.x) + abs(barb.y - cannon3.y) and cannon3.hitpoints>0):
                shortest_dist = abs(barb.x - cannon3.x) + abs(barb.y - cannon3.y)
                dest_x = cannon3.x
                dest_y = cannon3.y
            if(shortest_dist > abs(barb.x - cannon4.x) + abs(barb.y - cannon4.y) and cannon4.hitpoints>0):
                shortest_dist = abs(barb.x - cannon4.x) + abs(barb.y - cannon4.y)
                dest_x = cannon4.x
                dest_y = cannon4.y

            if(shortest_dist > abs(barb.x - hut1.x) + abs(barb.y - hut1.y) and hut1.hitpoints>0):
                shortest_dist = abs(barb.x - hut1.x) + abs(barb.y - hut1.y)
                dest_x = hut1.x
                dest_y = hut1.y
            if(shortest_dist > abs(barb.x - hut2.x) + abs(barb.y - hut2.y) and hut2.hitpoints>0):
                shortest_dist = abs(barb.x - hut2.x) + abs(barb.y - hut2.y)
                dest_x = hut2.x
                dest_y = hut2.y
            if(shortest_dist > abs(barb.x - hut3.x) + abs(barb.y - hut3.y) and hut3.hitpoints>0):
                shortest_dist = abs(barb.x - hut3.x) + abs(barb.y - hut3.y)
                dest_x = hut3.x
                dest_y = hut3.y
            if(shortest_dist > abs(barb.x - hut4.x) + abs(barb.y - hut4.y) and hut4.hitpoints>0):
                shortest_dist = abs(barb.x - hut4.x) + abs(barb.y - hut4.y)
                dest_x = hut4.x
                dest_y = hut4.y
            if(shortest_dist > abs(barb.x - hut5.x) + abs(barb.y - hut5.y) and hut5.hitpoints>0):
                shortest_dist = abs(barb.x - hut5.x) + abs(barb.y - hut5.y)
                dest_x = hut5.x
                dest_y = hut5.y
            
            if(shortest_dist > abs(barb.x - 11) + abs(barb.y - 15) and townhall.hitpoints>0):
                shortest_dist = abs(barb.x - 11) + abs(barb.y - 15)
                dest_type='th'
                
            
            if(dest_type=='build'):
                barb.move(dest_x, dest_y)

            elif(dest_type=='th'):
                for w in wall:
                    if(w.hitpoints<=0):
                        destroyed_wall = True
                        barb.moveto(w.x,w.y)
                        if(barb.x==w.x and barb.y==w.y):
                            townhall.hitpoints -= barb.damage
                if(destroyed_wall==False):
                    for w in wall:
                        if(shortest_dist > abs(barb.x-w.x) + abs(barb.y-w.y) and w.hitpoints>0):
                            dest_x = w.x
                            dest_y = w.y
                    barb.move(dest_x, dest_y)
                    if(len(barbarian)):
                        for barb in barbarian:
                            for w in wall:
                                if(((abs(barb.x-w.x)==1 and abs(barb.y-w.y)==0) or (abs(barb.y-w.y)==1 and abs(barb.x-w.x)==0)) and barb.health >0):
                                    w.hitpoints -= barb.damage
                

                

    if(len(barbarian)):
        for barb in barbarian:
            for build in building:
                if((abs(barb.x-build.x)==1 or abs(barb.x-build.x)==0) and (abs(barb.y-build.y)==1 or abs(barb.y-build.y)==0) and barb.health >0):
                    build.hitpoints -= barb.damage



    
    time.sleep(0.01)




