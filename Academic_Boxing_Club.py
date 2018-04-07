from math import *
from random import randint
import pygame,sys

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN)


font1=pygame.font.Font("fonty1.ttf",35)
font=pygame.font.SysFont("Comic Sans MS",30)
fonttimer=pygame.font.Font("timer.ttf",65)

ground_image=pygame.image.load("ground1.jpg")
question_background_image=pygame.image.load("questionback.jpg")
computer_player_image=pygame.image.load("nameback.jpg")
timer_image=pygame.image.load("timerimage.jpg")
main_image=pygame.image.load("mainpage.jpg")
over_image=pygame.image.load("over.png")
question_background_image=pygame.image.load("back.jpg")

idle_anim=[pygame.image.load("Idle"+str(i+1)+".png") for i in range(10)]
shoot_anim=[pygame.image.load("Shoot"+str(i+1)+".png") for i in range(4)]
bullet_anim=[pygame.image.load("Bullet"+str(i)+".png") for i in range(5)]


idla_anim=[pygame.image.load("Idla"+str(i+1)+".png") for i in range(10)]
shoat_anim=[pygame.image.load("Shoat"+str(i+1)+".png") for i in range(4)]
bullat_anim=[pygame.image.load("Bullat"+str(i)+".png") for i in range(5)]

pygame.mixer.music.load("29.mp3")

time_zero=pygame.time.get_ticks()

state="idle"
frame_time=100
fire_time=pygame.time.get_ticks()

state1="idla"
frame_time1=100
fire_time1=pygame.time.get_ticks()

computertexture=font1.render("Computer",False,(255,0,0))
playertexture=font1.render("Player",False,(255,0,0))
time_remaing_texture= [fonttimer.render(str(i),False,(255,0,0)) for i in range(10)]

pygame.mixer.music.play()
entered = False
while not entered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    entered=True
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

        screen.blit(main_image,(0,0))
        pygame.display.flip()


start_ticks=None #starter tick
question=None
questiontexture=None
answer=None
answers=None
answertextures=None

def generate(answered=True):
    
    global question
    global questiontexture
    global answers
    global answer
    global answertextures
    global start_ticks
    global state,fire_time
    global state1,fire_time1
    start_ticks=pygame.time.get_ticks()
    
    question_type=randint(0,2)
    if question_type==0:
        n1=randint(0,10)
        n2=randint(0,10)
        question="What is " + str(n1)+"x"+str(n2)+"?"
        answer=n1*n2
        answers=[randint(0,75),randint(0,75),randint(0,75),randint(0,75)]
        index=randint(0,3)
        answers[index]=answer 
        questiontexture=font.render(question,False,(1,6,78))
        answertextures= [font.render(chr(i+65) + ") "+ str(answers[i]),False,(1,6,78)) for i in range(4)]
    
    elif question_type==1:
        n1=randint(0,20)
        n2=randint(0,20)
        question="What is " + str(n1)+"+"+str(n2)+"?"
        answer=n1+n2
        answers=[randint(0,40),randint(0,40),randint(0,40),randint(0,40)]
        index=randint(0,3)
        answers[index]=answer 
        questiontexture=font.render(question,False,(71,1,78))
        answertextures= [font.render(chr(i+65) + ") "+ str(answers[i]),False,(71,1,78)) for i in range(4)]

    elif question_type==2:
        n1=randint(0,30)
        n2=randint(0,30)
        question="What is " + str(n1)+"-"+str(n2)+"?"
        answer=n1-n2
        answers=[randint(-30,30),randint(-30,30),randint(-30,30),randint(-30,30)]
        index=randint(0,3)
        answers[index]=answer 
        questiontexture=font.render(question,False,(40,72,11))
        answertextures= [font.render(chr(i+65) + ") "+ str(answers[i]),False,(40,72,11)) for i in range(4)]
    
    if answered==True:
        state="shoot"
        fire_time=pygame.time.get_ticks()
    else:
        state1="shoat"
        fire_time1=pygame.time.get_ticks()

computer_health=10
player_health=10
max_health=10
    
generate(False)

