import pygame
import random

##############################################################################################초기설정
pygame.init() #초기화

#게임 화면 크기
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("nojam-game") #게임 이름


#FPS
clock = pygame.time.Clock()
##############################################################################################


# 1 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등등)

#배경화면
background = pygame.image.load("C:/Users/최열음/OneDrive/바탕 화면/python/game/game_basic/background.png")


#캐릭터
character = pygame.image.load("C:/Users/최열음/OneDrive/바탕 화면/python/game/game_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height
character_speed = 0.2

#캐릭터 이동속도(좌우만 움직이면 되는 게임)
character_to_x = 0

#똥
enemy = pygame.image.load("C:/Users/최열음/OneDrive/바탕 화면/python/game/game_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = 0
enemy_y_pos = 0
enemy_speed = 0.5

#똥이 맨위에 있나
enemy_reset = 0

#폰트 정의
game_font = pygame.font.Font(None,40) #폰트 객체 생성

#점수
score = 0





# 이벤트 루프
running = True #게임이 진행중인가

while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정

    # 2 이벤트 처리 (키보드,마우스 등)


    #화면 창의 X버튼 누르면 게임 종료
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


    
    # 3 게임 케릭터 위치 정의

    #캐릭터의 위치 바뀜
    character_x_pos += character_to_x * dt
    

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    #똥의 위치 정의
    if enemy_y_pos == (0 - enemy_height) and enemy_reset == 0:
        enemy_x_pos += random.randint(0,480-enemy_width)
        enemy_reset = 1
    
    elif enemy_y_pos > screen_height:
        enemy_reset = 0
        enemy_y_pos = 0 - enemy_height
        enemy_x_pos = 0
        score += 10


    else:
        enemy_y_pos += enemy_speed * dt
    



    
    


    
    # 4 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("똥에 맞았어요 점수 : " + str(score) + " 점 입니다")
        pygame.time.delay(1000)
        running = False

    
    # 5 화면 크리기

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    #점수표시
    scoreboard = game_font.render(str(score),True,(255,255,255))
    screen.blit(scoreboard,(0,0))
    

    #pygame.display.flip()
    pygame.display.update() #게임화면 다시 그리기!


#pygame.time.delay(2000)

#게임 종료
pygame.quit()

