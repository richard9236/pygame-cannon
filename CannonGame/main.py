

from numbers import Real
import time
import os
import math
import random
import pygame, sys

pygame.init()
pygame.mixer.init()

class UIButton: # we init thee button 
    RealPosX, RealPosY = 0, 0
    
    def __init__(self, Window, Text, TextSize, RectColor, TextColor, Hight, Length, PosX, PosY):
        # the init self button. this is where we assign all of our unique global variables 
        self.Window = Window
        
        if type(Text) ==type("a"): # make sure what we have is actually a type a text 
            smallfont = pygame.font.SysFont('Corbel', TextSize)
            self.Text = smallfont.render(Text, True, TextColor)

        self.Rect = RectColor
        self.Hight = Hight
        self.Length = Length
        
        self.PosX, self.PosY = PosX, PosY
        global RealPosX, RealPosY 
        
        RealPosX, RealPosY = Hight, Length
        
    def TestIfWasButton(self, mousePos): # test if what we clicked was a button 
        # is called every second and if it 
        if self.PosX <= mousePos[0] and self.PosX + self.Length >= mousePos[0] and self.PosY <= mousePos[1] and self.PosY + self.Hight >= mousePos[1]:
            PS(4)

            return True
        
    def Draw(self, bulletInt): # draw the button, may not work 
        if bulletInt != 5 :
            pygame.draw.rect(self.Window, self.Rect, [self.PosX, self.PosY, self.Length, self.Hight])
            self.Window.blit(self.Text, (self.PosX, self.PosY))
        
    def ShowOrHide(self, action): # decide if we draw or hidee the button 
        if action == True: # show
            self.PosX = RealPosX
            self.PosY = RealPosY
            
        else: # hide
            hiddenInt = -5555
            self.PosX = hiddenInt
            self.PosY = hiddenInt
        
    
FpsLimit = 44
WinHight , WinLength = 1000, 650
Window = pygame.display.set_mode((WinHight, WinLength))
pygame.display.set_caption("Konosuba .v1")
_Blackout = False
NumOfBulletShot = 0
NumOfBulletHit = 0
NumOfReload = 0
    
BackdropsTB = [pygame.image.load(os.path.join("Assets", "Forest0.jpg")),
             
             ] # wher e we store our backdrops 
# where we store the images we cannot use 
MiscTB = [pygame.image.load(os.path.join("Assets", "Cannon.png")),
    pygame.image.load(os.path.join("Assets", "CannonBall.png")),
    pygame.image.load(os.path.join("Assets", "Explosion.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_0.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_1.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_2.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_3.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_4.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_5.png")),
    pygame.image.load(os.path.join("Assets", "Health_0.png")),
    pygame.image.load(os.path.join("Assets", "Health_1.png")),
    pygame.image.load(os.path.join("Assets", "Health_2.png")),
    pygame.image.load(os.path.join("Assets", "Health_3.png")),
    pygame.image.load(os.path.join("Assets", "Bat_0.png")),
    pygame.image.load(os.path.join("Assets", "Bat_1.png")),
    pygame.image.load(os.path.join("Assets", "Zombie_0.png")),
    pygame.image.load(os.path.join("Assets", "Zombie_1.png")),
    pygame.image.load(os.path.join("Assets", "Wolf_0.png")),
    pygame.image.load(os.path.join("Assets", "Wolf_1.png"))
]
MiscTB[0] = pygame.transform.scale(MiscTB[0], (200, 200)) # assign each scale independently 
MiscTB[1] = pygame.transform.scale(MiscTB[1], (40, 40))
MiscTB[2] = pygame.transform.scale(MiscTB[2], (110, 110))

#bullets
for i in range(6):
    i = i +3
    MiscTB[i] = pygame.transform.scale(MiscTB[i], (200, 40))
for i in range(3): # health
    i = i +9
    MiscTB[i] = pygame.transform.scale(MiscTB[i], (110, 40))

# these 2 are the bat
MiscTB[13] = pygame.transform.scale(MiscTB[13], pygame.math.Vector2(100, 100))
MiscTB[14] = pygame.transform.scale(MiscTB[14], pygame.math.Vector2(100, 100))