while 1:
   
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    time_remaining=5-seconds

    for event in pygame.event.get():
        
        
        
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if answers[0]==answer:
                    generate()
                    computer_health-=1
                else:
                    generate(False)
                    player_health-=1

                    
            elif event.key == pygame.K_s:
                if answers[1]==answer:
                    generate()
                    computer_health-=1
                else:
                    generate(False)
                    player_health-=1
            elif event.key == pygame.K_d:
                if answers[2]==answer:
                    generate()
                    computer_health-=1
                else:
                    generate(False)
                    player_health-=1
            elif event.key == pygame.K_f:
                if answers[3]==answer:
                    generate()
                    computer_health-=1
                else:
                    generate(False)
                    player_health-=1
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
    if seconds>6:# if more than 10 seconds close the game

       player_health-=1

       generate(False)

    
    if player_health==0 or player_health<0 :
        entered = False
        while not entered:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        entered=True
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()

            screen.blit(over_image,(0,0))
            pygame.display.flip()
    

        
    if computer_health==0 or computer_health<0 :
        entered = False
        while not entered:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        entered=True
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()

            screen.blit(over_image,(0,0))
            pygame.display.flip()



#pygamecall.drawwcall.rectanglecall(,screen par ,(colour from paint),[x,y,length,width],fill=0)
    pygame.draw.rect(screen,(200,191,231),[0,0,350,80],0)
    pygame.draw.rect(screen,(255,0,0),[350,0,100,80],0)
    
    screen.blit(timer_image,[350,0,100,80])
    pygame.draw.rect(screen,(200,191,231),[450,0,350,80],0)
    pygame.draw.rect(screen,(255,240,155),[0,80,800,100],0)
    pygame.draw.rect(screen,(3,167,209),[0,160,800,390],0)
    pygame.draw.rect(screen,(255,240,155),[0,550,800,50],0)

    #screen blit ka drawing ine thing on other (iamge[quardinates])
    screen.blit(question_background_image,[-3,80,800,100])
    screen.blit(questiontexture,(0,80))
    
    for i in range(0,4):
         screen.blit(answertextures[i],(i*100,120))

    screen.blit(computer_player_image,[-3,0,335,80])
    screen.blit(computer_player_image,[448,0,350,80])    
    screen.blit(ground_image,[0,550,800,50])
    screen.blit(question_background_image,[0,160,800,390])
    #screen.blit(target_image,[0,170,150,195])
    screen.blit(computertexture,(18,-3))
    screen.blit(playertexture,(712,-3))
    screen.blit(time_remaing_texture[int(time_remaining)],(390,20))


    pygame.draw.rect(screen,(0,255,0),[0,40,computer_health*350/10,40],0)
    pygame.draw.rect(screen,(0,255,0),[450+(350-player_health*350/10),40,350,40],0)



    if state=='idle':
        screen.blit(idle_anim[((pygame.time.get_ticks()-time_zero)// frame_time)%len( idle_anim)],(400,140))
    elif state=='shoot':
        index=(pygame.time.get_ticks()-fire_time)// frame_time
        if not (index>=len(shoot_anim)):
            screen.blit(shoot_anim[index],(400,140))
            screen.blit(bullet_anim[index],(75*(5.5-index),280))
        else:
            state="idle"
            screen.blit(idle_anim[((pygame.time.get_ticks()-time_zero)// frame_time)%len( idle_anim)],(400,140))


    if state1=='idla':
        screen.blit(idla_anim[((pygame.time.get_ticks()-time_zero)// frame_time1)%len( idla_anim)],(-100,140))
    elif state1=='shoat':
        index2=(pygame.time.get_ticks()-fire_time1)// frame_time1
        if not (index2>=len(shoat_anim)):
            screen.blit(shoat_anim[index2],(-100,140))
            screen.blit(bullat_anim[index2],(250+75*(index2),280))
        else:
            state1="idla"
            screen.blit(idla_anim[((pygame.time.get_ticks()-time_zero)// frame_time1)%len( idla_anim)],(-100,140))    



    pygame.display.flip()

