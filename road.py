




def road():    
    import pygame ,time, sys, math, random #modules

    pygame.init()
    pygame.mixer.init()
    screenW =800
    screenH = 1000
    WIN = pygame.display.set_mode((screenW,screenH)) #screen #window 
    pygame.display.set_caption('Elad Game') #window name
    bg = pygame.image.load('road.2.jpg')
    start_img = pygame.image.load('START.png').convert_alpha()
    quit_img = pygame.image.load('QUIT.png').convert_alpha()
    wizzardR = pygame.image.load('wizzardR.png')
    wizzardL = pygame.image.load('wizzardL1.png')
    music = pygame.mixer.music.load('menu.music.mp3')
    pygame.mixer.music.play(-1)
    FONT = pygame.font.SysFont('ariel', 30)
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
                        self.walkCount == 0

                
                    
                        
            
                
                

            
            

            
                
            if self.up == True:
                if self.walkCount > 4:
                    self.standing =False
                    self.left =False
                    self.down = False
                    self.right = False
                    WIN.blit(WB[blade.walkCount], (self.DMUTx-105, self.DMUTy-40))
                    blade.walkCount = (blade.walkCount + 1) % len(WB)
                    if blade.walkCount >= 12:
                        blade.walkCount =0
                
                if Keys [pygame.K_SPACE]:
                    pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
                    blade.hitbox = (man.DMUTx , man.DMUTy-50, 30,50)
                    
                    WIN.blit(WBhit[blade.frame_index], (self.DMUTx-105, self.DMUTy-39))
                    blade.frame_index = (blade.frame_index + 1) % len(WBhit)
                    if blade.walkCount >= 5:
                        blade.walkCount = 0
                else:
                    blade.hitbox = (self.DMUTx -55, self.DMUTy, 0,0)
                    WIN.blit(WU, (self.DMUTx-105, self.DMUTy-40))
                    if Keys [pygame.K_SPACE]:
                        pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
                        blade.hitbox = (self.DMUTx +5, self.DMUTy-35, 30,50)
                
                
            if self.down == True:
                if self.walkCount > 4:
                    self.standing =False
                    self.left =False
                    self.right = False
                    self.up = False
                    WIN.blit(WSF[blade.walkCount], (self.DMUTx-110, self.DMUTy-40))
                    blade.walkCount = (blade.walkCount + 1) % len(WSF)
                    if blade.walkCount >= 11 :
                        blade.walkCount = 0     
                    if Keys [pygame.K_SPACE]:
                        pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
                        blade.hitbox = (self.DMUTx +0, self.DMUTy+55, 30,50)
            
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
        
        WIN.blit( bg, (18,0))
        man.draw(WIN)
        #boundries
        pygame.draw.rect(WIN,(225,0,0),(man.DMUTx, man.DMUTy, man.DMUTw, man.DMUTh),2) #player
    # pygame.draw.rect(WIN, (255, 0, 0), (obs.x, obs.y, obs.w, obs.h),2) #table
        #pygame.draw.rect(WIN, (0, 255, 0), (obs3.x, obs3.y, obs3.w, obs3.h),2) #table2
        #pygame.draw.rect(WIN, (0, 255, 0), (obs2.x, obs2.y, obs2.w, obs2.h),2) #obs2
        #pygame.draw.rect(WIN,(255,55,0),(140,250,100,man.DMUTh)) exit boundries
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
    man =player(650,900,40,64)
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
            
                
            if Keys[pygame.K_UP] and man.DMUTy >120 :
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
            if Keys [pygame.K_LEFT] and man.DMUTx> 87: 
                        man.DMUTx -=man.VEL
                        man.standing = True
                        man.standing2 = False
                        man.down = False
                        man.up = False
                        man.walkCount +=1
                        if man.walkCount >3:
                            man.walkCount=0
                        blade.swordHitL = True   
                        
                        
                        
                    
                            
                        
                        
                    
                    
        

            if Keys [pygame.K_RIGHT] and man.DMUTx < 655 :
                            man.DMUTx += man.VEL
                            man.standing = False
                            man.standing2 = True
                            man.down = False
                            man.up = False
                            blade.swordHitR = True
                            #sword animation left
                            
                            
                            
                            
                            
            
            if Keys [pygame.K_DOWN] and man.DMUTy < 900 :
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
                if man.DMUTx < 350 and man.DMUTx >280  and man.DMUTy <150:
                    run = False
                    time.sleep(1)
                    from arena import arena
                    arena()
            
            if Keys[pygame.K_SPACE]:
                if man.DMUTx <700  and man.DMUTx >620  and man.DMUTy >860:
                    run = False
                    time.sleep(1)
                    from oout import oouts
                    oouts()
                    print('oouts')

    
            # if obs.x < man.DMUTx < obs.x + obs.w 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            
                
                

            #if  man.DMUTx < obs.x+ obs.w and obs.x < man.DMUTx + man.DMUTw:
            #        if obs.y <man.DMUTy + man.DMUTh and obs.y + obs.h > man.DMUTy:
            #            print ('ok')
            #            if man.DMUTx < obs.x:
            #                   man.DMUTx = obs.x - man.DMUTw  # Move left
            #           else:
            #               man.DMUTx = obs.x + obs.w  # Move right
                        
                    

                        
        # if  man.DMUTx < obs.x+ obs.w and obs.x < man.DMUTx + man.DMUTw:
            #       if obs3.y <man.DMUTy + man.DMUTh and obs3.y + obs3.h > man.DMUTy:                 
                        
            #           if man.DMUTy < obs3.y:
            #                  man.DMUTy = obs3.y - man.DMUTh  # Move up
            #          else:
            #                  man.DMUTy = obs3.y + obs3.h  # Move down
                                
        
        # if  man.DMUTx < obs2.x+ obs2.w and obs2.x < man.DMUTx + man.DMUTw:
        #          if obs2.y <man.DMUTy + man.DMUTh and obs2.y + obs2.h > man.DMUTy:
        #             if man.left:
            #                man.DMUTx = obs.x + man.DMUTw*2
            #           else:
            #8               man.DMUTy = obs.y*1.5-20

                                
                                            
                            
                        
                            # Set the flag to True
                
        
            redrawGAME()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse coordinates when the mouse is clicked
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(f"Mouse clicked at ({mouse_x}, {mouse_y})")
            
        # mTools()
    pygame.quit() # finish
road()




    #[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