# these are zombie
MiscTB[15] = pygame.transform.scale(MiscTB[15], pygame.math.Vector2(200, 200))
MiscTB[16] = pygame.transform.scale(MiscTB[16], pygame.math.Vector2(200, 200))

# wolf boy
MiscTB[17] = pygame.transform.scale(MiscTB[17], pygame.math.Vector2(150, 100))
MiscTB[18] = pygame.transform.scale(MiscTB[18], pygame.math.Vector2(150, 100))
# play sound of object 
SoundTB = [pygame.mixer.Sound(os.path.join("Assets", 'Fire.wav')),
           pygame.mixer.Sound(os.path.join("Assets", 'Pop.wav')),
           pygame.mixer.Sound(os.path.join("Assets", 'Pop.wav')),
           pygame.mixer.Sound(os.path.join("Assets", 'Pop.wav')),
           pygame.mixer.Sound(os.path.join("Assets", 'Pop.wav')),
           ]
def PS(i): # the place where we excecute the play sound 
    global SoundTB
    pygame.mixer.Sound.play(SoundTB[i])# window hight 

# all of our compiled colors 
ColorTB = [(170,170,170), (100, 100, 100)] 
for i in range(len(BackdropsTB)): # check if the backdrop has an integer 
    BackdropsTB[i] = pygame.transform.scale(BackdropsTB[i], (WinHight, WinLength))
CurrentBackdrop = 0 # to check if value was actually passed 

pygame.display.set_icon(BackdropsTB[0])

def wait(f): # each wait setatement to make it more effecient 
    time.sleep(f)
    a = 1
def Blackout(color): # our blackout to check if it blacked out 
    s = pygame.Surface((2000,2000))
    s.set_alpha(0)
    a, remoteInt = 1,0
    if (color == False):
        color = (0,0,0)
    
    while True:
        
        s.set_alpha(remoteInt)
        s.fill(color)
        Window.blit(s, (0,0))
        remoteInt = remoteInt +a
        wait(.02)
        if remoteInt >= 65 or remoteInt <= -5:
            break
        pygame.display.update()
    s.set_alpha(0)
    global _Blackout
    #_Blackout = False

def BuildBackdrop(x):
    # settup the backdrop 
    Window.blit(BackdropsTB[x], (0, 0))

_BulletImage = 0
_HealthImage = 0
_SpriteOffset = 0
_Gold = 5
DoubleCastUpgrade = 2
_HealCost = 0
bulletTB = []
bulletCacheTB = []
bulletHitBoxTB = []

MonsterTB = [] # will hold monster type
MonsterCacheTB= [] # will hold monster pos
MonsterCacheTB1 = []# will hold misc image int
MonsterCacheTB2 = [] # will hold monster health
MonsterCacheTB3 = [] # will hold monster speed

exploTB = []
exploCacheTB = []
exploCacheTB1 = []
for i in range(3):
    bulletCacheTB.append(1) 

CannonLocation = pygame.math.Vector2(0, Window.get_height() - 200)
CannonLocationHead = pygame.math.Vector2(130, Window.get_height() - 140)
def PullFloat(x, min, max): # make sure a designed x does not exceed a certain number 
    if x < min:
        x = min
    elif x > max:
        x = max
    return x

def DrawBullet(): # this is also coroutine 
    global Window
    global bulletTB
    global bulletCacheTB
    global bulletHitBoxTB
    global CannonLocationHead
    global CannonLocation
    
    for i in range(len(bulletTB)): # show poly gons and our bullets 
        if bulletTB[i] != True:
            sheet = CannonLocationHead + bulletTB[i] * bulletCacheTB[i]
            
            Window.blit(MiscTB[1], sheet)
            
            pygame.display.update() # check if the bullets exceeded the map 
            bulletCacheTB[i]= bulletCacheTB[i] +22
            if bulletCacheTB[i] >= 1500:
                bulletTB[i] = True
                bulletCacheTB[i] = 1

def ShowBullets(f): # show our bullet s
    global _BulletImage
    _BulletImage = f +3
def ShowHealth(f): # show our health 
    global _HealthImage
    _HealthImage = f +9

_Health = 3
ShowBullets(5)
ShowHealth(_Health)

