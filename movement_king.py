# Final Project
# Ben & Jerry
# Adventure game: King's Vengeance
from pygame import *
from random import *
from math import *

init()

#-------------------------------------------------------music------------------------------------------------
mixer.music.load("FloorMusic.mp3")
mixer.music.play(-1)
#-------------------------------------------------------------variables----------------------------------------------------------

floor = 0   #keep track of the floor, used as the index in 3D/2D loops that are related to the floor number

#--------------------conditions----------------------------
condition = 0  #the condition for the king, in this case the king is simply standing
rook_condition = 0 #the condition for the rook boss
queen_condition = 0 #the condition for the queen boss
dracula_condition = 0 #the condition for the dracula boss

#------------------dracula-variables----------------------
static_time = 0 #later used for boss' attacks
D_left = True #whether dracula
D_distance = 0 #the distance dracula moves when retreating

#-------------------other-variables-------------------
frame = 0 #the frame of the enemies/backgrounds
frame1 = 0 #frame of the main character, so his frame does not interfere with enemies and i can make change to it more easily
           #(e.g. when i set frame1 = 0, it does not stop enemies' movements)
SPEED = 10 #every sprite picture and gif picture will be blitted for 10 loops

storycounter = 0 #used in the story in menu to count for the story pics blitted

King_HP = 1500 #main character's initial health


def distance(x1,y1,x2,y2): # function used to calculate the distance between two points. mainly used between main character and enemies
    distance = hypot(x1-x2,y1-y2)
    return distance


def flipPic(pic): #function used to flip the pictures horizontally so that the ennemies/main character 's can face/ attack to different directions
    pic_flipped = transform.flip(pic, True, False)
    return pic_flipped

def transformpic(pic,size1,size2): #fuction used to transform pics into different sizes (as useless as the distance function above, we
                                   #created these two functions cuz we are too lazy and we can't remember the python functions)
    transformpic = transform.scale(pic,(size1,size2))
    return transformpic


#-------------------------------------------------------------background-pics----------------------------------------------------
backgroundpics = [[],[],[],[],[],[]]
for i in range(1,9):
    backgroundpics[0].append(image.load(f"FirstFloor/FirstFloor ({i}).gif")) #backgroundpics[0] now contains pics for the 1st floor
for i in range(1,6):
    backgroundpics[1].append(image.load(f"RookBoss/RookBoss ({i}).gif")) # rook boss room
for i in range(1,7):
    backgroundpics[2].append(image.load(f"ThirdFloor/ThirdFloor ({i}).gif")) # 2nd floor
for i in range(1,7):
    backgroundpics[3].append(image.load(f"QueenBoss/QueenBoss ({i}).gif")) # queen boss room
    
backgroundpics[4].append(image.load("ThirdFloor.png")) #3rd floor (not gif so no for loop)

for i in range(1,21):
    backgroundpics[5].append(image.load(f"KingBoss/KingBoss ({i}).gif")) #dracula boss room

spike_pic = image.load("Spike.png")
platform_pic = image.load("Platform.png")

chest = []
for i in range(1,4):
        chest_pic = image.load(f"Chest/Chest ({i}).gif")
        official_chest = transform.scale(chest_pic,(80,80))
        chest.append(official_chest)

backgroundmenu = []
for i in range(1,23):
    backgroundmenu.append(image.load(f"MenuBackground/MenuBackground ({i}).gif")) #background for the menu page

#-------------------------------------------------------------enemy-pics------------------------------------------------------------
pawnWalkingPic = [] # with enemies facing right
pawnWalkingPic_Left = [] # with enemies facing left
for i in range(0,6):
    walkingPawnPic = image.load(f"PawnWalking/PawnWalking{i}.png")
    pawnWalkingPic.append(walkingPawnPic)
    pawnWalkingPic_Left.append(flipPic(walkingPawnPic))

knightWalkingPic = []
knightWalkingPic_Left = []
for i in range(0,9):
    walkingKnightPic = image.load(f"KnightWalking/KnightWalking{i}.png")
    knightWalkingPic.append(walkingKnightPic)
    knightWalkingPic_Left.append(flipPic(walkingKnightPic))

knightRunningPic = []
knightRunningPic_Left = []
for i in range(0,10):
    runningKnightPic = image.load(f"KnightRunning/KnightRunning{i}.png")
    knightRunningPic.append(runningKnightPic)
    knightRunningPic_Left.append(flipPic(runningKnightPic))

knightAttackPic = []
knightAttackPic_Left = []
for i in range(0,10):
    AttackKnightPic = image.load(f"KnightAttack/KnightAttack{i}.png")
    knightAttackPic.append(AttackKnightPic)
    knightAttackPic_Left.append(flipPic(AttackKnightPic))

bishopAttack1Pic = []
bishopAttack1Pic_Left = []
for i in range (0,6):
    AttackingBishopPic1 = image.load(f"Bishop1Attack/Bishop1Attack{i}.png")
    bishopAttack1Pic.append(AttackingBishopPic1)
    bishopAttack1Pic_Left.append(flipPic(AttackingBishopPic1))

bishopAttack2Pic = []
bishopAttack2Pic_Left = []
for i in range (1,7):
    AttackingBishopPic2 = image.load(f"Bishop2Attack/Bishop2Attack ({i}).png")
    bishopAttack2Pic.append(AttackingBishopPic2)
    bishopAttack2Pic_Left.append(flipPic(AttackingBishopPic2))

bishopExplosionPic = []
for i in range(1,10):
    bishopExplosionPic.append(image.load(f"BishopExplosion/BishopExplosion ({i}).png"))

BishopBullet = image.load("BishopBullet.png")
BishopBullet_Left = flipPic(BishopBullet)

RookEntrancePic = []
RookEntrancePic_Left = []
for i in range(1,9):
    rookentrance = image.load(f"RookEntrance/RookEntrance ({i}).png")
    RookEntrancePic.append(rookentrance)
    RookEntrancePic_Left.append(flipPic(rookentrance))

RookIdlePic = image.load("RookIdle.png")
RookIdlePic_Left = flipPic(RookIdlePic)

RookDisappearPic = []
RookDisappearPic_Left = []
for i in range(1,10):
    DisappearingRook = image.load(f"RockDisappear/Rock{i}.png")
    RookDisappearPic.append(DisappearingRook)
    RookDisappearPic_Left.append(flipPic(DisappearingRook))

RockPic = image.load("Rock.png")

QueenEntrancePic = []
for i in range(0,4):
    queenentrance = image.load(f"QueenEntranceFall/QueenEntranceFall{i}.png")
    QueenEntrancePic.append(queenentrance)

QueenAttack1Pic = []
QueenAttack1Pic_Left = []
for i in range (0,9):
    AttackingQueenPic1 = image.load(f"ShortRangeQueenAttack/ShortRangeQueenAttack{i}.png")
    QueenAttack1Pic.append(AttackingQueenPic1)
    QueenAttack1Pic_Left.append(flipPic(AttackingQueenPic1))

QueenAttack2Pic = []
QueenAttack2Pic_Left = []
for i in range (0,14):
    AttackingQueenPic2 = image.load(f"LongRangeQueenAttack/LongRangeQueenAttack{i}.png")
    QueenAttack2Pic.append(AttackingQueenPic2)
    QueenAttack2Pic_Left.append(flipPic(AttackingQueenPic2))    

QueenWalkingPic = []
QueenWalkingPic_Left = []
for i in range(1,10):
    WalkingQueenPic = image.load(f"QueenWalking/QueenWalking ({i}).png")
    QueenWalkingPic.append(WalkingQueenPic)
    QueenWalkingPic_Left.append(flipPic(WalkingQueenPic))

QueenShortSpearPic = image.load("third_last_arrow0.png")
QueenShortSpearPic_Left = flipPic(QueenShortSpearPic)

QueenLongSpearPic = image.load("queen_last_arrow0.png")

#-------dracula-boss-pictures------------------------
BatPic = []
BatPic_Left = []
for i in range(1,11):
    batPic = image.load(f"Bats/Bats ({i}).png")
    BatPic.append(batPic)
    BatPic_Left.append(flipPic(batPic))

DIdle = image.load("EvilKingIdle (1).png")
DIdle_Left = flipPic(DIdle)

DAttackPic = []
DAttackPic_Left = []
for i in range(1,7):
    dattackPic = image.load(f"DAttack/EvilKingDisappear ({i}).png")
    DAttackPic.append(dattackPic)
    DAttackPic_Left.append(flipPic(dattackPic))

DRetreatPic = []
DRetreatPic_Left = []
for i in range(1,8):
    dretreatPic = image.load(f"DRetreat/EvilKingAppear ({i}).png")
    DRetreatPic.append(dretreatPic)
    DRetreatPic_Left.append(flipPic(dretreatPic))

DSummonPic = []
DSummonPic_Left = []
for i in range(1,10):
    summonPic = image.load(f"DSummon/EvilKingIdle ({i}).png")
    DSummonPic.append(summonPic)
    DSummonPic_Left.append(flipPic(summonPic))

DSummon2Pic = []
DSummon2Pic_Left = []
for i in range(1,9):
    dsummon2Pic = image.load(f"DSummon2/EvilKingLaugh ({i}).png")
    DSummon2Pic.append(dsummon2Pic)
    DSummon2Pic_Left.append(flipPic(dsummon2Pic))

FireballPic = []
FireballPic_Left = []
for i in range(1,8):
    fireballPic = image.load(f"Fireball/ShootingFireball ({i}).png")
    FireballPic.append(fireballPic)
    FireballPic_Left.append(flipPic(fireballPic))

WolfPic = []
WolfPic_Left = []
for i in range(1,7):
    wolfPic = image.load(f"Wolf/WolfRunning ({i}).png")
    WolfPic.append(wolfPic)
    WolfPic_Left.append(flipPic(wolfPic))

IceCream = image.load("icecream.png") # for the easter egg

#-----------congratulations---------------
CongratsWord = image.load("CongratsPic.png")
EndScene = image.load("EndScene.png")
offEndScene = transformpic(EndScene,1200,800)

    
#----------animation-set-up------------------
myClock = time.Clock() #so the pics are not blitted too fast


#-----------initial-screen-set-up---------
size = width, height = 1200,800 
screen = display.set_mode(size)

#-------------------------------------------------------------------king-pictures---------------------------------------
king_StandingPic = []
king_StandingPic_Left = []
StandingKing_pic = image.load(f"RunningKing/KingIdle0.png")
king_StandingPic.append(StandingKing_pic)
king_StandingPic_Left.append(flipPic(StandingKing_pic))

king_RunningPic = []
king_RunningPic_Left = []
for i in range (0,6):
    RunningKing_pic = image.load(f"RunningKing/RunningKing{i}.png")
    king_RunningPic.append(RunningKing_pic)
    king_RunningPic_Left.append(flipPic(RunningKing_pic))

king_JumpingPic = []
king_JumpingPic_Left = []
for i in range (0,4):
    JumpingKing_pic = image.load(f"KingJumping/KingJumping{i}.png")
    king_JumpingPic.append(JumpingKing_pic)
    king_JumpingPic_Left.append(flipPic(JumpingKing_pic))

king_AttackingPic = []
king_AttackingPic_Left = []
for i in range (0,4):
    AttackingKing_pic = image.load(f"KingAttacking/KingAttacking{i}.png")
    king_AttackingPic.append(AttackingKing_pic)
    king_AttackingPic_Left.append(flipPic(AttackingKing_pic))

