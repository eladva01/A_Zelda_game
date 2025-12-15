


def gagabed():    
    import pygame, time, sys
    #import button1
    pygame.init()
    screenW =825
    screenH = 825
    WIN = pygame.display.set_mode((screenW,screenH)) #screen
    pygame.display.set_caption('bedroom') #window name
    #window 
    run = True
    bg = pygame.image.load ('pokebedroom1.png')
    wizzardR = pygame.image.load('wizzardR.png')
    wizzardL = pygame.image.load('wizzardL1.png')
    #FONT = pygame.font.SysFont('ariel', 30)
    #pressM =pygame.mixer.Sound('ping.wav')
    #menuMusic = pygame.mixer.music.load('menu.Music.mp3')
    #pygame.mixer.music.load('room.Music.mp3')
    #pygame.mixer.music.play(-1)
    WSR = [pygame.image.load('WSR1.3.png'),pygame.image.load('WSR1.3.png'),pygame.image.load('WSR1.3.png'),pygame.image.load('WSR1.3.png'),pygame.image.load('WSR2.3.png'),pygame.image.load('WSR2.3.png'),pygame.image.load('WSR2.3.png'),pygame.image.load('WSR2.3.png'),pygame.image.load('WSR2.3.png'),pygame.image.load('WSR2.3.png'),pygame.image.load('WSR2.3.png'),pygame.image.load('WSR3.3.png'),pygame.image.load('WSR3.3.png'),pygame.image.load('WSR3.3.png'),pygame.image.load('WSR4.3.png'),pygame.image.load('WSR4.3.png'),pygame.image.load('WSR4.3.png')]
    WS = [pygame.image.load('WS1.3.png'),pygame.image.load('WS1.3.png'),pygame.image.load('WS1.3.png'),pygame.image.load('WS1.3.png'),pygame.image.load('WS2.3.png'),pygame.image.load('WS2.3.png'),pygame.image.load('WS2.3.png'),pygame.image.load('WS2.3.png'),pygame.image.load('WS2.3.png'),pygame.image.load('WS2.3.png'),pygame.image.load('WS2.3.png'),pygame.image.load('WS3.3.png'),pygame.image.load('WS3.3.png'),pygame.image.load('WS3.3.png'),pygame.image.load('WS4.3.png'),pygame.image.load('WS4.3.png'),pygame.image.load('WS4.3.png')]
    WL = pygame.image.load('WS1.3.png')
    WR = pygame.image.load('WSR1.3.png')
    WU=pygame.image.load('WB1.png')
    WD= pygame.image.load('WFF1.png')
    WB = [pygame.image.load('WB1.png'),pygame.image.load('WB1.png'),pygame.image.load('WB1.png'),pygame.image.load('WB1.png'),pygame.image.load("WB2.png"),pygame.image.load("WB2.png"),pygame.image.load("WB2.png"), pygame.image.load('WB3.png'), pygame.image.load('WB3.png'), pygame.image.load('WB3.png'), pygame.image.load('WB4.png'), pygame.image.load('WB4.png'), pygame.image.load('WB4.png')]
    WSF =[pygame.image.load('WFF1.png'),pygame.image.load('WFF1.png'),pygame.image.load('WFF1.png'),pygame.image.load('WFF2.png'),pygame.image.load('WFF2.png'),pygame.image.load('WFF2.png'),pygame.image.load('WFF3.png'),pygame.image.load('WFF3.png'),pygame.image.load('WFF3.png'),pygame.image.load('WFF4.png'),pygame.image.load('WFF4.png'),pygame.image.load('WFF4.png'),pygame.image.load('WFF4.png')]
    #Jally = [pygame.image.load('jelly (1).png'),pygame.image.load('jelly (2).png'),pygame.image.load('jelly (3).png'),pygame.image.load('jelly (4).png')]
    jj =[pygame.image.load('JELL.png'),pygame.image.load('JELL.png'),pygame.image.load('JELL.png'),pygame.image.load('JELL1.png'),pygame.image.load('JELL1.png'),pygame.image.load('JELL1.png'),pygame.image.load('JELL2.png'),pygame.image.load('JELL2.png'),pygame.image.load('JELL2.png'),pygame.image.load('JELL3.png'),pygame.image.load('JELL3.png'),pygame.image.load('JELL3.png')]
    empty_heart = pygame.image.load('empty_heart.2.png')
    redheart = pygame.image.load('redheart.png')
    WHL = [pygame.image.load('WIZH1.png'),pygame.image.load('WIZH2.png'),pygame.image.load('WIZH2.png'),pygame.image.load('WIZH2.png'),pygame.image.load('WIZH3.png'),pygame.image.load('WIZH3.png'),pygame.image.load('WIZH3.png'),pygame.image.load('WIZH4.png'),pygame.image.load('WIZH4.png'),pygame.image.load('WIZH4.png'),pygame.image.load('WIZH5.png'),pygame.image.load('WIZH5.png'),pygame.image.load('WIZH5.png'),pygame.image.load('WIZH5.png'),pygame.image.load('WIZH5.png'),pygame.image.load('WIZH4.png'),pygame.image.load('WIZH4.png'),pygame.image.load('WIZH4.png'),pygame.image.load('WIZH3.png')]
    WHR = [pygame.image.load('‏‏WIZH1 - עותק.png'),pygame.image.load('‏‏WIZH1 - עותק.png'),pygame.image.load('‏‏WIZH1 - עותק.png'), pygame.image.load('‏‏WIZH2 - עותק.png'), pygame.image.load('‏‏WIZH2 - עותק.png'), pygame.image.load('‏‏WIZH2 - עותק.png'), pygame.image.load('‏‏WIZH3 - עותק.png'), pygame.image.load('‏‏WIZH3 - עותק.png'), pygame.image.load('‏‏WIZH3 - עותק.png'), pygame.image.load('‏‏WIZH4 - עותק.png'), pygame.image.load('‏‏WIZH4 - עותק.png'), pygame.image.load('‏‏WIZH4 - עותק.png'), pygame.image.load('‏‏WIZH5 - עותק.png'), pygame.image.load('‏‏WIZH5 - עותק.png'), pygame.image.load('‏‏WIZH5 - עותק.png'), pygame.image.load('‏‏WIZH4 - עותק.png'), pygame.image.load('‏‏WIZH4 - עותק.png'), pygame.image.load('‏‏WIZH4 - עותק.png'), pygame.image.load('‏‏WIZH3 - עותק.png')]
    WBhit = [pygame.image.load('WBhit1.png'),pygame.image.load('WBhit1.png'),pygame.image.load('WBhit2.png'),pygame.image.load('WBhit2.png'),pygame.image.load('WBhit3.png'),pygame.image.load('WBhit3.png'),pygame.image.load('WBhit4.png'),pygame.image.load('WBhit4.png'),pygame.image.load('WBhit5.png'),pygame.image.load('WBhit5.png')]
    
            
    class player(object):
        def __init__(self,x, y, width, height):
            self.DMUTx = x
            self.DMUTy = y 
            self.DMUTw = width
            self.DMUTh = height
            self.VEL = 10
            self.collision = False
            self.health = 60
            self.walkCount = 0
            self.frame_index = 0
            self.standing = True
            self.standing2 = False
            
            self.left = False
            self.right = False
            self.up = False
            self.down = False
        
        def draw(self, WIN):
            
            if self.standing == True:
                self.left =False
                self.right =False
                self.down = False
                self.up = False
                
                
                #BLITING THE LEFT HIT ANIMATION
                        
                if Keys [pygame.K_SPACE]:
                            #man.standing = False
                            pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
                            blade.hitbox = (man.DMUTx -55, man.DMUTy, 30,50)
                            
                            WIN.blit(WHL[blade.frame_index], (self.DMUTx-100, self.DMUTy-39))
                            blade.frame_index = (blade.frame_index + 1) % len(WHL)
                            if blade.walkCount >= 12:
                                blade.walkCount = 0
                else:
                    blade.hitbox = (man.DMUTx -55, man.DMUTy, 0,0)
                    WIN.blit(WS[self.frame_index], (self.DMUTx-80, self.DMUTy-40))
                    self.frame_index = (self.frame_index + 1) % len(WS)
                    if self.walkCount >= 12:
                        self.walkCount = 0
                

                
            
            if self.standing2 == True:
                self.standing = False
                self.left =False
                self.right =False
                self.down = False
                self.up = False
                
                
                if Keys [pygame.K_SPACE]:
                        pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
                        blade.hitbox = (man.DMUTx +55, man.DMUTy, 30,50)
                        
                        WIN.blit(WHR[blade.frame_index], (self.DMUTx-15, self.DMUTy -78))
                        blade.frame_index = (blade.frame_index + 1) % len(WHR)
                        if blade.walkCount >= 12:
                            blade.walkCount = 0

                else:
                    blade.hitbox = (man.DMUTx -55, man.DMUTy, 0,0)
                    WIN.blit(WSR[self.frame_index], (self.DMUTx-50, self.DMUTy-39))
                    self.frame_index = (self.frame_index + 1) % len(WSR)
                    if self.walkCount >= 12:
                        self.walkCount = 0

                
                    
                        
            
                
                

            
            

            
                
            if self.up == True:
                if self.walkCount > 4:
                    self.standing =False
                    self.left =False
                    self.down = False
                    self.right = False
                    WIN.blit(WB[self.walkCount], (self.DMUTx-105, self.DMUTy-40))
                    self.walkCount = (self.walkCount + 1) % len(WB)
                    if self.walkCount >= 12:
                        self.walkCount = 0
                
                if Keys [pygame.K_SPACE]:
                    pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
                    blade.hitbox = (man.DMUTx , man.DMUTy-50, 30,50)
                    
                    WIN.blit(WBhit[blade.frame_index], (self.DMUTx-105, self.DMUTy-39))
                    blade.frame_index = (blade.frame_index + 1) % len(WBhit)
                    if blade.walkCount >= 5:
                        blade.walkCount = 0
                else:
                    blade.hitbox = (man.DMUTx -55, man.DMUTy, 0,0)
                    WIN.blit(WU, (self.DMUTx-105, self.DMUTy-40))
                    if Keys [pygame.K_SPACE]:
                        pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
                        blade.hitbox = (man.DMUTx +5, man.DMUTy-35, 30,50)
                
                
            if self.down == True:
                if self.walkCount > 4:
                    self.standing =False
                    self.left =False
                    self.right = False
                    self.up = False
                    WIN.blit(WSF[self.walkCount], (self.DMUTx-110, self.DMUTy-40))
                    self.walkCount = (self.walkCount + 1) % len(WSF)
                    if self.walkCount >= 12 :
                        self.walkCount = 0     
                    if Keys [pygame.K_SPACE]:
                        pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
                        blade.hitbox = (man.DMUTx +0, man.DMUTy+55, 30,50)
            
                else:
                    blade.hitbox = (man.DMUTx -55, man.DMUTy, 0,0)
                    WIN.blit(WD, (self.DMUTx-110, self.DMUTy-40))
                    if Keys [pygame.K_SPACE]:
                        pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
                        blade.hitbox = (man.DMUTx +0, man.DMUTy+55, 30,50)
        
        def hit(self):
            if self.health > 20:
                self.health -= 20
            else:
                self.visible = True
                self.health = 60
                print ('low health')
                man.DMUTx =  random.randint (1, 500)
                man.DMUTy  = random.randint (1, 450)

    class sword(object):
        def __init__(self,x,y,width,height): 
            self.x =x
            self.y =y
            self.w =width
            self.height =height
            self.hitbox = (man.DMUTx +17, man.DMUTy+11, 29,52)
            self.visible = False
            self.swordHitL = False
            self.swordHitR = False  
            self.frame_index = 0
            self.walkCount = 0
            
        
        
        
        
                

    class enemy():
        def __init__(self,x, y, width, height):
            self.x =x
            self.y =y-50
            self.width =width
            self.height= height
            self.VEL = 10
            self.collision = False
            self.walkCount = 0
            self.frame_index = 0
            self.health = 10
        
        def draw(self, WIN):
            WIN.blit(jj[self.walkCount], (self.x-20, self.y+10))
            self.walkCount = (self.walkCount + 1) % len(WSF)
            if self.walkCount >= 12:
                    self.walkCount = 0  
        
        def hit(self):
            if self.health > 0:
                self.health -= 1
            else:
                self.visible = True
                self.health = 10
                self.x =  random.randint (1, 820)
                self.y  = random.randint (1, 900)
                
            
            

    class mafteyah(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.w = width
            self.h = height 


    #from button import Button

    def redrawGAME():
        WIN.blit( bg, (65,90))
        man.draw(WIN)
        #boundries
        pygame.draw.rect(WIN,(225,0,0),(man.DMUTx, man.DMUTy, man.DMUTw, man.DMUTh),2) #player
    # pygame.draw.rect(WIN, (255, 0, 0), (obs.x, obs.y, obs.w, obs.h),2) #table
        #pygame.draw.rect(WIN, (0, 255, 0), (obs3.x, obs3.y, obs3.w, obs3.h),2) #table2
        pygame.draw.rect(WIN, (0, 255, 0), (500, 545, 30, 30),2) # key
        #pygame.draw.rect(WIN, (0, 255, 0), (obs2.x, obs2.y, obs2.w, obs2.h),2) #obs2
        #man.draw(WIN)
        
        #SWORD BLITING
        #---------------
                        
        
                        
        
        
        #health blit
        ############
        #rheart = WIN.blit(redheart, (10,20)),WIN.blit(redheart, (60,20)),WIN.blit(redheart, (110,20))
        pygame.draw.rect(WIN, (6, 20, 26), (00, 20, 140, 50))
        #pygame.draw.rect(WIN, (255, 0, 0), (00, 20, 140, 50))
        
        pygame.draw.rect(WIN , (255,0,0), (15, 18,10-(2* (5-man.health)), 50)) #player health
        WIN.blit(empty_heart, (10,20)),WIN.blit(empty_heart, (50,20)),WIN.blit(empty_heart, (90,20))


       
        pygame.display.update()                        
                        
                
    #mesure tools  
    def mTools():
        if  pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
        print(x,y)                 
        

        

    clock=pygame.time.Clock()    
    man =player(400,480,40,64)
    blade =sword(300, 410 ,64,64)

    #obs = obsticle(240,410 ,280, 120)
    #obs3 = obsticle(235,400 ,290, 140)
    maf = mafteyah(500, 545, 30, 30)
    #obs2 = obsticle2(80, 665, 250,100)
    #stB = Button(450,100,start_img)
    #quB = Button(450,400,quit_img)



            

    run = True
    while run:
            
            
            
            Keys = pygame.key.get_pressed()
            
            clock.tick(27) # FPS
            
                
            if Keys[pygame.K_UP] and man.DMUTy >220 :
                            if man.VEL > 0:
                                man.DMUTy -=man.VEL
                                man.down = False
                                man.up = True
                                man.left = False
                                man.right = False
                                man.standing = False
                                man.standing2 = False
                                
                                man.walkCount += 1
                                
                            
                                
                        
                        
                        
                        #man.DMUTy = max(man.DMUTy-man.VEL, 250) 
            if Keys [pygame.K_LEFT] and man.DMUTx> 185: 
                        man.DMUTx -=man.VEL
                        man.standing = True
                        man.standing2 = False
                        man.down = False
                        man.up = False
                        man.walkCount +=1
                        if man.walkCount >3:
                            man.walkCount=0
                        blade.swordHitL = True   
                        
                        
                        
                    
                            
                        
                        
                    
                    
        

            if Keys [pygame.K_RIGHT] and man.DMUTx < 625 :
                            man.DMUTx += man.VEL
                            man.standing = False
                            man.standing2 = True
                            man.down = False
                            man.up = False
                            blade.swordHitR = True
                            #sword animation left
                            
                            
                            
                            
                            
            
            if Keys [pygame.K_DOWN] and man.DMUTy < 475 :
                            man.DMUTy +=man.VEL
                            man.down = True
                            man.up = False
                            man.left = False
                            man.right = False
                            man.standing = False
                            man.standing2 = False
                            man.walkCount += 1
                            
                            
                            

                    
            if not Keys [pygame.K_DOWN] and not [pygame.K_UP] and not [pygame.K_LEFT] and not [pygame.K_RIGHT]:
                        if man.right:
                            man.standing2 = True
                            man.standing = False
                        else:
                            man.standing = True
                            man.standing2 = False
                        
            
            
                    
            if man.left and man.right == False:
                man.standing =True

            if Keys[pygame.K_SPACE]:
                    if man.DMUTx > 340 and man.DMUTx <440  and man.DMUTy> 470  :
                        print ('bedroom exit')
                        run = False
                        time.sleep(1)
                        from lv2_Outside import gaga2
                        gaga2()

        
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
            redrawGAME()
    pygame.quit()
gagabed()