def TakeDamage(): # take a pip of damage 
    global _Health
    _Health = _Health -1
    ShowHealth(PullFloat(_Health, 0, 3))
    
def AddExplosion(vec0): # the actual append 
    global exploTB
    global exploCacheTB
    global exploCacheTB1
    exploTB.append(pygame.math.Vector2(vec0[0] - 30,  vec0[1] - 80))
    exploCacheTB.append(1)
    exploCacheTB1.append(random.randint(1, 36) * 10)

def DrawExplosion():# coroutine
    global Window
    global MiscTB 
    global exploTB
    global exploCacheTB
    global exploCacheTB1
    
    for i in range(len(exploTB)): # where we add the explision 
        if exploTB[i] != 0:
            exploCacheTB[i] = exploCacheTB[i] +1# where we draw it over each frame 
            
            rotated_image = pygame.transform.rotate(MiscTB[2], exploCacheTB1[i])
            Window.blit(rotated_image, exploTB[i])
            
            if exploCacheTB[i] >= 66:
                exploTB[i] = 0

MonsterHealthTB = []
MonsterHealthTB1 = []
        
def SpawnMonster(monsterType, intt): #will be the fast times at ridgmont high
    global MonsterTB
    global MonsterCacheTB
    global MonsterCacheTB1
    global MonsterCacheTB2
    global MonsterCacheTB3
    
    global MonsterHealthTB
    global MonsterHealthTB1
     # wher ewe app end the object 
    monsterHealth, monsterSpeed, monsterImgInt = 0,0,0
    if monsterType == 1: # a bat
        monsterHealth, monsterSpeed, monsterImgInt = 5, 3, 13
    elif monsterType == 2: # a bear
        monsterHealth, monsterSpeed, monsterImgInt = 25, 1, 15
    elif monsterType == 3: # a wolf
        monsterHealth, monsterSpeed, monsterImgInt = 50, 4, 17
    monsterXAxis = random.randint(0, 5) + 10
    monsterXAxis = monsterXAxis * 100
    
    MonsterCacheTB.append(pygame.math.Vector2(monsterXAxis, intt)) # y spawn point
    MonsterCacheTB1.append(monsterImgInt) # misc img
    MonsterCacheTB2.append(monsterHealth) # health
    MonsterCacheTB3.append(monsterSpeed) # speed
    
    MonsterTB.append(monsterType) # monster type
def SpawnBat(i):
    for _i in range(i):
        SpawnMonster(1, random.randint(30, 250))
def SpawnZombie(i):
    for _i in range(i):
        print("l")
        # SpawnMonster(2, random.randint(400, 500))
def SpawnWolf(i):
    for _i in range(i):
        SpawnMonster(3, random.randint(400, 500))
        
def DrawTime(i):
    smallfont = pygame.font.SysFont('Corbel', 35)
    Text = smallfont.render("Time: "+ str(i / 2), True, (0,0,0))
    Window.blit(Text, (0, 0))
    
def DrawGold(i):
    smallfont = pygame.font.SysFont('Corbel', 35)
    Text = smallfont.render("Money: "+ str(i ), True, (0,0,0))
    Window.blit(Text, (200, 0))
def ClearCache(): # destroy none using 
    print("clearing cache")
    global MonsterTB
    global MonsterCacheTB
    global MonsterCacheTB1
    global MonsterCacheTB2
    global MonsterCacheTB3
    
    global bulletTB 
    global bulletCacheTB 
    global bulletHitBoxTB
    
    MonsterTB = []
    MonsterCacheTB = []
    MonsterCacheTB1= []
    MonsterCacheTB2= []
    MonsterCacheTB3= []
    
    bulletTB = []
    bulletCacheTB = []
    bulletHitBoxTB= []
    