SwordArcPic = image.load("SwordArc.png")
SwordArcPic_Left = flipPic(SwordArcPic)

king_JumpAttackPic = [] 
king_JumpAttackPic_Left = []
for i in range (0,7):
    JumpAttackKing_pic = image.load(f"KingJumpAttack/KingJumpAttack{i}.png")
    king_JumpAttackPic.append(JumpAttackKing_pic)
    king_JumpAttackPic_Left.append(flipPic(JumpAttackKing_pic))


#----------------------------------------------------Menu-pictures---------------------------------
firstpartstory = image.load("FirstPartStory.png")
secondpartstory = image.load("SecondPartStory.png")
thirdpartstory = image.load("ThirdPartStory.png")
fourthpartstory = image.load("FourthPartStory.png")
firststory = transformpic(firstpartstory,1200,800)
secondstory = transformpic(secondpartstory,1200,800)
thirdstory = transformpic(thirdpartstory,1200,800)
fourthstory = transformpic(fourthpartstory,1200,800)

credits = image.load("credits.png")
offcredits = transform.scale(credits,(200,50)) #"off" means official, the picture we are using in the end

title = image.load("Title.png")
offtitle = transform.scale(title,(500,260))

button1 = image.load("gamebutton.png")
button1clicked = image.load("gamebuttonclicked.png")
offbutton1 = transformpic(button1,230,70)
offbutton1clicked = transformpic(button1clicked,230,70)

button2 = image.load("controlbutton.png")
button2clicked = image.load("controlbuttonclicked.png")
offbutton2 = transformpic(button2,230,70)
offbutton2clicked = transformpic(button2clicked,230,70)

button3 = image.load("storybutton.png")
button3clicked = image.load("storybuttonclicked.png")
offbutton3 = transformpic(button3,230,70)
offbutton3clicked = transformpic(button3clicked,230,70)



#-----------------------------------------------------flags-------------------------------------------
facing_Right = True # for the main character so all his movements can change direction accordingly
jump = False #in order to distinguish jump and jump attack for the main character
attack = False #in order to distinguish jump and jump attack for the main character
onGround = True #checks whether the character is on the ground or not, used in checkplats function
inAir = False #checks whether the character is on the ground or not, used in checkplats function
king_attacking = False # check when to deal damage to the enemies
num_of_frame = 0 #a variable to replace (frame // SPEED % len(something) since its a bit too long, but not too useful
secret_room = False #checks whether the player reaches the easter egg or not


