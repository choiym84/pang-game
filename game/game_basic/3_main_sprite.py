import pygame


pygame.init() #초기화

#게임 화면 크기
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("nojam-game") #게임 이름

#배경 이미지
background = pygame.image.load("C:/Users/최열음/OneDrive/바탕 화면/python/game/game_basic/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/최열음/OneDrive/바탕 화면/python/game/game_basic/character.png")
character_size = character.get_rect().size #이미지의 크기 얻어옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2) #화면 중앙에 위치(가로)
character_y_pos = screen_height - character_height #화면 맨 밑에 위치(세로)

# 이벤트 루프
running = True #게임이 진행중인가

while running:
    for event in pygame.event.get(): #이벤트가 발생했는지 확인
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했다면
            running = False #게임이 진행중인가 확인하는 변수에 False값을 넣는다

    screen.blit(background,(0,0)) #배경을 넣음

    screen.blit(character,(character_x_pos,character_y_pos))

    

    
    pygame.display.update() #게임화면 다시 그리기!








#게임 종료
pygame.quit()