def DrawMonsters(): # a corutine 
    global MiscTB
    global _SpriteOffset
    global CannonLocationHead
    
    global MonsterTB
    global MonsterCacheTB
    global MonsterCacheTB1
    global MonsterCacheTB2
    global MonsterCacheTB3
    
    # these are to check if you actually hit the monster
    global bulletTB # direction vector 2
    global bulletCacheTB # magnitude
    global bulletHitBoxTB
    
    global MonsterHealthTB
    global MonsterHealthTB1
    
    global NumOfBulletShot
    global NumOfBulletHit
    global NumOfReload
    global _Gold
    
    for i in range(len(MonsterTB)):
        if MonsterTB[i] != 0:
            takeSomeDamage = False
            MonsterCacheTB[i] = MonsterCacheTB[i] + pygame.math.Vector2(-1, 0) * MonsterCacheTB3[i]
            for ii in range(len(bulletTB)):
                if bulletTB[ii] != True:
                    vec0 = pygame.math.Vector2(MonsterCacheTB[i][0] + 50, MonsterCacheTB[i][1] + 50)
                    vec1 =(CannonLocationHead + bulletCacheTB[ii] * bulletTB[ii])
                    #pygame.draw.rect(Window, (0, 0, 0), [vec0[0], vec0[1], 22, 22])
                    
                    if int((vec0 - vec1).magnitude()) <= 66:
                        PS(MonsterTB[i])
                        
                        bulletTB[ii] = True
                        MonsterTB[i] = 0
                        NumOfBulletHit = NumOfBulletHit +1
                        _Gold = _Gold +1
                        AddExplosion(vec0)
                        
            
            determinedImage = MiscTB[MonsterCacheTB1[i]+ _SpriteOffset]
            
            Window.blit(determinedImage, MonsterCacheTB[i])
            
            if MonsterCacheTB2[i] <= 0:
                MonsterTB[i] = 0 # died
            elif MonsterCacheTB[i][0] <= 0: # the x axis
                MonsterTB[i] = 0
                TakeDamage()
                AddExplosion(MonsterCacheTB[i])
                
            
def SecondsPast(intt, x):
    if intt == 4:#2.0 seconds
        SpawnZombie(1 +x)
    elif intt == 7:
        SpawnBat(2+ x)
        SpawnZombie(2 +x)
    elif intt == 20: # 10 seconds
        SpawnBat(2 +x)
        SpawnZombie(1 +x )
    elif intt == 44:
        SpawnBat(2 +x)
        SpawnWolf(1 +x)
    elif intt== 55:
        SpawnBat(3 +x)
        SpawnZombie(2 +x)
    elif intt == 66: 
        SpawnBat(2 +x)
        SpawnZombie(x)
        SpawnWolf(2 +x)
    elif intt > 77 and x <= 2:
        return True
    elif intt > 100 and x >=3:
        ClearCache()
        return True
    return False