#----------------------------------------------------Drawing----------------------------------------
def drawScene(screen, guy):
    """ draws the current state of the game """
    global frame
    global SPEED
    global num_of_frame
    global King_HP
    global king_attacking
    global chestcounter
    global frame1
    global rook_condition
    global queen_condition
    global dracula_condition
    global dracula
    global D_left
    global D_distance
    global static_time 
    global queen_longspear_rect_list
    global queen_longspear_Left_rect_list
    global secret_room
    global platforms_rect

    frame1 += 1 #the enemies' frame increases every loop, creating the animation
    frame += 1#the character's frame increases every loop, creating the animation
    
    #------------------------------------background------------------------------
    offset = 250 - guy[X] # so the background(and enemies) moves according to the position of the player, creating the illusion that our character is moving n the world

    screen.fill((255,255,255))######useless?
    
    if floor == 1 or floor == 3 or floor == 5: # backgrounds for the boss rooms, since we don'tneed the background to move with our character, we don't need to use offset 
        screen.blit(backgroundpics[floor][frame // SPEED % len(backgroundpics[floor])],(0,0))
        
    else: # backgrounds for the normal floors
        screen.blit(backgroundpics[floor][frame // SPEED % len(backgroundpics[floor])],(offset%1200,0)) #our background pica all have a width of 1200, this line and the one below ensures
                                                                                                        #that the background is smooth 
        screen.blit(backgroundpics[floor][frame // SPEED % len(backgroundpics[floor])],(offset%1200-1200,0))

    if floor == 1 and secret_room == True: #easter egg
        if Rect(200,550,110,20) in platforms_rect[1] and Rect(360,460,110,20) in platforms_rect[1] and Rect(520,370,110,20) in platforms_rect[1] and Rect(700,390,200,20) in platforms_rect[1]:
            platforms_rect[1].remove(Rect(200,550,110,20))
            platforms_rect[1].remove(Rect(360,460,110,20))
            platforms_rect[1].remove(Rect(520,370,110,20))
            platforms_rect[1].remove(Rect(700,390,200,20)) #delete the platforms in the room
        screen.blit(IceCream,(0,0)) #easter egg page
        guy[3] = 1 #so the character is now strengthened
        

    for s in spikes[floor]: #draws spikes
        screen.blit(spike_pic,(s[0]+offset,s[1]))

    for p in platforms[floor]: #draws platforms
        screen.blit(platform_pic,(p[0]+offset,p[1]))

    for c in chest_rect[floor]: #draws chests
        if c[1] == 0: #if its not opened
            screen.blit(chest[0],(c[0].x+offset,c[0].y)) #blit closed chest
            if king_rect.colliderect(c[0]):
                c[1] = 1
                King_HP += 150*(floor+1) #adds health to the character if colliderct
        elif c[1] == 1: #if it's opened
            screen.blit(chest[2],(c[0].x+offset,c[0].y)) #blit opened chest
            
    
    #draw.rect(screen, (255,255,0), (200,guy[Y],40,40))
    #draw.rect(screen, (255,255,0), wall.move(offset,0))
    #---------------------------enemy-drawing--------------------------
    for p in pawns[floor]: #draws pawns
        if p[2] <= 0: #if its killed
            pawns[floor].remove(p)
        else:
            if floor != 5: #if in normal floor
                if guy[0]-20 > p[0]:
                    screen.blit(pawnWalkingPic[int(frame // SPEED % len(pawnWalkingPic))],(p[0]+offset,p[1])) #has offset as it moves when our character moves
                if guy[0]-20 < p[0]:
                    screen.blit(pawnWalkingPic_Left[int(frame // SPEED % len(pawnWalkingPic_Left))],(p[0]+offset,p[1]))
                if distance(guy[0],guy[1],p[0],p[1]) <= (20+2*floor): #dealing damage
                    King_HP -= (10 + 2*floor)#damage increases as floor increases
            else: #if in boss room (only dracula can summon it, so it's only in floor == 5)
                if guy[0]-20 > p[0]:
                    screen.blit(pawnWalkingPic[int(frame // SPEED % len(pawnWalkingPic))],(p[0],p[1])) #does not has offset as the room is only 1200 wide and our character can move freely inside(not with x = 250)
                if guy[0]-20 < p[0]:
                    screen.blit(pawnWalkingPic_Left[int(frame // SPEED % len(pawnWalkingPic_Left))],(p[0],p[1]))
                if distance(guy[0],guy[1],p[0],p[1]) <= (20+2*floor):
                    King_HP -= (10 + 2*floor)
                
           

    for k in knights[floor]: #draw knights
        if k[2] <= 0: #if its killed
            knights[floor].remove(k)
        else:
            if floor != 5: #if in normal floor
                if abs(k[0]-20 - guy[0]) > 600: #if the player and the knight are far away from each other, the knight walk
                    if guy[0]-20 > k[0]:
                        screen.blit(knightWalkingPic_Left[int(frame // SPEED % len(knightWalkingPic_Left))],(k[0]+offset,k[1])) #same reason as above for offset
                    if guy[0]-20 < k[0]:
                        screen.blit(knightWalkingPic[int(frame // SPEED % len(knightWalkingPic))],(k[0]+offset,k[1]))
                elif abs(k[0] - guy[0]+20) <= 600 and abs(k[0] - guy[0]+20) > 50: #if the player and the knight are close to each other, the knight run
                    if guy[0]-20 > k[0]:
                        screen.blit(knightRunningPic_Left[int(frame // SPEED % len(knightRunningPic_Left))],(k[0]+offset,k[1]))
                    if guy[0]-20 < k[0]:
                        screen.blit(knightRunningPic[int(frame // SPEED % len(knightRunningPic))],(k[0]+offset,k[1]))
                else: #if player comes to knights' range of attack, the knight attacks
                    if guy[0]-20 > k[0]:
                        screen.blit(knightAttackPic_Left[int(frame // SPEED % len(knightAttackPic_Left))],(k[0]+offset,k[1]-22))
                        if int(frame // SPEED % len(knightAttackPic_Left)) == 4 or int(frame // SPEED % len(knightAttackPic_Left)) == 5:
                            if distance(guy[0],guy[1],k[0],k[1]) <= (35+3*floor):
                                King_HP -= (10 + 5*floor) #damage
                    if guy[0]-20 < k[0]:
                        screen.blit(knightAttackPic[int(frame // SPEED % len(knightAttackPic))],(k[0]+offset,k[1]-22))
                        if int(frame // SPEED % len(knightAttackPic_Left)) == 4 or int(frame // SPEED % len(knightAttackPic_Left)) == 5:
                            if distance(guy[0],guy[1],k[0],k[1]) <= (35+3*floor):
                                King_HP -= (10 + 5*floor)
            else:  #if in boss room,basically the same code but there is no longer offset
                if abs(k[0]-20 - guy[0]) > 600:
                    if guy[0]-20 > k[0]:
                        screen.blit(knightWalkingPic_Left[int(frame // SPEED % len(knightWalkingPic_Left))],(k[0],k[1]))
                    if guy[0]-20 < k[0]:
                        screen.blit(knightWalkingPic[int(frame // SPEED % len(knightWalkingPic))],(k[0],k[1]))
                elif abs(k[0] - guy[0]+20) <= 600 and abs(k[0] - guy[0]+20) > 50:
                    if guy[0]-20 > k[0]:
                        screen.blit(knightRunningPic_Left[int(frame // SPEED % len(knightRunningPic_Left))],(k[0],k[1]))
                    if guy[0]-20 < k[0]:
                        screen.blit(knightRunningPic[int(frame // SPEED % len(knightRunningPic))],(k[0],k[1]))
                else:
                    if guy[0]-20 > k[0]:
                        screen.blit(knightAttackPic_Left[int(frame // SPEED % len(knightAttackPic_Left))],(k[0],k[1]-22))
                        if int(frame // SPEED % len(knightAttackPic_Left)) == 4 or int(frame // SPEED % len(knightAttackPic_Left)) == 5:
                            if distance(guy[0],guy[1],k[0],k[1]) <= (35+3*floor): 
                                King_HP -= (10 + 5*floor)
                    if guy[0]-20 < k[0]:
                        screen.blit(knightAttackPic[int(frame // SPEED % len(knightAttackPic))],(k[0],k[1]-22))
                        if int(frame // SPEED % len(knightAttackPic_Left)) == 4 or int(frame // SPEED % len(knightAttackPic_Left)) == 5:
                            if distance(guy[0],guy[1],k[0],k[1]) <= (35+3*floor):
                                King_HP -= (10 + 5*floor)
                                

    for b in bishops[floor]: #draw bishop
        if b[2] <= 0: #if bishop
            bishops[floor].remove(b)

        elif b[2] != 0:
            if b[3] != 1: #if the bishop is not about to explode
                num_of_frame_bishop = int(frame // 10 % len(bishopAttack1Pic))
                if floor != 4: #the range of the bishop is larger in these floors (not 4)
                    if hypot((b[X]-guy[X]),(b[Y]-guy[Y])) <= 2000 and hypot((b[X]-guy[X]),(b[Y]-guy[Y])) >= 300:
                        if guy[0]-b[0] <= 0: #if king on left of bishop
                            screen.blit(bishopAttack1Pic_Left[num_of_frame_bishop],(b[0]+offset,b[1]))#shoots bullet towards left
                            if num_of_frame_bishop == 5:
                                bishop_bullet_Left_rect_list[floor].append(Rect(b[0],b[1],10,40))
                        elif guy[0]-b[0] >0: #if king on right of bishop
                            screen.blit(bishopAttack1Pic[num_of_frame_bishop],(b[0]+offset,b[1]))#shoots bullet towards right
                            if num_of_frame_bishop == 5:
                                bishop_bullet_rect_list[floor].append(Rect(b[0],b[1],10,40))
                    elif hypot((b[X]-guy[X]),(b[Y]-guy[Y])) < 300 and hypot((b[X]-guy[X]),(b[Y]-guy[Y])) >= 50: #if the player is close enough to the bishop 
                        screen.blit(bishopAttack2Pic[0],(b[0]+offset,b[1]))
                    elif distance(b[0],b[1],guy[0],guy[1]) < 50: #if player and bishop are really close to each other
                        b[3] = 1 #bishop is about to explode
                        
                else: #there are many bishops in floor 4, and i have to decrease its range of attack to avoid lag
                    if hypot((b[X]-guy[X]),(b[Y]-guy[Y])) <= 1200 and hypot((b[X]-guy[X]),(b[Y]-guy[Y])) >= 300:
                        if guy[0]-b[0] <= 0:
                            screen.blit(bishopAttack1Pic_Left[num_of_frame_bishop],(b[0]+offset,b[1]))
                            if num_of_frame_bishop == 5:
                                bishop_bullet_Left_rect_list[floor].append(Rect(b[0],b[1],10,40))
                        elif guy[0]-b[0] >0:
                            screen.blit(bishopAttack1Pic[num_of_frame_bishop],(b[0]+offset,b[1]))
                            if num_of_frame_bishop == 5:
                                bishop_bullet_rect_list[floor].append(Rect(b[0],b[1],10,40))
                    elif hypot((b[X]-guy[X]),(b[Y]-guy[Y])) < 300 and hypot((b[X]-guy[X]),(b[Y]-guy[Y])) >= 50:
                        screen.blit(bishopAttack2Pic[0],(b[0]+offset,b[1]))
                    elif distance(b[0],b[1],guy[0],guy[1]) < 50:
                        b[3] = 1
                
            else: #if the bishop is about to explode
                screen.blit(bishopExplosionPic[int(frame // 15 % len(bishopAttack1Pic))],(b[0]+offset,b[1]))
                if int(frame // 15 % len(bishopAttack1Pic)) == 5: #if it explodes, it dies
                    b[2] = 0
                    if distance(b[0]+20,b[1]+20,guy[0]+20,guy[1]+20) < (60+5*floor): #deals damage
                        King_HP -= (1000+100*floor)
                    


    for bu in bishop_bullet_rect_list[floor]: #blit the bullets facing left
        screen.blit(BishopBullet,(bu[0]+offset,bu[1]))
        if bu.colliderect(king_rect):
            bishop_bullet_rect_list[floor].remove(bu) #if it hits the player, it disappears
            King_HP -= 10
            del bu
                

    for bul in bishop_bullet_Left_rect_list[floor]: #blit the bullets facing right
        screen.blit(BishopBullet_Left,(bul[0]+offset,bul[1]))
        if bul.colliderect(king_rect):
            bishop_bullet_Left_rect_list[floor].remove(bul) #if it hits the player, it disappears
            King_HP -= 10
            del bul

    if floor == 1: #if in the rook boss room
        draw.rect(screen,(0,0,255),(215,100,0.25*rook[2],20)) #rook boss's health bar
        if rook[2] >= 0:
            if rook_condition == 0: #rook entrance
                screen.blit(RookEntrancePic[int(frame // SPEED % len(RookEntrancePic))],(rook[0],rook[1]))
                if int(frame // SPEED % len(RookEntrancePic)) == 7:
                    rook_condition = 2 #rook move towards the player

            elif rook_condition == 1: #if the rook is standinf still
                if distance (rook[0]+30,rook[1]+50,guy[0]+5,guy[1]-20) <= 70: #if the player is too close to the rook boss, player loses health
                    King_HP -= 5
                screen.blit(RookIdlePic,(rook[0],rook[1]))

            elif rook_condition == 2:
                if distance (rook[0]+30,rook[1]+50,guy[0]+5,guy[1]-20) <= 70: #if the rook moves towards the player and they are too close to each other, the player loses health
                    King_HP -= 5
                if rook[0] + 30 >= guy[0] +4: #if rook on the right of player
                    if int(frame // SPEED % len(RookDisappearPic)) != 7 and int(frame // SPEED % len(RookDisappearPic)) != 6: #the pictures have different height so i have to blit them on different levels
                        screen.blit(RookDisappearPic[int(frame // SPEED % len(RookDisappearPic))],(rook[0],rook[1]+int(frame // SPEED % len(RookDisappearPic))*2))
                    elif int(frame // SPEED % len(RookDisappearPic)) == 7 or int(frame // SPEED % len(RookDisappearPic)) == 6:
                        screen.blit(RookDisappearPic[int(frame // SPEED % len(RookDisappearPic))],(rook[0],rook[1]+60))
                    if int(frame // SPEED % len(RookDisappearPic)) == 8: #rook dives into the ground
                        rook_condition= 3
                        
                elif rook[0] +30 < guy[0] - 4: #if rook on the left of player
                    if int(frame // SPEED % len(RookDisappearPic)) != 7 and int(frame // SPEED % len(RookDisappearPic)) != 6:
                        screen.blit(RookDisappearPic_Left[int(frame // SPEED % len(RookDisappearPic))],(rook[0],rook[1]+int(frame // SPEED % len(RookDisappearPic))*2))
                    elif int(frame // SPEED % len(RookDisappearPic)) == 7 or int(frame // SPEED % len(RookDisappearPic)) == 6:
                        screen.blit(RookDisappearPic_Left[int(frame // SPEED % len(RookDisappearPic))],(rook[0],rook[1]+60))
                    if int(frame // SPEED % len(RookDisappearPic)) == 8:
                        rook_condition = 3
                        
            elif rook_condition == 3: #rook is in the ground
                screen.blit(RookDisappearPic[8],(rook[0],rook[1]+16))

            elif rook_condition == 4:#rook attack (it comes out of the ground)
                screen.blit(RookEntrancePic[int(frame // SPEED % len(RookEntrancePic))],(rook[0],rook[1]))
                if int(frame // SPEED % len(RookEntrancePic)) == 6 or int(frame // SPEED % len(RookEntrancePic)) == 5 : #if the rook comes out of the ground
                    if distance(rook[0]+30,rook[1]+50,guy[0]+5,guy[1]-20) <= 130: #damage
                        if rook[2] > 1500: #if rook health id above 1500 
                            King_HP -= 100
                        else: #if its health below 1500
                            King_HP -= 150
                    rook_condition = 1 

            for rock in rock_rect_list: #rock appears evry 5 seconds in the boss room from right hand side
                screen.blit(RockPic,(rock.x,500))
                if rock.colliderect(Rect(guy[0]+5,guy[1]-79,22,79)): #if the player is hit, damage is dealt
                    King_HP -= 20

            for rock in rock_Left_rect_list: #rock appears evry 5 seconds in the boss room from left hand side
                screen.blit(RockPic,(rock.x,500))
                if rock.colliderect(Rect(guy[0]+5,guy[1]-79,22,79)): #if the player is hit, damage is dealt
                    King_HP -= 20
        

    if floor == 3: #if in the queen boss room
        draw.rect(screen,(0,0,255),(100,100,0.25*queen[2],20)) #queen health bar
        
        if queen[2] >= 0: #queen entrance: queen falls from the ceiling
            if queen[3] <= 52:
                queen[3] += 1
                queen[1] += queen[3]
                screen.blit(QueenEntrancePic[int(frame // SPEED % len(QueenEntrancePic))],(queen[0],queen[1]))
                
            elif queen[3] == 53: #if queen is on the ground
                if queen_condition == 1: #queen walking
                    if queen[0] > guy[0]:
                        screen.blit(QueenWalkingPic[int(frame // SPEED % len(QueenWalkingPic))],(queen[0],queen[1]+20))
                    else:
                        screen.blit(QueenWalkingPic_Left[int(frame // SPEED % len(QueenWalkingPic_Left))],(queen[0],queen[1]+20))
                        
                elif queen_condition == 2: # queen close-range attack
                    if queen[0] > guy[0]:
                        screen.blit(QueenAttack1Pic[int(frame // 6 % len(QueenAttack1Pic))],(queen[0]-50,queen[1]))
                        if int(frame // 6 % len(QueenAttack1Pic)) == 5 and distance(queen[0]+20,queen[1]+30,guy[0]+40,guy[1]+20) <= 130: #damage
                            King_HP -= 31 
                            
                    else:
                        screen.blit(QueenAttack1Pic_Left[int(frame // 6 % len(QueenAttack1Pic_Left))],(queen[0]+20,queen[1]))
                        if int(frame // 6 % len(QueenAttack1Pic)) == 5 and distance(queen[0]+20,queen[1]+30,guy[0]+40,guy[1]+20) <= 130:
                            King_HP -= 31
                            
                elif queen_condition == 3: #queen long-range attack (throwing spears)
                    if queen[0] > guy[0]:
                        screen.blit(QueenAttack2Pic[int(frame // 6 % len(QueenAttack2Pic))],(queen[0],queen[1]))
                        if int(frame // 6 % len(QueenAttack2Pic)) == 13:
                            queen_condition = 0
                            queen_spear_rect_list.append(Rect(queen[0],queen[1]+60,40,10))
                    if queen[0] < guy[0]:
                        screen.blit(QueenAttack2Pic_Left[int(frame // 6 % len(QueenAttack2Pic_Left))],(queen[0],queen[1]))
                        if int(frame // 6 % len(QueenAttack2Pic)) == 13:
                            queen_condition = 0
                            queen_spear_Left_rect_list.append(Rect(queen[0],queen[1]+60,40,10))
                            
                elif queen_condition == 4:
                    if queen[0] > guy[0]: #strengthened long-range attack (spears fall from the ceiling)
                        screen.blit(QueenAttack2Pic[int(frame // 6 % len(QueenAttack2Pic))],(queen[0],queen[1]))
                        if int(frame // 6 % len(QueenAttack2Pic)) == 13:
                            queen_condition = 0
                            queen_spear_rect_list.append(Rect(queen[0],queen[1]+60,40,10))
                            queen_longspear_rect_list = queen_longspear_rect_list + [Rect(i,0,10,80) for i in range(200,1000,100)]
                            
                    if queen[0] < guy[0]:
                        screen.blit(QueenAttack2Pic_Left[int(frame // 6 % len(QueenAttack2Pic_Left))],(queen[0],queen[1]))
                        if int(frame // 6 % len(QueenAttack2Pic)) == 13:
                            queen_condition = 0
                            queen_spear_Left_rect_list.append(Rect(queen[0],queen[1]+60,40,10))
                            queen_longspear_Left_rect_list = queen_longspear_Left_rect_list + [Rect(i,10,8,80)for i in range(225,1000,100)]
                


        for s in queen_spear_rect_list: #draw speas facing left
            screen.blit(QueenShortSpearPic,(s.x,s.y))
            if s.colliderect(king_rect):
                queen_spear_rect_list.remove(s)
                King_HP -= 500

        for sp in queen_spear_Left_rect_list: #draw speas facing right
            screen.blit(QueenShortSpearPic_Left,(sp.x,sp.y))
            if sp.colliderect(king_rect):
                queen_spear_Left_rect_list.remove(sp)
                King_HP -= 500

        if len(queen_longspear_rect_list) > 0: #draw speas facing down
            for l in queen_longspear_rect_list:
                screen.blit(QueenLongSpearPic,(l.x,l.y))
                if l.colliderect(king_rect):
                    queen_longspear_rect_list.remove(l)
                    King_HP -= 500

        if len(queen_longspear_Left_rect_list) > 0: #draw speas facing down
            for ln in queen_longspear_Left_rect_list:
                screen.blit(QueenLongSpearPic,(ln.x,ln.y))
                if ln.colliderect(king_rect):
                    queen_longspear_Left_rect_list.remove(ln)
                    King_HP -= 500


    Dy = 0 #dracula's x and y value
    Dx = 0
    if floor == 5:
        draw.rect(screen,(0,0,255),(100,100,0.25*dracula[2],20)) #dracula health bar

        if dracula[2] >= 0: #dracula's entrance
            if dracula_condition == 0: #the pics have different y values so i adjusted them myself
                if int(frame // SPEED % len(BatPic)) == 0:
                    Dy = 720
                elif int(frame // SPEED % len(BatPic)) == 1:
                    Dy = 724
                elif int(frame // SPEED % len(BatPic)) == 2:
                    Dy = 722
                elif int(frame // SPEED % len(BatPic)) == 3:
                    Dy = 719
                elif int(frame // SPEED % len(BatPic)) == 4:
                    Dy = 702
                elif int(frame // SPEED % len(BatPic)) == 5:
                    Dy = 698
                elif int(frame // SPEED % len(BatPic)) == 6:
                    Dy = 700
                elif int(frame // SPEED % len(BatPic)) == 7:
                    Dy = 675
                elif int(frame // SPEED % len(BatPic)) == 8:
                    Dy = 660
                elif int(frame // SPEED % len(BatPic)) == 9:
                    Dy = 650
                    
                screen.blit(BatPic[int(frame // SPEED % len(BatPic))],(800,Dy))
                
                if int(frame // SPEED % len(BatPic)) == 9:
                    dracula_condition = 1 

            elif dracula_condition == 1: #dracula stands still
                if guy[0] > dracula[0]:
                    screen.blit(DIdle_Left,(dracula[0],dracula[1]))
                else:
                    screen.blit(DIdle,(dracula[0],dracula[1]))

            elif dracula_condition == 2: #dracula moves towards the player
                static_time = 0
                if dracula[0] >= guy[0]:
                    screen.blit(DAttackPic[int(frame // 6 % len(DAttackPic))],(dracula[0],dracula[1]))
                    if int(frame // 6 % len(DAttackPic)) == 2:
                        dracula_condition = 3
                elif dracula[0] < guy[0]:
                    screen.blit(DAttackPic_Left[int(frame // 6 % len(DAttackPic))],(dracula[0],dracula[1]))
                    if int(frame // 6 % len(DAttackPic)) == 2:
                        dracula_condition = 3

            elif dracula_condition == 3: #dracula moves towards the player, about to attack
                if dracula[0] >= guy[0]:
                    screen.blit(DAttackPic[2],(dracula[0],dracula[1]))
                    if distance(guy[0]+5,guy[1]+20,dracula[0]+10,dracula[1]+55) <= 130:
                        frame = 18
                        dracula_condition = 4

                elif dracula[0] < guy[0]:
                    screen.blit(DAttackPic_Left[2],(dracula[0],dracula[1]))
                    if distance(guy[0]+5,guy[1]+20,dracula[0]+10,dracula[1]+55) <= 130:
                        frame = 18
                        dracula_condition = 4
                        

            elif dracula_condition == 4: #dracula attack
                Dx = dracula[0]
                if int(frame // 6 % len(DAttackPic)) == 5: #the pics have different x and y values so i adjusted them myself
                    Dx = dracula[0] -40
                elif int(frame // 6 % len(DAttackPic)) == 4:
                    Dx = dracula[0] -40
                Dy = dracula[1]
                if int(frame // 6 % len(DAttackPic)) == 5:
                    Dy = 570
                elif int(frame // 6 % len(DAttackPic)) == 4:
                    Dy = 570
                if dracula[0] >= guy[0]: #if its on right of the player
                    screen.blit(DAttackPic[int(frame // 6 % len(DAttackPic))],(Dx,Dy))
                    if int(frame // 6 % len(DAttackPic)) == 5:
                        if distance(guy[0]+5,guy[1]+20,dracula[0]+10,dracula[1]+55) <= 140:
                            King_HP -= 250 #damage
                            
                        if dracula[0] <= 600:
                            D_left = True #checks whether its on the left or right side of the screen, for its later retreat
                        else:
                            D_left = False
                            
                        if D_left == True:
                            D_distance = (1000 - dracula[0])//60 #we want the dracula to retreat in exactly 60 loops so all the animation can be blitted, so we calculated its distance to its destination of retreat
                        else:
                            D_distance = (-200 + dracula[0])//60
                        frame = 0 #so the next animations can be smooth
                        dracula_condition = 5
                elif dracula[0] < guy[0]:# on left
                    screen.blit(DAttackPic_Left[int(frame // 6 % len(DAttackPic))],(Dx,Dy))
                    if int(frame // 6 % len(DAttackPic)) == 5:
                        if distance(guy[0]+5,guy[1]+20,dracula[0]+10,dracula[1]+55) <= 140: #damage
                            King_HP -= 250
                            
                        if dracula[0] <= 600:
                            D_left = True
                        else:
                            D_left = False
                        if D_left == True:
                            D_distance = (1000 - dracula[0])//60
                        else:
                            D_distance = (-200 + dracula[0])//60
                        frame = 0
                        dracula_condition = 5

            elif dracula_condition == 5: #dracula retreats
                screen.blit(DRetreatPic[int(frame // SPEED % len(DRetreatPic))],(dracula[0],dracula[1]))
                if int(frame // SPEED % len(DRetreatPic)) == 6:
                    dracula_condition = 1

            elif dracula_condition == 10: #dracula summons pawns and knights
                if int(frame // SPEED % len(BatPic)) == 0:#the pictures have different x values so i have to adjust them myself
                    Dx = dracula[0]
                elif int(frame // SPEED % len(BatPic)) == 1:
                    Dx = dracula[0]
                elif int(frame // SPEED % len(BatPic)) == 2:
                    Dx = dracula[0] 
                elif int(frame // SPEED % len(BatPic)) == 3:
                    Dx = dracula[0] - 7
                elif int(frame // SPEED % len(BatPic)) == 4:
                    Dx = dracula[0] - 18
                elif int(frame // SPEED % len(BatPic)) == 5:
                    Dx = dracula[0] - 29
                elif int(frame // SPEED % len(BatPic)) == 6:
                    Dx = dracula[0] - 29
                elif int(frame // SPEED % len(BatPic)) == 7:
                    Dx = dracula[0] - 28
                elif int(frame // SPEED % len(BatPic)) == 8:
                    Dx = dracula[0] - 23
                if dracula[0] >= 600:
                    screen.blit(DSummonPic_Left[int(frame // SPEED % len(DSummonPic))],(Dx,dracula[1]))
                    if int(frame // SPEED % len(DSummonPic)) == 8:
                        dracula_condition = 11
                elif dracula[0] < 600:
                    screen.blit(DSummonPic[int(frame // SPEED % len(DSummonPic))],(dracula[0],dracula[1]))
                    if int(frame // SPEED % len(DSummonPic)) == 8:
                        dracula_condition = 11

            elif dracula_condition == 6: #dracula shoots fireballs
                if int(frame // SPEED % len(BatPic)) == 0:
                    Dx = dracula[0]
                elif int(frame // SPEED % len(BatPic)) == 1:
                    Dx = dracula[0]
                elif int(frame // SPEED % len(BatPic)) == 2:
                    Dx = dracula[0] 
                elif int(frame // SPEED % len(BatPic)) == 3:
                    Dx = dracula[0] - 7
                elif int(frame // SPEED % len(BatPic)) == 4:
                    Dx = dracula[0] - 18
                elif int(frame // SPEED % len(BatPic)) == 5:
                    Dx = dracula[0] - 29
                elif int(frame // SPEED % len(BatPic)) == 6:
                    Dx = dracula[0] - 29
                elif int(frame // SPEED % len(BatPic)) == 7:
                    Dx = dracula[0] - 28
                elif int(frame // SPEED % len(BatPic)) == 8:
                    Dx = dracula[0] - 23
                if dracula[0] >= 600:
                    screen.blit(DSummonPic_Left[int(frame // SPEED % len(DSummonPic))],(Dx,dracula[1]))
                    if int(frame // SPEED % len(DSummonPic)) == 8:
                        dracula_condition = 7
                elif dracula[0] < 600:
                    screen.blit(DSummonPic[int(frame // SPEED % len(DSummonPic))],(dracula[0],dracula[1]))
                    if int(frame // SPEED % len(DSummonPic)) == 8:
                        dracula_condition = 7

            elif dracula_condition == 8: #dracula summons wolves
                if int(frame // SPEED % len(BatPic)) == 0:
                    Dx = dracula[0]
                elif int(frame // SPEED % len(BatPic)) == 1:
                    Dx = dracula[0]
                elif int(frame // SPEED % len(BatPic)) == 2:
                    Dx = dracula[0] 
                elif int(frame // SPEED % len(BatPic)) == 3:
                    Dx = dracula[0] - 7
                elif int(frame // SPEED % len(BatPic)) == 4:
                    Dx = dracula[0] - 18
                elif int(frame // SPEED % len(BatPic)) == 5:
                    Dx = dracula[0] - 29
                elif int(frame // SPEED % len(BatPic)) == 6:
                    Dx = dracula[0] - 29
                elif int(frame // SPEED % len(BatPic)) == 7:
                    Dx = dracula[0] - 28
                elif int(frame // SPEED % len(BatPic)) == 8:
                    Dx = dracula[0] - 23
                if dracula[0] >= 600:
                    screen.blit(DSummonPic_Left[int(frame // SPEED % len(DSummonPic))],(Dx,dracula[1]))
                    if int(frame // SPEED % len(DSummonPic)) == 8:
                        dracula_condition = 9
                elif dracula[0] < 600:
                    screen.blit(DSummonPic[int(frame // SPEED % len(DSummonPic))],(dracula[0],dracula[1]))
                    if int(frame // SPEED % len(DSummonPic)) == 8:
                        dracula_condition = 9

            elif dracula_condition == 7 or dracula_condition == 9 or dracula_condition == 11: #dracula summoning
                static_time += 1 #this is for the rate of adding the wolves/fireballs/knights/ pawns to their list
                if dracula[0] >= 600: #if dracula is on the right hand side of the screen: blit him facing left
                    screen.blit(DSummonPic_Left[8],(dracula[0]-23,dracula[1]))
                elif dracula[0] < 600: #if dracula is on the left hand side of the screen: blit him facing right
                    screen.blit(DSummonPic[8],(dracula[0],dracula[1]))

            elif dracula_condition == 12: #dracula rises up and summons enemies in the air
                if dracula[1] >= 250:
                    dracula[1] -= 3 # he rises up
                screen.blit(DSummon2Pic[int(frame // SPEED % len(DSummon2Pic))],(dracula[0],dracula[1]))
                if int(frame // SPEED % len(DSummon2Pic)) == 7:
                    dracula_condition = 13

            elif dracula_condition == 13: #summoning in the air
                screen.blit(DSummon2Pic[7],(dracula[0],dracula[1]))
                static_time += 1
                

            for fi in dfireball_rect_list: #draw fireballs
                screen.blit(FireballPic[int(frame // SPEED % len(FireballPic))],(fi.x,fi.y))

            for fir in dfireball_Left_rect_list: #draw fireballs
                screen.blit(FireballPic_Left[int(frame // SPEED % len(FireballPic))],(fir.x,fir.y))

            for wo in dwolf_rect_list: #draw wolves
                screen.blit(WolfPic[int(frame // SPEED % len(WolfPic))],(wo.x,wo.y))

            for wol in dwolf_Left_rect_list: #draw wolves
                screen.blit(WolfPic_Left[int(frame // SPEED % len(WolfPic))],(wol.x,wol.y))
                



#--------------------------------------king----------------------------------
    HP_Bar = (50,50,King_HP*0.2,20) 
    draw.rect(screen,(255,0,0),HP_Bar) #the health bar of the main character
    
    if floor == 1 or floor == 3 or floor == 5: #when the player is in the boss room, the character can move around freely in the room and so it's not drawn at a x value of 250
        if condition == 0: #character standing
            if facing_Right == False:
                screen.blit(king_StandingPic_Left[frame1 // SPEED % len(king_StandingPic_Left)], (guy[X],guy[Y]-king_stand_y_correction[floor])) #king_stand_y_correction[floor] avoids the effects of differences of the position of different backgrounds
            else:                                                                                                                                #on the character
                screen.blit(king_StandingPic[frame1 // SPEED % len(king_StandingPic)], (guy[X],guy[Y]-king_stand_y_correction[floor]))
                
        elif condition == 1: #character running
            if facing_Right == False:
                screen.blit(king_RunningPic_Left[frame1 // SPEED % len(king_RunningPic_Left)], (guy[X],guy[Y]-king_run_y_correction[floor]))
            else:
                screen.blit(king_RunningPic[frame1 // SPEED % len(king_RunningPic)], (guy[X],guy[Y]-king_run_y_correction[floor]))
                
        elif condition == 2: #character jumping
            if facing_Right == False:
                screen.blit(king_JumpingPic_Left[int(frame1 // SPEED % len(king_JumpingPic_Left))], (guy[X],guy[Y]-king_jump_y_correction[floor]))
            else:
                screen.blit(king_JumpingPic[int(frame1 // SPEED % len(king_JumpingPic))], (guy[X],guy[Y]-king_jump_y_correction[floor]))

        elif condition == 3: #character attacking
            num_of_frame = int(frame1 // SPEED % len(king_AttackingPic))
            if facing_Right == False:
                screen.blit(king_AttackingPic_Left[num_of_frame], (guy[X],guy[Y]-king_attack_y_correction[floor]))
                if int(num_of_frame) == 3: #dealing damage
                    king_attacking = True #used to distinguish jump and jump attack, however, we didn't do jump attack at the end, but maybe we'll add it in the game 
                    screen.blit(SwordArcPic_Left,(guy[X]-30,guy[Y]-king_sword_y_correction[floor]))
                    enemy_attacked() #checks the damage done by the character
            else:
                screen.blit(king_AttackingPic[num_of_frame], (guy[X],guy[Y]-king_attack_y_correction[floor]))
                if int(num_of_frame) == 3:
                    screen.blit(SwordArcPic,(guy[X]+50,guy[Y]-king_sword_y_correction[floor]))
                    king_attacking = True
                    enemy_attacked()#checks the damage done by the character
            
                          
        elif condition == 4:#jump attack
            #we initially wanted the player to use the jump attack to fight against bishops and bosses; however, we decided not to do it due to its complexity.
            #the jump attack now serve the same function as "jump", and we didn't put it in the instructions in the menu

            if facing_Right == False:
                screen.blit(king_JumpAttackPic_Left[frame1 // 5 % len(king_JumpAttackPic_Left)], (guy[X],guy[Y]-king_jump_attack_y_correction[floor]))
            else:
                screen.blit(king_JumpAttackPic[frame1 // 5 % len(king_JumpAttackPic)], (guy[X],guy[Y]-king_jump_attack_y_correction[floor]))



    else:  #when the player is NOT in the boss room, the character can't move around freely in the room and so it's drawn at a x value of 250 (its drawn at a firm location on the screen)
           #other than that, it is all the same functions
        if condition == 0:
            if facing_Right == False:
                screen.blit(king_StandingPic_Left[frame1 // SPEED % len(king_StandingPic_Left)], (250,guy[Y]-king_stand_y_correction[floor]))
            else:
                screen.blit(king_StandingPic[frame1 // SPEED % len(king_StandingPic)], (250,guy[Y]-king_stand_y_correction[floor]))
                
        elif condition == 1:
            if facing_Right == False:
                screen.blit(king_RunningPic_Left[frame1 // SPEED % len(king_RunningPic_Left)], (250,guy[Y]-king_run_y_correction[floor]))
            else:
                screen.blit(king_RunningPic[frame1 // SPEED % len(king_RunningPic)], (250,guy[Y]-king_run_y_correction[floor]))
                
        elif condition == 2:
            if facing_Right == False:
                screen.blit(king_JumpingPic_Left[int(frame1 // SPEED % len(king_JumpingPic_Left))], (250,guy[Y]-king_jump_y_correction[floor]))
            else:
                screen.blit(king_JumpingPic[int(frame1 // SPEED % len(king_JumpingPic))], (250,guy[Y]-king_jump_y_correction[floor]))

        elif condition == 3:
            num_of_frame = int(frame1 // SPEED % len(king_AttackingPic))
            if facing_Right == False:
                screen.blit(king_AttackingPic_Left[num_of_frame], (250,guy[Y]-king_attack_y_correction[floor]))
                if int(num_of_frame) == 3:
                    king_attacking = True
                    screen.blit(SwordArcPic_Left,(220,guy[Y]-king_sword_y_correction[floor]))
                    enemy_attacked()
            else:
                screen.blit(king_AttackingPic[num_of_frame], (250,guy[Y]-king_attack_y_correction[floor]))
                if int(num_of_frame) == 3:
                    screen.blit(SwordArcPic,(300,guy[Y]-king_sword_y_correction[floor]))
                    king_attacking = True
                    enemy_attacked()
            
                
                
        elif condition == 4:

            if facing_Right == False:
                screen.blit(king_JumpAttackPic_Left[frame1 // 5 % len(king_JumpAttackPic_Left)], (250,guy[Y]-king_jump_attack_y_correction[floor]))
            else:
                screen.blit(king_JumpAttackPic[frame1 // 5 % len(king_JumpAttackPic)], (250,guy[Y]-king_jump_attack_y_correction[floor]))

                
  
    SPEED = 10 #this means that each picture is going to be blitted for 10 loops
    
    if dracula[2] <= 0: #when you kill the final boss, the congratulation page will be blitted 
        screen.blit(offEndScene,(0,0))
        screen.blit(CongratsWord,(100,50))

    display.flip()
    myClock.tick(60)

#-------------------------------------------------------enemy-movement-----------------------------------------------------------------------------
def movePawns(pawns, kingX, kingY): #pawn movement
    ''' The AI for the badGuys is real simple. If the goodGuy is left/right
        they move left/right. Same with up/down.
        badGuys - A list of bad guy positions ([x,y] lists)
        goodX, goodY - good guy position
    '''
    for pawn in pawns[floor]:
        if abs(pawn[0] - kingX) <= 2000: #the pawn moves towards the player
            if kingX > pawn[0] + 10:
                pawn[0]+= 2                    
            elif kingX < pawn[0] - 10:   
                pawn[0]-= 2


def moveKnights(knights, kingX, kingY): #knight movement 
    ''' The AI for the badGuys is real simple. If the goodGuy is left/right
        they move left/right. Same with up/down.
        badGuys - A list of bad guy positions ([x,y] lists)
        goodX, goodY - good guy position
    '''
    for knight in knights[floor]:
        if abs(knight[0] - kingX) <= 2000: #if the player and the knight are far away from each other, the knight walks towards the player
            if kingX > knight[0] + 10:
                knight[0]+= 1                   
            elif kingX < knight[0] - 10:   
                knight[0]-= 1
        if abs(knight[0] - kingX) <= 600: #if the player and the knight are close to each other, the knight runs towards the player
            if kingX > knight[0] + 10:
                knight[0]+= 4                  
            elif kingX < knight[0] - 10:   
                knight[0]-= 4

def moveBishops(bishops, guy): #bishop movement
    for bishop in bishops[floor]:
        if hypot((bishop[0]- guy[0]),(bishop[1]-guy[1])) < 300 and hypot((bishop[0]- guy[0]),(bishop[1]-guy[1])) >= 50:
            #the bishop follows the player unless the distance between them is less then 50. Once the distance is below 50, it stops and explodes
            if bishop[X] > guy[X]:
                bishop[X] -= 6
            elif bishop[X] < guy[X]:
                bishop[X] += 6
                
            if bishop[Y] > guy[Y]:
                bishop[Y] -= 6
            elif bishop[Y] < guy[Y]:
                bishop[Y] += 6
        
        
def moveBishopBullet(): #bishop bullet movement
    for bullet in bishop_bullet_list[floor]:
        bullet[X] += 4
        if bullet[X] >= 5100 or bullet[X] <= 0: #the bullets are automatically deleted when it goes out of the floor
            bishop_bullet_list[floor].remove(bullet)
            
    for bullet in bishop_bullet_Left_list[floor]:
        bullet[X] -= 4
        if bullet[X] >= 5100 or bullet[X] <= 0:
            bishop_bullet_Left_list[floor].remove(bullet)
            
    for bullet in bishop_bullet_rect_list[floor]:
        bullet.x += 4
        if bullet[X] >= 5100 or bullet[X] <= 0:
            bishop_bullet_rect_list[floor].remove(bullet)
        
    for bullet in bishop_bullet_Left_rect_list[floor]:
        bullet.x -= 4
        if bullet[X] >= 5100 or bullet[X] <= 0:
            bishop_bullet_Left_rect_list[floor].remove(bullet)


def moveSpikes(): #spikes dealing damage
    global King_HP
    for spike in spikes_rect[floor]:
        if king_rect.colliderect(spike):
            King_HP -= 10
            
def moverook(): # rook boss moves
    global rook_condition
    global frame
    if floor == 1:
        current_time = time.get_ticks() #the rate of which rook boss attacks depends on the time passed since the player enters the boss room

        
    if rook[2] > 1500: #if the health of rook boss is more than half
        if rook_condition != 3 and rook_condition != 4: #if the rook is not doing anything
            if current_time % 7000 <= 50: #every 7 seconds
                frame = 0 #ensures that the future movements are smooth
                rook_condition = 2

        if current_time % 10000 <= 50: #every 10 seconds a rock appears from the very right end of the room
            rock_rect_list.append(Rect(1500,550,90,90))
            
    elif rook[2] <= 1500: #if the health of rook boss is less than half
        if rook_condition != 3 and rook_condition != 4:
            if current_time % 5000 <= 50:
                frame = 0
                rook_condition = 2

        if current_time % 8000 <= 50: #every 8 seconds 2 rocks appear in the room: one on the left side and one on the right
            rock_rect_list.append(Rect(1500,550,100,100))
            rock_Left_rect_list.append(Rect(-250,550,100,100))
            


    if rook_condition == 2: #the rook boss moves towards the character and dives into the ground
        if rook[0] < guy[0]:
            rook[0] += 2
        elif rook[0] >= guy[0]:
            rook[0] -= 2

    if rook_condition == 3: #after the rook is already in the ground, it moves faster towards the player
        if rook[0]+30 < guy[0]-4: #the +30 and -4 are used to get the centres of the rook boss and the character
            rook[0] += 4
        elif rook[0]+30 > guy[0] + 4:
            rook[0] -= 4

        elif abs(rook[0]+30 - guy[0]) <= 4 and distance(rook[0]+30,rook[1]+60,guy[0]+5,guy[1]-30) <= 20:
            rook_condition = 4 #it comes out of the ground and attacks
            frame = 0


def moverock(): #the rocks in the rook boss room moves
    global rock_rect_list
    global rock_Left_rect_list
    for r in rock_rect_list:
        if rook[2] > 1500: #the speed of rock changes as the health of rook boss goes below 1500
            r.x -= 2
        else:
            r.x -= 4
    for r in rock_Left_rect_list:
        r.x += 4
        

def movequeen(): #queen boss moves
    global queen_condition
    if floor == 3:
        current_time = time.get_ticks() # explained in rook boss
        
    if queen[2] >= 1500: #if health more than 1500
        if (current_time % 7500) <= 50: #every 7.5 seconds she teleports to the player
            if queen[X] <= guy[X]:
                queen[X] = guy[X]+50
            else:
                queen[X] = guy[X]-50
        if (current_time % 10000) <= 50 and queen_condition != 2:  #every 10 seconds she does long range attack
            queen_condition = 3
            if abs(guy[0]- 200) > abs (guy[0] - 1000): #the queen goes to the side of the screen that is further away from the player
                queen[X] = 200
            else:
                queen[X] = 1000

    elif queen[2] < 1500: #if health less than 1500
        if queen[2] >= 0:
            queen[2] += 0.5 #the queen regenerates
        if (current_time % 5500) <= 34: #she does special moves more frequently
            if queen[X] <= guy[X]:
                queen[X] = guy[X]+50
            else:
                queen[X] = guy[X]-50
        if (current_time % 7500) <= 34 and abs(current_time-30000) > 34 and abs(current_time-60000) > 34:
            queen_condition = 4
            if abs(guy[0]- 200) > abs (guy[0] - 1000):
                queen[X] = 200
            else:
                queen[X] = 1000
        

    if queen_condition != 3 and queen_condition != 4: #if she is not attacking (close&long rangely)
        if distance(queen[0]+20,queen[1]+30,guy[0]+40,guy[1]+20) < 750 and distance(queen[0]+20,queen[1]+30,guy[0]+20,guy[1]+20) > 130:
            queen_condition = 1 #queen walking
            if queen[0] < guy[0]:
                queen[0] += 2
            elif queen[0] > guy[0]:
                queen[0] -= 2
        elif distance(queen[0]+20,queen[1]+30,guy[0]+20,guy[1]+20) <= 130:#if the queen is close to the player, she attacks close-rangely
            queen_condition = 2
        elif distance(queen[0]+20,queen[1]+30,guy[0]+20,guy[1]+20) >= 750:#if the queen is very far away from the player, she keeps attacking long-rangely
            queen_condition = 3
        
        

def movespear(): #queen's spears' movement
    for spear in queen_spear_rect_list:
        spear.x -= 7
    for spears in queen_spear_Left_rect_list:
        spears.x += 7
    for spear in queen_longspear_rect_list:
        spear.y += 7
    for spears in queen_longspear_Left_rect_list:
        spears.y += 7



def movedracula(): #dracula boss moves
    global dracula_condition
    global frame
    global dfireball_rect_list 
    global dwolf_rect_list 
    global dfireball_Left_rect_list 
    global dwolf_Left_rect_list
    global static_time

    if floor == 5:
        current_time = time.get_ticks()

    if dracula[2] <= 1500 and dracula[2] > 0: #if his health is below 1500 he regenerates and there will be wolves appearing from the sides of the room
        dracula[2] += 0.5
        if current_time % 11000 <= 50 and dracula_condition != 13: #every 11 s
            frame = 0
            dwolf_rect_list.append(Rect(1200,720,50,30))
            dwolf_Left_rect_list.append(Rect(0,720,50,30))
            
            

    if dracula[2] > 1500:
        if current_time % 7000 <= 50 and dracula_condition != 13: #every 7 seconds he does close-range attacks
            frame = 0
            dracula_condition = 2
        if current_time % 3500 <= 50 and dracula_condition != 2 and dracula_condition != 13: #every 3.5 seconds he summons either wolves or pawns and knights, or he shoots fireballs
            frame = 0
            dracula_condition = choice(d_attack)# the attack he does is random(but will be long-range)
    else: #if his health is below 1500
        if current_time % 15000 <= 50 and dracula[3] == 0: #after 15 s dracula rises up and summons knights and pawns in the air
            frame = 0
            static_time = 0
            dracula_condition = 12
            dracula[3] = 1 #so that dracula only does this once per game
            
        if current_time % 6000 <= 50 and dracula_condition != 12 and dracula_condition != 13: #his frequency of attacking increases
            frame = 0
            dracula_condition = 2
        if current_time % 3000 <= 50 and dracula_condition != 2 and dracula_condition != 12 and dracula_condition != 13:
            frame = 0
            dracula_condition = choice(d_attack)


    if dracula_condition == 2: #dracula hides himself into his cape and moves towards the player
        if dracula[2] > 1500:
            if dracula[0] < guy[0]:
                dracula[0] += 9
            elif dracula[0] >= guy[0]:
                dracula[0] -= 9
        else:
            if dracula[0] < guy[0]: #his speed increases if his health is below 1500
                dracula[0] += 10
            elif dracula[0] >= guy[0]:
                dracula[0] -= 10

    elif dracula_condition == 3: #dracula in cape moves towards the player
        if dracula[2] > 1500:
            if dracula[0] < guy[0]:
                dracula[0] += 10
            elif dracula[0] >= guy[0]:
                dracula[0] -= 10
        else:   #his speed increases if his health is below 1500
            if dracula[0] < guy[0]:
                dracula[0] += 11
            elif dracula[0] >= guy[0]:
                dracula[0] -= 11

    elif dracula_condition == 5: #dracula retreats
        if D_left == True:
            if dracula[0] < 1000:
                dracula[0] += D_distance #D_distance ensures that dracula goes to its destination with exactly 60 loops
        else:
            if dracula[0] > 200:
                dracula[0] -= D_distance

    elif dracula_condition == 7: #dracula shoots fireballs
        if dracula[2] > 1500:
            if static_time % 55 == 0 :#every 55 loops
                if dracula[0] > 600: #if dracula is on the right side of screen, he shoots fireballs that are toward left
                    dfireball_rect_list.append(Rect(dracula[0],dracula[1]+20,20,15))
                    dfireball_rect_list.append(Rect(dracula[0],dracula[1]+50,20,15))
                    dfireball_rect_list.append(Rect(dracula[0],dracula[1]+80,20,15)) #shoots 3 fireballs with different heights
                else: #if dracula is on the left side of screen, he shoots fireballs that are toward right
                    dfireball_Left_rect_list.append(Rect(dracula[0]+10,dracula[1]+20,20,15))
                    dfireball_Left_rect_list.append(Rect(dracula[0]+10,dracula[1]+50,20,15))
                    dfireball_Left_rect_list.append(Rect(dracula[0]+10,dracula[1]+80,20,15))
        else:
            if static_time % 45 == 0 : #dracula shoots fireballs more frequently when its health is below 1500
                if dracula[0] > 600:
                    dfireball_rect_list.append(Rect(dracula[0],dracula[1]+10,20,15))
                    dfireball_rect_list.append(Rect(dracula[0],dracula[1]+40,20,15))
                    dfireball_rect_list.append(Rect(dracula[0],dracula[1]+70,20,15))
                    dfireball_rect_list.append(Rect(dracula[0],dracula[1]+100,20,15))
                else:
                    dfireball_Left_rect_list.append(Rect(dracula[0]+10,dracula[1]+10,20,15))
                    dfireball_Left_rect_list.append(Rect(dracula[0]+10,dracula[1]+40,20,15))
                    dfireball_Left_rect_list.append(Rect(dracula[0]+10,dracula[1]+70,20,15))
                    dfireball_Left_rect_list.append(Rect(dracula[0]+10,dracula[1]+100,20,15))

    elif dracula_condition == 9: #dracula summons wolves
        if static_time % 70 == 0: #same logic as the shooting fireball above
            if dracula[2] > 1500:
                if dracula[0] > 600:
                    dwolf_rect_list.append(Rect(dracula[0],dracula[1]+80,50,30)) #summons 2 wolves with different x values
                    dwolf_rect_list.append(Rect(dracula[0]-40,dracula[1]+80,50,30))
                else:
                    dwolf_Left_rect_list.append(Rect(dracula[0],dracula[1]+80,50,30))
                    dwolf_Left_rect_list.append(Rect(dracula[0]+40,dracula[1]+80,50,30))
            else: 
                if dracula[0] > 600: #dracula summons more wolves more frequently when its health is below 1500
                    dwolf_rect_list.append(Rect(dracula[0],dracula[1]+80,50,30))
                    dwolf_rect_list.append(Rect(dracula[0]-40,dracula[1]+80,50,30))
                    dwolf_rect_list.append(Rect(dracula[0]-80,dracula[1]+80,50,30))
                else:
                    dwolf_Left_rect_list.append(Rect(dracula[0],dracula[1]+80,50,30))
                    dwolf_Left_rect_list.append(Rect(dracula[0]+40,dracula[1]+80,50,30))
                    dwolf_Left_rect_list.append(Rect(dracula[0]+80,dracula[1]+80,50,30))

        
    elif dracula_condition == 11: #dracula summons pawns and knights
        if static_time % 70 ==0:
            if dracula[0] > 600:
                pawns[floor].append([dracula[0],690,250])
            else:
                pawns[floor].append([dracula[0]+10,690,250])
        if static_time % 200 == 0:
            if dracula[0] > 600:
                knights[floor].append([dracula[0],655,350])
            else:
                knights[floor].append([dracula[0]+10,655,350])

    elif dracula_condition == 13: #when dracula rises up and summons knights and pawns from the two sides of the room
        if static_time % 250 ==0:
            pawns[floor].append([0,690,250])
            pawns[floor].append([1200,690,250])
            
        if static_time % 300 == 0 and static_time != 0:
            knights[floor].append([0,655,350])
            knights[floor].append([1200,655,350])

        if static_time % 400 == 0 and static_time != 0: #dracula goes down to the ground after 400 loops
            dracula[1] = 640
            dracula_condition = 1


        

def movefireball(): #fireballs' movements & dealing damage
    global dfireball_rect_list
    global dfireball_Left_rect_list
    global King_HP
    
    for f in dfireball_rect_list:
        f.x -= 4
        if f.colliderect(king_rect):
            dfireball_rect_list.remove(f)
            if dracula[2]>0:
                King_HP -= 40

    for f in dfireball_Left_rect_list:
        f.x += 4
        if f.colliderect(king_rect):
            dfireball_Left_rect_list.remove(f)
            if dracula[2]>0:
                King_HP -= 40

          
        
def movewolf(): #wolves' movements & dealing damage
    global King_HP
    global dwolf_rect_list
    global dwolf_Left_rect_list
    global dracula

    
    for w in dwolf_rect_list:
        w.x -= 5
        if w.colliderect(king_rect):
            if dracula[2]>0:
                King_HP -= 4
                dracula[2] += 6 #it adds health to dracula if the wolf hits the player
        if w.x < 0: #automatically delete the wolf if it goes out of the room to avoid lag
            dwolf_rect_list.remove(w)

    for w in dwolf_Left_rect_list:
        w.x += 5
        if w.colliderect(king_rect):
            if dracula[2]>0:
                King_HP -= 4
                dracula[2] += 6
        if w.x > 1200:
            dwolf_Left_rect_list.remove(w) #automatically delete the wolf if it goes out of the room to avoid lag
        

        
def enemy_attacked(): #checks the damage dealt to the enemies during the player's attacks
    for knight in knights[floor]:
        if distance(knight[0]+20,knight[1]+20,guy[0]+40,guy[1]+20) <= 110 and king_attacking == True:
            if guy[3] == 0: #guy[3] tells the program whether the player discovers the easter egg or not
                            #if the player discovers the easter egg, he deals more damage
                knight[2] -= 20
            else:
                knight[2] -= 35
    for pawn in pawns[floor]:
        if distance(pawn[0]+20,pawn[1]+20,guy[0]+40,guy[1]+20) <= 110 and king_attacking == True:
            if guy[3] == 0:
                pawn[2] -= 20
            else:
                pawn[2] -= 35
        
    for bishop in bishops[floor]:
        if distance(bishop[0]+20,bishop[1]+20,guy[0]+40,guy[1]+20) <= 110 and king_attacking == True:
            if guy[3] == 0:
                bishop[2] -= 20
            else:
                bishop[2] -= 35

    if distance(queen[0]+20,queen[1]+30,guy[0]+40,guy[1]+20) <= 160:
        if guy[3] == 0:
            queen[2] -= 20
        else:
            queen[2] -= 30

    if distance(rook[0]+30,rook[1]+50,guy[0]+40,guy[1]+20) <= 160 and rook_condition == 1:
        rook[2] -= 14

    if distance(dracula[0]+20,dracula[1]+55,guy[0]+40,guy[1]+20) <= 160:
        if dracula_condition == 1 or dracula_condition == 7 or dracula_condition == 9 or dracula_condition == 11 or dracula_condition == 13:
            if guy[3] == 0:
                dracula[2] -= 25
            else:
                dracula[2] -= 30

        

        
def check_floor(): #changes the floor variable and the health of the player when they enters a different floor
    global floor
    global King_HP
    global frame
    global secret_room
    if king_rect.colliderect(doors[floor]) == True and len(knights[floor]) == 0 and len(bishops[floor]) == 0 and len(pawns[floor]) == 0: #the player has to kill all the enemies before they can enter the next floor
        if floor == 0: #from floor 1 to rook boss room
            guy[X] = 250 #resets player's location
            King_HP = 1500 #resetd player's health
            floor = 1 #the floor changes so the background & enemies change
            frame = 0 #resets the enemies' frame (in this case it's merely for rook boss, so its has a full entrance)
            mixer.music.load("RookMusic.mp3")           # When the king goes to rook boss room, it loads the music and plays it right after
            mixer.music.play(-1)
        elif floor == 1 and rook[2] <= 0: #from rook boss room to floor 2
            guy[X] = 250
            King_HP = 1550
            floor = 2
            mixer.music.load("FloorMusic.mp3")
            mixer.music.play(-1)
        elif floor == 2: #from floor 2 to queen boss room
            guy[X] = 250
            King_HP = 1600
            floor = 3
            mixer.music.load("QueenMusic.mp3")          
            mixer.music.play(-1)
        elif floor ==3 and queen[2] <= 0: #from queen boss room to floor 3
            guy[X] = 250
            King_HP = 1650
            floor = 4
            mixer.music.load("FloorMusic.mp3")
            mixer.music.play(-1)
            
        elif floor == 4: #from floor 3 to dracula boss room
            guy[X] = 250
            King_HP = 1800
            floor = 5
            frame = 0
            mixer.music.load("KingMusic.mp3")
            mixer.music.play(-1)

    if floor == 1: #in rook boss room
        if rook[2] <= 0 and secret_room == False and Rect(700,390,200,20) not in platforms_rect[1]: #after the rook boss is killed, secret platforms appear
            platforms_rect[1].append(Rect(200,550,110,20))
            platforms_rect[1].append(Rect(360,460,110,20))
            platforms_rect[1].append(Rect(520,370,110,20))
            platforms_rect[1].append(Rect(700,390,200,20))
        if king_rect.colliderect(secret_door): #if the player finds the easter egg
            secret_room = True
            

    

#---------------------------if-in-air----------------------------------------------
def ifinAir(): #checks whether the player is on a platform or not
    n = 0
    for plt in platforms_rect[floor]:
            if guy[Y] == plt.y - king_rect.h:
                n += 1
            else:
                n += 0
            #print(n)
    if n != 0:
        return False
    elif n == 0:
        return True
    
#---------------------------------------------------------king-movement-----------------------------------------------------            
'''
    The guy's x position is where he is in the "world" we then draw the map
    at a negative position to compensate.
'''
def moveGuy(guy): #character's movements
    global condition
    global facing_Right
    global frame
    global jump
    global attack
    global double_jump
    global inAir
    keys = key.get_pressed()

    inAir = ifinAir()

    if floor ==1 or floor == 3 or floor == 5: #in the  boss rooms
        
        condition = 0

        if keys[K_LEFT] and guy[X] > 100: #100 is the x value of the left end of the boss rooms
            guy[X] -= 7 #character's x value -= 7 (moves towards left)
            condition = 1 #the character is now running
            facing_Right = False #charactter is facing left
            
        if keys[K_RIGHT] and guy[X] <= 1100: #1100 is the x value of the right end of the boss rooms
            guy[X] += 7 
            condition = 1
            facing_Right = True #same logic as above
            
        if keys[K_UP] and onGround: #character jumps
                                    #onGround checks whether the character is on any platforms, he can only jump if he is on a platform
            jump = True
            guy[VY] = -16
        if inAir == True and jump == True:
            condition = 2 #character is jumping

        if keys[K_a]:
            condition = 3 #character is attacking

        if keys[K_d] and onGround: #jump attack
            attack = True
            guy[VY] = -15
        if inAir == True and attack == True:
            condition = 4

    else: #when the player is in a normal floor, the only difference here is the size of the floor (its now longer as its a floor)
        condition = 0

        if keys[K_LEFT] and guy[X] > 250: #the left end has x value 250
            guy[X] -= 7
            condition = 1
            facing_Right = False
            
        if keys[K_RIGHT] and guy[X] <= 5000: #the right end has x value 5000
            guy[X] += 7
            condition = 1
            facing_Right = True
            
        if keys[K_UP] and onGround:
            jump = True
            guy[VY] = -16
        if inAir == True and jump == True:
            condition = 2

        if keys[K_a]:
            condition = 3

        if keys[K_d] and onGround:
            attack = True
            guy[VY] = -15
        if inAir == True and attack == True:
            condition = 4
        
   

    guy[Y]+=guy[VY]     # add current speed to Y
    guy[VY]+=1        # add gravity to the VY
    
    #print(inAir)
   
#------------------------------------------------------check-platform---------------------------------------------------------
def checkPlats(): # checks whether the character is in touch with any platforms or not
    global onGround
    onGround = False
    for plat in platforms_rect[floor]:
        if king_rect.colliderect(plat) : #if the character is in touch with a platform
            onGround = True #its now on a platform
            guy[VY] = 0 #the jump motion stops
            guy[Y] = plat.y - king_rect.h   #the character is now on the platform



#-------------------------------------------------menu--------------------------------------------------------------------
def instructions():                 # Mr Mackenzie's code
    running = True
    inst = image.load("controls.png")                   # Blit the image
    inst = transform.smoothscale(inst, screen.get_size())
    screen.blit(inst,(0,0))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False               # If the escape key is pressed, running is False

        display.flip()
    return "Menu"


def story():
    global storycounter
    global counter 
    global pressed                    # Put King running
    global frame
    global SPEED
    running = True
    frame += 1
    counter = 0
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
            if evnt.type == MOUSEBUTTONDOWN:
                mb = mouse.get_pressed()
                if counter == 1 and mb[0]:
                    screen.blit(secondstory,(0,0))              # second story
                    counter = 2
                elif counter == 2 and mb[0]:
                    counter = 3
                    screen.blit(thirdstory,(0,0))            # third story
                elif counter == 3 and mb[0]:
                    screen.blit(fourthstory,(0,0))
        if counter == 0:
            screen.blit(firststory,(0,0))
            counter = 1

        if key.get_pressed()[27]: running = False
        display.flip()
    return "Menu"

def menu():                     # Mr Mackenzie helped us here to begin
    global King_HP
    if King_HP <= 0:                # When the king's HP is zero, we reset the HP
        King_HP = 1500

    running = True
    myClock = time.Clock()

    frame = 0
    
    buttons = [Rect(470,y*120+350,230,70) for y in range(3)] # The buttons


    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "Exit"

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        
        frame += 1
        screen.blit(backgroundmenu[frame // 60 % len(backgroundmenu)],(0,0))
        screen.blit(offcredits,(1000,740))
        screen.blit(offtitle,(350,50))
        screen.blit(offbutton1,(buttons[0]))
        screen.blit(offbutton2,(buttons[1]))
        screen.blit(offbutton3,(buttons[2]))

        if buttons[0].collidepoint(mpos):                   # When it collidespoint with the cursor, it blits a new image to make it look like a button
            screen.blit(offbutton1clicked,(buttons[0]))
            if mb[0] == 1:                          # If it is clicked, it returns the word "Game"
                return "Game"
        elif buttons[1].collidepoint(mpos):             # Same as the previous one
            screen.blit(offbutton2clicked,(buttons[1]))
            if mb[0] == 1:
                return "Instructions"
        elif buttons[2].collidepoint(mpos):
            screen.blit(offbutton3clicked,(buttons[2]))
            if mb[0] == 1:
                return "Story"
        
            
        display.flip()

#--------------------------------------------------------------

running = True          # allows for early exit if you find the aliens too scary
#myClock = time.Clock()  # although I don't need a constant frame rate here
X=0                      #used as list index
Y=1
VY=2

#-------------------------------------------------------Final function -----------------------------------------------
def finalfunction(): #the game function
    global frame
    global frame1
    global attack
    global jump
    global HP_Bar
    global king_attacking
    global king_rect
    global pawns
    global knights
    global bishops
    global bishop_bullet_Left_list 
    global bishop_bullet_Left_rect_list 
    global bishop_bullet_rect_list
    global bishop_bullet_list
    global rock_rect_list 
    global rock_Left_rect_list 
    global queen_spear_rect_list 
    global queen_longspear_rect_list 
    global queen_spear_Left_rect_list 
    global queen_longspear_Left_rect_list 
    global queen
    global rook 
    global chest_rect
    global guy
    global dracula
    global dfireball_rect_list 
    global dwolf_rect_list
    global dfireball_Left_rect_list
    global dwolf_Left_rect_list

    running = True
    while running:
        for evnt in event.get():                # checks all events that happen
            if evnt.type == QUIT:
                running = False
                return "Menu"
            if evnt.type == KEYDOWN:
                if evnt.key == K_a:
                    frame1 = 0 #the character's frame is reset to 0 as we want the attack to start from beginning every time the player clicks "a"
                    
                if evnt.key == K_UP:
                    frame1 = 0 #the character's frame is reset to 0 as we want the jump to start from beginning every time the player clicks "up"
                    attack = False #differs jump from jump attack (which we didn't finish, so there is no difference between them actually)
                    
                if evnt.key == K_d:
                    frame1 = 0
                    jump = False #differs jump from jump attack (which we didn't finish, so there is no difference between them actually)


        if King_HP <= 0:
            if floor == 1 or floor == 5:
                frame = 0 #so the entrance is full for dracula and rook (as their frame is reset)


            #-----------------------------the codes below reset the whole game after the character is killed by enemies----------------------------------------------------
            
            guy = [250,649,0,0]
            pawns = [[[1500,650,100],[2600,650,100],[3600,650,100],[5000,650,100]],
                [],
                [[1000,600,200],[1750,600,300],[2500,600,300],[3250,600,300],[4000,600,300],[4750,600,300],[5000,600,300]],
                [],
                [[1300,680,500],[2000,680,500],[2500,680,500],[2900,680,500],[3200,680,500],[3500,680,500],[3800,680,500],[4300,680,500],[4700,680,500],[5200,680,500],[5600,680,500],[6000,680,500],[6500,680,500]],
                []]
            knights = [[[2100,620,100],[3600,620,100],[5000,620,100]],
                [],
                [[1500,570,400],[2500,570,400],[3500,570,400],[4500,570,400],[5100,570,400]],
                [],
                [[1300,650,600],[2000,650,600],[2700,650,600],[3300,650,600],[4000,650,600],[4600,650,600],[5800,650,600],[6400,650,600]],
                []]
            bishops = [[[3600,427,200,0]],
                    [],
                    [[635,430,300,0],[1020,280,300,0],[3020,225,300,0],[4120,130,300,0],[4620,130,300,0]],
                    [],
                    [[1260,130,500,0],[1610,240,500,0],[2410,430,500,0],[3160,220,500,0],[5060,480,500,0]],
                    []]
            bishop_bullet_Left_list = [[],[],[],[],[],[]]
            bishop_bullet_Left_rect_list = [[],[],[],[],[],[]]
            bishop_bullet_rect_list = [[],[],[],[],[],[]]
            bishop_bullet_list = [[],[],[],[],[],[]]

            rock_rect_list = []
            rock_Left_rect_list = []

            queen_spear_rect_list = []

            queen_longspear_rect_list = []
            queen_spear_Left_rect_list = []
            queen_longspear_Left_rect_list = []

            dfireball_rect_list = []
            dwolf_rect_list = []
            dfireball_Left_rect_list = []
            dwolf_Left_rect_list = []

            queen = [900,-45,4000,-40]
            rook = [900,560,3000]
            dracula = [800,640,4000,0]
            
            chest_rect = [[[Rect(1210,218,80,80),0],[Rect(4210,80,80,80),0]],
                [],
                [[Rect(1400,130,80,80,),0],[Rect(3410,80,80,80),0],[Rect(4950,140,80,80),0]],
                [],
                [[Rect(3500,685,80,80),0],[Rect(4710,340,80,80),0],[Rect(800,442,80,80),0],[Rect(500,685,80,80),0]],
                []]
            
            running = False #when the character dies, the game stops running
            return "Menu" #goes back to menu
            
    #-------------------------------------------------------------
        movePawns(pawns, guy[0], guy[1])
        moveKnights(knights,guy[0],guy[1])
        moveBishops(bishops, guy)
        moveBishopBullet()
        moveSpikes()
        if floor == 1:
            moverook()
            moverock()
        if floor == 3:
            movequeen()
            movespear()
        if floor == 5:
            movedracula()
            movefireball()
            movewolf()
        moveGuy(guy)
        king_rect = Rect(guy[X]+10,guy[Y],22,79)
        checkPlats()
        check_floor()


        drawScene(screen, guy)
        #draw.rect(screen,(255,255,255),doors[floor])
        king_attacking = False
        #print(King_HP)

    


#---------------------------------------------------------------rects--------------------------------------------------------------
guy = [250,649,0,0]  #character's position and shows whether they find the easter egg ot not
king_rect = Rect(guy[X]-20,guy[Y],42,79) #character's rectangle

#------------------------------locations of enemies in the floor----------------------------------
pawns = [[[1500,650,100],[2600,650,100],[3600,650,100],[5000,650,100]],
         [],
         [[1000,600,200],[1750,600,300],[2500,600,300],[3250,600,300],[4000,600,300],[4750,600,300],[5000,600,300]],
         [],
         [[1300,680,500],[2000,680,500],[2500,680,500],[2900,680,500],[3200,680,500],[3500,680,500],[3800,680,500],[4300,680,500],[4700,680,500],[5200,680,500],[5600,680,500],[6000,680,500],[6500,680,500]],
         []]
knights = [[[2100,620,100],[3600,620,100],[5000,620,100]],
           [],
           [[1500,570,400],[2500,570,400],[3500,570,400],[4500,570,400],[5100,570,400]],
           [],
           [[1300,650,600],[2000,650,600],[2700,650,600],[3300,650,600],[4000,650,600],[4600,650,600],[5800,650,600],[6400,650,600]],
           []]
bishops = [[[3600,427,200,0]],
           [],
           [[635,430,300,0],[1020,280,300,0],[3020,225,300,0],[4120,130,300,0],[4620,130,300,0]],
           [],
           [[1260,130,500,0],[1610,240,500,0],[2410,430,500,0],[3160,220,500,0],[5060,480,500,0]],
           []]

bishop_bullet_Left_list = [[],[],[],[],[],[]] #bishop bullet
bishop_bullet_Left_rect_list = [[],[],[],[],[],[]]
bishop_bullet_rect_list = [[],[],[],[],[],[]]
bishop_bullet_list = [[],[],[],[],[],[]]

rock_rect_list = []#rock in rook boss room
rock_Left_rect_list = []

queen_spear_rect_list = [] #spear in queen boss room
queen_longspear_rect_list = []
queen_spear_Left_rect_list = []
queen_longspear_Left_rect_list = []

dfireball_rect_list = [] #fireballs in dracula's room
dwolf_rect_list = []
dfireball_Left_rect_list = []
dwolf_Left_rect_list = []

spikes = [[[750,690],[2000,690],[3000,690],[4450,690]], #spikes
          [],
          [],
          [],
          [[880,470],[3890,200],[3990,200],[4090,200],[4000,720],[4050,720],[1500,720],[3000,720]],
          []]
spikes_rect = [[Rect(750,690,100,46),Rect(2000,690,100,46),Rect(3000,690,100,46),Rect(4450,690,100,46)],
               [],
               [],
               [],
               [Rect(880,470,100,46),Rect(3890,200,100,46),Rect(3990,200,100,46),Rect(4090,200,100,46),Rect(4000,720,100,46),Rect(4050,720,100,46),Rect(1500,720,100,46),Rect(3000,720,100,46)],
               []]

platforms = [[[900,493],[1100,273],[1500,493],[2700,493],[3000,293],[3500,493],[3800,343],[4100,143],[4600,343]], #platforms
             [],
             [[500,500],[900,350],[1290,190],[620,200],[2000,460],[2400,290],[2900,290],[3300,140],[4000,200],[4500,200],[4140,500],[4900,200]],
             [],
             [[700,500],[1150,200],[1500,310],[1850,470],[2300,500],[2700,400],[3050,290],[3500,160],[3900,60],[4250,240],[4600,400],[4950,550],[4600,80]],
             []]
platforms_rect = [[Rect(0,728,6000,80),Rect(900,500,280,15),Rect(1100,280,280,15),Rect(1500,500,280,15),Rect(2700,500,280,15),Rect(3000,300,280,15),Rect(3500,500,280,15),Rect(3800,350,280,15),Rect(4100,150,280,15),Rect(4600,350,280,15)],
                  [Rect(0,728,6000,80)],
                  [Rect(0,678,6000,80),Rect(500,510,285,5),Rect(900,360,280,5),Rect(1290,200,280,5),Rect(620,200,200,5),Rect(340,0,200,5),Rect(500,-100,4450,5),Rect(2000,470,280,5),Rect(2400,300,280,5),Rect(2900,300,280,5),Rect(3300,150,280,5),Rect(4000,210,280,5),Rect(4500,210,280,5),Rect(4140,510,280,5),Rect(4900,210,280,5)],
                  [Rect(0,728,6000,80)],
                  [Rect(0,758,6000,80),Rect(700,510,285,5),Rect(1150,210,280,5),Rect(1500,320,280,5),Rect(1850,480,280,5),Rect(2300,510,280,5),Rect(2700,400,280,5),Rect(3050,300,280,5),Rect(3500,170,280,5),Rect(4250,250,280,5),Rect(3700,0,1000,5),Rect(4600,70,280,5),Rect(4600,410,280,5),Rect(4950,560,280,5)],
                  [Rect(0,758,6000,80)]]

chest_rect = [[[Rect(1210,218,80,80),0],[Rect(4210,80,80,80),0]],#chests
              [],
              [[Rect(1400,130,80,80,),0],[Rect(3410,80,80,80),0],[Rect(4950,140,80,80),0]],
              [],
              [[Rect(3500,685,80,80),0],[Rect(4710,340,80,80),0],[Rect(800,442,80,80),0],[Rect(500,685,80,80),0]],
              []]

doors = [Rect(5000,600,100,100), #rects that connect each floor
         Rect(1100,600,100,100),
         Rect(5000,600,100,100),
         Rect(1100,600,100,100),
         Rect(5000,600,100,100),
         Rect(1100,600,100,100)]
secret_door = Rect(890,180,20,200)

#-------------------------------bosses'x,y,health'  --------------------------------------------
queen = [900,-45,4000,-40] #-40 is the y value from which the queen fells
rook = [900,560,3000] 
dracula = [800,640,4000,0] #0 keeps track of the "rise up summon", dracula can only do it one time per game
d_attack = [6]*35 + [8]*45 + [10]*20

###############################problem
king_stand_y_correction = [5,80,5,5,5,5]
king_run_y_correction = [18,93,18,18,18,18]
king_jump_y_correction = [23,98,23,23,23,23]
king_attack_y_correction = [8,83,8,8,8,8]
king_jump_attack_y_correction = [24,99,24,24,24,24]
king_sword_y_correction = [30,105,30,30,30,30]

screen = display.set_mode((1200,800))
running = True
x,y = 0,0
OUTLINE = (150,50,30)###########
init()
storycounter = 0
arialFnt = font.SysFont("Biome", 21)
page = "Menu"

while page != "Exit":
    print(">>>",page)
    if page == "Menu":
        page = menu()
    if page == "Game":
        page = finalfunction()
    if page == "Instructions":
        page = instructions()    
    if page == "Story":
        page = story()   
        counter = 0
    
quit()
