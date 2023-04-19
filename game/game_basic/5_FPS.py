import pygame


pygame.init() #초기화

#게임 화면 크기
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("nojam-game") #게임 이름


#FPS
clock = pygame.time.Clock()


#배경 이미지
background = pygame.image.load("C:/Users/최열음/OneDrive/바탕 화면/python/game/game_basic/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/최열음/OneDrive/바탕 화면/python/game/game_basic/character.png")
character_size = character.get_rect().size #이미지의 크기 얻어옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2) #화면 중앙에 위치(가로)
character_y_pos = screen_height - character_height #화면 맨 밑에 위치(세로)

init_character_x_pos = (screen_width / 2) - (character_width/2) #화면 중앙에 위치(가로)
init_character_y_pos = screen_height - character_height #화면 맨 밑에 위치(세로)



#이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed = 0.5


# 이벤트 루프
running = True #게임이 진행중인가

while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get(): #이벤트가 발생했는지 확인
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했다면
            running = False #게임이 진행중인가 확인하는 변수에 False값을 넣는다

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                to_y = 0


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                character_x_pos = init_character_x_pos
                character_y_pos = init_character_y_pos

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    



    screen.blit(background,(0,0)) #배경을 넣음

    screen.blit(character,(character_x_pos,character_y_pos))

    

    
    pygame.display.update() #게임화면 다시 그리기!








#게임 종료
pygame.quit()