def Main():
    run = True
    global MiscTB
    global bulletTB
    global bulletCacheTB
    global _SpriteOffset 
    
    global exploTB
    global exploCacheTB
    
    global _Blackout
    global _BulletImage
    global _HealthImage
    global _Health
    clock = pygame.time.Clock() # a clock that does nothing 
    global CannonLocationHead
    global CannonLocation
    
    global NumOfBulletShot
    global NumOfBulletHit
    global NumOfReload
    global _Gold
    global _HealCost
    global DoubleCastUpgrade 
    
    CannonBulletLimit = 5
    CannonBullets = CannonBulletLimit 

    # we have done nothing about here 
    # Button(Window, "text", textSize,   (color), size y, size x, pos x, pos y)
    ReloadB = UIButton(Window, "Reload!", 22, (177, 177, 177),(0, 0, 0), 40 * 1.7, 77 ,    0,   200)
    
    TimeCache = len(MiscTB)
    RealHalfSeconds, FakeHalfSeconds, Difficulty = 0, 0, 0
    while run:
        TimeCache = TimeCache + 1;
        
        BuildBackdrop(CurrentBackdrop)
        clock.tick(44)
        if TimeCache >= 20: # the real clock
            if (_SpriteOffset == 0):
                _SpriteOffset = 1
            else:
                _SpriteOffset = 0
            
            n = SecondsPast(FakeHalfSeconds, Difficulty)
            if (n == True):
                FakeHalfSeconds = 1
                Difficulty = Difficulty +1
            TimeCache = 0
            
            FakeHalfSeconds = FakeHalfSeconds +1
            RealHalfSeconds = RealHalfSeconds +1
        
        
        for event in pygame.event.get(): # loop each event 
            mousePos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT: # check if we clicked the exit game 
                run = False
                pygame.quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                wutt0 = ReloadB.TestIfWasButton(mousePos)
                
                if (wutt0 != True and CannonBullets >= 1): # didn't click a button, and we have some ammo. Lets shoot
                    CannonBullets = CannonBullets -1
                    NumOfBulletShot = NumOfBulletShot +1
                    
                    ShowBullets(CannonBullets)
                    
                    AddExplosion(CannonLocationHead)
                    PS(0)
                    mouseVector = pygame.math.Vector2(int(mousePos[0]), int(mousePos[1]) )
                    
                    fireDirection = (mouseVector - CannonLocationHead).normalize()
                    bulletTB.append(fireDirection)
                    bulletCacheTB.append(1)
                    if (DoubleCastUpgrade == 5):
                        bulletTB.append(fireDirection)
                        bulletCacheTB.append(-20)
                        PS(0)
                        NumOfBulletShot = NumOfBulletShot +1
                        
                elif wutt0 == True and (CannonBullets < CannonBulletLimit):# clicked the button
                    CannonBullets = CannonBulletLimit #CannonBullets +1
                    ShowBullets(CannonBullets)
                    NumOfReload = NumOfReload +1
                    
                elif (CannonBullets <= 0):
                    print("Must reload!")
                
            elif event.type == pygame.KEYDOWN:
                _Blackout = True
                # Blackout(False)
            elif _Health <= 0:
                run = False
                Blackout(False)
                return RealHalfSeconds
                
        
        UIButton.Draw(ReloadB, CannonBullets)
        
        Window.blit(MiscTB[0], CannonLocation)
        
        Window.blit(MiscTB[_HealthImage], (0, 300))
        Window.blit(MiscTB[_BulletImage], (0, 360))
        
        if ( False):
            Window.blit(MiscTB[13 +1], (500, 350))
        
        DrawTime((RealHalfSeconds))
        DrawGold(_Gold)
        
        DrawMonsters()
        DrawBullet()
        DrawExplosion()
        
        pygame.display.update()

if __name__ == "__main__":
    BuildBackdrop(0)
    
    while True:
        
        n = (Main()) / 2
        if (True):
            smallfont = pygame.font.SysFont('Corbel', 100)
            Text0 = smallfont.render("YOU DIED", True, (255,255,255))
            
            smallfont = pygame.font.SysFont('Corbel', 35)
            Text1 = smallfont.render("Seconds lasted: " + str(n), True, (255,255,255))
            
            smallfont = pygame.font.SysFont('Corbel', 35)
            Text2 = smallfont.render("Bullets Fired: " + str(NumOfBulletShot), True, (255,255,255))
            
            smallfont = pygame.font.SysFont('Corbel', 35)
            Text3 = smallfont.render("Bullets Landed: " + str(NumOfBulletHit), True, (255,255,255))
            
            smallfont = pygame.font.SysFont('Corbel', 35)
            Text4 = smallfont.render("Accuracy: " + str(math.floor((NumOfBulletHit / NumOfBulletShot) * 100)) +"%", True, (255,255,255))
            
            smallfont = pygame.font.SysFont('Corbel', 35)
            Text5 = smallfont.render("Gold: " + str(_Gold) +"", True, (255,255,255))
            
            Window.blit(Text0, (0, 0))
            Window.blit(Text1, (0, 100))
            
            Window.blit(Text4, (0, 135))
            Window.blit(Text3, (0, 135 + 35))
            Window.blit(Text2, (0, 135 + 35 +35))
            Window.blit(Text5, (0, 135 + 35 +70))
            
            pygame.display.update()
            wait(5)
            pygame.quit()
            bulletTB = []
            bulletHitBoxTB = []
            bulletCacheTB = []

            MonsterTB = [] # will hold monster type
            MonsterCacheTB= [] # will hold monster pos
            MonsterCacheTB1 = []# will hold misc image int
            MonsterCacheTB2 = [] # will hold monster health
            MonsterCacheTB3 = [] # will hold monster speed

            exploTB = []
            exploCacheTB = []
            exploCacheTB1 = []
            
            _Health = 3
            ShowBullets(5)
            ShowHealth(_Health)
        
